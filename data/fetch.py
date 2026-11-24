#!/usr/bin/env python
"""
fetch.py — read one A-share company's financial data from the two local JSON sources,
cross-check them, and write a fact sheet for the expert panel. No network, no database
needed for the default run.

Sources (both are static agent-friendly JSON APIs, read from their local build folders)
  S1  AshareValueLine   /Users/lin/Desktop/AshareValueLine/_site/api/v1/a_share/companies/<ts_code>.json
      (published at https://chenjing002.github.io/AshareValueLine/api/v1/ ; yuan, shares)
  S2  business-model-explorer   /Users/lin/Desktop/business-model-explorer/build/pages/
      business-model-explorer[-data]/api/v1/companies/<ts_code>.json   (SZ companies live in the
      `-data` site; published at https://chenjing002.github.io/business-model-explorer/ ; yuan)
  Optional S2 supplement (--duckdb): bme.duckdb for what the JSON lacks — quarterly 归母净利润 /
  CFO / capex / OI, the required-return reverse curve, raw_daily_basic.

Usage
  python3 data/fetch.py 600519            # bare code, resolved to 600519.SH
  python3 data/fetch.py 600519.SH --out sessions/600519.SH/2026-11-23-01/data
  python3 data/fetch.py 贵州茅台           # Chinese name, resolved from the BME company index
  /Users/lin/Desktop/business-model-explorer/.venv/bin/python data/fetch.py 600519 --duckdb

Override locations with BME_PAGES_ROOT / AVL_API_ROOT (or --bme-root / --avl-root).

Outputs (in --out, default data/cache/<ts_code>/)
  factsheet.md    human-readable sheet the experts read; every number labelled with its source
  factsheet.json  the same data, machine-readable, with provenance per block
  avl_raw.json    S1 JSON as read (yuan), for traceability
  bme_raw.json    S2 JSON as read (yuan), for traceability

Design rules
  - Never silently merge the two sources. Each table says where it came from.
  - Cross-check flags any |diff| > 1% between sources on the same annual concept and explains
    known definitional differences. S1 amounts are rounded to 0.01 亿元 upstream.
  - The local JSON folders are build products: the sheet states each source's version / export
    time so a stale copy is visible. Missing values stay missing (never zero).
  - Nothing here is a conclusion. The sheet is evidence; experts reason.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

DUCKDB_PATH = "/Users/lin/Desktop/business-model-explorer/data/bme.duckdb"
BME_PAGES_ROOT = os.environ.get("BME_PAGES_ROOT", "/Users/lin/Desktop/business-model-explorer/build/pages")
AVL_API_ROOT = os.environ.get("AVL_API_ROOT", "/Users/lin/Desktop/AshareValueLine/_site/api/v1/a_share")
YI = 1e8  # 1 亿元 = 100,000,000 元

# --------------------------------------------------------------------------- helpers


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


def _yi(x):
    return None if x is None else x / YI


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


# --------------------------------------------------------------------------- company lookup


def bme_site_dirs(root: Path) -> list[Path]:
    return [root / "business-model-explorer", root / "business-model-explorer-data"]


def bme_index(root: Path) -> list[dict]:
    p = root / "business-model-explorer" / "api" / "v1" / "companies.json"
    if not p.exists():
        sys.exit(f"BME company index not found: {p}\nBuild it with `.venv/bin/python -m pipeline.cli pages` in business-model-explorer.")
    return _load(p)["companies"]


def resolve_code(index: list[dict], query: str) -> dict:
    """Return the BME index row for a code / 6-digit symbol / Chinese name."""
    q = query.strip().upper()
    if re.fullmatch(r"\d{6}\.(SH|SZ|BJ)", q):
        rows = [c for c in index if c["ts_code"] == q]
    elif re.fullmatch(r"\d{6}", q):
        rows = [c for c in index if c["ts_code"].startswith(q + ".")]
    else:
        rows = [c for c in index if query.strip() in c["name"]]
        exact = [c for c in rows if c["name"] == query.strip()]
        if len(rows) > 1 and len(exact) == 1:
            rows = exact
        if len(rows) > 1:
            sys.exit("ambiguous name, candidates: " + ", ".join(f"{c['ts_code']} {c['name']}" for c in rows[:10]))
    if not rows:
        sys.exit(f"company not found in the BME company index: {query}")
    return rows[0]


def bme_company_path(root: Path, ts_code: str) -> Path:
    for d in bme_site_dirs(root):
        p = d / "api" / "v1" / "companies" / f"{ts_code}.json"
        if p.exists():
            return p
    return bme_site_dirs(root)[1 if ts_code.endswith(".SZ") else 0] / "api" / "v1" / "companies" / f"{ts_code}.json"


# --------------------------------------------------------------------------- S1 (AshareValueLine)


def avl_to_yi(a: dict) -> dict:
    """Return a copy of the S1 payload with yuan/shares converted to 亿元/亿股, so the sheet and the
    cross-check keep the units the experts already read. Percent, days and multiples are unchanged."""
    out = json.loads(json.dumps(a))
    fields = a.get("annual_fields", {})
    for k, series in out.get("annual", {}).items():
        if fields.get(k, {}).get("unit") in ("CNY_yuan", "shares"):
            out["annual"][k] = {y: _yi(v) for y, v in series.items()}
    q = out.get("quote") or {}
    if q:
        q["total_mv_yi"] = _yi(q.get("total_mv"))
        q["total_share_yi"] = _yi(q.get("total_share"))
    qr = out.get("quarterly_revenue") or {}
    for y, d in qr.get("data", {}).items():
        qr["data"][y] = {k: _yi(v) for k, v in d.items()}
    for p, d in (out.get("period_trend") or {}).items():
        out["period_trend"][p] = {k: _yi(v) for k, v in d.items()}
    for p, d in (out.get("main_business") or {}).get("P", {}).items():
        d["total"] = _yi(d.get("total"))
        d["items"] = [[i[0], _yi(i[1]), _yi(i[2])] for i in d.get("items", [])]
    ev = out.get("ev_items")
    if ev:
        out["ev_items"] = {k: (v if k == "报告期" else _yi(v)) for k, v in ev.items()}
    bs = out.get("balance_sheet") or {}
    for k, series in bs.get("data", {}).items():
        bs["data"][k] = {y: _yi(v) for y, v in series.items()}
    return out


# --------------------------------------------------------------------------- S2 (BME JSON)


class Bme:
    def __init__(self, h: dict):
        self.h = h
        self.years = h["years"]  # ascending 'YYYYMMDD'
        self.m = h["metrics"]

    def v(self, key: str, year: str):
        met = self.m.get(key)
        if not met:
            return None
        try:
            return met["values"][self.years.index(year)]
        except (ValueError, IndexError):
            return None

    def why(self, key: str, year: str):
        met = self.m.get(key) or {}
        return (met.get("missing_reasons") or {}).get(year)

    def flags(self, key: str, year: str):
        r = self.why(key, year)
        return r if r else ""


def _sum(*xs):
    xs = [x for x in xs if x is not None]
    return sum(xs) if xs else None


def _ratio(a, b):
    return None if a is None or not b else a / b


# Paired-line divergence scan: line A should follow line B. The sheet reports growth(A) − growth(B)
# in percentage points per year plus the latest absolute changes, so a percentage never travels
# without its base. Keys are BME metric ids; a list is summed, None entries are skipped.
# Formula: scripts/calc.py growth_gap. Evidence only — the panel decides what a gap means.
DIVERGENCE_PAIRS = [
    # income statement
    ("IS", "营业成本", ["raw:cost_of_goods_sold"], "营业收入", ["raw:revenue"]),
    ("IS", "销售费用", ["raw:selling_expenses"], "营业收入", ["raw:revenue"]),
    ("IS", "管理费用", ["raw:admin_expenses"], "营业收入", ["raw:revenue"]),
    ("IS", "研发费用", ["raw:rd_expenses"], "营业收入", ["raw:revenue"]),
    ("IS", "所得税费用", ["raw:income_tax_expense"], "利润总额", ["raw:pretax_profit"]),
    ("IS", "少数股东损益", ["raw:minority_income"], "净利润", ["raw:net_income_total"]),
    # balance sheet against the flow that drives it
    ("BS", "应收票据及应收账款", ["raw:receivables_combined"], "营业收入", ["raw:revenue"]),
    ("BS", "存货", ["raw:inventory"], "营业成本", ["raw:cost_of_goods_sold"]),
    ("BS", "预付款项", ["raw:prepayments"], "营业成本", ["raw:cost_of_goods_sold"]),
    ("BS", "其他应收款", ["raw:other_receivables_combined", "raw:other_receivables"], "营业收入", ["raw:revenue"]),
    ("BS", "应付票据及应付账款", ["raw:payables_combined"], "营业成本", ["raw:cost_of_goods_sold"]),
    ("BS", "合同负债+预收款项", ["raw:contract_liabilities", "raw:advances_from_customers"], "营业收入", ["raw:revenue"]),
    ("BS", "固定资产+在建工程", ["raw:ppe", "raw:construction_in_progress"], "营业收入", ["raw:revenue"]),
    ("BS", "无形资产+商誉+开发支出", ["raw:intangible_assets", "raw:goodwill", "raw:development_expenditure"], "营业收入", ["raw:revenue"]),
    ("BS", "货币资金", ["raw:cash_and_equivalents"], "有息负债", ["raw:short_term_borrowings", "raw:current_portion_lt_debt", "raw:long_term_borrowings", "raw:bonds_payable", "raw:short_term_bonds_payable", "raw:lease_liabilities"]),
    ("BS", "净经营资产 NOA", ["noa"], "营业总收入", ["raw:total_revenue"]),
    # cash flow against the accrual line it should track
    ("CF", "经营现金流净额 CFO", ["raw:cfo"], "净利润", ["raw:net_income_total"]),
    ("CF", "销售商品收到的现金", ["raw:cash_received_from_sales"], "营业收入", ["raw:revenue"]),
    ("CF", "购买商品支付的现金", ["raw:cash_paid_for_goods"], "营业成本", ["raw:cost_of_goods_sold"]),
    ("CF", "支付给职工的现金", ["raw:cash_paid_to_employees"], "营业收入", ["raw:revenue"]),
    ("CF", "支付的各项税费", ["raw:cash_paid_for_taxes"], "利润总额", ["raw:pretax_profit"]),
    ("CF", "购建长期资产支付 capex", ["raw:capex_paid"], "折旧摊销 D&A", ["da_total"]),
    ("CF", "分配股利利润或偿付利息支付", ["raw:dividends_and_interest_paid"], "经营现金流净额 CFO", ["raw:cfo"]),
    ("CF", "取得借款收到的现金", ["raw:cash_from_borrowings"], "购建长期资产支付 capex", ["raw:capex_paid"]),
]


def _val(B: "Bme", keys: list[str], year: str):
    """Sum of the listed metrics for a year (yuan); None when none of them is present.
    For an alias list (first key preferred) pass the alias first: the first present value wins
    when the keys describe the same line (`*_combined` over its component)."""
    if keys and keys[0].endswith("_combined"):
        for k in keys:
            v = B.v(k, year)
            if v is not None:
                return v
        return None
    return _sum(*(B.v(k, year) for k in keys))


def divergence_block(B: "Bme", ys: list[str], window: int = 5) -> dict:
    """Rows of DIVERGENCE_PAIRS × the last `window` fiscal years: gap in percentage points
    (growth A − growth B, `calc.growth_gap`), plus latest-year levels and absolute changes in 亿元."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("calc", Path(__file__).resolve().parent.parent / "scripts" / "calc.py")
    calc = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(calc)
    full = B.years
    prev = {full[i]: (full[i - 1] if i else None) for i in range(len(full))}
    fys = ys[:window]  # descending
    rows = []
    for group, a_label, a_keys, b_label, b_keys in DIVERGENCE_PAIRS:
        gaps, latest = {}, None
        for y in fys:
            py = prev.get(y)
            if not py:
                gaps[y] = None
                continue
            a1, a0, b1, b0 = _val(B, a_keys, y), _val(B, a_keys, py), _val(B, b_keys, y), _val(B, b_keys, py)
            if None in (a1, a0, b1, b0) or a0 <= 0 or b0 <= 0:
                gaps[y] = None
                g = None
            else:
                g = calc.growth_gap(a_new=a1, a_old=a0, b_new=b1, b_old=b0)
                gaps[y] = g["gap_pp"]
            if y == fys[0]:
                latest = {"a_yi": _yi(a1), "b_yi": _yi(b1),
                          "delta_a_yi": _yi(a1 - a0) if None not in (a1, a0) else None,
                          "delta_b_yi": _yi(b1 - b0) if None not in (b1, b0) else None,
                          "growth_a": g["growth_a"] if g else None, "growth_b": g["growth_b"] if g else None,
                          "excess_a_yi": _yi(g["excess_a"]) if g else None}
        if all(v is None for v in gaps.values()) and (latest is None or latest["a_yi"] is None):
            continue  # line absent for this company (e.g. no R&D, no goodwill)
        rows.append({"group": group, "a": a_label, "b": b_label, "gaps_pp": gaps, **(latest or {})})
    ranked = sorted((r for r in rows if r.get("excess_a_yi") is not None), key=lambda r: -abs(r["excess_a_yi"]))
    return {"years": fys, "rows": rows,
            "largest_latest": [f"{r['a']} vs {r['b']} ({r['excess_a_yi']:+.1f}亿)" for r in ranked[:5]],
            "formula": "calc.growth_gap: gap_pp = 100 × (A_t/A_t−1 − B_t/B_t−1); excess_a = A_t−1 × (growth_a − growth_b); — when a base is ≤ 0 or a line is missing"}


