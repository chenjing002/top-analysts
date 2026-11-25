#!/usr/bin/env python3
"""Shared financial formulas for the panel and the round checker.

One definition per formula, with the basis stated, so the discussion, the workpaper and
`scripts/check_round.py` all compute the same number. Every function carries a doctest;
run `python3 scripts/calc.py --test`. Command line: `python3 scripts/calc.py <fn> k=v ...`.

Conventions
- Money in 亿元 unless the function says otherwise (`yi()` converts yuan).
- Rates as decimals: 8% is 0.08. Percent is a display concern.
- "begin" means the opening balance of the period (Penman); "avg" means the average of
  opening and closing. Say which one you used — S2 `ratios_annual` uses `basis=average`.
"""
from __future__ import annotations

import math
import statistics
import sys


# ---------- units and growth ----------

def yi(x_yuan: float) -> float:
    """Yuan to 亿元 (1亿 = 1e8 yuan; 1 billion = 10亿).

    >>> yi(600_429_400_000)
    6004.294
    """
    return x_yuan / 1e8


def pct_change(new: float, old: float) -> float:
    """Simple growth (new/old − 1). Undefined when old ≤ 0.

    >>> round(pct_change(600.4, 416.7), 4)
    0.4408
    """
    if old <= 0:
        raise ValueError("pct_change needs a positive base")
    return new / old - 1


def cagr(begin: float, end: float, years: float) -> float:
    """Compound annual growth over `years` periods.

    >>> round(cagr(16, 31, 35), 4)
    0.0191
    """
    if begin <= 0 or end <= 0 or years <= 0:
        raise ValueError("cagr needs positive begin, end and years")
    return (end / begin) ** (1 / years) - 1


def growth_gap(a_new: float, a_old: float, b_new: float, b_old: float) -> dict:
    """Paired-line divergence: growth of line A minus growth of line B over the same period, in
    percentage points, with both absolute changes so a percentage never travels without its base.
    A is the line that should follow B (cost of sales follows revenue, receivables follow revenue,
    inventory follows cost of sales, capex follows D&A, CFO follows net income). A positive gap
    means A outgrew B. `excess_a` = a_old × (growth_a − growth_b) is the part of ΔA that following
    B would not explain, in A's own unit: rank divergences by it, not by the percentage, because a
    small base turns any move into a huge percentage. Undefined when either old value is not
    positive (sign change, zero base).

    >>> g = growth_gap(a_new=88.9, a_old=61.5, b_new=600.4, b_old=544.5)
    >>> round(g['gap_pp'], 1), round(g['delta_a'], 1), round(g['delta_b'], 1), round(g['excess_a'], 1)
    (34.3, 27.4, 55.9, 21.1)
    """
    if a_old <= 0 or b_old <= 0:
        raise ValueError("growth_gap needs positive bases for both lines")
    ga, gb = pct_change(a_new, a_old), pct_change(b_new, b_old)
    return {"growth_a": ga, "growth_b": gb, "gap_pp": 100 * (ga - gb),
            "delta_a": a_new - a_old, "delta_b": b_new - b_old, "excess_a": a_old * (ga - gb)}


# ---------- cash and owner earnings ----------

def fcf(cfo: float, capex: float) -> float:
    """Free cash flow = cash from operations − capital expenditure (capex as a positive outflow).

    >>> round(fcf(470.7, 209.9), 1)
    260.8
    """
    return cfo - capex


def fcf_conversion(sum_fcf: float, sum_net_income: float) -> float:
    """Decade test: cumulative FCF / cumulative net income. >1 means cash backed the profit.

    >>> round(fcf_conversion(260.8, 230.1), 2)
    1.13
    """
    return sum_fcf / sum_net_income


def owner_earnings(net_income: float, da: float, maintenance_capex: float) -> float:
    """Buffett (1986 Appendix): reported earnings + depreciation/amortisation − the capex needed
    to hold unit volume. Maintenance capex is an estimate; label it.

    >>> round(owner_earnings(60.5, 18.6, 18.6), 1)
    60.5
    """
    return net_income + da - maintenance_capex


def net_cash(cash: float, trading_financial_assets: float, debt_items: list[float]) -> float:
    """Cash + trading financial assets − interest-bearing debt (all items, same balance-sheet date).

    >>> round(net_cash(193.71, 38.07, [6.52, 13.34, 0.13]), 2)
    211.79
    """
    return cash + trading_financial_assets - sum(debt_items)


