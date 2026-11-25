# Round 1 — Gruesome on the full decade: is the 3,836亿 of net operating assets still earning anything, or is the book just carrying it at cost?

**Session** 000002.SZ / 2026-11-25-01 · **started** 2026-11-25T00:40:00-08:00 · **ended** 2026-11-25T01:15:00-08:00
**Participants** Warren Buffett, Stephen Penman, Jeff Bezos, Li Lu (李录, Himalaya Capital), Joel Greenblatt

> Round one of a new session, business before news: ROE near 20% in FY2016–20 turned into 1,380亿 of parent losses in FY2024–25, and ten-year Penman free cash flow is negative. The great/good/gruesome verdict and whether book (0.36×) is a floor decide everything that follows.

## Discussion

_Simulated expert perspectives._

### Warren Buffett

Gruesome, on the full decade. Vanke's operations earned 2,055亿 after tax over FY2016–25, yet produced −273亿 of free cash on Penman's measure, because net operating assets nearly tripled by 2023 to earn it. I reread the passage: "The worst sort of business is one that grows rapidly, requires significant capital to engender the growth, and then earns little or no money." Stephen, last year the asset base shrank about 505亿 less than it would have if it had followed sales — is what's left still earning anything, or just sitting at cost?

<details>
<summary>Evidence and turn notes</summary>

confidence high · 2026-11-25T00:40:00-08:00

**Evidence**
- Verdict gruesome: the worst sort of business grows rapidly, requires significant capital to engender the growth, and then earns little or no money _(source: SRC source-files/Warren Buffett/Businesses – The Great, the Good and the Gruesome.md, paragraph 'Now let’s move to the gruesome' (line 81))_
- Operating income after tax (total firm, before minorities) FY2016–FY2025 sums to 2,054.6亿; same scope as Penman FCF = OI − ΔNOA _(source: derived: sum of S2 reformulated_is oi_after_tax FY2016–FY2025)_
- Penman free cash flow from operations (OI − ΔNOA) FY2016–FY2025 sums to −273.4亿 _(source: derived: sum of S2 fcf_from_oi FY2016–FY2025 (capital & reinvestment table))_
- NOA 1,802.3亿 (end FY2016) to 5,344.8亿 (end FY2023), ratio 2.97 _(source: derived: S2 capital & reinvestment NOA end)_
- FY2025 NOA fell 1,061.9亿 while 营业总收入 fell 1,097.4亿; growth gap +10.3pp, so NOA fell 504.5亿 less than proportional to sales (excess move = NOA begin × gap); NOA end 3,836.3亿 _(source: S2 paired-line divergence scan FY2025 (calc.growth_gap))_ — {"noa_end": 3836.3, "d_noa": -1061.9, "d_rev": -1097.4, "excess": 504.5, "gap_pp": 10.3}

</details>

### Stephen Penman

No — return on net operating assets was −19.7% in FY2025. But let me test 'gruesome' first: in FY2016–20 operating cash more than covered parent profit, which looks like a great business. The catch is who supplied that cash. In 2021 operating liabilities, mostly buyers' deposits and supplier bills, were 2.77× the net operating assets; netting them out, as my lecture says to, shows the cash was the homebuyers', not earned. So the counter-case fails. Jeff, deposits are down 89% from their 2021 peak — what replaced that funding as they unwound?

<details>
<summary>Evidence and turn notes</summary>

confidence high · 2026-11-25T00:43:00-08:00

**Evidence**
- RNOA (average NOA basis) −19.7% FY2025 _(source: S2 ratios_annual basis=average (rnoa))_ — {"2025": -0.197}
- Counter-case tested: FY2016–20 CFO 2,543.9亿 against parent net income 1,632.36亿 _(source: derived: S2 raw:cfo and raw:net_income_parent FY2016–FY2020)_
- Operating liabilities 12,492.1亿 / NOA 4,512.3亿 = 2.77× at FY2021 year-end _(source: derived: S2 reformulated_bs FY2021 (OL / NOA))_
- View operating assets as net operating assets, that is, net of operating liabilities, and debt as net debt _(source: SRC source-files/Stephen Penman/Penman_What_Matters_in_Company_Valuation.pdf p.9 (PDF page; passage before 'The financial statements tie together'))_
- 合同负债 + 预收款项 6,382.23亿 (FY2021) → 677.2亿 (2026Q3), −89.4% _(source: derived: calc.pct_change on S2 raw_balancesheet contract_liab + adv_receipts FY2021, 20260930)_