def bme_blocks(h: dict, years: int = 10) -> dict:
    B = Bme(h)
    ys = sorted(B.years, reverse=True)
    if years > 0:
        ys = ys[:years]
    yi = lambda k, y: _yi(B.v(k, y))  # noqa: E731
    b: dict = {}
    b["raw_annual"] = [
        {
            "end_date": y,
            "revenue_yi": yi("raw:revenue", y), "total_revenue_yi": yi("raw:total_revenue", y),
            "operate_profit_yi": yi("raw:operating_profit_reported", y), "total_profit_yi": yi("raw:pretax_profit", y),
            "ni_parent_yi": yi("raw:net_income_parent", y), "ni_total_yi": yi("raw:net_income_total", y),
            "total_assets_yi": yi("raw:total_assets", y), "total_liab_yi": yi("raw:total_liabilities", y),
            "money_cap_yi": yi("raw:cash_and_equivalents", y), "inventories_yi": yi("raw:inventory", y),
            "parent_equity_yi": yi("raw:parent_equity", y), "total_share_yi": yi("shares", y),
            "cfo_yi": yi("raw:cfo", y), "capex_paid_yi": yi("raw:capex_paid", y), "fcf_simple_yi": yi("fcf_simple", y),
        }
        for y in ys
    ]
    ratio_cols = ["rnoa", "opm", "opm_core", "ato", "ollev", "flev", "nbc", "spread", "gross_margin", "roce_parent"]
    b["ratios"] = []
    for y in ys:
        rev = B.v("raw:total_revenue", y)
        b["ratios"].append({
            "end_date": y, "revenue_yi": _yi(rev), "oi_after_tax_yi": yi("oi_after_tax", y),
            "noa_yi": yi("noa_capital", y), "nfo_yi": yi("nfo_capital", y), "cse_yi": yi("te_capital", y),
            **{c: B.v(c, y) for c in ratio_cols}, "rotce": B.v("rotce_direct", y),
            "receivables_to_sales": _ratio(B.v("raw:receivables_combined", y), rev),
            "inventory_to_sales": _ratio(B.v("raw:inventory", y), rev),
            "ppe_to_sales": _ratio(B.v("raw:ppe", y), rev),
            "intangibles_to_sales": _ratio(B.v("raw:intangible_assets", y), rev),
            "customer_advances_to_sales": _ratio(_sum(B.v("raw:contract_liabilities", y), B.v("raw:advances_from_customers", y)), rev),
            "op_payables_to_sales": _ratio(B.v("raw:payables_combined", y), rev),
            "ratio_flags": B.flags("rnoa", y),
        })
    b["reformulated_is"] = [
        {
            "end_date": y, "revenue_yi": yi("raw:revenue", y), "oi_core_pretax_yi": yi("oi_core_pretax", y),
            "unusual_pretax_yi": yi("unusual_pretax", y), "oi_pretax_yi": yi("oi_pretax", y),
            "nfe_pretax_yi": yi("nfe_pretax", y), "tax_reported_yi": yi("raw:income_tax_expense", y),
            "tax_rate_assumed": B.v("tax_rate_assumed", y), "oi_after_tax_yi": yi("oi_after_tax", y),
            "oi_core_after_tax_yi": yi("oi_core_after_tax", y), "nfe_after_tax_yi": yi("nfe_after_tax", y),
            "ni_parent_yi": yi("raw:net_income_parent", y), "minority_income_yi": yi("raw:minority_income", y),
            "ci_total_yi": yi("raw:total_comprehensive_income", y),
        }
        for y in ys
    ]
    b["reformulated_bs"] = [
        {
            "end_date": y, "oa_yi": yi("oa", y), "ol_yi": yi("ol", y), "noa_yi": yi("noa", y), "fa_yi": yi("fa", y),
            "fo_yi": yi("fo", y), "nfo_yi": yi("nfo", y), "mi_yi": yi("minority_interests", y), "cse_yi": yi("cse_calc", y),
            "total_assets_yi": yi("raw:total_assets", y), "parent_equity_yi": yi("raw:parent_equity", y),
        }
        for y in ys
    ]
    b["cash"] = [
        {
            "end_date": y, "ni_total_yi": yi("raw:net_income_total", y), "cfo_yi": yi("raw:cfo", y),
            "capex_paid_yi": yi("raw:capex_paid", y), "disposals_yi": yi("raw:cash_from_asset_disposals", y),
            "fcf_simple_yi": yi("fcf_simple", y), "cash_conversion": B.v("cash_conversion", y),
            "cf_flags": B.flags("cash_conversion", y),
        }
        for y in ys
    ]
    prev = {B.years[i]: (B.years[i - 1] if i else None) for i in range(len(B.years))}
    b["capital"] = [
        {
            "end_date": y, "noa_begin_yi": _yi(B.v("noa", prev[y])) if prev[y] else None, "noa_end_yi": yi("noa", y),
            "delta_noa_yi": yi("delta_noa", y), "revenue_growth": B.v("revenue_growth", y), "noa_growth": B.v("noa_growth", y),
            "reinvestment_rate": B.v("reinvestment_rate", y), "capex_paid_yi": yi("raw:capex_paid", y),
            "da_yi": yi("da_total", y), "capex_to_da": B.v("capex_to_da", y), "fcf_from_oi_yi": yi("fcf_from_oi", y),
            "cap_flags": B.flags("reinvestment_rate", y),
        }
        for y in ys
    ]
    b["working_capital"] = [
        {"end_date": y, **{c: B.v(c, y) for c in ["dso", "dio", "dpo", "ccc", "advance_days", "ccc_net_advances", "owc_pct_sales", "incr_owc_per_incr_revenue"]},
         "wc_flags": B.flags("ccc", y)}
        for y in ys
    ]
    b["residual_income"] = [
        {
            "end_date": y, **{c: B.v(c, y) for c in ["r_op_assumed", "r_e_assumed", "pm", "pm_core", "rnoa_open", "ato_open", "spread_op", "roce_open"]},
            "reoi_yi": yi("reoi", y), "reoi_core_yi": yi("reoi_core", y), "re_common_yi": yi("re_common", y),
            "delta_reoi_yi": yi("delta_reoi", y), "ri_flags": B.flags("reoi", y),
        }
        for y in ys
    ]
    b["valuation"] = [
        {
            "end_date": y, "price": B.v("price", y), "shares_yi": yi("shares", y), "market_cap_yi": yi("market_cap", y),
            "market_ev_yi": yi("market_ev", y), **{c: B.v(c, y) for c in ["r_op_assumed", "r_e_assumed", "g_assumed"]},
            "v_equity_reoi_flat_yi": yi("v_equity_reoi_flat", y), "v_equity_reoi_g_yi": yi("v_equity_reoi_g", y),
            "v_per_share": B.v("v_per_share", y), "v_to_p": B.v("v_to_p", y), "trailing_pe": B.v("trailing_pe", y),
            "forward_pe_market": B.v("forward_pe_market", y), "normal_pe": B.v("normal_pe", y),
            "implied_g_reoi": B.v("implied_g_reoi", y), "implied_g_fcf": B.v("implied_g_fcf", y),
            "implied_r_op": B.v("implied_r_op", y),
        }
        for y in ys[:3]
    ]
    b["divergence"] = divergence_block(B, ys)
    b["coverage"] = []
    b["reverse_curve"] = []
    b["market_latest"] = []
    b["latest_quarters"] = []
    return b


