# Round 1 — Great, good or gruesome on the decade — and does the 2026 break change the verdict or only the price?

**Session** 000915.SZ / 2026-11-25-01 · **started** 2026-11-25T02:05:00-08:00 · **ended** 2026-11-25T02:50:00-08:00
**Participants** Warren Buffett, Stephen Penman, Jeff Bezos, Li Lu (李录, Himalaya Capital), Joekray Mond (Joe K. Raymond)

> A new session's first round judges the business on its full ten-year record. Here the decade (operating profit ×2.7 on shrinking operating assets) and 2026 (9M revenue −45%, Q3 revenue below cost, price −44% since year-end) point in opposite directions, so the verdict has to say which one the price should be read against.

## Discussion

_Simulated expert perspectives._

### Warren Buffett

Great, on the decade. Operating profit after tax nearly tripled to 10.0亿 by 2025, while the net operating assets needed to earn it shrank to 8.5亿: growth that handed capital back instead of eating it. The See's passage fits almost word for word: "It's far better to have an ever-increasing stream of earnings with virtually no major capital requirements." The line that surprised me is cash. Last year customers paid in 1.56 times reported revenue, far more than VAT explains. Stephen, is the profit I'm calling great measured net of something the cash statement shows gross?

<details>
<summary>Evidence and turn notes</summary>

confidence medium · 2026-11-25T02:10:00-08:00

**Evidence**
- Operating income after tax (total firm, Penman OI) 3.69亿 FY2016 → 9.96亿 FY2025 _(source: S2 reformulated_is oi_after_tax FY2016, FY2025)_ — {"FY2016": 3.6945, "FY2025": 9.955}
- OI after tax FY2025 / FY2016 = 2.69 ('nearly tripled') _(source: derived: S2 reformulated_is oi_after_tax)_
- Net operating assets 12.21亿 (end FY2016) → 8.55亿 (end FY2025) _(source: S2 reformulated_bs noa FY2016, FY2025)_ — {"FY2016": 12.2095, "FY2025": 8.5468}
- Cash received from sales / 营业收入 FY2025 = 1.56 (VAT-gross norm about 1.13 at the 13% rate) _(source: derived: S2 raw_cashflow cash_received_from_sales / raw_income revenue FY2025)_
- It's far better to have an ever-increasing stream of earnings with virtually no major capital requirements. _(source: SRC source-files/Warren Buffett/Businesses – The Great, the Good and the Gruesome.md, See's / FlightSafety passage (lines 62–63))_

</details>

### Stephen Penman

Yes, and the lines move in step. From 2020 to 2025 the excess of cash collected over revenue grew 8.8亿 while 'other' operating cash paid grew 7.9亿; VAT and a 1.6亿 rise in selling, admin and R&D explain only part. It fits invoices collected gross and rebates paid back in cash, with revenue booked net, though cash-paid marketing would look similar. My reading, not a disclosed fact. The text says to "Follow the trail to the balance sheet and cash flow statement". Jeff, Q3 revenue was 0.33亿, below its cost of sales: does the cash side read as a rebate true-up or as lost demand?

<details>
<summary>Evidence and turn notes</summary>

confidence medium · 2026-11-25T02:14:00-08:00

**Evidence**
- (Cash received from sales − 营业收入) rose 8.75亿, FY2020 → FY2025 _(source: derived: S2 raw_cashflow cash_received_from_sales, raw_income revenue)_
- Other operating cash paid (支付其他与经营活动有关的现金) rose 7.92亿, FY2020 → FY2025 _(source: derived: S2 raw_cashflow other_operating_cash_paid)_
- Selling + admin + R&D expense rose 1.63亿 over the same years (selling alone +2.15亿 from a 2020 trough) _(source: derived: S2 raw_income selling, admin, rd expenses)_
- VAT at 13% on the FY2020→FY2025 revenue increase explains about 0.53亿 of the gap's rise _(source: derived: S2 raw_income revenue FY2020, FY2025 × 13% VAT rate (statutory rate for medicines, not a company disclosure))_
- 2026 Q3 single-quarter 营业收入 0.33亿 _(source: S2 latest quarterly filings 20260930 revenue_sq)_ — {"revenue_sq_2026Q3": 0.3325}
- 2026 Q3 single-quarter 营业成本 0.47亿 (9M 1.9557 − H1 1.4904), above Q3 revenue _(source: derived: S2 raw_income oper_cost YTD (DuckDB; workpaper A2))_
- Rebates paid in cash with revenue booked net _(source: hypothesis (labelled in text))_
- Follow the trail to the balance sheet and cash flow statement to detect manipulated income. _(source: SRC source-files/Stephen Penman/Financial Statement Analysis for Value Investing.html, Chapter 10 'Keeping the Book: The Anchoring Income Statement')_