def enterprise_value(market_cap: float, debt: float, minority: float, cash: float,
                     trading_financial_assets: float = 0.0, operating_cash: float = 0.0) -> float:
    """EV = market cap + interest-bearing debt + minority interest − cash − trading financial assets
    + operating cash kept back. `operating_cash` is the part of cash the business needs (often
    1–2% of sales, an analyst assumption); default 0 strips all cash.

    >>> round(enterprise_value(728.62, 19.99, 48.67, 193.71, 38.07), 2)
    565.5
    """
    return market_cap + debt + minority - cash - trading_financial_assets + operating_cash


def like_for_like_earnings(earnings: float, excess_cash: float, pretax_yield: float, tax: float) -> float:
    """Earnings with the after-tax interest on `excess_cash` removed, for use when the price
    or EV also has that cash stripped. Stripping cash from P without stripping its income from E
    overstates the earnings yield.

    >>> round(like_for_like_earnings(47.99, 98.85, 0.03, 0.15), 2)
    45.47
    """
    return earnings - excess_cash * pretax_yield * (1 - tax)


def after_tax(x: float, tax: float) -> float:
    """x × (1 − tax). S2 defaults tax to 25%; a company-specific rate changes the answer.

    >>> after_tax(70, 0.25)
    52.5
    """
    return x * (1 - tax)


# ---------- returns and decomposition ----------

def dupont(net_income: float, revenue: float, assets: float, equity: float) -> dict:
    """ROE = margin × turnover × multiplier. Pass the same basis (begin or avg) for assets and
    equity and say which.

    >>> d = dupont(60.55, 600.4, 609.6, 441.76)
    >>> round(d['margin'], 4), round(d['turnover'], 3), round(d['multiplier'], 3), round(d['roe'], 4)
    (0.1008, 0.985, 1.38, 0.1371)
    """
    margin = net_income / revenue
    turnover = revenue / assets
    multiplier = assets / equity
    return {"margin": margin, "turnover": turnover, "multiplier": multiplier, "roe": margin * turnover * multiplier}


def rnoa_decomp(oi_after_tax: float, sales: float, noa: float) -> dict:
    """Penman: RNOA = PM × ATO with PM = OI/Sales and ATO = Sales/NOA. `noa` is beginning NOA in
    Penman's text; S2 ratios use average NOA. State the basis.

    >>> d = rnoa_decomp(72.9, 600.4, 254.3)
    >>> round(d['pm'], 4), round(d['ato'], 3), round(d['rnoa'], 4)
    (0.1214, 2.361, 0.2867)
    """
    pm = oi_after_tax / sales
    ato = sales / noa
    return {"pm": pm, "ato": ato, "rnoa": pm * ato}


def leverage_equation(rnoa: float, flev: float, nbc: float) -> float:
    """Penman: ROCE = RNOA + FLEV × (RNOA − NBC). The second term is leverage-made return.

    >>> round(leverage_equation(0.20, 0.5, 0.04), 3)
    0.28
    """
    return rnoa + flev * (rnoa - nbc)


def greenblatt_roc(ebit: float, net_working_capital: float, net_fixed_assets: float) -> float:
    """Greenblatt return on tangible capital = EBIT / (net working capital + net fixed assets).
    Pre-tax, excludes goodwill and excess cash. Not comparable to RNOA or ROE.

    >>> round(greenblatt_roc(70, 30, 200), 4)
    0.3043
    """
    return ebit / (net_working_capital + net_fixed_assets)


def ebit_ev_yield(ebit: float, ev: float) -> float:
    """Greenblatt earnings yield = EBIT / EV (pre-tax). Use normalized EBIT for cyclicals.

    >>> round(ebit_ev_yield(70, 565.5), 4)
    0.1238
    """
    return ebit / ev


# ---------- Penman residual earnings and reverse engineering ----------

def residual_earnings(earnings: float, book_begin: float, r: float) -> float:
    """RE = earnings − r × beginning book value.

    >>> round(residual_earnings(55, 420.9, 0.08), 3)
    21.328
    """
    return earnings - r * book_begin


def implied_growth_re(price: float, book: float, earnings_next: float, r: float) -> float:
    """Penman reverse engineering, equity basis: with RE growing at g forever after year 1,
    P = B + RE1/(r − g)  ⇒  g = r − RE1/(P − B). Requires P > B. Inputs: today's price (market cap), today's book,
    next-year earnings (or normalized), hurdle r.

    >>> round(implied_growth_re(728.62, 420.9, 55, 0.08), 4)
    0.0107
    """
    if price <= book:
        raise ValueError("price must exceed book for a positive RE premium")
    re1 = residual_earnings(earnings_next, book, r)
    return r - re1 / (price - book)


