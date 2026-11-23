# Round 3 — Restated on the 2026 share issue and the local quarterly statements: what do 2026 profit, cash flow and advances show, and what growth does the 20261120 price imply on a like-for-like definition?

**Session** 605499.SH / 2026-11-23-01 · **started** 2026-11-23T06:00:00-08:00 · **ended** 2026-11-23T06:00:00-08:00
**Participants** Stephen Penman, Li Lu (李录, Himalaya Capital), Warren Buffett, Jeff Bezos

> Rounds 1 and 2 left the 2026 share-count increase, the missing 2026 profit and cash flow, and the like-for-like reverse curve as open items. The local quarterly tables cover them through 20260930.

## Discussion

_Simulated expert perspectives._

### Stephen Penman

Before we argue about the shares, a correction to our own first two rounds. We said the sheet had no 2026 profit, cash flow or advances. The local quarterly tables do, through 20260930. Two things stand out. The share count went from 5.20 亿 to 5.65 亿 in Q1 and to 7.34 亿 in Q2, and Q1 cash flow shows 98.85 亿 received as capital contributions. So the 'apparent raise' was cash, about 99 亿 by nine months. Second, 7.34 / 5.65 = 1.30, which looks like a 3-for-10 bonus issue in Q2 on top. Both the price and the market cap we compared with year-end 2025 sit on different share bases. Do we agree to restate before we read anything into the 40% fall?

<details>
<summary>Evidence and turn notes</summary>

confidence medium · 2026-11-23T06:00:00-08:00

**Evidence**
- Total shares (亿股) by quarter-end _(source: S2 raw_balancesheet total_share)_ — {"20251231": 5.2, "20260331": 5.65, "20260630": 7.34, "20260930": 7.34}
- Cash received from capital contributions (亿元, cumulative) _(source: S2 raw_cashflow c_recp_cap_contrib)_ — {"20260331": 98.85, "20260630": 99.27, "20260930": 99.27}
- Capital reserve jumped with the cash and stayed high _(source: S2 raw_balancesheet cap_rese)_ — {"20251231": 19.6, "20260331": 117.65, "20260930": 114.99}
- Bonus ratio and implied issue price per pre-bonus share (rounded shares, so approximate) _(source: derived: 7.342/5.65 = 1.30; 98.85/(5.65-5.20) = about 220 yuan)_
- Per-share price move on a split-adjusted basis _(source: S1 quote 20261120 price 113.55; S2 raw_daily_basic close 20251231 267.39)_ — {"derived": "113.55 x 1.3 = 147.6; 147.6/267.39 - 1 = -44.8%"}

</details>

### Li Lu (李录, Himalaya Capital)

Agreed on restating, with one limit. Local tables tell us cash arrived and the share count moved. They do not tell us the type of issue, the date, the buyers or the fees, so I keep 'placement, listing or other' open. Now the bear case I owe you. If the company raised 99 亿 and still reports 62.73 亿 of short-term borrowings and a financial expense that turned positive, either the cash is earmarked or the books are doing something I do not understand. What does the financial line show?

<details>
<summary>Evidence and turn notes</summary>

confidence medium · 2026-11-23T06:00:00-08:00

**Evidence**
- Financial expense (亿元, cumulative) turned from income to cost _(source: S2 raw_income fin_exp)_ — {"9M2025": -0.74, "H1 2026": 0.96, "9M2026": 1.45}
- Short-term borrowings and cash plus trading assets at 20260930 (亿元) _(source: S2 raw_balancesheet st_borr, money_cap, trad_asset)_ — {"st_borr": 62.73, "money_cap": 141.52, "trad_asset": 65.66, "sum_cash_trading": 207.18}

**Challenges**
- → Stephen Penman: A fall in the market cap that includes new shares is not a fall in value per share.

</details>

### Stephen Penman

The financial line cannot be explained locally. Single-quarter financial expense was −0.10 in Q3 2025 and +0.49 in Q3 2026, so it moves against 207 亿 of cash. A foreign-currency loss on the proceeds or the cost of the debt would both fit, and I cannot separate them. What I can do is take it out of operating profit, together with fair-value and investment gains, and ask what the core business did. That matters because reported net income fell 7.8% in Q3 and I suspect that is the financial lines.

<details>
<summary>Evidence and turn notes</summary>