</details>

### Jeff Bezos

Read against prior years, the cash broke before the profit did. Second-quarter collections ran near 7亿 in 2022–24, jumped to 10.9亿 in Q2 2025, then fell to 3.4亿 in Q2 2026, a quarter that still booked a profit. "Earnings don't directly translate into cash flows". Here a heavy-collection year was followed by half-normal ones, which looks like distributors buying ahead in 2025 and working stock off in 2026. That's a hypothesis: channel stock isn't in our data, so I can't yet tell it from lost demand. Warren, does the first-half pharma margin say the price held while volume fell?

<details>
<summary>Evidence and turn notes</summary>

confidence medium · 2026-11-25T02:18:00-08:00

**Evidence**
- Second-quarter cash received from sales 6.98亿 (2022), 6.60亿 (2023), 6.64亿 (2024): near 7亿 _(source: S2 raw_cashflow single quarter Q2 (DuckDB de-cumulated; workpaper A5))_ — {"Q2_2022": 6.98, "Q2_2023": 6.6, "Q2_2024": 6.64}
- Q2 2025 cash received from sales 10.86亿; Q2 2026 3.44亿 _(source: S2 raw_cashflow single quarter Q2 (DuckDB de-cumulated; workpaper A5))_ — {"Q2_2025": 10.86, "Q2_2026": 3.44}
- Q2 2026 parent net profit still positive, 1.13亿 _(source: S2 latest quarterly filings 20260630 ni_parent_sq)_ — {"ni_parent_sq_2026Q2": 1.1284}
- Distributors bought ahead in 2025 and are destocking in 2026 _(source: hypothesis (labelled in text))_
- earnings don't directly translate into cash flows, and shares are worth only the present value of their future cash flows _(source: SRC source-files/Jeff Bezos/Amazon Shareholder Letter 2004.html, opening free-cash-flow-per-share passage)_

</details>

### Warren Buffett

Not clearly. First-half pharma revenue fell 28% while the segment's cost of sales fell only about 12%. That fits less volume with some fixed costs, or, if unit cost held, a net price roughly 18% lower, which is what bigger rebates would look like. At an 86% margin the gross margin can't tell those apart. My rule asks for "demonstrated consistent earning power" and rules out "turn-around" situations, and right now this is one. Li Lu, what is the specific threat, and which document would name it?

<details>
<summary>Evidence and turn notes</summary>

confidence medium · 2026-11-25T02:21:00-08:00

**Evidence**
- H1 pharma segment revenue fell 28.0%: 11.54亿 (H1 2025) → 8.31亿 (H1 2026) _(source: derived: S1 main_business 医药产品 20250630, 20260630)_
- H1 pharma segment cost of sales (revenue − gross profit) fell 11.7%: 1.62亿 → 1.43亿 _(source: derived: S1 main_business 医药产品 20250630, 20260630)_
- If unit cost were unchanged, volume fell 11.7% and net price per unit fell 18.5% _(source: derived: S1 main_business; assumption unit cost constant (stated in text))_
- H1 2025 pharma segment gross margin 86.0% (82.8% in H1 2026) _(source: derived: S1 main_business 医药产品 gross profit / revenue 20250630)_
- demonstrated consistent earning power (future projections are of little interest to us, nor are "turn-around" situations) _(source: SRC source-files/Warren Buffett/Berkshire Hathaway Shareholder Letter 1986.html, acquisition criteria)_