**Challenges**
- → Warren Buffett: Counter-case to 'gruesome': FY2016–20 operating cash (2,543.9亿) more than covered parent profit (1,632.4亿); tested and rejected because the cash came from operating liabilities (2.77× NOA in 2021)

</details>

### Jeff Bezos

Nothing did. Most deposits were settled by handing over finished homes, which uses up inventory rather than cash. The cash-flow bridge shows inventory releasing about 7,575亿 over 2022–25 while lower deposits and supplier balances took out about 8,718亿, so four years of operations left almost nothing to replace the float. Amazon's 2004 letter prizes "collecting payments from our customers before payments are due to suppliers"; Vanke ran that cycle for a decade and is now running it backwards. Li Lu, other receivables shrank about 248亿 less than the fall in sales would explain — how much of that balance is partner money that won't come back?

<details>
<summary>Evidence and turn notes</summary>

confidence medium · 2026-11-25T00:46:00-08:00

**Evidence**
- Indirect-method CFO: decrease in inventories FY2022–25 sums to 7,574.5亿 _(source: derived: sum of S2 raw_cashflow decr_inventories FY2022–FY2025)_
- Increase in operating payables (incl. customer advances) FY2022–25 sums to −8,718.0亿 in the indirect-method bridge; much of the advance decline is settled by delivery (non-cash, offset by inventory), so this is a bridge reading, not a cash repayment of deposits _(source: derived: sum of S2 raw_cashflow incr_oper_payable FY2022–FY2025)_
- CFO FY2022–25 sums to 94.7亿 (left almost nothing) _(source: derived: sum of S2 raw:cfo FY2022–FY2025)_
- Amazon's operating cycle: collecting payments from our customers before payments are due to suppliers _(source: SRC source-files/Jeff Bezos/Amazon Shareholder Letter 2004.html (operating-cycle paragraph in the free cash flow discussion))_
- 其他应收款 FY2025 fell 460.1亿 while 营业收入 fell 1,097.4亿; excess move 248.0亿; balance 1,754.1亿 _(source: S2 paired-line divergence scan FY2025 (calc.growth_gap))_ — {"latest": 1754.1, "d_a": -460.1, "d_b": -1097.4, "excess": 248.0}

</details>

### Li Lu (李录, Himalaya Capital)

I can't tell from here, and that is the bear case. Other receivables were 1,754亿 at FY2025, and a 342亿 credit write-down landed the same year — my hypothesis is loans to project partners, which only the receivables note can confirm. Then there's a liability that grew to 356亿 since 2024 with no lender named in our data. My lecture's test is whether I want to be a passive minority shareholder here; I can't answer while I don't know who ranks ahead of me. Joel, with the equity this thin, what does a small error in asset values do to the stock?

<details>
<summary>Evidence and turn notes</summary>

confidence medium · 2026-11-25T00:49:00-08:00

**Evidence**
- 其他应收款(合计) 1,754.14亿 FY2025 _(source: S1 balance_sheet oth_rcv_total FY2025)_ — {"2025": 1754.14}
- Credit impairment loss (信用减值损失) −341.74亿 FY2025 _(source: S2 raw_income credit_impa_loss FY2025)_ — {"2025": -341.74}
- The credit impairment sits mainly on partner/JV loans inside other receivables _(source: hypothesis (labelled in text))_
- 其他非流动负债 17.75亿 FY2024 → 356.21亿 2026Q3; no counterparty in the local data _(source: S2 raw_balancesheet oth_ncl FY2024, 20260930 (DuckDB; workpaper Appendix C))_ — {"2024": 17.75, "2026Q3": 356.21}
- Do I want to be a passive minority shareholder in this company? It's a question that must be answered before you make any investment _(source: SRC source-files/Li Lu/Li Lu_CBS Lecture Notes.pdf p.15)_

