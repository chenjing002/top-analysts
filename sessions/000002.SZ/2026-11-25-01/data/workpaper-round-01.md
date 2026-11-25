# Workpaper — 000002.SZ 万科A · session 2026-11-25-01 · round 01

Data: S1 AshareValueLine `20261121_201610` (quote 2026-11-20, price 2.82, mkt cap 336.45亿, 119.31亿
shares); S2 BME local JSON exported 2026-11-22 (annual FY2014–FY2025) + DuckDB supplement (quarterly
filings through 20260930; `raw_daily_basic` last 20251231). Amounts in 亿元 unless noted. Computed
figures use `scripts/calc.py` (named) or state formula + inputs. DuckDB queries dedupe
`raw_*` rows by `update_flag DESC, f_ann_date DESC, _fetched_at DESC`, `report_type='1'`.
Controller per `raw_stock_basic`: 无实际控制人 (no actual controller of record); largest-holder
identity and any shareholder loans are not in the local data (→ open questions).

## §0 Cross-check

98 S1/S2 comparisons, **0 mismatches >1%**. No reconciliation topic; Buffett opens.

## Business scorecard (the decade FY2016–FY2025 is the subject; 2026 is read against it)

**1. What kind of business? — GRUESOME on the full cycle. It looked great only while other people's money was growing.**
Penman operating income after tax (OI) summed over FY2016–25 is 2,054.6亿, but net operating assets
had to grow from 1,802.3亿 (end-2016) to 5,344.8亿 (end-2023) to produce it; ten-year free cash
flow from operations on Penman's basis (OI − ΔNOA, S2 `fcf_from_oi`) is **−273.4亿**. Core OI
pre-tax rose 417.3 (2016) → 834.8 (2020), then fell to −74.4 (2025). Parent NI: FY2016–20 Σ1,632.4亿,
FY2021–25 Σ−807.3亿; decade Σ825.1亿. Growth required capital, then earned less than nothing on it:
Buffett's worst kind of business (role card §3 Step 2; source passage to be read in-turn).

**2. Does cash back the profit? — In the boom, yes, but only through customer deposits; from 2021 no.**
CFO (operating cash, S2 raw) FY2016–20 Σ2,543.9亿 against parent NI 1,632.4亿; FY2021–23 CFO Σ107.7亿
against parent NI 573.1亿 (19%) — the profit stopped turning into cash two years before the losses.
CFO − capex over ten years is 2,056.5亿 (`calc.fcf`, 2.49× NI by `calc.fcf_conversion`), **but that
is the wrong measure for a developer**: land sits in inventory inside CFO, and project/JV stakes sit
in investing cash flow (net investing outflow ex-capex ≈ 1,523亿 over the decade). CFO + investing
CF = 533.5亿. Capex 623.2 vs D&A 648.0 (0.96×) — fixed capex is not where the money went; land,
JV stakes and loans to partners are. No maintenance/growth split is meaningful for fixed capex here;
the "maintenance" question is the land bank, an **estimate** the panel should not attempt from
local data.

**3. What drives the return? — Leverage, mostly the float.**
DuPont year-end (`calc.dupont`, parent NI / 营业收入 / total assets / parent equity):
2016 margin 8.7% × turnover 0.29 × multiplier 7.3 = ROE 18.5%; 2018 11.4% × 0.19 × 9.8 = 21.7%;
2021 5.0% × 0.23 × 8.2 = 9.6%; 2023 2.6% × 0.31 × 6.0 = 4.9%; 2025 −37.9% × 0.23 × 8.7 = −75.8%.
Turnover was always ~0.2–0.3; the multiplier of 6–10× made the ROE. Penman RNOA (average basis, S2)
17.8% (2016) → 26.4% (2018) → 4.0% (2023) → −19.7% (2025), with FLEV only 0.04–0.52: the leverage
is hidden in **operating** liabilities (customer advances, payables). OL/NOA 2.77× (2021) → 1.14×
(2025). RNOA was high because homebuyers and suppliers funded most of the operating assets.

