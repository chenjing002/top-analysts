# Workpaper — 000807.SZ 云铝股份 · session 2026-11-24-01 · round 01

Data: S1 AshareValueLine `20261121_201610` (quote 2026-11-20, price 21.01); S2 BME local JSON
exported 2026-11-22 (annual FY2014–FY2025) + DuckDB supplement (quarterly filings through
20260930, `raw_daily_basic` last 20251231). Amounts in 亿元 unless noted. All computed figures use
`scripts/calc.py` (named below) or state formula + inputs. This is a system-test rerun of
2026-11-23-05 r1 after the self-improving loop and Greenblatt 1.1; the prior session is kept.

## §0 Cross-check resolution (before the panel speaks)

98 S1/S2 comparisons, **1 mismatch >1%**: 总股本 FY2019 — S1 31.28亿 vs S2 26.07亿 (+20.0%).

**Explained, not a data error.** S1 uses the annual-report balance-sheet share capital
(`balancesheet.total_share`); the S2 cross-check line uses `daily_basic.total_share` at the
year-end price date (listed shares). The FY2019 placement cash arrived within FY2019:
`raw:cash_from_equity_issuance` FY2019 = 30.07亿, of which 8.96亿 is subsidiary minority
contributions (`raw:minority_equity_contributions`), so parent placement ≈ 21.11亿; share capital
rose 26.0684 → 31.2821亿 (+5.2137亿 shares at ¥1 par) and capital reserve 64.40 → 80.23亿. The
new shares listed in 2020, so `daily_basic` at 20191231 still showed 26.07亿.

**Consequence:** only FY2019–20 per-share figures are affected. For year-end book per share use
the balance-sheet count (S1); for market-based historical per-share series note the daily_basic
lag. No 10-year total (profit, capex, FCF) is touched. The series the story rests on (decade
profit/capex/FCF, FY2025–26 valuation) are clean. → not an opening topic.

## Business scorecard (the decade FY2016–FY2025 is the subject; 2026 is read against it)

**1. What kind of business? — GOOD in harvest, commodity spread not franchise; the decade splits in two.**
Ten-year parent NI 230.1亿 on capex 209.9亿 (`calc.fcf` sums). But FY2016–20 build-out: parent NI
Σ6.99亿 on capex Σ167.3亿, FCF Σ−47.8亿 (gruesome, airline-like); FY2021–25 harvest: NI Σ223.1亿
on capex Σ42.7亿, FCF Σ308.6亿. The harvest looks great only because growth stopped needing
capital — it is a cost-position commodity smelter, not a pricing-power franchise.

**2. Does cash back the profit? — Yes over the decade, but current FCF overstates owner cash.**
10y FCF 260.8亿 = 1.13× parent NI 230.1亿 (`calc.fcf_conversion`). Capex/D&A: decade 1.36,
harvest 0.47 (capex 42.7 vs D&A 91.2). Harvest capex 6–7亿/yr is far below D&A ~18.6亿 — either
true maintenance is genuinely low (asset base mature, staggered pot-relining) or the company is
under-investing. Maintenance-vs-growth split is an **estimate**, not a reported figure; the
annual-report capex note and 大修 (pot-relining) treatment would close it.

**3. What drives the return? — Margin and turnover up on a growing base over the decade; a shrinking base only in the harvest window.**
DuPont (year-end basis, `calc.dupont`): net margin 0.71% (2016) → 10.08% (2025); asset turnover
0.49 → 1.36; equity multiplier 3.46 → 1.38. Penman RNOA (average basis, S2) 5.0% → 28.6% = OPM
5.2% → 12.2% × ATO 0.96 → 2.35. **Windows explicit (P-015):** over FY2016–25 NOA GREW 170.5 →
254.3亿 (+49%), so the decade RNOA rise is margin × turnover on a growing base, not shrinkage.
Shrinkage is FY2021–25 only: NOA peak 291.6亿 (2021) → 254.3亿 (2025), −12.8%, worth about a
quarter of that sub-window's RNOA rise. NFO +133.8亿 (2018) → −99.9亿 (FY2025) → net cash 211.8亿
(2026Q3).