</details>

### Li Lu (李录, Himalaya Capital)

Our data shows the damage, not the cause. My Megastudy rule is to name the specific threat and watch whether the next quarters confirm it. The lecture's test is whether I know enough to be entitled to an opinion. Not yet. Three fears: the unknown threat; a holding structure where minorities took 46.9% of the decade's profit; and payouts above profit that look like the owner harvesting. The 2026 Q3 report, the 2025 annual-report note on subsidiaries and any exchange inquiry letter would test them. Joe, if about half the profit isn't ours, what does the floor under the 43.5亿 price cover?

<details>
<summary>Evidence and turn notes</summary>

confidence medium · 2026-11-25T02:25:00-08:00

**Evidence**
- Minority holders took 46.9% of FY2016–FY2025 total net income (31.88 of 67.97亿) _(source: derived: S2 raw_income minority_income / net_income_total FY2016–FY2025)_
- Declared dividends 5.86亿 in FY2024 and FY2025 against parent net profit 5.16亿 and 5.35亿 (114%, 110%) _(source: S1 annual.分红, annual.归母净利润 FY2024–FY2025)_ — {"div_FY2024": 5.86, "div_FY2025": 5.86, "ni_FY2024": 5.1559, "ni_FY2025": 5.3508}
- Market cap 43.52亿 at 18.57元 _(source: S1 quote 2026-11-20)_ — {"mkt_cap": 43.52, "price": 18.57}
- Parent's ownership of 达因药业 and the cause of the 2026 break _(source: AR not read)_
- Paraphrase of 'You need to ask yourself: Do I know enough to be entitled to an opinion' (read this turn) _(source: SRC source-files/Li Lu/Li Lu_CBS Lecture Notes.pdf p.7 (Megastudy, Q1 2005 results))_

</details>

### Joekray Mond (Joe K. Raymond)

Less than half. If minorities own the share of the subsidiary their profit share implies, and it holds all the operations, the parent's net financial assets are about 18亿. That's an estimate, inside limits of 10.8亿 and 21.7亿 set by where their claim sits, at book value with no haircut on the trading assets. So the floor is about two-fifths of the price, and this is no net-net. My nearest case is Eskimo Pie: controlled and cash-rich, but there the majority owner's sale was the catalyst. A provincial state owner has no exit we can see. Stephen, what profit does the rest of the price need?

<details>
<summary>Evidence and turn notes</summary>

confidence medium · 2026-11-25T02:29:00-08:00

**Evidence**
- Limit case: parent net financial assets 10.82亿 if the minority claim sat wholly on financial assets (minorities owning none of NOA) _(source: derived: S1 ev_items 20260930 (cash, trading assets, minority interest) + S2 raw_balancesheet (DuckDB 20260930: other non-current financial assets, investment property, financial obligations))_
- Limit case: 21.71亿 if the minority claim sat wholly on operating assets (minorities owning 74% of NOA 14.67亿, against a 48% profit share) _(source: derived: same inputs, Tukey 2.5 opposite-bias bracket)_
- Central estimate: parent net financial assets 17.86亿, assuming the minority owns the FY2025 profit share (48.0%) of a subsidiary holding all group NOA (14.67亿, 2026Q3) _(source: derived: S1 ev_items 20260930; S2 raw_income FY2025 minority_income / net_income_total; S2 reformulated_bs 20260930 (DuckDB))_
- Central floor = 41% of market cap ('about two-fifths') _(source: derived: central estimate / S1 quote total_mv 2026-11-20)_
- Controller Shandong SASAC (地方国企); no disclosed exit or sale process _(source: S2 raw_stock_basic act_name (DuckDB); interpretation)_
- Eskimo Pie: controlled by Reynolds Metals (88%), net cash; the catalyst was the parent's sale via IPO _(source: SRC source-files/Joekray Mond/100-irr-in-ice-cream.md, setup section (line 62))_

_[reasoning method, not evidence — john-tukey · 2.5]_

</details>

### Stephen Penman