def implied_growth_reoi(ev: float, noa: float, oi_next: float, r_f: float) -> float:
    """Operations basis: EV (= P + NFO) against NOA with ReOI1 = OI1 − r_F × NOA.
    g = r_F − ReOI1/(EV − NOA).

    >>> round(implied_growth_reoi(693, 6.4, 46.2, 0.08), 4)
    0.0135
    """
    if ev <= noa:
        raise ValueError("EV must exceed NOA")
    reoi1 = oi_next - r_f * noa
    return r_f - reoi1 / (ev - noa)


def implied_return_re(price: float, book: float, earnings_next: float, g: float) -> float:
    """The r that solves P = B + (E1 − rB)/(r − g): r = E1/P + g × (P − B)/P.
    With g = 0 this is the zero-growth return E/P.

    >>> round(implied_return_re(728.62, 420.9, 55, 0.0), 4)
    0.0755
    >>> round(implied_return_re(728.62, 420.9, 55, 0.0107), 4)
    0.08
    """
    return earnings_next / price + g * (price - book) / price


def implied_earnings_re(price: float, book: float, r: float, g: float = 0.0) -> float:
    """The next-year earnings the price implies, given r and g: E1 = rB + (r − g)(P − B).
    Use it when the price is below book (implied_growth_re needs P > B): with g = 0 it is r × P,
    the steady profit a below-book price asks the business to earn on the current book.

    >>> round(implied_earnings_re(336.45, 930.94, 0.08), 3)
    26.916
    >>> round(implied_earnings_re(728.62, 420.9, 0.08, 0.0107), 1)
    55.0
    """
    return r * book + (r - g) * (price - book)


def zero_growth_return(earnings: float, price: float) -> float:
    """E/P: the return earned if residual earnings never grow. Same as implied_return_re(g=0).

    >>> round(zero_growth_return(60, 728.62), 4)
    0.0823
    """
    return earnings / price


def value_re_constant_growth(book: float, earnings_next: float, r: float, g: float) -> float:
    """V = B + RE1/(r − g), the scenario value for fixed r and g (S2 `v_per_share` style).

    >>> round(value_re_constant_growth(420.9, 55, 0.08, 0.0107), 1)
    728.7
    """
    if r <= g:
        raise ValueError("r must exceed g")
    return book + residual_earnings(earnings_next, book, r) / (r - g)


# ---------- cyclicals ----------

def normalized_band(series: list[float]) -> dict:
    """Mid-cycle band from an annual series: low = min, mid = median, high = max, mean. Use a
    full cycle (both a trough and a peak year) or say the window is truncated.

    >>> b = normalized_band([55, 60, 45, 90, 50])
    >>> b['low'], b['mid'], b['high'], round(b['mean'], 1)
    (45, 55, 90, 60)
    """
    return {"low": min(series), "mid": statistics.median(series), "high": max(series),
            "mean": statistics.mean(series)}


def per_share(x: float, shares: float) -> float:
    """Amount per share with both in the same unit (e.g. 亿元 and 亿 shares → 元).

    >>> round(per_share(151.5, 34.68), 2)
    4.37
    """
    return x / shares


# ---------- cli ----------

_PUBLIC = {k: v for k, v in list(globals().items()) if callable(v) and not k.startswith("_") and k not in ("annotations",)}


def _main(argv: list[str]) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        for name, fn in sorted(_PUBLIC.items()):
            if fn.__module__ == __name__ and fn.__doc__:
                print(f"  {name:28s} {fn.__doc__.strip().splitlines()[0]}")
        return 0
    if argv[0] == "--test":
        import doctest
        failed, total = doctest.testmod(sys.modules[__name__])
        print(f"calc: {total - failed}/{total} doctests passed")
        return 1 if failed else 0
    fn = _PUBLIC.get(argv[0])
    if fn is None or fn.__module__ != __name__:
        print(f"unknown function {argv[0]}")
        return 2
    kwargs = {}
    for kv in argv[1:]:
        k, v = kv.split("=", 1)
        if v.startswith("["):
            kwargs[k] = [float(x) for x in v.strip("[]").split(",") if x]
        else:
            kwargs[k] = float(v)
    out = fn(**kwargs)
    if isinstance(out, dict):
        for k, v in out.items():
            print(f"{k} = {v:.6g}")
    else:
        print(f"{out:.6g}")
    return 0


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