**4. Is it cheap, and what is the floor? — Priced at mid-cycle no-growth, not at the 2026 peak.**
At S1 quote 2026-11-20 (21.01): mkt cap 728.6亿, PB 1.73 (B 420.9亿 2026Q3), PE(TTM) 5.5 on peak
TTM parent NI 132.6亿, FCF yield 20.8% on peak TTM FCF 151.5亿 — both peak mirages. Net cash
211.8亿 = 29% of cap. Asset floor ≈ 272亿 ≈ 37% of cap (50% haircut on fixed assets + intangibles,
80% on inventory, receivables at face, less operating payables and minorities; all lines at 2026Q3
except other payables at FY2025, labelled — Appendix E). On the harvest median parent NI 44.1亿
the price is 16.5× and the zero-growth return is 6.1%; on 55亿 it is 13.2× and 7.6%. Reverse curve
(`calc.implied_growth_re`, B 420.9, P 728.6): at r 8%, E 55 implies g ≈ 1.1%, E 44 implies
g ≈ 4.6%; at r 7% / 10% the E 55 implied g is −1.3% / +5.8%.

**5. What did management do with the cash? — Placements funded the build-out; payout now rising; hoard idle.**
Dividends Σ57.7亿 over the decade (2017 1.82, 2021 3.92, 2022 5.55, 2023 7.98, 2024 14.22,
2025 24.24); FY2025 payout 40.0% (24.24/60.55). Three parent placements ≈ 87.4亿 (2016 36.3,
2019 21.1, 2021 30.0); shares 26.07 → 34.68亿 (+33%). No buybacks. The 211.8亿 net-cash hoard is
the swing factor: dividend, acquisition, or policy reinvestment?

**6. Where does the story bend? — Five headlines.**
(a) FY2018 parent loss −14.7亿; (b) FY2020 capex peak 52.9亿 then FY2021 harvest begins (capex
12.7亿); (c) FY2023 revenue −12% (Yunnan dry-season power-rationing hypothesis, unverified);
(d) 2026 cost-side margin spike — 9M26 revenue +19.4% YoY while cost of sales −4.1%, cumulative
gross margin 15.4% (2025 9M) → 32.0% (2026 9M); (e) stock −36% YTD (32.84 → 21.01) while TTM
parent NI rose ~165%. **Verdict:** the market is pricing spread normalization, not the boom.

---

## Appendix A — 10-year series (S2 raw annual, 亿元; FY2016–FY2025)

| FY | parent NI | CFO | capex | D&A | FCF (`calc.fcf`) | revenue | NOA end | NFO end |
|---|---|---|---|---|---|---|---|---|
| 2016 | 1.11 | 9.11 | 14.2 | 9.83 | −5.1 | 155.4 | 170.5 | 71.8 |
| 2017 | 6.57 | 20.32 | 28.1 | 11.44 | −7.8 | 221.3 | 207.4 | 98.0 |
| 2018 | −14.66 | 3.37 | 36.7 | 12.72 | −33.3 | 216.9 | 226.0 | 133.8 |
| 2019 | 4.95 | 36.84 | 35.4 | 13.81 | 1.4 | 242.8 | 254.8 | 129.1 |
| 2020 | 9.03 | 49.81 | 52.9 | 15.71 | −3.1 | 295.7 | 288.8 | 151.2 |
| 2021 | 33.19 | 69.62 | 12.7 | 18.71 | 56.9 | 416.7 | 291.6 | 82.5 |
| 2022 | 45.69 | 69.14 | 9.6 | 18.20 | 59.5 | 484.6 | 275.7 | 23.0 |
| 2023 | 39.56 | 58.71 | 7.3 | 17.56 | 51.4 | 426.7 | 270.7 | −21.7 |
| 2024 | 44.12 | 69.47 | 6.6 | 18.08 | 62.9 | 544.5 | 257.4 | −64.1 |
| 2025 | 60.55 | 84.32 | 6.4 | 18.60 | 77.9 | 600.4 | 254.3 | −99.9 |