</details>

### Joel Greenblatt

It gets magnified about twelve times. The equity is under 8% of a 4,245亿 enterprise, so each 1% error in what the whole enterprise is worth moves the stock about 12.6%. And I can't fall back on normal earnings: core operating profit before tax went from its 2020 peak to a loss last year, on a company whose sales have more than halved. When I can't estimate normalized EBIT with confidence, I pass — this is a speculation on asset values and refinancing, not an investment. Warren, does anything in the book give a floor above zero?

<details>
<summary>Evidence and turn notes</summary>

confidence medium · 2026-11-25T00:52:00-08:00

**Evidence**
- EV 4,245.10亿 = mkt cap 336.45 + interest-bearing debt (291.81 + 1,606.21 + 1,210.02 + 89.27 + 111.26) + minority 1,124.74 − cash 524.46 − trading 0.20 (2026Q3 balances, S1 quote 2026-11-20) _(source: derived: calc.enterprise_value)_
- Equity is 7.93% of EV _(source: derived: market cap / calc.enterprise_value)_
- A 1% change in EV (42.45亿) is a 12.6% change in market cap _(source: derived: 0.01 × EV / market cap)_
- S2 OI core pretax 834.8亿 FY2020 (peak) → −74.4亿 FY2025 _(source: S2 reformulated_is oi_core_pretax)_ — {"2020": 834.8, "2025": -74.4}
- 营业收入 5,038.38亿 FY2022 → 2,334.33亿 FY2025, ratio 0.463 (more than halved) _(source: derived: S1 annual.营业收入)_

</details>

### Warren Buffett

One I wouldn't lean on. Strip out goodwill, intangibles and the tax credits that need future profits, and tangible book is about 554亿 — still above the 336亿 price. But a write-down averaging under 3% on the remaining non-cash assets erases that margin, assuming the parent bears all of it. That's a thin cushion. Stephen, is this year's selling still covering cost once sales taxes and interest are paid?

<details>
<summary>Evidence and turn notes</summary>

confidence medium · 2026-11-25T00:55:00-08:00

**Evidence**
- Tangible book ex goodwill, intangibles and deferred tax assets 553.60亿 (2026Q3) _(source: derived: parent equity − goodwill − intangibles − deferred tax assets (S2 raw_balancesheet 20260930))_
- Market cap 336.45亿 at S1 quote 2026-11-20 (price 2.82元) _(source: S1 quote)_ — {"mkt_cap": 336.45, "price": 2.82}
- (Tangible book ex DTA 553.60 − market cap 336.45) / tangible non-cash assets 8,426.01亿 = 2.58% average write-down takes tangible book to the price, assuming all of it falls on the parent (none on minorities or tax); tangible non-cash assets = total assets − cash − trading − goodwill − intangibles − DTA _(source: derived: 2026Q3 S2 raw_balancesheet; S1 quote 2026-11-20)_

</details>

### Stephen Penman

No, and that's why I don't count your cushion. In the first nine months of 2026, gross profit left after sales taxes was about 12亿 — under a fifth of the 62亿 interest bill alone, before any selling or admin cost. So each home sold now loses money once it's carried, and the parent is losing about 80亿 a quarter even with small write-downs. Book isn't a floor here; it's a balance that shrinks every quarter. Jeff, with sales losing money, is there any cash to service the debt without new borrowing?

<details>
<summary>Evidence and turn notes</summary>

confidence high · 2026-11-25T00:58:00-08:00