confidence medium · 2026-11-23T06:00:00-08:00

**Evidence**
- Single-quarter reported net income to parent (亿元) _(source: S2 raw_income/raw_balancesheet/raw_cashflow, ts_code='605499.SH', report_type='1', end_date in 20250331..20260930; single quarter = cumulative minus prior cumulative within the year)_ — {"Q3 2025": 13.86, "Q3 2026": 12.78, "yoy": "-7.8%"}
- Core pretax operating profit = operate_profit − (fv_value_chg_gain + invest_income) + fin_exp, single quarter (亿元) _(source: derived from S2 raw_income; formula as stated)_ — {"Q1 2025": 11.73, "Q1 2026": 15.33, "Q2 2025": 16.34, "Q2 2026": 18.51, "Q3 2025": 16.12, "Q3 2026": 17.17}
- Single-quarter growth, revenue versus core operating profit _(source: derived from the two rows above and S2 revenue)_ — {"revenue Q1/Q2/Q3": "21.5% / 11.3% / 0.8%", "core op profit Q1/Q2/Q3": "30.7% / 13.3% / 6.5%"}

**Challenges**
- → Li Lu (李录, Himalaya Capital): The financial expense is a cost of the proceeds, not evidence of a weaker drink business.

</details>

### Warren Buffett

So revenue was flat in Q3 and the earnings of the drink business still rose. How? Selling expense fell about 11% on flat sales. That can be good discipline, or it can be a company that stopped paying for shelf space and promotions and will pay later. I would ask Q4 whether the price has held. Gross margin tells me something. It did not widen in Q3 the way it did in Q2.

<details>
<summary>Evidence and turn notes</summary>

confidence medium · 2026-11-23T06:00:00-08:00

**Evidence**
- Single-quarter gross margin and selling-expense ratio _(source: S2 raw_income/raw_balancesheet/raw_cashflow, ts_code='605499.SH', report_type='1', end_date in 20250331..20260930; single quarter = cumulative minus prior cumulative within the year; GM = 1 − oper_cost/revenue; ratio = sell_exp/revenue)_ — {"GM Q2 2025/Q3 2025": "45.7% / 45.2%", "GM Q1/Q2/Q3 2026": "46.9% / 49.7% / 45.7%", "sell ratio Q3 2025 vs Q3 2026": "15.2% vs 13.4%", "sell_exp Q3 2025 vs Q3 2026 (亿元)": "9.31 vs 8.26"}

**Challenges**
- → Stephen Penman: A flat Q3 gross margin after a 49.7% Q2 is the figure I would check against the product mix, not against a price rise.

</details>

### Jeff Bezos

Cash is the cleaner witness. Q3 operating cash flow was 10.49 against 13.93 a year before, down 25%, while net income fell 8%. Contract liabilities, the advances distributors pay, sit at 50.9 亿, flat on Q2 and up 43% on a year ago. Last year they also barely moved between Q2 and Q3 and jumped in Q4, so the flat quarter is the normal pattern. The advances do not say distributors are withdrawing money. Capex also dropped to 2.94 in Q3, from 5.35 in Q2. Is that finished construction or a pause in building capacity for growth that is not there?

<details>
<summary>Evidence and turn notes</summary>

confidence medium · 2026-11-23T06:00:00-08:00

**Evidence**
- Single-quarter operating cash flow (亿元) _(source: S2 raw_income/raw_balancesheet/raw_cashflow, ts_code='605499.SH', report_type='1', end_date in 20250331..20260930; single quarter = cumulative minus prior cumulative within the year)_ — {"Q1 2025/2026": "6.31 / 4.52", "Q2 2025/2026": "11.09 / 20.41", "Q3 2025/2026": "13.93 / 10.49", "Q4 2025": 30.41}
- Contract liabilities (亿元) _(source: S2 raw_balancesheet contract_liab)_ — {"20250630": 36.67, "20250930": 35.63, "20251231": 59.74, "20260630": 51.3, "20260930": 50.9}
- Single-quarter capex (cash paid for fixed and intangible assets, 亿元) _(source: S2 raw_cashflow c_pay_acq_const_fiolta, de-cumulated)_ — {"Q2 2026": 5.35, "Q3 2026": 2.94, "Q3 2025": 6.95}
- Inventory 20260930 versus 20250930 (亿元) _(source: S2 raw_balancesheet inventories)_ — {"20250930": 5.52, "20260930": 6.65, "change": "+20.5%"}

