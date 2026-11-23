# Workpaper — round 1 (not shown in the chat view)
Sources: S1 `avl_raw.json` (quote 20261120), S2 `bme.duckdb` raw_income / raw_balancesheet / raw_cashflow (report_type 1, latest filed quarter 20260930, quarters de-cumulated), S2 reformulated tables from the fact sheet. 亿元 unless stated.

## Decade read (one page)
**What the business is.** A single-flagship energy-drink brand (能量饮料 = 156.0 of 208.8 revenue in FY2025) sold through dealers who prepay (contract liabilities 59.74 at FY2025 = 25.7% of sales, up from 2.5% in FY2018). It runs on negative working capital (cash conversion cycle −13 days before advances), very little inventory (4% of sales) and plants that are cheap relative to sales (PP&E 22% of sales).
**What eight years show (FY2017→FY2025).** Revenue 28.44 → 208.75 (CAGR 28.3%); parent profit 2.96 → 44.15 (CAGR 40.2%); net margin ~10% → 21%; gross margin flat at 43–47% (44.9% FY2025); operating cash flow 1.9 → 61.7 and above reported profit every year since FY2019 (CFO/NI 1.4–2.1); capex runs 3–5× depreciation (22.7 vs 5.0 in FY2025) and still leaves simple FCF of 39–41 in FY2024–25; ROE 22–52%; reformulated NOA is near zero (6.4 at FY2025), so RNOA is not meaningful, the business is funded by dealers, suppliers and equity; dividends 27.1 in FY2025 (61% of profit). Share count 1.51 → 5.20 (splits/bonus, no large cash raise until 2026).
**Where the story bends.** (1) Growth: quarterly revenue growth 2025 +39/+34/+30/+23% → 2026 +21.5/+11.3/+0.75% (Q4 2026 still to come; Q4 2025 base 40.31). (2) FY2025 growth came less from the flagship: energy +17%, electrolyte +118%, other +95%; electrolyte and other earn 34.9% and 15.6% gross margin against 50.8% for energy. (3) Balance sheet: short-term borrowing of 62–70 sits next to 120+ of cash and trading assets every year since FY2023. (4) 2026 equity raise: 98.85 paid in during Q1 2026, shares 5.20 → 7.342 (includes a ×1.30 step with no matching cash, nature not in local data). (5) Market value 1,390.5 (20251231) → 833.7 (20261120), PE(TTM) 31.7 → 17.4.
**Headline numbers.** Revenue CAGR 28% FY2017–25; Q3 2026 revenue +0.75%; flagship energy drink only +17% in FY2025; prepayments 25.7% of sales; price implies about 1.4–4% perpetual growth for the operating business (8–10% required return, assumptions).

## Single-quarter revenue and growth
| | Q1 | Q2 | Q3 | Q4 | yoy by quarter |
|---|---|---|---|---|---|
| 2024 (S1) | 34.82 | 43.91 | 46.85 | 32.81 | |
| 2025 | 48.48 | 58.89 | 61.07 | 40.31 | 39% / 34% / 30% / 23% |
| 2026 | 58.88 | 65.55 | 61.53 | — | 21.5% / 11.3% / 0.75% |
Two-year growth (2026 vs 2024): Q1 +69%, Q2 +49%, Q3 +31% — still falling, so the 2025 base is not the whole story.
Q4 / Q3 ratio: 2023 0.82, 2024 0.70, 2025 0.66. Q4 2026 at 0.66 → 40.6 (+0.7%); at 0.70 → 43.1 (+6.8%).
Nine-month revenue 2026 185.96 vs 168.48 (+10.4%).

## Product mix, FY2025 vs FY2024 (S1 main_business)
| | rev 2025 | rev 2024 | change | share of +50.4 | GM 2025 | GM 2024 |
|---|---|---|---|---|---|---|
| 能量饮料 | 156.0 | 133.0 | +23.0 (+17%) | 46% | 50.8% | 48.3% |
| 电解质饮料 | 32.7 | 15.0 | +17.7 (+118%) | 35% | 34.9% | 29.3% |
| 其他饮料 | 19.9 | 10.2 | +9.7 (+95%) | 19% | 15.6% | 22.5% |
2026 product split is not in local data.