**Evidence**
- 9M26 营业收入 1,049.99 − 营业成本 980.29 − 税金及附加 58.16 = 11.54亿 _(source: derived: S2 raw_income 20260930 YTD (DuckDB; workpaper Appendix C))_
- 9M26 interest expense (财务费用-利息费用) 62.23亿 _(source: S2 raw_income fin_exp_int_exp 20260930)_ — {"9M26": 62.23}
- Gross profit after sales taxes / interest expense = 0.185 (under a fifth) _(source: derived: S2 raw_income 20260930)_
- Parent net loss by single quarter 2026: Q1 −59.5, Q2 −90.0, Q3 −89.9; average −79.8亿 _(source: derived: S2 quarterly filings (de-cumulated raw_income n_income_attr_p))_
- 9M26 asset impairment −39.37亿 and credit impairment −4.07亿, small against FY2025 −219.29亿 and −341.74亿 _(source: S2 raw_income 20260930, FY2025)_ — {"asset_9m26": -39.37, "credit_9m26": -4.07, "asset_fy25": -219.29, "credit_fy25": -341.74}

**Challenges**
- → Warren Buffett: Tangible book is not a cushion when 2026 sales lose money after carrying cost; the parent book shrinks about 80亿 a quarter

</details>

### Jeff Bezos

No. In the first nine months of 2026 it repaid 186亿 of debt but could raise only 105亿 of new borrowing, and covered the gap out of a shrinking cash pile. That is a business being run for its lenders, not its owners. And debt falling due within a year is about 3.6× the cash on hand. Li Lu, does anything in the record tell us who is rolling that debt?

<details>
<summary>Evidence and turn notes</summary>

confidence high · 2026-11-25T01:01:00-08:00

**Evidence**
- 9M26 cash repaid on borrowings 185.85亿; cash received from borrowings 104.79亿 _(source: S2 raw_cashflow 20260930 YTD (c_prepay_amt_borr, c_recp_borrow))_ — {"repaid": 185.85, "borrowed": 104.79}
- Cash and equivalents fell 146.56亿 in 9M26; 货币资金 672.41亿 (FY2025) → 524.46亿 (2026Q3) _(source: S2 raw_cashflow n_incr_cash_cash_equ 20260930; S1 EV items 20260930)_ — {"chg": -146.56, "cash25": 672.41, "cash26q3": 524.46}
- Debt due within a year 1,898.02亿 (短期借款 291.81 + 一年内到期的非流动负债 1,606.21) = 3.62× cash 524.46亿 (2026Q3) _(source: derived: S1 EV items 20260930)_

</details>

### Li Lu (李录, Himalaya Capital)

Not locally, and that's the point. Bracketing helps [reasoning method, not evidence — Tukey 2.5]: take the tangible book at par and the equity is worth up to 554亿; an average write-down of about 6.6% on the remaining non-cash assets takes it to nothing. A judgment that small separates the two brackets, so the answer sits in two lines — inventory and partner receivables — plus whoever holds the 356亿. What would refute my bear case is the FY2025 annual report's receivables note and a note naming that lender and its rank. Stephen, setting the documents aside, what does today's price itself assume?

<details>
<summary>Evidence and turn notes</summary>

confidence medium · 2026-11-25T01:04:00-08:00

**Evidence**
- Bracket: upper = tangible book ex DTA 553.60亿 at par; lower = 0 after a 6.57% average write-down on the 8,426.01亿 tangible non-cash assets (2026Q3; parent bears all, labelled) _(source: derived: tangible book ex DTA / tangible non-cash assets)_
- Documents that would close the bear case: FY2025 annual report notes on other receivables (counterparties, ageing, security, provisions) and on other non-current liabilities (lender, rank, rate, maturity) _(source: hypothesis (labelled in text))_

_[reasoning method, not evidence — john-tukey · 2.5]_

</details>

### Stephen Penman

A turnaround the record doesn't show yet. With the price below book and no growth, the price is just steady profit divided by the required return. I'd argue 12% here, an assumption that prices in the refinancing risk, and it asks for about 40亿 a year on today's book; at 8% it's 27亿, at 15% about 50亿. Against this year's losses, the price is a bet that the bleeding stops soon and most of the book survives. Jeff, does management's record with cash give us any reason to trust it with that bet?

