# Workpaper — 000915.SZ 华特达因 · session 2026-11-25-01 · round 01

Data: S1 AshareValueLine `20261121_201610` (quote 2026-11-20, price 18.57, mkt cap 43.52亿, 2.3433亿
shares); S2 BME local JSON exported 2026-11-22 (annual FY2014–FY2025) + DuckDB supplement (quarterly
filings through 20260930; `raw_daily_basic` last 20251231). Amounts in 亿元 unless noted. Computed
figures use `scripts/calc.py` (named) or state formula + inputs. DuckDB queries dedupe `raw_*` rows
by `update_flag DESC, f_ann_date DESC, _fetched_at DESC`, `report_type='1'`.
Controller per `raw_stock_basic`: 山东省人民政府国有资产监督管理委员会 (地方国企, Shandong SASAC).
The parent's stake in the operating subsidiary (达因药业) is **not in the local data**; the
minority share of consolidated profit (S2) is the only proxy (→ open questions).

## §0 Cross-check

98 S1/S2 comparisons, **0 mismatches >1%**. No reconciliation topic; Buffett opens.

## Business scorecard (the decade FY2016–FY2025 is the subject; 2026 is read against it)

**1. What kind of business? — GREAT on the decade record: profit nearly tripled on less operating capital.**
Penman OI after tax (S2 reformulated_is) 3.69 (FY2016) → 9.96 (FY2025), ×2.70 (`calc.cagr` 11.6%/yr).
Net operating assets (S2 reformulated_bs) 12.21 → 8.55, **−3.66**. Ten-year Σ OI 66.00 vs Σ (OI − ΔNOA)
(S2 `fcf_from_oi`) 69.06: more cash than profit. **Float split (Observer fix):** operating assets
16.79 → 14.91 (−1.88), operating liabilities 4.58 → 6.36 (+1.78, 49% of the NOA fall); that float
(taxes payable, other payables, contract liabilities, payroll) unwound to 2.84 by 2026Q3, so the capital
release is about half genuine and half liability timing that can reverse. The rise is the pharma business, not price: pharma
segment (S1 main_business 医药产品) revenue 11.24 (2020) → 22.15 (2025), +97.0%, at a segment gross
margin of 83.8% (2020) → 84.6% (2025) — flat. The consolidated gross margin's climb from 60.85% (2020)
to 85.11% (2025) is **mix**: environmental equipment (3.49 revenue, 2020), education (2.10), road
materials, parks and electronics (≈1.4) were exited 2021–2023 (non-pharma 2020 revenue 6.97 at ~24%
GM; ≈0.33 by 2025). Verdict caveat: one segment, product split not in local data — whether this is
one product (伊可新 vitamin AD drops is the commonly cited franchise; **unverified locally**) is the
durability question.

**2. Does cash back the profit? — Yes, fully, until 2026.**
Σ FY2016–25 (S2 cash_summary): CFO 77.73, capex 11.66, FCF 66.07 vs total net income 67.97
(`calc.fcf_conversion` 0.972) and parent NI 36.09. Capex 11.66 vs D&A 6.39 (1.83×), but front-loaded:
2016–19 capex 2.30/1.78/1.31/1.72 against D&A 0.4–0.6 (the build); 2023–25 capex 0.51/0.44/0.48 below
D&A 0.75–0.77. Maintenance capex **estimate** ≈ D&A ≈ 0.7/yr; the rest of the decade's capex was growth.
Cash-collection oddity: 销售商品收到的现金 34.75 vs 营业收入 22.28 in FY2025 (1.56×; 2016 1.13×, 2020
1.20×, VAT-gross norm ≈1.13×), while 支付其他与经营活动有关的现金 rose 4.25 (2020) → 12.17 (2025) against
selling + admin + R&D expense of ≈6.7. A gross flow of roughly 8–10亿/yr runs through both lines —
hypothesis: invoices collected gross and distributor rebates/market fees paid back in cash, with
revenue booked net. Not settled locally (AR 2025 cash-flow notes 收到/支付的其他与经营活动有关的现金 and
the revenue-recognition note would settle it).