Less than our workpaper said: it charged the cash the business's 10% hurdle. With the cash at face, about 26亿 of the price sits on the operating stake, which at 10% needs about 2.6亿 a year, no growth. That's roughly the trailing year's 2.8亿, but those months hold three quarters from before the break, and Q3 alone lost money. So the price assumes Q3 was a one-off, not that 2025 comes back. I hold 10% because there's no debt but one shaky segment; at 12% the need rises to about 3.1亿. Warren, does that make a full recovery free upside?

<details>
<summary>Evidence and turn notes</summary>

confidence medium · 2026-11-25T02:33:00-08:00

**Evidence**
- Operating stake priced at 25.66亿 (central parent NFA 17.86亿; limits 21.81–32.70亿) _(source: derived: S1 quote total_mv − central parent NFA (t6))_
- At r = 10%, g = 0 the 25.66亿 stake needs 2.57亿/yr of parent operating earnings (limits 2.18–3.27亿) _(source: derived: calc.implied_earnings_re (g = 0 → E = r × P))_
- At r = 8%: 2.05亿/yr (limits 1.74–2.62亿) _(source: derived: calc.implied_earnings_re (g = 0))_
- At r = 12%: 3.08亿/yr (limits 2.62–3.92亿) _(source: derived: calc.implied_earnings_re (g = 0))_
- Trailing-year quarters of parent net profit: 2025Q4 1.27亿, 2026Q1 1.11亿, 2026Q2 1.13亿, 2026Q3 −0.67亿 _(source: S2 latest quarterly filings ni_parent_sq 20251231–20260930)_ — {"2025Q4": 1.2702, "2026Q1": 1.1058, "2026Q2": 1.1284, "2026Q3": -0.6693}
- TTM parent net profit 2.83亿 (FY2025 − 9M2025 + 9M2026) _(source: derived: S2 raw_annual ni_parent + latest quarterly filings ni_parent_ytd)_
- TTM total-firm net financial income after tax 0.45亿 ('a few tenths'), the most the parent's interest could be _(source: derived: S2 raw_income net income and reformulated_is OI after tax, cumulative (DuckDB 9M rows; workpaper A6))_
- 9M 2026 营业收入 down 45.0% (8.82 vs 16.03亿) _(source: derived: S2 latest quarterly filings revenue_ytd 20260930, 20250930)_
- Hurdle argued at 10%: no interest-bearing debt and provincial-state control argue lower; a single pharma segment whose 9M revenue fell 45% argues higher _(source: interpretation (labelled in text))_

**Challenges**
- → Warren Buffett: the workpaper's 4.35亿/yr (E = r × P on the full price) charged cash the operating hurdle; like-for-like the operating stake (about 26亿) needs about 2.6亿/yr at 10%, roughly the trailing year, which still holds three pre-break quarters

</details>

### Warren Buffett

Close to free, if the franchise survives, and that's the whole if. Last year the parent's operating profit was at least 5.0亿; at Stephen's 10% that's about 50亿, against roughly 26亿 the market puts on the stake. But recoveries priced as free often never come, which is why my rule excludes turnarounds. One loss quarter can't tell a one-off charge from the start of something. Jeff, what would the fourth quarter have to show for you to call the bottom?

<details>
<summary>Evidence and turn notes</summary>

confidence medium · 2026-11-25T02:37:00-08:00

**Evidence**
- FY2025 parent operating earnings at least 5.02亿 (parent net profit less all FY2025 net financial income after tax, charged to the parent) _(source: derived: S2 raw_income net_income_parent − reformulated_is net financial income (−nfe_after_tax) FY2025)_
- Capitalised at r = 10%, g = 0: 50.2亿 _(source: derived: calc.implied_earnings_re inverted at g = 0 (V = E / r))_
- 2026 Q3 parent net profit −0.67亿 (loss quarter) _(source: S2 latest quarterly filings 20260930 ni_parent_sq)_ — {"ni_parent_sq_2026Q3": -0.6693}
- demonstrated consistent earning power (future projections are of little interest to us, nor are "turn-around" situations) _(source: SRC source-files/Warren Buffett/Berkshire Hathaway Shareholder Letter 1986.html, acquisition criteria)_

