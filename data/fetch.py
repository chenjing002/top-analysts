#!/usr/bin/env python
"""
fetch.py — pull one A-share company's financial data from the two primary sources,
cross-check them, and write a fact sheet for the expert panel.

Sources
  1. AshareValueLine (static GitHub Pages site, JSONP files, amounts in 亿元)
     https://chenjing002.github.io/AshareValueLine/
  2. bme.duckdb (Tushare raw statements + Penman reformulation, amounts in yuan)
     /Users/lin/Desktop/business-model-explorer/data/bme.duckdb

Usage
  python data/fetch.py 600519            # bare code, resolved to 600519.SH
  python data/fetch.py 600519.SH --out sessions/600519.SH/2026-11-23-01/data
  python data/fetch.py 贵州茅台           # Chinese name also works (via duckdb raw_stock_basic)

Run with the interpreter that has duckdb>=2.0:
  /Users/lin/Desktop/business-model-explorer/.venv/bin/python data/fetch.py 600519

Outputs (in --out, default data/cache/<ts_code>/)
  factsheet.md    human-readable sheet the experts read; every number labelled with its source
  factsheet.json  the same data, machine-readable, with provenance per block
  avl_raw.json    raw AshareValueLine stock payload (for traceability)

Design rules
  - Never silently merge the two sources. Each table says where it came from.
  - Cross-check block flags any |diff| > 1% between sources on the same concept and
    explains known definitional differences (e.g. duckdb ratios use 营业总收入).
  - Nothing here is a conclusion. The sheet is evidence; experts reason.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

DUCKDB_PATH = "/Users/lin/Desktop/business-model-explorer/data/bme.duckdb"
AVL_BASE = "https://chenjing002.github.io/AshareValueLine/"
YI = 1e8  # 1 亿元 = 100,000,000 元

# --------------------------------------------------------------------------- helpers


def _get(url: str, timeout: int = 30) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "top-analysts/0.1"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8")


def _jsonp(text: str) -> dict:
    """Strip `window.X = {...};` or `window.X({...});` wrappers."""
    i = text.find("{")
    j = text.rfind("}")
    if i < 0 or j < 0:
        raise ValueError("no JSON object found in JSONP payload")
    return json.loads(text[i : j + 1])


def _r(x, nd=2):
    if x is None:
        return None
    try:
        return round(float(x), nd)
    except (TypeError, ValueError):
        return None


def _pct_diff(a, b):
    if a is None or b is None:
        return None
    if abs(b) < 1e-9:
        return None
    return (a - b) / abs(b)


# --------------------------------------------------------------------------- AshareValueLine


def avl_latest_version() -> dict:
    v = _jsonp(_get(AVL_BASE + "data/versions.js"))
    return v["a_share"][0]


def avl_stock(ts_code: str, version: str) -> dict:
    url = f"{AVL_BASE}data/versions/a_share/{version}/stocks/{ts_code}.js"
    return _jsonp(_get(url)), url


# --------------------------------------------------------------------------- duckdb


def open_db():
    try:
        import duckdb  # noqa
    except ImportError:
        sys.exit(
            "duckdb python module not found. Run with "
            "/Users/lin/Desktop/business-model-explorer/.venv/bin/python"
        )
    import duckdb

    return duckdb.connect(DUCKDB_PATH, read_only=True)


def resolve_code(con, query: str) -> tuple[str, str, str]:
    """Return (ts_code, name, industry) for a code / 6-digit symbol / Chinese name."""
    q = query.strip().upper()
    if re.fullmatch(r"\d{6}\.(SH|SZ|BJ)", q):
        row = con.execute(
            "select ts_code,name,industry from raw_stock_basic where ts_code=?", [q]
        ).fetchone()
    elif re.fullmatch(r"\d{6}", q):
        row = con.execute(
            "select ts_code,name,industry from raw_stock_basic where symbol=?", [q]
        ).fetchone()
    else:
        rows = con.execute(
            "select ts_code,name,industry from raw_stock_basic where name like ? order by ts_code",
            [f"%{query.strip()}%"],
        ).fetchall()
        if len(rows) > 1:
            exact = [r for r in rows if r[1] == query.strip()]
            if len(exact) == 1:
                rows = exact
            else:
                sys.exit("ambiguous name, candidates: " + ", ".join(f"{r[0]} {r[1]}" for r in rows[:10]))
        row = rows[0] if rows else None
    if not row:
        sys.exit(f"company not found in duckdb raw_stock_basic: {query}")
    return row


def df_rows(con, sql, params=()):
    cur = con.execute(sql, params)
    cols = [d[0] for d in cur.description]
    return [dict(zip(cols, r)) for r in cur.fetchall()]


def duck_blocks(con, ts_code: str, years: int = 10) -> dict:
    b: dict = {}
    # Raw statements, annual, de-duplicated (raw tables hold repeated rows for the same period).
    b["raw_annual"] = df_rows(
        con,
        f"""
        with i as (select * from (select end_date, f_ann_date, update_flag, revenue, total_revenue, operate_profit,
                       total_profit, n_income, n_income_attr_p, ebit,
                       row_number() over (partition by end_date order by f_ann_date desc, update_flag desc) rn
                   from raw_income where ts_code=? and end_date like '%1231') where rn=1),
             bs as (select * from (select end_date, total_assets, total_liab, total_cur_assets, total_cur_liab,
                        money_cap, inventories, total_hldr_eqy_exc_min_int, total_hldr_eqy_inc_min_int, total_share,
                        row_number() over (partition by end_date order by f_ann_date desc, update_flag desc) rn
                    from raw_balancesheet where ts_code=? and end_date like '%1231') where rn=1),
             cf as (select * from (select end_date, n_cashflow_act, c_pay_acq_const_fiolta,
                        row_number() over (partition by end_date order by f_ann_date desc, update_flag desc) rn
                    from raw_cashflow where ts_code=? and end_date like '%1231') where rn=1)
        select i.end_date, i.f_ann_date, i.update_flag,
               i.revenue/1e8 as revenue_yi, i.total_revenue/1e8 as total_revenue_yi,
               i.operate_profit/1e8 as operate_profit_yi, i.total_profit/1e8 as total_profit_yi,
               i.n_income_attr_p/1e8 as ni_parent_yi, i.n_income/1e8 as ni_total_yi,
               bs.total_assets/1e8 as total_assets_yi, bs.total_liab/1e8 as total_liab_yi,
               bs.money_cap/1e8 as money_cap_yi, bs.inventories/1e8 as inventories_yi,
               bs.total_hldr_eqy_exc_min_int/1e8 as parent_equity_yi,
               bs.total_share/1e8 as total_share_yi,
               cf.n_cashflow_act/1e8 as cfo_yi, cf.c_pay_acq_const_fiolta/1e8 as capex_paid_yi,
               (cf.n_cashflow_act - cf.c_pay_acq_const_fiolta)/1e8 as fcf_simple_yi
        from i left join bs on i.end_date=bs.end_date left join cf on i.end_date=cf.end_date
        order by i.end_date desc limit {years}
        """,
        [ts_code, ts_code, ts_code],
    )
    b["ratios"] = df_rows(
        con,
        f"""select end_date, basis, revenue/1e8 as revenue_yi, oi_after_tax/1e8 as oi_after_tax_yi,
                   noa_capital/1e8 as noa_yi, nfo_capital/1e8 as nfo_yi, te_capital/1e8 as cse_yi,
                   rnoa, opm, opm_core, ato, ollev, flev, nbc, spread, rotce, roce_parent, gross_margin,
                   receivables_to_sales, inventory_to_sales, ppe_to_sales, intangibles_to_sales,
                   customer_advances_to_sales, op_payables_to_sales, ratio_flags
            from ratios_annual where ts_code=? and basis='average' order by end_date desc limit {years}""",
        [ts_code],
    )
    b["reformulated_is"] = df_rows(
        con,
        f"""select end_date, revenue/1e8 as revenue_yi, oi_core_pretax/1e8 as oi_core_pretax_yi,
                   unusual_pretax/1e8 as unusual_pretax_yi, oi_pretax/1e8 as oi_pretax_yi,
                   nfe_pretax/1e8 as nfe_pretax_yi, tax_reported/1e8 as tax_reported_yi, tax_rate_assumed,
                   oi_after_tax/1e8 as oi_after_tax_yi, oi_core_after_tax/1e8 as oi_core_after_tax_yi,
                   nfe_after_tax/1e8 as nfe_after_tax_yi, ni_parent/1e8 as ni_parent_yi,
                   minority_income/1e8 as minority_income_yi, comprehensive_income_total/1e8 as ci_total_yi
            from reformulated_is where ts_code=? and period_kind='cumulative' and end_date like '%1231' order by end_date desc limit {years}""",
        [ts_code],
    )
    b["reformulated_bs"] = df_rows(
        con,
        f"""select end_date, oa/1e8 as oa_yi, ol/1e8 as ol_yi, noa/1e8 as noa_yi, fa/1e8 as fa_yi, fo/1e8 as fo_yi,
                   nfo/1e8 as nfo_yi, minority_interests/1e8 as mi_yi, cse_calc/1e8 as cse_yi,
                   total_assets_reported/1e8 as total_assets_yi, parent_equity_reported/1e8 as parent_equity_yi,
                   r1_assets_residual, r2_liab_residual, r3_cse_residual
            from reformulated_bs where ts_code=? and end_date like '%1231' order by end_date desc limit {years}""",
        [ts_code],
    )
    b["cash"] = df_rows(
        con,
        f"""select end_date, ni_total/1e8 as ni_total_yi, cfo/1e8 as cfo_yi, capex_paid/1e8 as capex_paid_yi,
                   asset_disposal_proceeds/1e8 as disposals_yi, fcf_simple/1e8 as fcf_simple_yi,
                   cash_conversion, accruals/1e8 as accruals_yi, cf_flags
            from cash_summary_annual where ts_code=? order by end_date desc limit {years}""",
        [ts_code],
    )
    b["capital"] = df_rows(
        con,
        f"""select end_date, noa_begin/1e8 as noa_begin_yi, noa_end/1e8 as noa_end_yi, delta_noa/1e8 as delta_noa_yi,
                   revenue_growth, noa_growth, reinvestment_rate, capex_paid/1e8 as capex_paid_yi,
                   da_total/1e8 as da_yi, capex_to_da, fcf_from_oi/1e8 as fcf_from_oi_yi, cap_flags
            from capital_summary_annual where ts_code=? order by end_date desc limit {years}""",
        [ts_code],
    )
    b["working_capital"] = df_rows(
        con,
        f"""select end_date, dso, dio, dpo, ccc, advance_days, ccc_net_advances, owc_pct_sales,
                   incr_owc_per_incr_revenue, wc_flags
            from working_capital_annual where ts_code=? order by end_date desc limit {years}""",
        [ts_code],
    )
    b["residual_income"] = df_rows(
        con,
        f"""select end_date, r_op_assumed, r_e_assumed, pm, pm_core, rnoa_open, ato_open, spread_op,
                   reoi/1e8 as reoi_yi, reoi_core/1e8 as reoi_core_yi, re_common/1e8 as re_common_yi,
                   roce_open, delta_reoi/1e8 as delta_reoi_yi, ri_flags
            from residual_income_annual where ts_code=? order by end_date desc limit {years}""",
        [ts_code],
    )
    b["valuation"] = df_rows(
        con,
        """select end_date, trade_date, price, shares/1e8 as shares_yi, market_cap/1e8 as market_cap_yi,
                  market_ev/1e8 as market_ev_yi, r_op_assumed, r_e_assumed, g_assumed,
                  v_equity_book/1e8 as v_equity_book_yi, v_equity_reoi_flat/1e8 as v_equity_reoi_flat_yi,
                  v_equity_reoi_g/1e8 as v_equity_reoi_g_yi, v_per_share, v_to_p,
                  trailing_pe, forward_pe_market, normal_pe, implied_g_reoi, implied_g_fcf, implied_r_op
           from valuation_annual where ts_code=? order by end_date desc limit 3""",
        [ts_code],
    )
    latest = con.execute(
        "select max(end_date) from valuation_reverse_curve where ts_code=?", [ts_code]
    ).fetchone()[0]
    b["reverse_curve"] = (
        df_rows(
            con,
            """select r, implied_g_reoi, implied_g_fcf, implied_g_equity from valuation_reverse_curve
               where ts_code=? and end_date=? order by r""",
            [ts_code, latest],
        )
        if latest
        else []
    )
    b["reverse_curve_end_date"] = latest
    b["market_latest"] = df_rows(
        con,
        """select trade_date, close, total_share, float_share, total_mv, circ_mv, pe, pe_ttm, pb, dv_ttm
           from raw_daily_basic where ts_code=? order by trade_date desc limit 1""",
        [ts_code],
    )
    b["analysis_log"] = df_rows(
        con,
        """select status, reason, step, n_annual, first_end, last_end, check_failures, finished_at
           from analysis_log where ts_code=? order by finished_at desc limit 1""",
        [ts_code],
    )
    # Industry peers: same Tushare industry, latest year, average basis.
    b["peers"] = df_rows(
        con,
        """with ind as (select industry from raw_stock_basic where ts_code=?),
                ly as (select max(end_date) e from ratios_annual where ts_code=?)
           select r.ts_code, s.name, r.end_date, r.revenue/1e8 as revenue_yi, r.rnoa, r.opm, r.ato, r.flev,
                  r.gross_margin, m.market_cap/1e8 as market_cap_yi
           from ratios_annual r join raw_stock_basic s on s.ts_code=r.ts_code
           left join market_snapshot_annual m on m.ts_code=r.ts_code and m.end_date=r.end_date
           where s.industry=(select industry from ind) and r.basis='average' and r.end_date=(select e from ly)
           order by r.revenue desc nulls last limit 12""",
        [ts_code, ts_code],
    )
    return b


# --------------------------------------------------------------------------- cross-check


def cross_check(avl: dict, duck: dict) -> list[dict]:
    """Compare the same concepts across sources for overlapping years. AVL in 亿元."""
    ann = avl.get("annual", {})
    rows = {r["end_date"][:4]: r for r in duck["raw_annual"]}
    checks = []
    pairs = [
        # (AVL key, duckdb field, note)
        ("营业收入", "revenue_yi", "AVL 营业收入 vs duckdb raw_income.revenue (营业收入). duckdb *ratios* use 营业总收入 instead."),
        ("利润总额", "total_profit_yi", ""),
        ("归母净利润", "ni_parent_yi", ""),
        ("总资产", "total_assets_yi", ""),
        ("总负债", "total_liab_yi", ""),
        ("货币资金", "money_cap_yi", ""),
        ("存货", "inventories_yi", ""),
        ("经营现金净额", "cfo_yi", ""),
        ("总股本", "total_share_yi", "亿股"),
    ]
    for akey, dkey, note in pairs:
        series = ann.get(akey, {})
        for year, aval in sorted(series.items(), reverse=True):
            d = rows.get(year)
            if d is None:
                continue
            dval = d.get(dkey)
            diff = _pct_diff(aval, dval)
            checks.append(
                {
                    "concept": akey,
                    "year": year,
                    "avl": _r(aval, 4),
                    "duckdb": _r(dval, 4),
                    "pct_diff": _r(diff, 4) if diff is not None else None,
                    "flag": "MISMATCH" if (diff is not None and abs(diff) > 0.01) else ("n/a" if diff is None else "ok"),
                    "note": note,
                }
            )
    return checks


# --------------------------------------------------------------------------- rendering


def _fmt(x, nd=1, pct=False):
    if x is None:
        return "—"
    if pct:
        return f"{100*x:.1f}%"
    return f"{x:,.{nd}f}"


def _table(rows: list[dict], cols: list[tuple[str, str, dict]]) -> str:
    """cols: (header, key, fmt kwargs)."""
    if not rows:
        return "_no data_\n"
    out = ["| " + " | ".join(h for h, _, _ in cols) + " |", "|" + "---|" * len(cols)]
    for r in rows:
        cells = []
        for _, k, kw in cols:
            v = r.get(k)
            cells.append(str(v) if kw.get("raw") else _fmt(v, **kw))
        out.append("| " + " | ".join(cells) + " |")
    return "\n".join(out) + "\n"


def render_md(meta: dict, avl: dict, avl_url: str, duck: dict, checks: list[dict]) -> str:
    L = []
    L.append(f"# Fact sheet — {meta['name']} ({meta['ts_code']}) · {meta['industry']}")
    L.append("")
    L.append(f"Generated {meta['generated_at']} by `data/fetch.py`. Amounts in **亿元 (1e8 CNY)** unless stated; ratios as decimals.")
    L.append("")
    L.append("## Sources")
    L.append(f"- **S1 AshareValueLine** version `{meta['avl_version']}` (financials fetched {avl.get('fetched_at')}, quote {avl.get('quote_refreshed_at')}): `{avl_url}`")
    L.append(f"- **S2 bme.duckdb** `{DUCKDB_PATH}` (Tushare raw statements + Penman reformulation). Analysis log: {duck['analysis_log'][0] if duck['analysis_log'] else 'none'}")
    L.append("")
    # Quote
    q = avl.get("quote", {})
    m = duck["market_latest"][0] if duck["market_latest"] else {}
    L.append("## Market snapshot")
    L.append(f"- S1 quote {q.get('trade_date')}: price {q.get('price')} · PE {q.get('pe')} · PE(TTM) {q.get('pe_ttm')} · PB {q.get('pb')} · total mkt cap {q.get('total_mv_yi')} 亿 · shares {q.get('total_share_yi')} 亿股")
    if m:
        L.append(f"- S2 raw_daily_basic {m.get('trade_date')}: close {m.get('close')} · PE(TTM) {m.get('pe_ttm')} · PB {m.get('pb')} · total_mv {_fmt((m.get('total_mv') or 0)/1e4,1)} 亿 (Tushare 万元 converted) · dv_ttm {m.get('dv_ttm')}%")
    L.append("")
    # Cross-check
    L.append("## Cross-check S1 vs S2 (same concept, same fiscal year)")
    bad = [c for c in checks if c["flag"] == "MISMATCH"]
    L.append(f"{len(checks)} comparisons, **{len(bad)} mismatches >1%**." + (" All matched." if not bad else ""))
    if bad:
        L.append("")
        L.append(_table(bad, [("concept", "concept", {"raw": True}), ("year", "year", {"raw": True}), ("S1 AVL", "avl", {"nd": 2}), ("S2 duckdb", "duckdb", {"nd": 2}), ("diff", "pct_diff", {"pct": True}), ("note", "note", {"raw": True})]))
    L.append("")
    # AVL annual
    L.append("## S1 · AshareValueLine annual indicators (亿元; %, days, 亿股 where labelled)")
    ann = avl.get("annual", {})
    years = sorted({y for s in ann.values() for y in s}, reverse=True)[:10]
    if ann:
        L.append("| indicator | " + " | ".join(years) + " |")
        L.append("|---|" + "---|" * len(years))
        for k, s in ann.items():
            L.append(f"| {k} | " + " | ".join(_fmt(s.get(y), 2) if s.get(y) is not None else "—" for y in years) + " |")
    L.append("")
    qr = avl.get("quarterly_revenue", {})
    if qr:
        L.append("### S1 · Quarterly revenue (single quarter, 亿元)")
        L.append("| year | Q1 | Q2 | Q3 | Q4 | FY |")
        L.append("|---|---|---|---|---|---|")
        for y in qr.get("years", []):
            d = qr["data"].get(str(y), {})
            L.append(f"| {y} | " + " | ".join(_fmt(d.get(k), 1) for k in ["Q1", "Q2", "Q3", "Q4", "FY"]) + " |")
        L.append("")
    mb = avl.get("main_business", {}).get("P", {})
    if mb:
        L.append("### S1 · Main business by product (latest annual; revenue, gross profit 亿元)")
        annual_periods = sorted([p for p in mb if p.endswith("1231")], reverse=True)[:2]
        for p in annual_periods:
            L.append(f"- **{p}** total {_fmt(mb[p].get('total'),1)}: " + "; ".join(f"{i[0]} {_fmt(i[1],1)} (GP {_fmt(i[2],1)})" for i in mb[p].get("items", [])))
        L.append("")
    ev = avl.get("ev_items")
    if ev:
        L.append(f"### S1 · EV items ({ev.get('报告期')}, 亿元)")
        L.append(", ".join(f"{k} {v}" for k, v in ev.items() if k != "报告期"))
        L.append("")
    # duckdb raw
    L.append("## S2 · Raw annual statements (亿元; latest filing per period from raw_income/raw_balancesheet/raw_cashflow)")
    L.append(_table(duck["raw_annual"], [
        ("FY", "end_date", {"raw": True}), ("营业收入", "revenue_yi", {}), ("营业总收入", "total_revenue_yi", {}),
        ("营业利润", "operate_profit_yi", {}), ("归母净利润", "ni_parent_yi", {}), ("总资产", "total_assets_yi", {}),
        ("货币资金", "money_cap_yi", {}), ("存货", "inventories_yi", {}), ("归母权益", "parent_equity_yi", {}),
        ("CFO", "cfo_yi", {}), ("capex paid", "capex_paid_yi", {}), ("FCF simple", "fcf_simple_yi", {}),
        ("股本(亿)", "total_share_yi", {"nd": 2}), ("announced", "f_ann_date", {"raw": True}),
    ]))
    L.append("## S2 · Penman ratios (basis = average capital; `ratios_annual`)")
    L.append("Definitions: OI = operating income after tax (reformulated, ≠ 营业利润); NOA = OA − OL; NFO = FO − FA (negative = net financial assets); RNOA = OI/NOA; OPM = OI/营业总收入; ATO = 营业总收入/NOA; FLEV = NFO/CSE; spread = RNOA − NBC; ROCE = RNOA + FLEV × spread.")
    L.append(_table(duck["ratios"], [
        ("FY", "end_date", {"raw": True}), ("营业总收入", "revenue_yi", {}), ("OI after tax", "oi_after_tax_yi", {}),
        ("NOA", "noa_yi", {}), ("NFO", "nfo_yi", {}), ("CSE", "cse_yi", {}),
        ("RNOA", "rnoa", {"pct": True}), ("OPM", "opm", {"pct": True}), ("OPM core", "opm_core", {"pct": True}),
        ("ATO", "ato", {"nd": 2}), ("FLEV", "flev", {"nd": 2}), ("NBC", "nbc", {"pct": True}),
        ("spread", "spread", {"pct": True}), ("ROCE", "rotce", {"pct": True}), ("GM", "gross_margin", {"pct": True}),
        ("flags", "ratio_flags", {"raw": True}),
    ]))
    L.append("### S2 · Balance-sheet intensity (share of 营业总收入)")
    L.append(_table(duck["ratios"], [
        ("FY", "end_date", {"raw": True}), ("receivables", "receivables_to_sales", {"pct": True}),
        ("inventory", "inventory_to_sales", {"pct": True}), ("PP&E", "ppe_to_sales", {"pct": True}),
        ("intangibles", "intangibles_to_sales", {"pct": True}), ("customer advances", "customer_advances_to_sales", {"pct": True}),
        ("op. payables", "op_payables_to_sales", {"pct": True}),
    ]))
    L.append("## S2 · Reformulated income statement (亿元; cumulative full-year rows)")
    L.append(_table(duck["reformulated_is"], [
        ("FY", "end_date", {"raw": True}), ("revenue", "revenue_yi", {}), ("OI core pretax", "oi_core_pretax_yi", {}),
        ("unusual pretax", "unusual_pretax_yi", {}), ("NFE pretax", "nfe_pretax_yi", {}), ("tax reported", "tax_reported_yi", {}),
        ("tax rate assumed", "tax_rate_assumed", {"pct": True}), ("OI after tax", "oi_after_tax_yi", {}),
        ("OI core after tax", "oi_core_after_tax_yi", {}), ("NFE after tax", "nfe_after_tax_yi", {}),
        ("NI parent", "ni_parent_yi", {}), ("minority", "minority_income_yi", {}), ("CI total", "ci_total_yi", {}),
    ]))
    L.append("## S2 · Reformulated balance sheet (亿元)")
    L.append(_table(duck["reformulated_bs"], [
        ("FY", "end_date", {"raw": True}), ("OA", "oa_yi", {}), ("OL", "ol_yi", {}), ("NOA", "noa_yi", {}),
        ("FA", "fa_yi", {}), ("FO", "fo_yi", {}), ("NFO", "nfo_yi", {}), ("MI", "mi_yi", {}), ("CSE", "cse_yi", {}),
        ("total assets", "total_assets_yi", {}), ("parent equity", "parent_equity_yi", {}),
        ("r1", "r1_assets_residual", {"nd": 0}), ("r2", "r2_liab_residual", {"nd": 0}), ("r3", "r3_cse_residual", {"nd": 0}),
    ]))
    L.append("## S2 · Cash reconciliation (亿元)")
    L.append(_table(duck["cash"], [
        ("FY", "end_date", {"raw": True}), ("NI total", "ni_total_yi", {}), ("CFO", "cfo_yi", {}), ("capex paid", "capex_paid_yi", {}),
        ("disposals", "disposals_yi", {}), ("FCF simple", "fcf_simple_yi", {}), ("CFO/NI", "cash_conversion", {"nd": 2}),
        ("accruals", "accruals_yi", {}), ("flags", "cf_flags", {"raw": True}),
    ]))
    L.append("## S2 · Capital & reinvestment")
    L.append(_table(duck["capital"], [
        ("FY", "end_date", {"raw": True}), ("NOA begin", "noa_begin_yi", {}), ("NOA end", "noa_end_yi", {}), ("ΔNOA", "delta_noa_yi", {}),
        ("rev growth", "revenue_growth", {"pct": True}), ("NOA growth", "noa_growth", {"pct": True}),
        ("reinvest rate", "reinvestment_rate", {"pct": True}), ("capex", "capex_paid_yi", {}), ("D&A", "da_yi", {}),
        ("capex/D&A", "capex_to_da", {"nd": 2}), ("FCF from OI", "fcf_from_oi_yi", {}), ("flags", "cap_flags", {"raw": True}),
    ]))
    L.append("## S2 · Working capital (days)")
    L.append(_table(duck["working_capital"], [
        ("FY", "end_date", {"raw": True}), ("DSO", "dso", {}), ("DIO", "dio", {}), ("DPO", "dpo", {}), ("CCC", "ccc", {}),
        ("advance days", "advance_days", {}), ("CCC net adv.", "ccc_net_advances", {}), ("OWC % sales", "owc_pct_sales", {"pct": True}),
        ("ΔOWC/ΔRev", "incr_owc_per_incr_revenue", {"nd": 2}), ("flags", "wc_flags", {"raw": True}),
    ]))
    L.append("## S2 · Residual operating income (亿元; r_op assumed, not a conclusion)")
    L.append(_table(duck["residual_income"], [
        ("FY", "end_date", {"raw": True}), ("r_op", "r_op_assumed", {"pct": True}), ("PM", "pm", {"pct": True}),
        ("PM core", "pm_core", {"pct": True}), ("RNOA (open)", "rnoa_open", {"pct": True}), ("ATO (open)", "ato_open", {"nd": 2}),
        ("spread", "spread_op", {"pct": True}), ("ReOI", "reoi_yi", {}), ("ReOI core", "reoi_core_yi", {}), ("ΔReOI", "delta_reoi_yi", {}),
        ("RE common", "re_common_yi", {}), ("flags", "ri_flags", {"raw": True}),
    ]))
    L.append("## S2 · Valuation anchors (model defaults r_op/r_e/g are assumptions; use the reverse curve, not the point value)")
    L.append(_table(duck["valuation"], [
        ("FY", "end_date", {"raw": True}), ("trade date", "trade_date", {"raw": True}), ("price", "price", {"nd": 2}),
        ("mkt cap", "market_cap_yi", {}), ("EV", "market_ev_yi", {}), ("r_op", "r_op_assumed", {"pct": True}), ("g", "g_assumed", {"pct": True}),
        ("V book", "v_equity_book_yi", {}), ("V ReOI flat", "v_equity_reoi_flat_yi", {}), ("V ReOI g", "v_equity_reoi_g_yi", {}),
        ("V/P", "v_to_p", {"nd": 2}), ("trailing PE", "trailing_pe", {}), ("fwd PE mkt", "forward_pe_market", {}),
        ("normal PE", "normal_pe", {}), ("implied g (ReOI)", "implied_g_reoi", {"pct": True}), ("implied g (FCF)", "implied_g_fcf", {"pct": True}),
    ]))
    if duck["reverse_curve"]:
        L.append(f"### S2 · Reverse-engineered growth the market price implies, by required return (end {duck['reverse_curve_end_date']})")
        L.append(_table(duck["reverse_curve"], [
            ("r", "r", {"pct": True}), ("implied g ReOI", "implied_g_reoi", {"pct": True}),
            ("implied g FCF", "implied_g_fcf", {"pct": True}), ("implied g equity", "implied_g_equity", {"pct": True}),
        ]))
    L.append("## S2 · Industry peers (same Tushare industry, latest FY, average basis)")
    L.append(_table(duck["peers"], [
        ("code", "ts_code", {"raw": True}), ("name", "name", {"raw": True}), ("FY", "end_date", {"raw": True}),
        ("营业总收入", "revenue_yi", {}), ("RNOA", "rnoa", {"pct": True}), ("OPM", "opm", {"pct": True}), ("ATO", "ato", {"nd": 2}),
        ("FLEV", "flev", {"nd": 2}), ("GM", "gross_margin", {"pct": True}), ("mkt cap", "market_cap_yi", {}),
    ]))
    bsf = avl.get("balance_sheet", {})
    if bsf:
        L.append("## S1 · Full balance sheet (亿元; Tushare field keys; latest 5 years)")
        yrs = [str(y) for y in bsf.get("years", [])[:5]]
        L.append("| item | key | " + " | ".join(yrs) + " |")
        L.append("|---|---|" + "---|" * len(yrs))
        for f in bsf.get("fields", []):
            s = bsf.get("data", {}).get(f["key"], {})
            if not any(s.get(y) not in (None, 0) for y in yrs):
                continue
            L.append(f"| {f['label']} | {f['key']} | " + " | ".join(_fmt(s.get(y), 2) if s.get(y) is not None else "—" for y in yrs) + " |")
        L.append("")
    L.append("---")
    L.append("_Evidence only. Every figure above is traceable to S1 or S2; nothing here is an analytical conclusion._")
    return "\n".join(L) + "\n"


# --------------------------------------------------------------------------- main


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("company", help="ts_code (600519.SH), 6-digit code, or Chinese name")
    ap.add_argument("--out", help="output directory (default data/cache/<ts_code>)")
    ap.add_argument("--years", type=int, default=10)
    ap.add_argument("--no-avl", action="store_true", help="skip AshareValueLine (offline)")
    args = ap.parse_args()

    con = open_db()
    ts_code, name, industry = resolve_code(con, args.company)
    out = Path(args.out) if args.out else Path(__file__).resolve().parent / "cache" / ts_code
    out.mkdir(parents=True, exist_ok=True)

    avl, avl_url, version = {}, "", "offline"
    if not args.no_avl:
        try:
            v = avl_latest_version()
            version = v["version"]
            avl, avl_url = avl_stock(ts_code, version)
            (out / "avl_raw.json").write_text(json.dumps(avl, ensure_ascii=False, indent=1), encoding="utf-8")
        except Exception as e:  # keep going with duckdb only, but say so loudly
            print(f"WARNING: AshareValueLine fetch failed: {e}", file=sys.stderr)
            avl, avl_url, version = {}, f"FAILED: {e}", "unavailable"

    duck = duck_blocks(con, ts_code, args.years)
    checks = cross_check(avl, duck) if avl else []
    meta = {
        "ts_code": ts_code,
        "name": name,
        "industry": industry,
        "generated_at": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
        "avl_version": version,
        "avl_url": avl_url,
        "duckdb_path": DUCKDB_PATH,
    }
    md = render_md(meta, avl, avl_url, duck, checks)
    (out / "factsheet.md").write_text(md, encoding="utf-8")
    (out / "factsheet.json").write_text(
        json.dumps({"meta": meta, "cross_check": checks, "duckdb": duck, "avl": avl}, ensure_ascii=False, indent=1, default=str),
        encoding="utf-8",
    )
    bad = [c for c in checks if c["flag"] == "MISMATCH"]
    print(f"{ts_code} {name} ({industry}) → {out}")
    print(f"  AVL version {version}; duckdb years {duck['raw_annual'][-1]['end_date'][:4] if duck['raw_annual'] else '?'}–{duck['raw_annual'][0]['end_date'][:4] if duck['raw_annual'] else '?'}")
    print(f"  cross-check: {len(checks)} comparisons, {len(bad)} mismatches >1%")
    for c in bad[:10]:
        print(f"    {c['concept']} {c['year']}: AVL {c['avl']} vs duckdb {c['duckdb']} ({c['pct_diff']:+.1%})")


if __name__ == "__main__":
    main()