**3. What drives the return? — Margin and an almost capital-free operation; the cash pile and the
minority dilute it.**
DuPont year-end (`calc.dupont`, parent NI / 营业收入 / total assets / parent equity):
2016 margin 12.8% × turnover 0.62 × multiplier 1.93 = ROE 15.5%; 2020 16.0% × 0.49 × 1.89 = 14.9%;
2025 24.0% × 0.45 × 1.75 = 18.7%. The multiplier is minority interest, not debt (total liabilities
6.47 of 49.98 assets; FO 0.11). Turnover falls because cash piles up. Penman (S2 ratios, average
basis): RNOA 31.0% (2016) → 38.3% (2020) → 102.1% (2025) = OPM 44.7% × ATO 2.29; FLEV −0.78 (net
financial assets), total-equity ROCE 23.5%. Minorities took 46.9% of decade net income (31.88 of
67.97); 43.5% (2016) → 48.0% (2025) as pharma became nearly all the profit.

**4. Is it cheap, and what is the floor? — Cheap on last year, not on this year; half the floor is
the minority's.**
At S1 quote 2026-11-20: mkt cap 43.52, parent book 25.49 (2026Q3) → PB 1.71. Earnings yield
(`calc.zero_growth_return`) on FY2025 parent NI 5.35: 12.3%; on TTM parent NI 2.835 (= FY2025 5.351 −
9M25 4.081 + 9M26 1.565): **6.5%**. FCF: FY2025 group FCF 12.23; TTM CFO −0.16 (12.715 − 9.550 − 3.324)
and capex 0.16 → TTM FCF ≈ −0.32. FY2025 dividend (S1 年度现金分红总额) 5.86 = 13.5% of today's cap.
Book 2026Q3 (DuckDB raw_balancesheet / reformulated_bs): financial assets 21.82 = cash 5.38 + trading
financial assets 14.05 + other non-current financial assets 1.01 + investment property 1.38 (BME
classes investment property as financial); financial obligations 0.11 → NFA 21.71. NOA 14.67
(OA 17.51 − OL 2.84). Receivables 3.79 (notes 1.94 + accounts 1.84), inventory 1.13, fixed assets
≈7.7 (2026H1), intangibles 1.77, goodwill 0.26. No interest-bearing debt. Minority interest 10.89.
EV (`calc.enterprise_value`, cash + trading assets stripped, MI at book) 34.98.
**Floor (parent shareholders):** the consolidated NFA is shared with minorities. Bounds without an
ownership assumption: if the minority claim sits entirely on financial assets, parent NFA = 21.71 −
10.89 = **10.82**; if it sits entirely on operating assets, parent NFA = 21.71. So parent net
financial assets are 10.8–21.7亿 (25–50% of the cap) — both ends are limit cases (minorities owning none
of NOA, or 74% of it, against a 48% profit share). **Central case (Observer fix):** minorities own their
FY2025 profit share (4.93/10.29 = 48.0%) of a subsidiary holding all group NOA 14.67 → their claim on
financial assets = 10.89 − 0.480 × 14.67 = 3.85 → parent NFA ≈ **17.86亿 (41% of the cap; estimate)**.
**Reverse curve (P > B; `calc.implied_earnings_re`, g = 0, E = r × P):** r 8% → 3.48亿/yr of parent
earnings; r 10% → 4.35; r 12% → 5.22. Against FY2025 5.35 and TTM 2.835. `calc.implied_growth_re`
on E = 5.35: g −10.4% (r 8%), −5.5% (10%), −0.7% (12%); on E = 2.835: +3.6% (8%), +8.4% (10%), +13.3%
(12%). Round one argues r = 10% (SOE control, no debt, but a single-segment franchise whose 2026
revenue fell 45%) and shows 8% and 12%: ~~the price asks for parent earnings of about 4.4亿 a year
forever — a recovery most of the way back~~. **Corrected in round (t7, Penman):** E = r × P charges
the parent's cash the operating hurdle. Like-for-like (cash at face, P-007/P-012), the operating stake
is priced at about 25.7亿 (central case; limits 21.8–32.7亿) and needs **about 2.6亿/yr at 10%** (2.1 at
8%, 3.1 at 12%; limits 2.2–3.3 at 10%) against TTM parent operating profit ≈2.4–2.8, a TTM that still
holds three pre-break quarters while Q3 2026 alone lost 0.67 — the price bets Q3 was a one-off, not a
return to 2025. See A6 (revised after the Observer review).