**Concessions**
- ← Stephen Penman: accepts the like-for-like correction: the price bets Q3 was a one-off, not that 2025 comes back

</details>

### Jeff Bezos

There's a precedent: in 2024 a 2.2亿 third quarter was followed by 7.6亿 in the fourth, the year's best. This time Q3 is below cost and the first half was already down, so I'd want more than a revenue rebound: cash collected back above revenue, receivables down from 3.8亿, and no new rebate charge. Receivables rising again into year-end would mean the company is financing its distributors, and that is how a franchise quietly gives up its price. Li Lu, will the parent keep paying out dividends the business didn't earn in cash this year?

<details>
<summary>Evidence and turn notes</summary>

confidence medium · 2026-11-25T02:40:00-08:00

**Evidence**
- Q3 2024 single-quarter 营业收入 2.24亿, followed by Q4 2024 7.57亿, the year's highest quarter _(source: S1 quarterly_revenue 2024)_ — {"Q3_2024": 2.2357, "Q4_2024": 7.565}
- Receivables (应收票据及应收账款) 3.79亿 at 2026Q3 vs 2.11亿 at FY2025 _(source: S1 period_trend 20260930, 20251231)_ — {"2026Q3": 3.7855, "FY2025": 2.11}
- Rising receivables would mean financing distributors _(source: interpretation (labelled in text))_

</details>

### Li Lu (李录, Himalaya Capital)

So far, yes. In nine months of 2026 the group paid 9.7亿 of dividends while operations burned 3.3亿, and cash fell to 5.4亿. There's no debt, so this is a choice, not distress. But it shows the state owner treats the subsidiary as a cash pipe, and a pipe can be throttled. I'd pass until a document names the threat. Can you supply the 2026 Q3 report and the 2025 annual-report notes, or authorize us to fetch them?

<details>
<summary>Evidence and turn notes</summary>

confidence medium · 2026-11-25T02:43:00-08:00

**Evidence**
- Dividends and interest paid 9M2026 9.73亿, of which 5.04亿 to the subsidiary's minority holders _(source: S2 raw_cashflow c_pay_dist_dpcp_int_exp, incl_dvd_profit_paid_sc_ms 20260930 (DuckDB; workpaper A3))_ — {"div_9M2026": 9.7308, "to_minority": 5.0441}
- 9M2026 operating cash flow −3.32亿 _(source: S2 latest quarterly filings 20260930 cfo_ytd)_ — {"cfo_ytd_2026Q3": -3.3235}
- 货币资金 5.38亿 at 2026Q3 (20.14亿 at FY2025); no interest-bearing debt _(source: S1 ev_items 20260930; S1 balance_sheet FY2025)_ — {"cash_2026Q3": 5.38, "cash_FY2025": 20.14, "st_borr": 0.0, "lt_borr": 0.0}
- The owner treats the subsidiary as a cash pipe _(source: interpretation (labelled in text))_

**Challenges**
- → Warren Buffett: a recovery is not 'free' while the owner keeps extracting more cash than operations produce

</details>

### Stephen Penman

Where we land: a great business on its decade, profit nearly tripled while it needed less capital, though about half of that was operating liabilities like taxes and customer advances, which reversed this year. 2026 broke for reasons our data can't show. With the cash at face, the price asks the operating stake for about the trailing year's profit, a bet that Q3 was a one-off. Two cautions keep us from calling it a bargain: revenue is a net figure set by an accrual that just produced a quarter below cost, and the floor is only about two-fifths of the price. Pass for now; the Q3 notes decide it.

<details>
<summary>Evidence and turn notes</summary>

confidence medium · 2026-11-25T02:46:00-08:00