<details>
<summary>Evidence and turn notes</summary>

confidence medium · 2026-11-25T01:07:00-08:00

**Evidence**
- Implied steady parent earnings at r = 12%, g = 0: 40.37亿 (4.3% on 930.94亿 book) _(source: derived: calc.implied_earnings_re(price=336.45, book=930.94, r=0.12))_
- Implied steady parent earnings at r = 8%, g = 0: 26.92亿 _(source: derived: calc.implied_earnings_re(price=336.45, book=930.94, r=0.08))_
- Implied steady parent earnings at r = 15%, g = 0: 50.47亿 _(source: derived: calc.implied_earnings_re(price=336.45, book=930.94, r=0.15))_
- Required return 12% argued for rollover risk on 3.6× cash falling due within a year; 8% and 15% shown as the reverse curve _(source: assumption (labelled in text))_

</details>

### Jeff Bezos

Not much. Over FY2016–22 the board declared 761亿 of dividends, while those same seven years of operations and investment produced only about 368亿 of cash. Financing filled the gap: partners put 1,335亿 into project companies and debt excluding leases roughly quadrupled. Share count barely moved, so the problem wasn't dilution; it was paying out profits whose cash had already gone into land and partner stakes. Warren, does that leave this in your too-hard pile?

<details>
<summary>Evidence and turn notes</summary>

confidence high · 2026-11-25T01:10:00-08:00

**Evidence**
- Cash dividends declared FY2016–FY2022 sum to 761.41亿 (年度现金分红总额; none FY2023–25) _(source: derived: sum of S1 annual.分红 FY2016–FY2022)_
- CFO + investing cash flow FY2016–FY2022 = 2,612.5 − 2,245.0 = 367.5亿 (same window as the dividends) _(source: derived: S2 raw_cashflow n_cashflow_act + n_cashflow_inv_act FY2016–FY2022)_
- Minority partners' capital received (吸收投资收到的现金-子公司吸收少数股东投资) FY2016–FY2022 sums to 1,335.0亿 _(source: derived: sum of S2 raw_cashflow incl_cash_rec_saims FY2016–FY2022)_
- Interest-bearing debt ex leases (短期借款 + 一年内到期 + 长期借款 + 应付债券) 795.0亿 FY2015 → 3,176.4亿 FY2022, ratio 4.0 _(source: derived: S2 raw_balancesheet FY2015, FY2022)_
- Total shares 110.39亿 (FY2016) → 119.31亿 (FY2025), +8.1% (barely moved) _(source: derived: S1 annual.总股本)_

</details>

### Warren Buffett

Yes — the too-hard pile, and I'll concede Stephen's point: a book that shrinks every quarter isn't a cushion. The business verdict is settled: gruesome, a decade of growth that consumed capital and left owners nothing in operating free cash. The stock is cheap only if the inventory and partner loans are worth close to book and lenders keep rolling the debt, and neither is in our data. I'd want the annual-report notes, and one quarter where sales cover their carrying cost, before calling it an investment.

<details>
<summary>Evidence and turn notes</summary>

confidence medium · 2026-11-25T01:13:00-08:00

**Concessions**
- ← Stephen Penman: Tangible book is not a cushion while 2026 sales lose money after carrying cost; the book is a shrinking balance, not a floor

</details>

## Disagreements

- **Does tangible book give the equity a floor?** — resolved
  - Warren Buffett: tangible book ex deferred tax assets, about 554亿, sits above the 336亿 price; a write-down averaging under 3% on the remaining non-cash assets closes the gap — a thin cushion
  - Stephen Penman: no cushion: 9M26 gross profit after sales taxes was 11.5亿 against 62.2亿 of interest, so the parent book shrinks about 80亿 a quarter
  - _resolution_: Buffett conceded in the closing turn: the book is a shrinking balance, not a floor, until a quarter shows sales covering selling, admin and interest (9M26: 11.5亿 against 128.7亿).