**5. What did management do with the cash? — Paid out most of it; lately more than all of it.**
Declared cash dividends FY2016–25 (S1 分红) Σ23.23 vs parent NI 36.09 (64%); FY2024 5.86 vs NI 5.16
(114%), FY2025 5.86 vs 5.35 (110%). Cash dividends paid to minorities (S2 raw_cashflow
`incl_dvd_profit_paid_sc_ms`) 5.04 in each of 2024, 2025 and 9M2026 — the subsidiary distributes
roughly all it earns. Shares 1.80 → 2.34亿 in FY2017 with capital reserve unchanged (0.35 → 0.35):
a bonus issue (送股), not a cash raise. No equity issuance or buybacks in the decade (S2
`cash_from_equity_issuance` empty). No acquisitions of note (goodwill 0.26 throughout FY2021–25).

**6. Where does the story bend? — Five headlines.**
(a) 2021–23: the non-pharma exits; consolidated GM 60.9% → 86.4%, revenue base reset to pharma.
(b) 2020 → 2022: receivables (应收票据及应收账款, S2 raw) 5.46 → 2.48 while revenue rose 18.21 →
23.41 (DSO 122 → 38 days): a working-capital release that helped CFO 7.36 → 11.96.
(c) 2024: revenue −14.1% (24.84 → 21.34) but parent NI only −11.8% (5.85 → 5.16), Q3 2024 revenue 2.2
vs ~5.7 in other quarters — a first stumble, then FY2025 +4.4%.
(d) **2026: the break.** 9M revenue 8.82 vs 16.03 (−45.0%); Q3 single quarter 0.33 vs 4.32 (−92.3%),
below its own cost of sales 0.47; Q3 parent NI −0.67, OI after tax −1.34 (reformulated_is
single_quarter). 9M parent NI 1.56 vs 4.08 (−61.7%). 9M CFO −3.32 vs +9.55. H1 pharma revenue (S1
main_business) 8.31 vs 11.54 (−28.0%), segment GM 82.8% vs 86.0%. NOA rose 8.55 → 14.67 (+6.12) in
nine months: operating liabilities −3.52 (taxes payable 1.28 → 0.06, other payables 1.45 → 0.51,
contract liabilities 1.07 → 0.15), receivables 2.11 → 3.79 (+1.68), inventory 0.78 → 1.13.
(e) Price 33.04 (2025-12-31, S2 daily_basic) → 18.57 (S1 2026-11-20), −43.8%.
Verdict: a great business on the decade, whose 2026 record is a break the local data cannot explain.
Whether 2026 is a one-off charge (rebates, price protection, channel destock) or a lost franchise
is the whole valuation; with cash at face (A6) the price assumes roughly the depressed 2026 level
persists — a recovery would be upside, a further fall would not be covered.

**7. Divergence scan (FY2025, `calc.growth_gap`, ranked by excess move in 亿) — the question menu.**
| # | pair | gap / both changes | what would be surprising | owner |
|---|---|---|---|---|
| 1 | 销售商品收到的现金 vs 营业收入 | +18.6pp; cash +6.50 (28.25 → 34.75) vs revenue +0.94; excess **+5.3** | cash collected 1.56× revenue vs a VAT norm ≈1.13×; paired with other operating cash paid 12.17 | `stephen-penman` (and `li-lu` for the channel) |
| 2 | 分配股利利润或偿付利息支付 vs CFO | −36.8pp; dividends +0.00 (10.90 → 10.90) vs CFO +3.42; excess **−4.0** | flat payout above CFO in 2024 (10.90 vs 9.30); 2026 9M paid 9.73 against CFO −3.32 | `jeff-bezos` |
| 3 | CFO vs 净利润 | +34.5pp; CFO +3.42 vs NI +0.22; excess **+3.2** | receivables release (−1.07) and advances (+0.51) explain ≈1.6; rest unexplained | `stephen-penman` |
| 4 | NOA vs 营业总收入 | −26.3pp; NOA −2.40 vs revenue +0.94; excess **−2.9**; **sign flips in 2026**: NOA +6.12 in 9M while revenue −45% | operating capital shrank in 2025, then rebuilt fast as sales collapsed | `jeff-bezos` |
| 5 | 支付的各项税费 vs 利润总额 | +38.4pp; cash taxes +1.46 (3.57 → 5.03) vs pretax +0.29; excess **+1.4** | cash taxes include VAT; consistent with gross invoicing (item 1) — a test, not a finding | `stephen-penman` |
| — | 少数股东损益 vs 净利润 | minority 4.93 of 10.29 (48.0%), decade 46.9% | the listed company owns about half the profit it reports | `li-lu` / `joekray-mond` |
| — | 营业成本 vs 营业收入 | −35.9pp (2022), −38.8pp (2023) | explained by the segment exits (item 1): one-line note, not a question | `warren-buffett` |
Sign changes between years: receivables vs revenue (+15.5pp 2024 → −38.1pp 2025), NOA vs revenue
(+24.8 → −26.3), cost of sales vs revenue (+16.3 → −8.3). Items not reached go to
`next_question_candidates` with the pair named.