**Evidence**
- Operating liabilities rose 1.78亿 FY2016→FY2025, 49% of the 3.66亿 NOA fall; operating assets fell 1.88亿 _(source: derived: S2 reformulated_bs ol, noa FY2016, FY2025)_
- Operating liabilities 6.36亿 (FY2025) → 2.84亿 (2026Q3); NOA 8.55亿 → 14.67亿 _(source: S2 reformulated_bs FY2025; DuckDB reformulated_bs 20260930)_ — {"ol_FY2025": 6.3617, "ol_2026Q3": 2.8418, "noa_FY2025": 8.5468, "noa_2026Q3": 14.6664}

</details>

## Disagreements

- **Does the price require a recovery?** — resolved
  - Stephen Penman: no 2025-level recovery: with cash at face the operating stake (about 26亿, central estimate; limits 21.8–32.7亿) needs about 2.6亿/yr at 10%, roughly the trailing year, which still holds three pre-break quarters; the bet is that Q3 was a one-off
  - Warren Buffett: initially read from the workpaper's 4.35亿/yr (E = r × P on the full price) as a bet on a full recovery
  - _resolution_: Buffett conceded in t8; workpaper item 4 is corrected and A6 shows the like-for-like curve at 8/10/12% with the central case and both limit cases.
- **Is a recovery free upside or a pass?** — narrowed
  - Warren Buffett: close to free if the franchise survives: FY2025 parent operating earnings of at least 5.0亿 capitalise to about 50亿 at 10% against about 26亿 priced; but he does not buy turnarounds
  - Li Lu (李录, Himalaya Capital): pass: the threat is unnamed, the owner extracts more cash than operations produce in 2026, and the floor is only partly ours
  - _resolution_: Both agree the 2026 Q3 report and the FY2025 annual-report notes decide it; the remaining fact is whether the Q3 revenue deduction is a one-off rebate/price-protection charge or lost end demand.
- **What broke in 2026: price, channel or demand?** — narrowed
  - Warren Buffett: the H1 gross margin cannot separate the two: pharma cost of sales −11.7% against revenue −28% fits lower volume with fixed costs or, at constant unit cost, a net price about 18% lower
  - Jeff Bezos: collections halved from Q2 2026 after an outlier 2025; destock and credit extension look alike without receivable ageing; 2024 shows a Q3 dip (2.2亿) recovering in Q4 (7.6亿)
  - _resolution_: Test named: Q4 2026 cash collected back above revenue with receivables falling from 3.79亿 = channel normalising; receivables rising again = financing distributors.

## Conclusion

**Answer (medium confidence):** 华特达因 is a great business on its decade that broke in 2026 for reasons the local record cannot show. Its pediatric-pharma subsidiary nearly tripled operating profit after tax (3.69亿 FY2016 → 9.96亿 FY2025) while net operating assets shrank (12.21亿 → 8.55亿), and free cash flow (66.07亿) matched total profit (67.97亿) over ten years; about half of the capital release was operating liabilities that reversed in 2026 (6.36亿 → 2.84亿). In 2026, 9M revenue fell 45%, Q3 revenue (0.33亿) came in below its cost of sales, and operating cash flow turned negative (−3.32亿). At 43.52亿 (S1 quote 2026-11-20, 18.57元) the price is not betting on a return to 2025. Valuing the parent's cash at face (central estimate about 17.9亿 of parent net financial assets, assuming minorities own their 48% profit share of a subsidiary holding all operations; limits 10.8–21.7亿), it asks the roughly 26亿 operating stake for about 2.6亿 a year at a 10% hurdle (2.1亿 at 8%, 3.1亿 at 12%). That is about the trailing parent profit of 2.8亿, but that year still holds three pre-break quarters and Q3 alone lost 0.67亿, so the price bets that Q3 was a one-off; FY2025 parent operating profit was at least 5.0亿. The insight to remember: the decisive questions are measurement and cause, not the multiple. Revenue looks booked net of rebates paid back in cash (from 2020 to 2025 the excess of cash collected over revenue grew 8.8亿 while other operating cash paid grew 7.9亿; VAT and expense growth explain only part — a hypothesis until the notes are read), so a single accrual can swing a whole quarter. The panel passes until the 2026 Q3 report names the cause. Scorecard: business type GREAT on the decade (operating profit ×2.7 while gross operating assets also fell, 16.8 → 14.9亿; the consolidated gross-margin climb from 60.9% to 85.1% is the exit from low-margin side businesses, the pharma segment held near 84%); cash backing YES through FY2025 (FCF/NI 0.97; capex front-loaded in 2016–19, recent capex below depreciation), NO in 2026 (9M operating cash −3.32亿 while 9.73亿 of dividends went out); return driver MARGIN on an almost capital-free operation (RNOA 102% in FY2025 = margin 44.7% × turnover 2.29, partly levered by operating-liability float), with the parent's ROE (18.7%) diluted by a cash pile and by minorities taking 46.9% of the decade's profit; cheap or not CHEAP on FY2025 (12.3% earnings yield), FAIR on the trailing year (6.5%) and not cheap on the Q3 run-rate; floor PARTIAL: about two-fifths of the price in parent net financial assets at book (central case), a quarter to a half at the limits. Capital allocation: 64% of the decade's parent profit was declared as dividends, FY2024–25 payouts exceeded profit (114%, 110%); no raises or buybacks. Confidence medium: the business verdict rests on direct S2 series, but the valuation depends on an argued hurdle, an estimated ownership split, unverified rebate mechanics, and documents not in the local data.