def bme_peers(root: Path, index: list[dict], me: dict, year: str, limit: int = 12) -> list[dict]:
    """Same Tushare industry, same fiscal year, from the local per-company JSON (average basis)."""
    rows = []
    for c in index:
        if c.get("industry") != me.get("industry") or not c.get("available") or year[:4] not in [y[:4] for y in c.get("years", [])]:
            continue
        p = bme_company_path(root, c["ts_code"])
        if not p.exists():
            continue
        B = Bme(_load(p))
        if year not in B.years:
            continue
        rows.append({
            "ts_code": c["ts_code"], "name": c["name"], "end_date": year,
            "revenue_yi": _yi(B.v("raw:total_revenue", year)), "rnoa": B.v("rnoa", year), "opm": B.v("opm", year),
            "ato": B.v("ato", year), "flev": B.v("flev", year), "gross_margin": B.v("gross_margin", year),
            "market_cap_yi": _yi(B.v("market_cap", year)),
        })
    rows.sort(key=lambda r: -(r["revenue_yi"] or 0))
    return rows[:limit]


# --------------------------------------------------------------------------- optional DuckDB supplement


def open_db():
    try:
        import duckdb  # noqa
    except ImportError:
        sys.exit(
            "duckdb python module not found. Run with "
            "/Users/lin/Desktop/business-model-explorer/.venv/bin/python or drop --duckdb"
        )
    import duckdb

    return duckdb.connect(DUCKDB_PATH, read_only=True)