## Reference appendix

### A1. Ten-year series (S2 raw, 亿)
| FY | 营业收入 | 营业成本 | 销售费用 | 销售收现 | 其他经营付现 | CFO | capex | D&A(折旧) | parent NI | minority NI | MI (BS) | 分红 (S1) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 15.45 | 6.11 | 3.35 | 17.48 | 4.73 | 5.01 | 2.30 | 0.34 | 1.98 | 1.53 | 6.65 | 0.27 |
| 2017 | 17.67 | 5.71 | 4.80 | 18.60 | 4.63 | 4.26 | 1.78 | 0.36 | 2.43 | 2.08 | 7.19 | 0.59 |
| 2018 | 15.26 | 6.06 | 4.33 | 19.79 | 5.04 | 5.39 | 1.31 | 0.41 | 1.30 | 1.10 | 7.43 | 0.70 |
| 2019 | 18.00 | 7.35 | 4.45 | 16.51 | 4.10 | 2.44 | 1.72 | 0.50 | 2.04 | 1.55 | 8.36 | 0.70 |
| 2020 | 18.21 | 7.13 | 2.78 | 21.92 | 4.25 | 7.36 | 1.02 | 0.59 | 2.91 | 2.42 | 9.83 | 0.82 |
| 2021 | 20.27 | 6.31 | 3.72 | 24.48 | 5.04 | 7.56 | 1.20 | 0.64 | 3.80 | 3.24 | 11.55 | 1.87 |
| 2022 | 23.41 | 5.02 | 4.89 | 29.07 | 5.91 | 11.96 | 0.90 | 0.63 | 5.27 | 4.71 | 14.77 | 1.87 |
| 2023 | 24.84 | 3.38 | 6.32 | 29.68 | 7.39 | 11.75 | 0.51 | 0.68 | 5.85 | 5.42 | 15.15 | 4.69 |
| 2024 | 21.34 | 3.45 | 4.17 | 28.25 | 10.46 | 9.30 | 0.44 | 0.68 | 5.16 | 4.90 | 15.01 | 5.86 |
| 2025 | 22.28 | 3.32 | 4.92 | 34.75 | 12.17 | 12.72 | 0.48 | 0.64 | 5.35 | 4.93 | 14.90 | 5.86 |
D&A column is fixed-asset depreciation only (`supp_depreciation`); S2 capital_summary `da_total`
(incl. amortization) is 0.75 (FY2025) and Σ6.39 over the decade.

### A2. 2025–2026 quarters (DuckDB raw, single quarter de-cumulated; 亿)
| quarter | 营业收入 | 营业成本 | parent NI | OI after tax | CFO (sq) | 销售收现 (sq) | 其他经营付现 (sq) |
|---|---|---|---|---|---|---|---|
| 2025Q1 | 6.16 | 0.84 | 1.82 | 3.38 | 0.54 | 5.63 | 2.59 |
| 2025Q2 | 5.54 | 0.82 | 1.55 | 2.84 | 6.21 | 10.87 | 2.31 |
| 2025Q3 | 4.32 | 0.83 | 0.71 | 1.23 | 2.80 | 9.46 | 4.13 |
| 2025Q4 | 6.26 | 0.82 | 1.27 | 2.50 | 3.17 | 8.79 | 3.14 |
| 2026Q1 | 4.12 | 0.75 | 1.11 | 2.05 | 0.19 | 6.52 | 3.74 |
| 2026Q2 | 4.36 | 0.74 | 1.13 | 1.70 | −1.00 | 3.44 | 2.63 |
| 2026Q3 | 0.33 | 0.47 | −0.67 | −1.34 | −2.51 | 2.61 | 2.84 |
Q3 2026 asset impairment −0.26 (9M −0.26 vs H1 −0.01). Q3 2026 revenue below cost of sales is
consistent with a revenue deduction (rebate / price-protection / return provision) rather than a
pure volume fall — **hypothesis**; the Q3 2026 report notes would settle it.