- **Who rolls the 1,898亿 due within a year, and does the 356亿 new liability rank ahead of equity?** — open
  - Li Lu (李录, Himalaya Capital): bear case unrefuted locally: the lender is unnamed and may be senior, and no actual controller is on record
  - Joel Greenblatt: pass until known: the equity moves about 12.6% for each 1% of enterprise value
  - Jeff Bezos: the company repaid 186亿 while raising 105亿 in 9M26 — it is being run for its lenders
  - _resolution_: Needs the FY2025 annual-report notes on other non-current liabilities and other receivables, and the debt-maturity schedule. The Tukey bracket shows the equity's value turns on inventory, partner receivables and that lender, not on earnings power.

## Conclusion

**Answer (medium confidence):** Vanke was a gruesome business dressed as a great one. For a decade homebuyers' deposits and suppliers funded the growth, so ROE ran near 20% while operations produced no free cash: ten-year operating income after tax of 2,055亿 against Penman free cash flow (OI − ΔNOA) of −273亿 (same total-firm scope; parent profit 825亿), with net operating assets nearly tripling to 2023. Since 2021 the float has run in reverse — customer deposits down 89%, mostly settled by delivering homes — and selling down the land bank left almost no cash (FY2022–25 operating cash 95亿); in 2026 sales lose money once sales taxes and interest are paid. At 336亿 (S1 quote 2026-11-20, 2.82元) the stock is 0.36× parent book, but the book is not a floor: the equity is 7.9% of a 4,245亿 enterprise (each 1% on enterprise value moves the stock about 12.6%), tangible book of 554亿 falls to the price with a write-down averaging under 3% on the remaining non-cash assets and to zero at about 6.6%, and 1,898亿 of debt falls due within a year against 524亿 of cash. The price asks for about 40亿 a year of steady profit at the argued 12% hurdle (27亿 at 8%, 50亿 at 15%) against losses near 80亿 a quarter. The insight to remember: this is no longer an earnings question but a bet on asset realization and on who rolls the debt — a speculation the local record cannot underwrite, so the panel passes for now. Scorecard: business type GRUESOME on the full cycle (capital-hungry growth, then losses; OI core pretax 835亿 in 2020 to a loss in FY2025); cash backing NO — CFO 2,544亿 in FY2016–20 rode the deposit float, FY2021–23 CFO was 108亿 against 573亿 of parent profit, and CFO − capex (2,057亿) overstates owner cash because land sits in CFO and JV stakes in investing (CFO + investing 534亿); return driver LEVERAGE — asset turnover 0.2–0.3 and a 6–10× equity multiplier, with the leverage hidden in operating liabilities (2.77× NOA in 2021); capital allocation: 761亿 of dividends declared FY2016–22 against 368亿 of operating and investing cash in the same years, with partners' capital (1,335亿) and debt filling the gap; cheap or not CHEAP TO BOOK ONLY (PB 0.36, earnings and after-interest cash negative); floor NONE for the equity — tangible book ex deferred tax assets 554亿 is above the price but shrinks about 80亿 a quarter and vanishes with a write-down averaging about 6.6% on the remaining non-cash assets (parent bearing all of it, labelled). Confidence medium: the business verdict rests on direct S2 series, but the valuation pass depends on an argued hurdle and on annual-report notes not in the local data.

**What would change our mind**
- The FY2025 annual-report receivables note showing most of the 1,754亿 other receivables secured and current would lift the lower bracket toward book
- A named lender for the 356亿 ranking behind or alongside equity, plus a refinancing of the 1,898亿 due within a year, would turn the stub from a speculation into a priced option on the book
- A quarter in which gross profit after sales taxes covers selling, admin and interest (9M26: 11.5亿 against 128.7亿) would show the book has stopped shrinking
- Another year of impairments at the FY2025 scale (asset −219.3亿, credit −341.7亿) would take parent book below the 336亿 market cap