## Core profit (to separate unusual and financial lines)
TTM to Q3 2026 = Q4 2025 + 9M 2026. Pretax 61.10; investment income 1.19; fair-value gains 2.53; net financial expense (fin_exp) +1.19 (net cost: 2026 Q1 interest income 0.86 but "other" financial cost, see below). Core pretax = pretax − investment income − fair value + financial expense = 58.57. Actual TTM tax rate 13.10 / 61.10 = 21.4% → core after-tax operating profit 46.01. Reported parent profit TTM 47.99.
Q3 pretax: 16.77 vs 17.76 (−5.6%). Q3 core pretax: 17.18 vs 16.12 (+6.6%). Difference is fair-value and investment lines (Q3 2025 +1.54 vs Q3 2026 +0.08).
Selling ratio Q3 13.4% (8.25) vs 15.3% (9.32); nine months 16.0% vs 15.5%. Gross margin Q3 45.7% vs 45.2%; nine months 47.5% vs 45.2%.
Financial cost 9M 2026: fin_exp 1.45 vs interest net (2.78 − 0.68 → income 2.10) → other financial cost ≈ 3.55, nature not in local data.

## Cash and net financial assets (20260930, S1 EV items)
Cash 141.52 + trading assets 65.66 = 207.18; less short-term borrowings 62.73, due within one year 0.17, lease liabilities 3.84 = net financial assets ≈ 140.4. Other financial assets (non-current, debt investments, 18.0 due within one year) excluded; treatment is conservative on the cash side.
Equity B = 185.55; NOA = B − 140.4 = 45.2; market cap P = 833.68; EV = 693.2.
Contract liabilities 50.90 (20260930) vs 35.63 (20250930), +43%; 59.74 at FY2025. Q3→Q4 build: 2023 +6.9, 2024 +23.8, 2025 +24.1.

## Reverse curve (assumed required return r; g = perpetual growth of residual operating income, RE1 = RE0 (1+g))
g = ((EV − NOA)·r − RE0) / ((EV − NOA) + RE0), RE0 = core NOPAT 46.01 − r·NOA.
| r | operating basis, all net cash excess (EV 693, NOA 45) | prepayments treated as debt (EV 744, NOA 96) | equity basis, reported profit (P 834, B 186, NI 47.99) |
|---|---|---|---|
| 7% | 0.4% | — | 1.5% |
| 8% | 1.4% | 2.0% | 2.8% |
| 9% | 2.4% | — | 4.0% |
| 10% | 3.4% | 4.15% | 5.2% |
No-growth value (core NOPAT / r): 575 at 8%, 460 at 10%. Equivalent market cap = no-growth EV + net financial assets 140.4 → 716 (−14% vs 834) and 600 (−28%); with prepayments treated as debt (net 89.5): 665 (−20%), 550 (−34%).
S2 year-end 2025 curve for reference (equity basis, FCF/ReOI as in fact sheet): 4.7% at 8% (price 267.39, mkt cap 1,390.5).
r range is an assumption (the S2 default is 8%); there is no local evidence that fixes it.

## Cash flow and capex (single quarters)
CFO 2026 Q1/Q2/Q3: 4.52 / 20.40 / 10.49; 2025: 6.31 / 11.09 / 13.92 (9M 35.42 vs 31.33). Capex 2026: 6.00 / 5.35 / 2.94; 2025: 6.32 / 3.80 / 6.95 (9M 14.29 vs 17.07, −16%). Dividends and interest paid 9M 2026: 34.5. Borrowings drawn 9M 2026: 71.5 (c_recp_borrow).

## Share base
total_share 5.20 (Q4 2025) → 5.648 (Q1 2026) → 7.342 (Q2, Q3). 7.342/5.648 = 1.30. c_recp_cap_contrib 98.85 (Q1), 99.27 (9M). Equity 94.21 → 204.66 → 194.75 → 185.55. Price 113.55 × 7.342 = 833.68 (S1).

## Not checked locally
Use of the 99 亿 proceeds; the ×1.30 share step; the 3.55 other financial cost; 2026 product mix; dealer count and channel inventory; competitor pricing. All need filings or channel checks.