</details>

### Stephen Penman

Now the valuation, rebuilt on one definition. Price minus book equals the present value of future residual income, so I do not need to settle how much of the 207 亿 is operating. At 20260930 that is 833.68 − 185.55 = 648.1 亿. At 20251231 it was 1,390.5 − 94.2 = 1,296.3 亿. Residual income for the base year uses core after-tax operating income of 45.9 亿 (TTM, 21.8% tax from 9M 2026) less r times NOA. NOA is not pinned down: the sheet says about 6.4 at FY2025, and my book-less-cash approximation gives 41. I show both. At r = 8%, the price implies perpetual residual-income growth of about 1.0% to 1.3%, against 4.7% at the end of 2025. Not zero. A fall of about 3.5 points in what growth the market pays for.

<details>
<summary>Evidence and turn notes</summary>

confidence low · 2026-11-23T06:00:00-08:00

**Evidence**
- Implied perpetual growth g = (r·(P−B) − ReOI0)/((P−B) + ReOI0), ReOI0 = OI − r·NOA; OI = 45.9 (TTM) _(source: derived: P−B = S1 mkt cap 833.68 − S2 equity attributable 185.55; OI = (TTM operate_profit 61.23 − fair value and investment gains 3.72 + financial expense 1.19) x (1 − 21.8%); TTM = FY2025 + 9M2026 − 9M2025)_ — {"NOA=10: r 6/7/8/9/10%": "-0.9 / 0.0 / 1.0 / 1.9 / 2.9 (%)", "NOA=41: r 6/7/8/9/10%": "-0.7 / 0.3 / 1.3 / 2.3 / 3.3 (%)", "20251231 (S2 ReOI0 41.4 convention, OI 41.0, NOA 6.4): r 6/8/10%": "2.8 / 4.7 / 6.7 (%)"}
- Core operating income of 45.9 compares with 41.0 at FY2025 _(source: S2 reformulated_is OI after tax FY2025 41.0 (fact sheet); derived above)_

</details>

### Li Lu (李录, Himalaya Capital)

Then my bear case needs more than the price. Revenue growth went 21.5%, 11.3%, 0.8%. If Q4 repeats Q3 against a weak 40.31 亿 comparison base, TTM revenue growth stays near 12% only because of the first half. The core energy-drink revenue was down 8.6% in Q3 from the product disclosures we used last round. A price of about 1% perpetual growth at 8% does not seem to protect me against that. But I concede the profit data are better than I expected. Core operating profit rose 6.5% on 0.8% revenue.

<details>
<summary>Evidence and turn notes</summary>

confidence medium · 2026-11-23T06:00:00-08:00

**Evidence**
- Q4 2025 single-quarter revenue is the comparison base _(source: S2 raw_income/raw_balancesheet/raw_cashflow, ts_code='605499.SH', report_type='1', end_date in 20250331..20260930; single quarter = cumulative minus prior cumulative within the year)_ — {"Q4 2025": 40.31, "Q3 2026": 61.53}
- Q3 energy-drink revenue fell 8.56% year over year _(source: Eastroc operating disclosures 2026-097 and 2026-074 §I(a), as recorded in round 2)_

**Concessions**
- ← Stephen Penman: Profit growth in Q3 held up on a core basis.

</details>

### Warren Buffett

I take that as the round's finding. The price does not say growth is over, it says growth is small. The fact I cannot see is whether Q3's cost savings repeat. A business with a 45% gross margin that cuts selling cost by a tenth and still sells the same bottles is either getting leaner or borrowing from next year. I would not pay for either until Q4 shows which.

<details>
<summary>Evidence and turn notes</summary>

confidence low · 2026-11-23T06:00:00-08:00

</details>

## Disagreements