**4. Is it cheap, and what is the floor? — Cheap to book, no floor under the equity.**
At S1 quote 2026-11-20: mkt cap 336.45亿, parent book 930.94亿 (2026Q3) → PB 0.361. Earnings
yield negative (TTM parent NI −844.8亿 = FY2025 −885.6 − 9M25 −280.2 + 9M26 −239.4). TTM CFO 26.8 −
capex 14.2 = FCF 12.6亿 (3.7% of cap) — before interest, which CAS puts in financing.
Book contents 2026Q3: cash 524.5, inventory 3,300.5, other receivables 1,703.2 (2026H1; Q3 not
broken out), LT equity investments 1,015.3, investment property 1,225.7, deferred tax assets 252.2,
goodwill 57.0 + intangibles 68.2. Against: interest-bearing debt 3,308.6 (short 291.8, due-in-1y
1,606.2, long 1,210.0, bonds 89.3, leases 111.3), other non-current liabilities 356.2 (17.8 at
FY2024; +338.5亿 — hypothesis: shareholder loans, not confirmed locally), payables 1,116.0, other
payables 1,352.9, contract liabilities 658.9, minority interest 1,124.7.
Net debt (`calc.net_cash`) −2,783.9亿; EV (`calc.enterprise_value`) 4,245.1亿, equity = 7.9% of EV.
Total assets / parent equity = 10.0×. **Floor:** tangible book ex goodwill/intangibles 805.8; ex
deferred tax assets too 553.6. **Write-downs, one base per figure** (assumption throughout: all of
it falls on the parent, none on minorities or tax): full book 930.9 → price needs 6.75% of the
8,803.4亿 non-cash assets (594.5亿; 18% of inventory alone), and → zero needs 10.6%. On the tangible
base (tangible book ex DTA 553.6 against tangible non-cash assets 8,426.0 = non-cash assets less
goodwill, intangibles and DTA): → price needs **2.58%** (217.2亿), → zero needs **6.57%**. Round one
speaks the tangible-base pair (corrected after the Observer review). The book does not protect the
downside at 10× leverage.
**Reverse curve (P < B, so solve for earnings, `calc.implied_earnings_re`, g = 0, E = r × P):**
r 8% → 26.9亿/yr (ROE 2.9% on current book); r 10% → 33.6亿 (3.6%); r 12% → 40.4亿 (4.3%); r 15% → 50.5亿 (5.4%).
Round one argues r = 12% (rollover risk: 3.6× cash due within a year) and shows 8% and 15%.
The price asks for a small, steady profit on today's book — against a 2026 run-rate loss of 79.8亿
per quarter (Q1 −59.5, Q2 −90.0, Q3 −89.9). At that pace the book reaches the price in ~7.5 quarters
(illustrative arithmetic, not a forecast).

**5. What did management do with the cash? — Paid out almost the whole decade's profit.**
Cash dividends declared FY2016–22 Σ761.4亿 (S1 年度现金分红总额; none FY2023–25) against decade parent
NI 825.1亿. Parent equity raised ≈172.8亿 (H-share placements 2019 66.4, 2020 71.7, 2023 34.7;
c_recp_cap_contrib − minority part); shares 110.39 → 119.31亿 (+8.1%). Minority partners put in
1,425.9亿 and took out 837.8亿 in dividends (S2 raw cash flow). One buyback (treasury stock 12.9亿,
2022–24; cleared by FY2025).

**6. Where does the story bend? — Five headlines.**
(a) FY2021: CFO 531.9 → 41.1 while parent NI still 225.2 — cash broke first.
(b) Customer advances (合同负债 + 预收款项) 6,382.2 (2021) → 677.2 (2026Q3), −89.4%: the float is gone.
(c) Gross margin (S1 销售毛利率) 37.5% (2018) → 9.5% (2025) → 6.6% (9M26, raw_income).
(d) FY2024–25 parent losses Σ−1,380.3亿 with credit impairments −264.0 and −341.7 (on receivables —
largely partner/JV funding, hypothesis) and asset impairments −71.7 and −219.3.
(e) Debt due within a year 1,898.0亿 = 3.6× cash 524.5亿 (2026Q3); 9M26 borrowed 104.8, repaid 185.9.
**Verdict:** a decade-long float-and-leverage machine that is now a liquidation-and-refinancing
question. The equity is a 7.9% stub on a 4,245亿 enterprise; its value turns on asset realization and
debt rollover, not on earnings power.

**7. Paired-line divergence scan (`calc.growth_gap`, fact sheet FY2025) — largest excess moves in 亿, owners.**