### A3. 2026 balance-sheet walk (FY2025 → 2026Q3, 亿)
Cash 20.14 → 5.38 (−14.76): CFO −3.32, financing −9.87 (dividends 9.73: parent 4.69, minority 5.04),
investing −1.43 (trading assets 12.49 → 14.05); ≈0.14 residual is restricted cash outside cash
equivalents (not broken out locally). Parent equity 28.61 → 25.49 (NI +1.56, dividends −4.69). Minority
14.90 → 10.89 (minority NI +1.17, dividends −5.04). Liabilities 6.47 → 2.95.

### A4. Reverse curve detail (`calc.implied_growth_re`, P = 43.52, B = 25.49)
| r | E = 5.35 (FY2025) | E = 2.835 (TTM) | E implied at g = 0 |
|---|---|---|---|
| 8% | −10.4% | +3.6% | 3.48 |
| 10% | −5.5% | +8.4% | 4.35 |
| 12% | −0.7% | +13.3% | 5.22 |

### A5. Cash collected by quarter (销售商品提供劳务收到的现金, DuckDB raw_cashflow de-cumulated; 亿)
| year | Q1 | Q2 | Q3 | Q4 | FY | FY 营业收入 |
|---|---|---|---|---|---|---|
| 2022 | 6.71 | 6.98 | 7.46 | 7.92 | 29.07 | 23.41 |
| 2023 | 6.96 | 6.60 | 7.14 | 8.98 | 29.68 | 24.84 |
| 2024 | 6.45 | 6.64 | 6.52 | 8.64 | 28.25 | 21.34 |
| 2025 | 5.63 | **10.86** | 9.46 | 8.79 | 34.75 | 22.28 |
| 2026 | 6.52 | **3.44** | **2.61** | — | — | — |
Q2 2025 was the outlier (prior Q2s 6.60–6.98); Q2–Q3 2026 ran at roughly half the 2022–24 quarterly
norm. A heavy-collection 2025 followed by half-normal 2026 quarters fits a channel that bought ahead
and is destocking — **hypothesis**; distributor inventory and receivable ageing are not local.
Gross-flow test (Penman, t2): FY2020 → FY2025, (销售收现 − 营业收入) 3.71 → 12.46 (+8.75) and
其他经营付现 4.25 → 12.17 (+7.92), while selling + admin + R&D 5.08 → 6.71 (+1.63). The two cash lines
move together over the five years (FY2025 alone: gap +5.55 vs other paid +1.71 — the 2025 excess is
not all gross flow; receivables −1.07 and contract liabilities +0.51 explain ≈1.6 more).

### A6. Like-for-like reverse curve (cash at face; operating stake only; t7)
Parent NFA bounds 2026Q3 (Tukey 2.5 bracket, opposite biases on where the minority claim sits):
cash 5.3847 + trading 14.0503 + other non-current FA 1.0057 + investment property 1.3802 − FO 0.1128
= 21.708 (upper, minority claim wholly on operations); − MI 10.8872 = 10.821 (lower, wholly on cash).
Operating stake = 43.52 − NFA_parent: 21.81 (upper NFA) to 32.70 (lower NFA); both are limit cases.
Central case: NFA_parent = 21.708 − (10.8872 − (4.9347/10.2855) × 14.6664) = 17.857 → stake 25.663 →
needs 2.053 (8%), 2.566 (10%), 3.080 (12%).
Needed parent operating earnings at g = 0 (`calc.implied_earnings_re`, E = r × P):
| r | stake 21.81 | stake 32.70 |
|---|---|---|
| 8% | 1.745 | 2.616 |
| 10% | 2.181 | 3.270 |
| 12% | 2.617 | 3.924 |
TTM parent NI 2.835; TTM total-firm net financial income after tax = TTM NI total 5.349 (10.2855 −
7.6742 + 2.7377) − TTM OI after tax 4.903 (9.9550 − 7.4536 + 2.4019) = 0.446, so TTM parent operating
earnings ≈2.39–2.84 (all vs none of it the parent's). FY2025 parent operating earnings ≥ 5.351 − 0.330
= 5.020 (all FY2025 net financial income charged to the parent; conservative); at 10%, 5.020 / 0.10
≈ 50.2 against a stake priced at 21.8–32.7 (t8). The bracket's spread (10.8亿) is the parent's stake in
达因药业 and where the parent's own cash sits — the AR 2025 subsidiaries note closes it.