Sums: NI 230.09, CFO 470.72, capex 209.96, D&A 154.66, FCF 260.77. D&A =
`raw:supp_depreciation + supp_intangible_amortization + supp_lt_deferred_amortization +
supp_rou_asset_depreciation` (cash-flow indirect-method add-backs). NFO here is the reformulated
`noa`/`nfo` (FA includes 其他权益工具投资); the strict `calc.net_cash` (cash + trading assets −
interest-bearing debt) is 87.9亿 FY2025 and 211.8亿 2026Q3 — state which definition is used.

## Appendix B — DuPont and RNOA decomposition

DuPont year-end (`calc.dupont(ni, revenue, total_assets, parent_equity)`):
- 2016: margin 0.0071 × turnover 0.4868 × multiplier 3.4562 = ROE 0.0120
- 2020: 0.0305 × 0.7210 × 3.4745 = 0.0765
- 2021: 0.0797 × 1.1013 × 2.0800 = 0.1825
- 2025: 0.1008 × 1.3592 × 1.3791 = 0.1890
(S1 reported ROE 2025 = 20.06% uses average equity; year-end basis gives 18.9% — basis stated.)

RNOA average basis (S2 `rnoa`,`opm`,`ato`): 2016 5.0% = 5.2% × 0.96; 2025 28.6% = 12.2% × 2.35.
NOA peak 291.6 (2021) → 254.3 (2025), −12.8%. `calc.rnoa_decomp` confirms PM × ATO.

## Appendix C — TTM bridge, valuation, reverse curve (S1 quote 2026-11-20)

TTM parent NI = FY2025 60.5 − 9M25 44.0 + 9M26 116.1 = **132.6亿** (S2 quarterly filings).
TTM CFO = 84.3 − 69.8 + 141.3 = 155.8; TTM capex = 6.4 − 4.9 + 2.8 = 4.3; TTM FCF
(`calc.fcf`) = **151.5亿**. PE(TTM) = 728.6/132.6 = 5.49; FCF yield = 151.5/728.6 = 20.8%.
PB = 728.6/420.9 = 1.73. These are peak readings.

Net cash 2026Q3 (`calc.net_cash(193.71, 38.07, [0, 6.52, 13.34, 0, 0.13])`) = **211.79亿** = 29.1%
of cap. EV (`calc.enterprise_value(728.62, 19.99, 48.67, 193.71, 38.07)`, all cash deducted) =
565.5亿. Greenblatt excess-cash range: operating cash 1–2% of sales ≈ 6–12亿, so excess ≈
200–206亿; EV under recoverable-cash scenarios is shown in Appendix G (card 1.1 availability check).

Reverse curve (`calc.implied_growth_re(price=728.62, book=420.9, earnings_next=E, r)`):
| E (normalized parent NI) | zero-g return (`calc.zero_growth_return`) | g @ r7% | g @ r8% | g @ r10% |
|---|---|---|---|---|
| 44.12 (harvest median) | 6.06% | 2.24% | 4.60% | 9.34% |
| 33.19 (harvest low) | 4.55% | 5.79% | 8.16% | 12.89% |
| 55 | 7.55% | −1.30% | 1.07% | 5.80% |
| 60 | 8.23% | −2.92% | −0.56% | 4.18% |
| 132.6 (TTM peak) | 18.20% | −26.5% | −24.2% | −19.4% |