| # | pair (FY2025) | gap / ΔA / ΔB | what would be surprising | owner |
|---|---|---|---|---|
| 1 | NOA vs 营业总收入 | +10.3pp; NOA −1,061.9 vs revenue −1,097.4; excess +504.5 | Capital shrinks slower than sales: the asset base is stuck while revenue halves | `stephen-penman` |
| 2 | 合同负债+预收款项 vs 营业收入 | −19.2pp; −993.3 vs −1,097.4; excess −372.2 | Advances fall faster than revenue: fewer new pre-sales, the float unwinds | `jeff-bezos` |
| 3 | 其他应收款 vs 营业收入 | +11.2pp; −460.1 vs −1,097.4; excess +248.0 | Partner/JV receivables 1,754亿 do not shrink with the business; credit impairment −341.7 sits on them | `li-lu` |
| 4 | 应付票据及应付账款 vs 营业成本 | +13.1pp; −294.0 vs −969.2; excess +209.1 | Payables hold up while costs fall: supplier stretch (DPO 554.8 → 802.8 days) | `jeff-bezos` |
| 5 | 预付款项 vs 营业成本 | −35.3pp; −363.6 vs −969.2; excess −192.4 | **Explained:** Q4 2025 prepayments −333.1 while other current assets +295.6 — a reclassification, one-line note | (note) |
| 6 | 分配股利利润或偿付利息 vs CFO | +110.8pp; 145.5 paid vs CFO −9.9; excess +190.2 | Interest and minority dividends paid with no operating cash | `jeff-bezos` |
| 7 | 存货 vs 营业成本 | +3.4pp; −1,452.7 vs −969.2; excess +179.0 | Inventory falls more than cost of sales: write-downs (asset impairment −219.3) plus sales | `warren-buffett` |
| 8 | 所得税费用 vs 利润总额 | tax 178.9 on pre-tax −739.2 | **Explained:** deferred tax assets 440.7 → 275.8 (−164.9) written down; one-line note | (note) |
| 9 | 货币资金 vs 有息负债 | −14.3pp; −209.2 vs −360.5; excess −126.0 | Cash falls faster than debt: the cushion shrinks | `stephen-penman` (Mauboussin not seated) |

Not reached in the round go to `next_question_candidates` with the pair named.

---

## Appendix A — 10-year series (S2 raw annual, 亿元)

| FY | parent NI | CFO | capex | D&A | CFO−capex | OI after tax | Penman FCF (OI−ΔNOA) | NOA end | 营业收入 | GM (S1) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 210.23 | 395.7 | 21.5 | 11.5 | 374.2 | 294.8 | 0.8 | 1,802.3 | 2,404.8 | 29.4% |
| 2017 | 280.52 | 823.2 | 23.6 | 19.3 | 799.6 | 375.1 | 427.1 | 1,750.3 | 2,429.0 | 34.1% |
| 2018 | 337.73 | 336.2 | 59.0 | 29.2 | 277.2 | 533.3 | 0.4 | 2,283.1 | 2,976.8 | 37.5% |
| 2019 | 388.72 | 456.9 | 62.4 | 63.1 | 394.4 | 585.9 | −105.6 | 2,974.6 | 3,678.9 | 36.3% |
| 2020 | 415.16 | 531.9 | 72.1 | 69.8 | 459.8 | 603.2 | −8.2 | 3,586.1 | 4,191.1 | 29.3% |
| 2021 | 225.24 | 41.1 | 95.8 | 80.6 | −54.6 | 400.6 | −525.6 | 4,512.3 | 4,528.0 | 21.8% |
| 2022 | 226.18 | 27.5 | 128.3 | 93.0 | −100.8 | 358.4 | −176.3 | 5,047.0 | 5,038.4 | 19.6% |
| 2023 | 121.63 | 39.1 | 83.3 | 90.8 | −44.2 | 210.1 | −87.6 | 5,344.8 | 4,657.4 | 15.2% |
| 2024 | −494.78 | 38.0 | 45.2 | 87.2 | −7.2 | −444.9 | 1.6 | 4,898.2 | 3,431.8 | 10.2% |
| 2025 | −885.56 | −9.9 | 32.0 | 103.5 | −41.8 | −861.9 | 200.0 | 3,836.3 | 2,334.3 | 9.5% |
| Σ | 825.07 | 2,679.7 | 623.2 | 648.0 | 2,056.5 | 2,054.6 | −273.4 | | | |

NOA here is the S2 capital table (year-end); the reformulated BS gives the same end values within
rounding except FY2016–17 (1,655.3 average vs 1,802.3 end). Penman FCF from S2 capital table uses
NOA begin 1,508.3 (FY2016) → end 3,836.3 (FY2025).

## Appendix B — Float and working capital (S2 raw balance sheet, 亿元)

| date | inventory | contract liab + adv. receipts | payables | other payables | LT equity inv. | minority int. |
|---|---|---|---|---|---|---|
| 2016 | 4,673.6 | 2,746.5 | — | — | 617.0 | 482.3 |
| 2018 | 7,503.0 | 5,049.6 | — | — | 1,295.3 | 798.6 |
| 2021 | 10,756.2 | 6,382.2 | 3,305.4 | 1,903.2 | 1,444.5 | 1,568.2 |
| 2023 | 7,017.0 | 3,104.4 | 2,217.0 | 1,612.4 | 1,305.6 | 1,521.5 |
| 2025 | 3,737.4 | 949.2 | 1,306.3 | 1,333.9 | 1,069.1 | 1,189.5 |
| 2026Q3 | 3,300.5 | 677.2 | 1,116.0 | 1,352.9 | 1,015.3 | 1,124.7 |