def df_rows(con, sql, params=()):
    cur = con.execute(sql, params)
    cols = [d[0] for d in cur.description]
    return [dict(zip(cols, r)) for r in cur.fetchall()]


def duck_extras(con, ts_code: str) -> dict:
    """What the S2 JSON does not carry: quarterly filings, reverse curve, daily_basic, coverage."""
    b: dict = {}
    dedupe = "update_flag desc, f_ann_date desc, _fetched_at desc"
    # Latest quarterly filings: cumulative YTD as filed, plus single-quarter revenue/NI
    # de-cumulated only when the immediately preceding quarter of the same year exists
    # (missing stays missing). BS items are point-in-time; OI sq from the Penman table.
    b["latest_quarters"] = df_rows(
        con,
        f"""
        with i as (select * from (select end_date, f_ann_date, update_flag, revenue, n_income_attr_p,
                       row_number() over (partition by end_date order by {dedupe}) rn
                   from raw_income where ts_code=? and substr(end_date,5,4) in ('0331','0630','0930','1231')) where rn=1),
             sq as (select end_date, f_ann_date, update_flag, revenue, n_income_attr_p,
                       case substr(end_date,5,4) when '0331' then revenue
                            else case when lag(end_date) over w = substr(end_date,1,4) ||
                                 (case substr(end_date,5,4) when '0630' then '0331' when '0930' then '0630' else '0930' end)
                                 then revenue - lag(revenue) over w end end as revenue_sq,
                       case substr(end_date,5,4) when '0331' then n_income_attr_p
                            else case when lag(end_date) over w = substr(end_date,1,4) ||
                                 (case substr(end_date,5,4) when '0630' then '0331' when '0930' then '0630' else '0930' end)
                                 then n_income_attr_p - lag(n_income_attr_p) over w end end as ni_parent_sq
                   from i window w as (partition by substr(end_date,1,4) order by end_date)),
             bs as (select * from (select end_date, money_cap, inventories, total_assets,
                        total_hldr_eqy_exc_min_int, total_share,
                        row_number() over (partition by end_date order by {dedupe}) rn
                    from raw_balancesheet where ts_code=? and substr(end_date,5,4) in ('0331','0630','0930','1231')) where rn=1),
             cf as (select * from (select end_date, n_cashflow_act, c_pay_acq_const_fiolta,
                        row_number() over (partition by end_date order by {dedupe}) rn
                    from raw_cashflow where ts_code=? and substr(end_date,5,4) in ('0331','0630','0930','1231')) where rn=1),
             pi as (select end_date, oi_after_tax from reformulated_is
                    where ts_code=? and period_kind='single_quarter')
        select sq.end_date, sq.f_ann_date, sq.update_flag,
               sq.revenue/1e8 as revenue_ytd_yi, sq.revenue_sq/1e8 as revenue_sq_yi,
               sq.n_income_attr_p/1e8 as ni_parent_ytd_yi, sq.ni_parent_sq/1e8 as ni_parent_sq_yi,
               pi.oi_after_tax/1e8 as oi_after_tax_sq_yi,
               bs.money_cap/1e8 as money_cap_yi, bs.inventories/1e8 as inventories_yi,
               bs.total_assets/1e8 as total_assets_yi,
               bs.total_hldr_eqy_exc_min_int/1e8 as parent_equity_yi,
               bs.total_share/1e8 as total_share_yi,
               cf.n_cashflow_act/1e8 as cfo_ytd_yi, cf.c_pay_acq_const_fiolta/1e8 as capex_ytd_yi
        from sq left join bs on sq.end_date=bs.end_date left join cf on sq.end_date=cf.end_date
                left join pi on sq.end_date=pi.end_date
        order by sq.end_date desc limit 8
        """,
        [ts_code, ts_code, ts_code, ts_code],
    )
    b["coverage"] = df_rows(
        con,
        """select (select max(end_date) from raw_income where ts_code=?) as income_last_end,
                  (select max(end_date) from raw_balancesheet where ts_code=?) as bs_last_end,
                  (select max(end_date) from raw_cashflow where ts_code=?) as cf_last_end,
                  (select max(end_date) from reformulated_bs where ts_code=?) as penman_last_end,
                  (select max(trade_date) from raw_daily_basic where ts_code=?) as daily_basic_last_trade""",
        [ts_code] * 5,
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
    return b


# --------------------------------------------------------------------------- cross-check


def cross_check(avl: dict, duck: dict) -> list[dict]:
    """Compare the same concepts across sources for overlapping years. S1 in 亿元."""
    ann = avl.get("annual", {})
    rows = {r["end_date"][:4]: r for r in duck["raw_annual"]}
    checks = []
    pairs = [
        # (S1 key, duckdb field, note)
        ("营业收入", "revenue_yi", "S1 营业收入 vs S2 raw_income.revenue (营业收入). S2 *ratios* use 营业总收入 instead."),
        ("利润总额", "total_profit_yi", ""),
        ("归母净利润", "ni_parent_yi", ""),
        ("总资产", "total_assets_yi", ""),
        ("总负债", "total_liab_yi", ""),
        ("货币资金", "money_cap_yi", ""),
        ("存货", "inventories_yi", ""),
        ("经营现金净额", "cfo_yi", ""),
        ("总股本", "total_share_yi", "亿股; S2 = year-end share count at price date (daily_basic), S1 = reported 总股本"),
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
                    "bme": _r(dval, 4),
                    "pct_diff": _r(diff, 4) if diff is not None else None,
                    "flag": "MISMATCH" if (diff is not None and abs(diff) > 0.01) else ("n/a" if diff is None else "ok"),
                    "note": note,
                }
            )
    # Latest quarters: S1 quarterly_revenue is single-quarter 营业收入; S2 side is
    # de-cumulated from raw_income cumulative 营业收入 (Qn − Qn−1, Q1 as filed).
    qrows = {r["end_date"]: r for r in duck.get("latest_quarters", [])}
    qr = avl.get("quarterly_revenue", {})
    qsuffix = {"Q1": "0331", "Q2": "0630", "Q3": "0930", "Q4": "1231"}
    for y in qr.get("years", []):
        for qk, suf in qsuffix.items():
            aval = qr.get("data", {}).get(str(y), {}).get(qk)
            d = qrows.get(f"{y}{suf}")
            if aval is None or d is None:
                continue
            dval = d.get("revenue_sq_yi")
            diff = _pct_diff(aval, dval)
            checks.append(
                {
                    "concept": f"营业收入单季{qk}",
                    "year": str(y),
                    "avl": _r(aval, 4),
                    "bme": _r(dval, 4),
                    "pct_diff": _r(diff, 4) if diff is not None else None,
                    "flag": "MISMATCH" if (diff is not None and abs(diff) > 0.01) else ("n/a" if diff is None else "ok"),
                    "note": "S1 single-quarter 营业收入 vs S2 raw_income de-cumulated 营业收入.",
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
    L.append(f"- **S1 AshareValueLine** version `{meta['avl_version']}` (financials fetched {avl.get('fetched_at')}, quote {avl.get('quote_refreshed_at')}), local JSON `{avl_url}`; S1 amounts converted from yuan to 亿元 here.")
    L.append(f"- **S2 business-model-explorer** local JSON `{meta['bme_path']}` exported {meta['bme_exported_at']} (Tushare annual statements + Penman reformulation); amounts converted from yuan to 亿元 here. Annual periods {meta['bme_first_year']}–{meta['bme_last_year']} only: no quarterly rows, no filing dates, no required-return reverse curve (see the `--duckdb` supplement).")
    if duck.get("extras"):
        cov = duck["coverage"][0] if duck.get("coverage") else {}
        L.append(f"- **S2 DuckDB supplement** (`--duckdb`): raw income filed through {cov.get('income_last_end')}, balance sheet {cov.get('bs_last_end')}, cash flow {cov.get('cf_last_end')}; Penman tables through {cov.get('penman_last_end')}; raw_daily_basic last trade {cov.get('daily_basic_last_trade')} (December windows only, not a live quote).")
    L.append("")
    # Quote
    q = avl.get("quote", {})
    m = duck["market_latest"][0] if duck.get("market_latest") else {}
    L.append("## Market snapshot")
    L.append(f"- S1 quote {q.get('trade_date')}: price {q.get('price')} · PE {q.get('pe')} · PE(TTM) {q.get('pe_ttm')} · PB {q.get('pb')} · total mkt cap {q.get('total_mv_yi')} 亿 · shares {q.get('total_share_yi')} 亿股")
    if m:
        L.append(f"- S2 raw_daily_basic {m.get('trade_date')}: close {m.get('close')} · PE(TTM) {m.get('pe_ttm')} · PB {m.get('pb')} · total_mv {_fmt((m.get('total_mv') or 0)/1e4,1)} 亿 (Tushare 万元 converted) · dv_ttm {m.get('dv_ttm')}%")
    L.append("")
    # Cross-check
    L.append("## Cross-check S1 vs S2 (same concept, same period; annual and latest single quarters)")
    bad = [c for c in checks if c["flag"] == "MISMATCH"]
    L.append(f"{len(checks)} comparisons, **{len(bad)} mismatches >1%**." + (" All matched." if not bad else ""))
    if bad:
        L.append("")
        L.append(_table(bad, [("concept", "concept", {"raw": True}), ("year", "year", {"raw": True}), ("S1 AVL", "avl", {"nd": 2}), ("S2 BME", "bme", {"nd": 2}), ("diff", "pct_diff", {"pct": True}), ("note", "note", {"raw": True})]))
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
    pt = avl.get("period_trend", {})
    if pt:
        L.append("### S1 · Latest periods (period_trend; 营业收入 is cumulative YTD, 存货/应收 point-in-time, 亿元)")
        L.append("| period | 营业收入 YTD | 存货 | 应收账款 | 应收票据及应收账款 |")
        L.append("|---|---|---|---|---|")
        for p in sorted(pt, reverse=True)[:8]:
            d = pt[p]
            L.append(f"| {p} | " + " | ".join(_fmt(d.get(k), 2) for k in ["营业收入", "存货", "应收账款", "应收票据及应收账款"]) + " |")
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
    L.append("## S2 · Raw annual statements (亿元; BME annual consolidated, `raw:*` metrics)")
    L.append(_table(duck["raw_annual"], [
        ("FY", "end_date", {"raw": True}), ("营业收入", "revenue_yi", {}), ("营业总收入", "total_revenue_yi", {}),
        ("营业利润", "operate_profit_yi", {}), ("归母净利润", "ni_parent_yi", {}), ("总资产", "total_assets_yi", {}),
        ("货币资金", "money_cap_yi", {}), ("存货", "inventories_yi", {}), ("归母权益", "parent_equity_yi", {}),
        ("CFO", "cfo_yi", {}), ("capex paid", "capex_paid_yi", {}), ("FCF simple", "fcf_simple_yi", {}),
        ("股本(亿,年末)", "total_share_yi", {"nd": 2}),
    ]))
    if duck.get("latest_quarters"):
        L.append("## S2 · Latest quarterly filings (亿元; YTD = cumulative as filed, sq = single quarter; BS items point-in-time)")
        L.append("Single-quarter 营业收入/归母净利润 de-cumulated from raw_income (Qn − Qn−1; Q1 as filed; missing prior quarter → —). OI after tax sq from `reformulated_is` single_quarter rows. update_flag 1 = revised filing.")
        L.append(_table(duck.get("latest_quarters", []), [
            ("period", "end_date", {"raw": True}), ("营业收入YTD", "revenue_ytd_yi", {}), ("营业收入sq", "revenue_sq_yi", {}),
            ("归母净利YTD", "ni_parent_ytd_yi", {}), ("归母净利sq", "ni_parent_sq_yi", {}), ("OI after tax sq", "oi_after_tax_sq_yi", {}),
            ("货币资金", "money_cap_yi", {}), ("存货", "inventories_yi", {}), ("总资产", "total_assets_yi", {}),
            ("归母权益", "parent_equity_yi", {}), ("股本(亿)", "total_share_yi", {"nd": 2}),
            ("CFO YTD", "cfo_ytd_yi", {}), ("capex YTD", "capex_ytd_yi", {}),
            ("announced", "f_ann_date", {"raw": True}), ("upd", "update_flag", {"raw": True}),
        ]))
    else:
        L.append("## S2 · Latest quarterly filings")
        L.append("_Not in the S2 JSON (annual only). S1 period_trend above carries 营业收入 YTD, 存货 and 应收账款 by period; run with `--duckdb` for 归母净利润, CFO, capex and OI by quarter._")
        L.append("")
    L.append("## S2 · Penman ratios (average-capital basis: BME `rnoa`, `noa_capital` …)")
    L.append("Definitions: OI = operating income after tax (reformulated, ≠ 营业利润); NOA = OA − OL; NFO = FO − FA (negative = net financial assets); RNOA = OI/NOA; OPM = OI/营业总收入; ATO = 营业总收入/NOA; FLEV = NFO/CSE; spread = RNOA − NBC; ROCE = RNOA + FLEV × spread.")
    L.append(_table(duck["ratios"], [
        ("FY", "end_date", {"raw": True}), ("营业总收入", "revenue_yi", {}), ("OI after tax", "oi_after_tax_yi", {}),
        ("NOA", "noa_yi", {}), ("NFO", "nfo_yi", {}), ("CSE", "cse_yi", {}),
        ("RNOA", "rnoa", {"pct": True}), ("OPM", "opm", {"pct": True}), ("OPM core", "opm_core", {"pct": True}),
        ("ATO", "ato", {"nd": 2}), ("FLEV", "flev", {"nd": 2}), ("NBC", "nbc", {"pct": True}),
        ("spread", "spread", {"pct": True}), ("ROCE", "rotce", {"pct": True}), ("GM", "gross_margin", {"pct": True}),
        ("flags", "ratio_flags", {"raw": True}),
    ]))
    L.append("### S2 · Balance-sheet intensity (share of 营业总收入; simple ratios computed in fetch.py from raw lines: receivables = raw:receivables_combined, PP&E = raw:ppe, customer advances = raw:contract_liabilities + raw:advances_from_customers, op. payables = raw:payables_combined)")
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
            ]))
    L.append("## S2 · Cash reconciliation (亿元)")
    L.append(_table(duck["cash"], [
        ("FY", "end_date", {"raw": True}), ("NI total", "ni_total_yi", {}), ("CFO", "cfo_yi", {}), ("capex paid", "capex_paid_yi", {}),
        ("disposals", "disposals_yi", {}), ("FCF simple", "fcf_simple_yi", {}), ("CFO/NI", "cash_conversion", {"nd": 2}),
        ("flags", "cf_flags", {"raw": True}),
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
    dv = duck.get("divergence") or {}
    if dv.get("rows"):
        fys = dv["years"]
        L.append("## S2 · Paired-line divergence scan (question generator; `calc.growth_gap`)")
        L.append("Each row pairs a line A with the line B it should follow. Cells are growth(A) − growth(B) in percentage points for that fiscal year; "
                 "— means a base ≤ 0 or a missing line. The last five columns give the latest fiscal year in 亿元: levels, absolute changes, and "
                 "the excess move of A (A_t−1 × gap), i.e. how much of ΔA following B would not explain — rank by that column, not by the "
                 "percentage, because a small base turns any move into a large gap. A gap is a question to ask, not a finding.")
        L.append("| group | A | follows B | " + " | ".join(f"gap {y[:4]}" for y in fys) + " | A latest | ΔA | B latest | ΔB | excess ΔA |")
        L.append("|---|---|---|" + "---|" * len(fys) + "---|---|---|---|---|")
        for r in dv["rows"]:
            cells = [("—" if r["gaps_pp"].get(y) is None else f"{r['gaps_pp'][y]:+.1f}") for y in fys]
            L.append(f"| {r['group']} | {r['a']} | {r['b']} | " + " | ".join(cells)
                     + f" | {_fmt(r.get('a_yi'))} | {_fmt(r.get('delta_a_yi'))} | {_fmt(r.get('b_yi'))} | {_fmt(r.get('delta_b_yi'))} | {_fmt(r.get('excess_a_yi'))} |")
        L.append("")
        if dv.get("largest_latest"):
            L.append(f"Largest excess moves in FY{fys[0][:4]} (by 亿, not by %): " + "; ".join(dv["largest_latest"]) + ".")
        L.append("")
    L.append("## S2 · Residual operating income (亿元; r_op assumed, not a conclusion)")
    L.append(_table(duck["residual_income"], [
        ("FY", "end_date", {"raw": True}), ("r_op", "r_op_assumed", {"pct": True}), ("PM", "pm", {"pct": True}),
        ("PM core", "pm_core", {"pct": True}), ("RNOA (open)", "rnoa_open", {"pct": True}), ("ATO (open)", "ato_open", {"nd": 2}),
        ("spread", "spread_op", {"pct": True}), ("ReOI", "reoi_yi", {}), ("ReOI core", "reoi_core_yi", {}), ("ΔReOI", "delta_reoi_yi", {}),
        ("RE common", "re_common_yi", {}), ("flags", "ri_flags", {"raw": True}),
    ]))
    L.append("## S2 · Valuation anchors (model defaults r_op/r_e/g are assumptions; use the reverse curve, not the point value)")
    L.append(_table(duck["valuation"], [
        ("FY", "end_date", {"raw": True}), ("price (year-end)", "price", {"nd": 2}),
        ("mkt cap", "market_cap_yi", {}), ("EV", "market_ev_yi", {}), ("r_op", "r_op_assumed", {"pct": True}), ("g", "g_assumed", {"pct": True}),
        ("V ReOI flat", "v_equity_reoi_flat_yi", {}), ("V ReOI g", "v_equity_reoi_g_yi", {}),
        ("V/P", "v_to_p", {"nd": 2}), ("trailing PE", "trailing_pe", {}), ("fwd PE mkt", "forward_pe_market", {}),
        ("normal PE", "normal_pe", {}), ("implied g (ReOI)", "implied_g_reoi", {"pct": True}), ("implied g (FCF)", "implied_g_fcf", {"pct": True}),
    ]))
    if duck.get("reverse_curve"):
        L.append(f"### S2 · Reverse-engineered growth the market price implies, by required return (end {duck['reverse_curve_end_date']})")
        L.append(_table(duck["reverse_curve"], [
            ("r", "r", {"pct": True}), ("implied g ReOI", "implied_g_reoi", {"pct": True}),
            ("implied g FCF", "implied_g_fcf", {"pct": True}), ("implied g equity", "implied_g_equity", {"pct": True}),
        ]))
    if not duck.get("reverse_curve"):
        L.append("_S2 reverse curve (implied growth across required returns) is not in the JSON; only the implied g at the assumed r above. Run with `--duckdb` for the curve._")
        L.append("")
    L.append("## S2 · Industry peers (same Tushare industry, same FY, average basis; top 12 by 营业总收入, from local BME JSON)")
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
    ap.add_argument("--years", type=int, default=10, help="S2 annual history depth; 0 = every year in the JSON (FY2014 onward)")
    ap.add_argument("--bme-root", default=BME_PAGES_ROOT, help="folder holding business-model-explorer[-data] Pages builds")
    ap.add_argument("--avl-root", default=AVL_API_ROOT, help="AshareValueLine api/v1/a_share folder")
    ap.add_argument("--no-avl", action="store_true", help="skip S1 AshareValueLine")
    ap.add_argument("--duckdb", action="store_true", help="add quarterly NI/CFO/capex/OI, reverse curve and daily_basic from bme.duckdb")
    args = ap.parse_args()

    bme_root, avl_root = Path(args.bme_root), Path(args.avl_root)
    index = bme_index(bme_root)
    me = resolve_code(index, args.company)
    ts_code, name, industry = me["ts_code"], me["name"], me["industry"]
    if not me.get("available"):
        reason = (me.get("unavailable") or {}).get("reason")
        sys.exit(f"{ts_code} {name}: no S2 history in the BME JSON (reason: {reason}). Financial-format and new listings are excluded.")
    cache_dir = Path(__file__).resolve().parent / "cache" / ts_code
    out = Path(args.out) if args.out else cache_dir
    out.mkdir(parents=True, exist_ok=True)

    bme_path = bme_company_path(bme_root, ts_code)
    if not bme_path.exists():
        sys.exit(f"S2 JSON missing: {bme_path}")
    h = _load(bme_path)
    duck = bme_blocks(h, args.years)

    avl, avl_raw, avl_path, version, avl_note = {}, {}, "", "offline", ""
    if not args.no_avl:
        p = avl_root / "companies" / f"{ts_code}.json"
        if p.exists():
            avl_raw = _load(p)
            avl, avl_path, version = avl_to_yi(avl_raw), str(p), avl_raw.get("version", "unknown")
        else:
            avl_note = f"S1 JSON not found: {p}"
            print(f"WARNING: {avl_note}", file=sys.stderr)
            version, avl_path = "unavailable", f"MISSING {p}"
        if avl_raw:
            (out / "avl_raw.json").write_text(json.dumps(avl_raw, ensure_ascii=False, indent=1), encoding="utf-8")
    (out / "bme_raw.json").write_text(json.dumps(h, ensure_ascii=False, indent=1), encoding="utf-8")

    latest_year = max(h["years"])
    duck["peers"] = bme_peers(bme_root, index, me, latest_year)

    if args.duckdb:
        con = open_db()
        extras = duck_extras(con, ts_code)
        duck.update(extras)
        duck["extras"] = True
    checks = cross_check(avl, duck) if avl else []
    meta = {
        "ts_code": ts_code,
        "name": name,
        "industry": industry,
        "generated_at": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
        "avl_version": version,
        "avl_path": avl_path,
        "avl_note": avl_note,
        "bme_path": str(bme_path),
        "bme_exported_at": h.get("exported_at"),
        "bme_first_year": min(h["years"])[:4],
        "bme_last_year": latest_year[:4],
        "duckdb_used": bool(args.duckdb),
    }
    md = render_md(meta, avl, avl_path, duck, checks)
    (out / "factsheet.md").write_text(md, encoding="utf-8")
    (out / "factsheet.json").write_text(
        json.dumps({"meta": meta, "cross_check": checks, "bme": duck, "avl": avl}, ensure_ascii=False, indent=1, default=str),
        encoding="utf-8",
    )
    bad = [c for c in checks if c["flag"] == "MISMATCH"]
    print(f"{ts_code} {name} ({industry}) → {out}")
    print(f"  S1 AVL version {version} (quote {avl.get('quote', {}).get('trade_date')}); S2 BME exported {h.get('exported_at')}, FY{meta['bme_first_year']}–FY{meta['bme_last_year']}")
    print(f"  cross-check: {len(checks)} comparisons, {len(bad)} mismatches >1%")
    for c in bad[:10]:
        print(f"    {c['concept']} {c['year']}: S1 {c['avl']} vs S2 {c['bme']} ({c['pct_diff']:+.1%})")


if __name__ == "__main__":
    main()