- **Is Q3 a pause or the start of a stall?** — narrowed
  - Li Lu (李录, Himalaya Capital): Energy-drink revenue fell 8.6% and growth decelerated for three quarters, so a stall is not ruled out.
  - Warren Buffett: Core profit still grew, but a selling-expense cut may be borrowed from next year.
  - Jeff Bezos: Advances are flat in the usual seasonal pattern, but operating cash flow fell 25% and capex fell.
  - Stephen Penman: Price implies about 1% perpetual growth, not zero. Pause versus stall is not decided by the data.
  - _resolution_: All accept that the price is not a no-growth price and that core profit grew 6.5% in Q3. They disagree on whether Q3 selling-expense savings are repeatable. Q4 2026 results decide.

## Conclusion

**Answer (low confidence):** The 2026 share-count rise included about 99 亿 of cash capital contributions in Q1 (5.20 to 5.65 亿 shares). The further rise to 7.34 亿 in Q2 is 1.30 times the Q1 count and may be a 3-for-10 bonus issue; type, date and buyers are not in local data. If it is a bonus issue, the split-adjusted share price fell about 45% from 20251231, not the 40% market-cap fall quoted earlier; if not, the per-share fall is larger (about 58%). Q3 revenue grew 0.8%. On the panel's 'core' definition (excluding fair-value and investment gains and adding back financial expense) operating profit grew about 6.5%; reported operating profit fell 5.7% and net income to parent fell 7.8%, and the core reading leans on the financial-expense add-back, so it is provisional. Q3 operating cash flow fell 25% against a Q2 surge; nine-month operating cash flow is +13% year on year. Contract liabilities of 50.9 亿 are flat on Q2 (the usual seasonal pattern) and up 43% year on year. At r = 8% the 20261120 price implies about 1.0%–1.3% perpetual residual-income growth (range −0.9% to 3.3% across r = 6%–10%; g is about zero at r near 7%). The 2025 figure of 4.7% uses a different OI and NOA basis, so the fall is indicative, not 3.5 points exactly. It is not a zero-growth price at the 8% default. Confidence is low: it depends on the S2 default r, an unpinned NOA and a core-income definition chosen by the panel.

**What would change our mind**
- Q4 2026 revenue against the 40.31 亿 base and Q4 selling-expense ratio, which would show whether Q3 savings repeat.
- The announcement of the 2026 issue showing the instrument, proceeds net of fees and any restrictions on use.
- A note explaining the positive 2026 financial expense (FX or interest).
- A pinned NOA at 20260930 from the S2 reformulation once the 2026 quarter is loaded.

**Open questions**
- What was the issue type, date, price and net proceeds of the 2026 share issue? Local data show cash received of 98.85 亿 and shares rising to 5.65 亿 only.
- Why did financial expense turn positive (single quarter +0.49 in Q3 2026 against −0.10) while holding 207.18 亿 of cash and trading assets? Unverified.
- Is the Q3 selling-expense cut (9.31 to 8.26 亿) a lasting efficiency or timing?
- Why did Q3 operating cash flow fall to 10.49 from 13.93?
- NOA at 20260930 on the S2 definition is not available. The two cases used (10 and 41) bracket the answer.
- Comparable-store units and stockouts are still unavailable (carried from round 2).
- Reported-basis check: does Q3 profit growth survive when financial expense stays in operating profit (about +3%) or when net income is used (−7.8%)? Selling-expense savings of 1.05 亿 and 2026 dividends paid (34.56 亿 in nine months) are not yet bridged to cash flow.

## Candidate questions for the next round

- Does Q4 2026 repeat Q3 selling-expense discipline, and does core profit growth hold when revenue growth is near zero?
- Why do 62.73 亿 of short-term borrowings and a positive financial expense coexist with 207.18 亿 of cash and trading assets?
- What return will the 99 亿 raised earn, and what are the plans for it?
- What do comparable-store energy-drink till units, stockouts and channel stock movements show for the summer?

## Knowledge candidates (to be validated before entering knowledge/)

- [fact, medium] Eastroc total shares rose from 5.20 to 5.65 亿 in Q1 2026 with 98.85 亿 of capital contributions received, and to 7.34 亿 in Q2 2026 (ratio 1.30 to Q1). _(source: S2 raw_balancesheet total_share; raw_cashflow c_recp_cap_contrib at 20251231, 20260331, 20260630)_
- [method, medium] Price minus book equals the present value of residual income, so the reverse curve does not need the operating-versus-financial split of cash when NOA is uncertain; only ReOI0 depends on it. _(source: derived: P − B = ReOI1/(r − g) with NOA = B − NFA)_