Indirect-method CFO block FY2022–25: decrease in inventories Σ+7,574.5亿 (cash released) against
increase in operating payables (incl. advances) Σ−8,718.0亿 (cash consumed) — selling down the land
bank went to delivering pre-sold homes and paying suppliers; CFO Σ94.7亿 over those four years. Most of
the advance decline is settled by delivery (non-cash: advances and inventory fall together), so the
bridge is not a cash repayment of deposits.

## Appendix C — Debt, liquidity and financing (2026Q3 unless stated)

Interest-bearing debt 3,308.57 = st_borr 291.81 + non_cur_liab_due_1y 1,606.21 + lt_borr 1,210.02 +
bond_payable 89.27 + lease_liab 111.26 (S1 EV items 20260930). Cash 524.46 (cash equivalents at
period end 468.6 → ~55.8 restricted). Due within a year 1,898.02 = 3.62× cash.
Other non-current liabilities: 17.75 (FY2024) → 274.73 (2025Q3) → 312.66 (FY2025) → 344.98 (2026H1)
→ 356.21 (2026Q3). Not interest-bearing in the vendor's field map; if these are shareholder loans
(hypothesis), debt is ~3,664.8亿. 9M26 financing: borrowings received 104.8, repaid 185.9, dividends
+ interest paid 48.1; net financing −140.9; cash and equivalents −146.6.
9M26 income: revenue 1,050.0 (−34.9% vs 9M25 1,613.9), gross margin 6.6% (9M25 9.6%), interest
expense 62.2, investment income from associates −30.6, asset impairment −39.4, credit impairment
−4.1, income tax 39.1 on pre-tax −218.4; parent NI −239.4.

## Appendix D — Valuation arithmetic (S1 quote 2026-11-20)

- PB = 336.45 / 930.94 = 0.361; book per share (`calc.per_share`) 7.80元 vs price 2.82元.
- `calc.enterprise_value(336.45, 3308.57, 1124.74, 524.46, 0.20)` = 4,245.10; equity/EV 7.93%.
- `calc.net_cash(524.46, 0.20, [291.81, 1606.21, 1210.02, 89.27, 111.26])` = −2,783.91.
- `calc.implied_earnings_re(336.45, 930.94, r, 0)`: r 0.08 → 26.92; 0.10 → 33.65; 0.12 → 40.37; 0.15 → 50.47.
  (`implied_growth_re` is undefined when P < B; this solves the same equation for E1 instead of g.)
- Gap to book 594.49 / non-cash assets 8,803.35 (total assets 9,328.01 − cash − trading) = 6.75%;
  / inventory 3,300.52 = 18.0%; full book to zero 930.94 / 8,803.35 = 10.57%.
- Tangible base: tangible non-cash assets 8,803.35 − 56.95 − 68.15 − 252.24 = 8,426.01;
  (553.60 − 336.45) / 8,426.01 = 2.58% (tangible book to price); 553.60 / 8,426.01 = 6.57% (to zero).
- Magnifier bases (do not mix): EV / market cap = 4,245.10 / 336.45 = 12.6 (1% of EV → 12.6% of
  equity); total assets / parent book = 10.0; 1% of non-cash assets 88.0亿 = 26% of market cap.
- Dividend window matched (round one, Bezos): FY2016–22 CFO 2,612.5 + investing −2,245.0 = 367.5
  against 761.41 declared; minority capital received FY2016–22 1,335.0; debt ex leases 795.0 (FY2015)
  → 3,176.4 (FY2022).
- Tangible book 930.94 − 56.95 − 68.15 = 805.84; less DTA 252.24 = 553.60.
- Decade parent NI band (`calc.normalized_band`): low −885.56, median 225.71, high 415.16 — a
  truncated and non-stationary series (the company is half its 2022 size); not a normal band.
- TTM: parent NI −844.84; CFO 26.79; capex 14.22; FCF 12.57 (3.74% of cap, before interest).
- 9M26 margin walk (raw_income 20260930): 营业收入 1,049.99 − 营业成本 980.29 − 税金及附加 58.16 = 11.54
  gross profit after sales taxes; selling 29.28 + admin 37.16 + interest expense 62.23 = 128.67; ratio
  11.54 / 62.23 = 0.185. Parent NI single quarters 2026: −59.5, −90.0, −89.9 (avg −79.8).
- Tukey 2.5 bracket (round one, Li Lu): upper = tangible book ex DTA 553.60 at par; lower = 0 after a
  6.57% average write-down on tangible non-cash assets (corrected from 6.75%, which only reaches the
  price from full book). Diagnostic only — it locates inventory, partner
  receivables and the 356.2亿 liability as the lines to verify.