**What would change our mind**
- The 2026 Q3 report attributing the revenue deduction to a one-off price-protection or rebate true-up, with Q4 2026 cash collected back above revenue and receivables falling from 3.79亿, would turn the pass into a priced option on recovery (FY2025 parent operating earnings of at least 5.0亿 capitalise to about 50亿 at 10% against a stake priced near 26亿)
- Evidence of lost end demand or share (a named competitor, a policy or label change, or a second quarter of collections near half the 2022–24 norm) would make the trailing 2.8亿 the ceiling and the price full
- An annual-report subsidiaries note showing the parent owns well over half of 达因药业, or holds most of the group cash at parent level, would lift the floor from the ~17.9亿 central case toward its 21.7亿 limit; a lower stake or subsidiary-held cash would push it toward 10.8亿
- A dividend cut to what operating cash supports would show that the owner is not harvesting at minority holders' expense

**Open questions**
- What caused the 2026 Q3 revenue of 0.33亿 (below cost of sales 0.47亿) and the 0.26亿 Q3 asset impairment: a rebate or price-protection accrual, sales returns, or lost volume? Document: 2026 Q3 report notes and any exchange inquiry letter (问询函) with the company's reply.
- What is in the 12.17亿 of other operating cash paid (FY2025), and is revenue recognised net of distributor rebates or market fees paid in cash? Document: FY2025 annual-report notes on 收到/支付的其他与经营活动有关的现金 and the revenue-recognition policy.
- What is the parent's percentage ownership of 达因药业, and how much of the group's 21.7亿 of net financial assets sits at parent level? Document: FY2025 annual-report subsidiaries note and the parent-only balance sheet (母公司资产负债表).
- Product concentration: what share of pharma revenue is one product (伊可新 vitamin AD drops is commonly cited, unverified locally)? Document: FY2025 annual-report MD&A product table.
- Why did FY2025 cash collected (34.75亿) exceed FY2024 by 6.50亿 on revenue up only 0.94亿, with Q2 2025 alone at 10.86亿: a pull-forward by distributors? Document: FY2025 receivable and contract-liability notes and distributor-inventory disclosure, if any.

## Thinkers consulted (reasoning methods, not evidence)

- john-tukey · 2.5 — The floor as two estimates with opposite biases (minority claim wholly on cash → parent NFA 10.8亿; wholly on operations → 21.7亿). The 10.9亿 spread locates the one line to verify, the parent's stake in 达因药业 and where its own cash sits, instead of assuming a 51% stake. Diagnostic, not a valuation range. [reasoning method, not evidence — Tukey 2.5]
- declined — The two narrowed disagreements (recovery free vs pass; channel vs demand) each turn on a named document (2026 Q3 report notes, receivable ageing). A reasoning method cannot substitute for them.

## Candidate questions for the next round