Like-for-like (`calc.like_for_like_earnings(55, 211.79, pretax_yield, 0.25)`): stripping the
net-cash carry at an assumed 1.5–2.0% pre-tax yield gives adjusted E 52.6–51.8亿 against an
ex-cash price 516.8亿 → zero-growth return ~10.0–10.2%. The carry yield is an **assumption**
(FY2025 reformulated net financial income was only 0.4亿 after tax); label it.

## Appendix D — 2026 cost-side margin walk (DuckDB `raw_income`, report_type='1', deduped)

Query: `SELECT end_date, revenue, oper_cost FROM raw_income WHERE ts_code='000807.SZ' AND
report_type='1'` deduped by `update_flag DESC, f_ann_date DESC, _fetched_at DESC`. Cumulative GM
= (revenue − oper_cost)/revenue (营业收入 basis):
- 2025Q1 9.96% → 2025H1 14.07% → 2025 9M 15.39% → FY2025 16.79%
- 2026Q1 31.58% → 2026H1 31.84% → 2026 9M 32.04%
9M YoY: revenue 526.16/440.72 − 1 = **+19.4%**; oper_cost 357.59/372.90 − 1 = **−4.1%**.
Single-Q3 GM: 2026Q3 32.44% vs 2025Q3 17.95%. Revenue up while cost of sales falls → the margin
spike is **cost-side**, consistent with an alumina-price-collapse hypothesis (KB H-000807-001,
unverified — no local commodity price series). Confirms KB F-000807-002.

## Appendix E — Floor build (labelled haircuts, one window per line)

Current floor ≈ **271.9亿** ≈ 37.3% of cap, ¥7.84/share (`calc.per_share`), all at 2026Q3 except
where labelled:
net cash 211.79 (S1 2026Q3) + 50% × (fix_assets_total 192.50 + cip_total 4.70 = 197.20, DuckDB
`raw_balancesheet` 20260930) = 98.60 + 50% × intangibles 26.42 (2026Q3) = 13.21 + 80% × inventory
39.29 (2026Q3) = 31.43 + receivables (15.99 + 12.04) = 28.03 (S1 2026Q3) − operating payables
62.46 (S1 2026Q3 应付票据及应付账款 54.11 + **FY2025** other payables 8.35, labelled: DuckDB
`oth_payable` at 20260930 is null) − minorities 48.67 (2026Q3).
Formula: `211.79 + 0.5*197.20 + 0.5*26.42 + 0.8*39.29 + 28.03 - 62.46 - 48.67 = 271.93`.
Sensitivity on the same build: 100% fixed-asset recovery → 271.93 + 98.60 = **370.5亿**; the 50%
case is the 271.9亿 headline. (The earlier 279/163 pair mixed FY2025 net cash with current
haircuts and is withdrawn.) The floor protects about a third of the cap; net cash alone covers 29%.

## Appendix F — Capital allocation

Dividends (S1 分红): 2017 1.82, 2021 3.92, 2022 5.55, 2023 7.98, 2024 14.22, 2025 24.24; Σ57.73.
FY2025 payout 24.24/60.55 = 40.0%. Placements (`raw:cash_from_equity_issuance` less
`raw:minority_equity_contributions`): 2016 36.34−0.01≈36.3; 2019 30.07−8.96≈21.1; 2021
30.49−0.49≈30.0; Σ≈87.4亿. Shares 26.0684 → 34.6796亿 = +33.0%. No 注销 buybacks in the record.

## Appendix G — Greenblatt ROC and EV yield (card 1.1)