**Open questions**
- Who holds the 356.2亿 of other non-current liabilities (17.8亿 at FY2024), at what rate, maturity and rank? Document: FY2025 annual report note on 其他非流动负债 and the 2026 Q3 report.
- What is in the 1,754亿 other receivables (counterparties, ageing, security, provisions), and what did the −341.7亿 FY2025 credit impairment hit? Document: FY2025 annual report notes on 其他应收款 and 信用减值损失.
- Maturity schedule of the 1,606.2亿 一年内到期的非流动负债 and any bond extensions or shareholder support agreements. Document: FY2025 annual report and 2026 announcements (not in local data).
- Largest shareholder and its holding: raw_stock_basic shows 无实际控制人; the shareholder register is needed.
- Inventory realization by project vintage: carrying cost against 2026 selling prices. Document: FY2025 annual report note on 存货跌价准备.

## Thinkers consulted (reasoning methods, not evidence)

- john-tukey · 2.5 — Two brackets with opposite biases on the book (tangible book at par vs a 6.6% average write-down on the remaining non-cash assets) to locate the lines that decide the equity value: inventory, partner receivables and the 356亿 lender. Diagnostic, not a valuation range.

## Candidate questions for the next round

- Who is the lender behind the 356亿 of other non-current liabilities, and does it rank ahead of shareholders? (Needs the FY2025 annual-report note — can you supply it or authorize fetching it?)
- Inventory vs cost of sales (scan item 7, +179亿 excess move FY2025): is the 3,300亿 land bank carried above what 2026 sales realize, project by project?
- Payables vs cost of sales (scan item 4, +209亿 excess move; supplier days 555 → 803): how much of the 1,116亿 of payables is overdue construction cost that will need cash in 2027?

## Knowledge candidates (to be validated before entering knowledge/)

- [fact, high] FY2016–FY2025 operating income after tax (total firm) sums to 2,054.6亿 while Penman free cash flow from operations (OI − ΔNOA, S2 fcf_from_oi) sums to −273.4亿 (parent net income 825.07亿); NOA rose from 1,802.3亿 (end FY2016) to 5,344.8亿 (end FY2023). _(source: S2 raw:net_income_parent, fcf_from_oi, capital & reinvestment FY2016–FY2025)_
- [fact, high] Customer advances (合同负债 + 预收款项) fell from 6,382.2亿 at FY2021 to 677.2亿 at 2026Q3 (−89.4%); FY2022–FY2025 inventory decreases released 7,574.5亿 in the indirect CFO block while operating payables absorbed 8,718.0亿, leaving CFO of 94.7亿 over the four years. _(source: S2 raw_balancesheet, raw_cashflow FY2021–FY2025, 20260930)_
- [fact, high] 9M26 gross profit after 税金及附加 was 11.54亿 (营业收入 1,049.99 − 营业成本 980.29 − 58.16) against interest expense of 62.23亿; parent net loss averaged 79.8亿 per quarter in 2026 Q1–Q3. _(source: S2 raw_income 20260930 (DuckDB), quarterly filings)_
- [hypothesis, low] The rise in other non-current liabilities from 17.75亿 (FY2024) to 356.21亿 (2026Q3) is shareholder or related-party loans that may rank ahead of equity; verify in the FY2025 annual-report note on 其他非流动负债. _(source: S2 raw_balancesheet oth_ncl; no counterparty in local data)_
- [hypothesis, low] The FY2025 credit impairment of −341.74亿 sits mainly on partner/JV loans inside the 1,754亿 of other receivables; verify in the FY2025 annual-report notes on 其他应收款 and 信用减值损失. _(source: S2 raw_income credit_impa_loss; S1 oth_rcv_total)_
- [method, medium] For a developer priced below book: solve the reverse curve for earnings rather than growth (calc.implied_earnings_re; E = r × P at g = 0), express the book–price gap as an average write-down on non-cash assets, and measure owner cash as CFO + investing cash flow, not CFO − capex, because land sits in CFO and JV stakes in investing. _(source: panel method this round (Penman reverse curve, Bezos float, Buffett floor))_