- Divergence item 4 reversed with items 3 and 5 (owners jeff-bezos and stephen-penman): how much of the 3.32亿 nine-month cash burn and the +6.12亿 NOA rebuild is settlement of 2025's accrued liabilities (operating liabilities −3.52亿: taxes payable 1.28 → 0.06亿, other payables 1.45 → 0.51亿, contract liabilities 1.07 → 0.15亿) rather than lost sales, and does it change the 5.0亿 FY2025 earning-power base?
- User: can you supply the 2026 Q3 report and the FY2025 annual-report notes (subsidiaries, other operating cash, revenue recognition), or authorize fetching them? The remaining disagreements turn on them.
- Divergence item 5, cash taxes vs pretax profit (支付的各项税费 vs 利润总额, +1.4亿 excess FY2025; cash taxes 3.57 → 5.03亿 on pretax +0.29亿): does VAT on gross invoices confirm the rebate gross-up hypothesis? (owner: stephen-penman)

## Knowledge candidates (to be validated before entering knowledge/)

- [fact, high] FY2016–FY2025: operating income after tax (total firm) rose from 3.69亿 to 9.96亿 while net operating assets fell from 12.21亿 to 8.55亿; ten-year CFO − capex 66.07亿 against total net income 67.97亿 (parent 36.09亿). Operating liabilities rose 1.78亿 over the decade (49% of the NOA fall) and fell from 6.36亿 to 2.84亿 in 9M2026. _(source: S2 reformulated_is, reformulated_bs, cash_summary FY2016–FY2025)_
- [fact, high] The consolidated gross margin rose from 60.85% (FY2020) to 85.11% (FY2025) through the exit of non-pharma segments (environmental equipment, education, materials, parks). The pharma segment's gross margin was 83.8% in FY2020 and 84.6% in FY2025, and its revenue rose from 11.24亿 to 22.15亿. _(source: S1 main_business 20201231, 20251231; S1 annual.销售毛利率)_
- [fact, high] Minority holders took 46.9% of FY2016–FY2025 total net income (31.88 of 67.97亿), and 4.93 of 10.29亿 in FY2025. Dividends paid to minorities were 5.04亿 in each of 2024, 2025 and 9M2026. _(source: S2 raw_income minority_income, net_income_total; S2 raw_cashflow dividends_paid_to_minority)_
- [fact, high] FY2020 → FY2025: (cash received from sales − 营业收入) rose 8.75亿 (3.71 → 12.46) while other operating cash paid rose 7.92亿 (4.25 → 12.17), and selling + admin + R&D expense rose only 1.63亿. VAT on the revenue increase explains about 0.53亿 of the gap's rise; the two series correlate across the decade. _(source: S2 raw_cashflow, raw_income FY2020, FY2025)_
- [hypothesis, low] Revenue is booked net of distributor rebates or market fees that are paid back in cash (gross invoices collected). The 2026 Q3 revenue of 0.33亿, below cost of sales, reflects a rebate or price-protection deduction rather than a pure volume fall. Precedent: Q3 2024 revenue 2.24亿 was followed by Q4 2024 7.57亿. _(source: derived from S2 raw_cashflow / raw_income FY2020–FY2025 and DuckDB 2026Q3; verifier: FY2025 annual-report other-operating-cash notes, 2026 Q3 report)_
- [hypothesis, low] Distributors bought ahead in 2025 (Q2 2025 collections 10.86亿 against 6.60–6.98亿 in prior second quarters) and destocked in 2026 (Q2–Q3 2026 collections 3.44亿 and 2.61亿). _(source: S2 raw_cashflow single quarters (DuckDB, workpaper A5); verifier: distributor inventory or receivable ageing)_
- [method, low] For a holding company with large minority interests and net cash, bound the parent's net financial assets before any reverse curve (minority claim wholly on cash; wholly on operations), state a central case from the minority profit share applied to the subsidiary's NOA, then value the cash at face and solve only the operating stake. Applying the operating hurdle to the full price (E = r × P) overstates the earnings the price needs. _(source: 000915.SZ/2026-11-25-01 r1 t6–t7; Penman like-for-like (P-007, P-012))_