ROC = core EBIT / (NWC + NFA), `calc.greenblatt_roc`. EBIT proxy = S2 `oi_core_pretax`
(reformulated core operating income pre-tax). **The proxy gap is closable locally** (observer
round-01 check): DuckDB `raw_income` carries biz_tax_surchg, sell_exp, admin_exp, rd_exp, so
bottom-up core EBIT = 营业收入 − 营业成本 − 税金及附加 − 销售/管理/研发费用 rebuilds to harvest
median **60.85亿** (excl 其他收益) / 61.51亿 (incl) vs proxy 61.8, and decade median **38.57亿** vs
proxy 40 — gap ≤1.5亿, verdict unchanged. NWC = S2 `owc_end`; NFA = `raw:ppe +
raw:construction_in_progress`.
- 2021: 72.9 / (−31.1 + 277.8) = 29.5%
- 2023: 56.5 / (−8.3 + 234.9) = 24.9%
- 2025: 88.9 / (2.8 + 206.1) = 42.6%
All comfortably above the 20% pre-tax hurdle — but 2025 is a strong year and the denominator is
shrinking. Normalized core EBIT (harvest `oi_core_pretax` 72.9/61.8/56.5/61.5/88.9, median 61.8)
is the band to test, not the 2025 peak.

EV yield (`calc.ebit_ev_yield` + `calc.after_tax` @25%, labelled default): harvest-mid EBIT 61.8 →
10.93% pre-tax / 8.20% after-tax at EV 565.5 (all cash deducted), 9.07% / 6.80% at EV 681.39 (half
cash recoverable). Rebuilt decade-mid EBIT 38.57 → 6.82% / 5.11% and 5.66% / 4.24% — the low end
fails the 6% after-tax bogey at both cash assumptions; the harvest mid passes. Card 1.1
availability check: the 211.8亿 cash is real (reconciles to CFO) but its reachability (controller,
related-party alumina purchases, policy reinvestment) is unverified — show EV at full vs partial
cash recovery rather than a flat haircut. Rebuilt decade-mid after-tax yields 5.11% / 4.25%.

---

## Divergence scan (paired lines, `calc.growth_gap`; same window per pair; ranked by |excess_a|)

A gap is a question, not a finding. Every item below has an owner in the round.

| # | Pair (A follows B) | Window | growth A / B | gap pp | excess_a 亿 | Owner / where asked |
|---|---|---|---|---|---|---|
| 1 | 营业成本 follows 营业收入 | 9M26 vs 9M25 | −4.1% / +19.4% | −23.5 | −87.6 | li-lu t5 (cost-side windfall, bear case) |
| 2 | CFO follows parent NI | FY2025 vs FY2024 | +21.4% / +37.2% | −15.9 | −11.0 | warren-buffett t1 (cash backs profit?) |
| 3 | 应收账款 follows 营业收入 | Sept26 vs Sept25 | +28.2% / +19.4% | +8.8 | +1.1 | stephen-penman t10 (receivables quality) |
| 4 | capex follows D&A | FY2025 vs FY2024 | −3.0% / +2.9% | −5.9 | −0.4 | warren-buffett t1 / greenblatt t2 (maintenance) |

**Receivables seasonality (P-014/P-015):** the alarming "+365%" (3.44亿 FY2025 → 15.99亿 Sept26)
compares a year-end collection point with a Q3 point. The same-window series is FY2024 3.44 →
Sept25 12.47 → FY2025 3.44 → Sept26 15.99: receivables build through the year and are collected at
year-end. Year-on-year at Q3 the gap is only +8.8pp / +1.1亿 excess — small against 526亿 of 9M
revenue. The aging note (AR2026) would confirm collectability; the floor counts 28.03亿 at face.

---

## Appendix H — Normalized band (`calc.normalized_band`)

Parent NI decade FY2016–25: low −14.66, mid 21.11, high 60.55, mean 23.01 (includes the
build-out loss years — not the right normal for a completed, deleveraged smelter).
Parent NI harvest FY2021–25: low 33.19, **mid 44.12**, high 60.55, mean 44.62.
The mechanical mid-cycle anchor is ~44亿; arguing "normal" above it (toward 55–60) requires a
case that the 2021–22 power-rationing/alumina-cost depression was temporary AND that part of the
2026 cost windfall persists. That case is the round's central disagreement.