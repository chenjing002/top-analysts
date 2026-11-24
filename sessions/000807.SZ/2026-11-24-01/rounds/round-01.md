# Round 1 — Is the harvest's free cash real owner cash, and what normal earning power should today's price be tested against?

**Session** 000807.SZ / 2026-11-24-01 · **started** 2026-11-24T10:00:00+08:00 · **ended** 2026-11-24T10:55:00+08:00
**Participants** Warren Buffett, Joel Greenblatt, Stephen Penman, Li Lu (李录, Himalaya Capital), Jeff Bezos

> Round one of a system-test rerun: the decade splits into a capital-hungry build-out (FY2016-20) and a cash-rich harvest (FY2021-25), and harvest capex runs below half of depreciation, so the headline free cash may overstate what owners can actually take.

## Discussion

_Simulated expert perspectives._

### Warren Buffett

Good in harvest, not great: a cost-position smelter with no pricing power, so the moat is policy and power cost, not franchise. The line that surprised me: 2021–25 free cash 308.6亿 against parent profit 223.1亿, while capex ran at less than half of depreciation. Either maintenance is genuinely cheap or spending is being deferred. Joel, if holding volume costs depreciation-level capex, how much of that cash is really owner cash?

<details>
<summary>Evidence and turn notes</summary>

confidence medium · 2026-11-24T10:00:00+08:00

**Evidence**
- Verdict good in harvest, not great: no enduring moat, a commodity spread rather than a franchise; the good savings account pays an attractive rate but this one needed a decade of deposits first _(source: SRC source-files/Warren Buffett/Businesses – The Great, the Good and the Gruesome.md pp.6-7 (moat criterion; three savings accounts))_
- Harvest FY2021-25 free cash flow 308.57亿 _(source: derived: calc.fcf)_
- Harvest FY2021-25 parent net income 223.11亿 _(source: S2 raw:net_income_parent FY2021-FY2025)_ — {"2021": 33.19, "2022": 45.69, "2023": 39.56, "2024": 44.12, "2025": 60.55}
- Harvest capex 42.69亿 vs D&A 91.15亿, ratio 0.467 (workpaper Appendix A; D&A is the sum of four cash-flow add-backs) _(source: derived: calc.fcf_conversion)_

</details>

### Joel Greenblatt

Deferred, I'd guess — pot relining comes in waves, so maintenance near depreciation is my estimate, not a reported figure; the capex note would close it. Then owner cash is roughly profit itself. The harvest band runs 33.2亿 to 60.6亿 with a 44.1亿 median, and 2026's windfall sits outside that window. That median, not the trailing peak, is what I'd underwrite. Stephen, at 44.1亿 of normal profit, what growth is today's price buying?

<details>
<summary>Evidence and turn notes</summary>

confidence medium · 2026-11-24T10:05:00+08:00

**Evidence**
- Maintenance capex guess near depreciation (18.6亿/yr FY2025 D&A) rather than harvest spend (8.5亿/yr); owner earnings then equal profit, 44.12亿 at the median _(source: estimate (labelled in text))_
- Harvest parent-NI band low 33.19亿 (FY2021) _(source: derived: calc.normalized_band)_
- Harvest parent-NI band high 60.55亿 (FY2025) _(source: derived: calc.normalized_band)_
- Harvest median 44.12亿 equals FY2024 parent NI (middle of the five harvest years; calc.normalized_band in workpaper Appendix H) _(source: S2 raw:net_income_parent FY2024)_ — {"2024": 44.12}

**Challenges**
- → Warren Buffett: Harvest free cash 308.6亿 overstates owner cash if maintenance capex is deferred below depreciation; owner earnings a+b-c with c at depreciation leaves roughly profit itself

</details>

### Stephen Penman

With no growth the price pays 6.1% on that median. My hurdle is 8% — arguable for a policy-exposed commodity, so the workpaper shows two other hurdles and I conclude at 8%, where the price needs 4.6% perpetual growth. A capacity-capped smelter growing forever at 4.6% is a stretch. Joel, does your enterprise-value test pass your bogey once the hoard's reachability is priced?

<details>
<summary>Evidence and turn notes</summary>

confidence medium · 2026-11-24T10:10:00+08:00

**Evidence**
- Zero-growth return 6.06% at price 728.62亿 on normalized earnings 44.12亿 _(source: derived: calc.zero_growth_return)_
- Implied perpetual growth 4.60% at r = 8% (the hurdle the conclusion uses), price 728.62亿, book 420.9亿 _(source: derived: calc.implied_growth_re)_
- Reverse curve at r = 7%: implied growth 2.24% _(source: derived: calc.implied_growth_re)_
- Reverse curve at r = 10%: implied growth 9.34% _(source: derived: calc.implied_growth_re)_
- Band low end tested: at E 33.19亿 the zero-growth return is 4.55% and implied growth at r = 8% is 8.16% (r = 7%: 5.79%, r = 10%: 12.89%) — the low end fails the hurdle outright _(source: derived: calc.implied_growth_re)_

</details>

### Joel Greenblatt

Mid-cycle core EBIT 61.8亿 — a proxy from reformulated operating income, disclosed in the workpaper — yields 8.2% after tax if all the cash reaches us, 6.8% if only half does. Both clear my bogey; the decade-wide mid EBIT fails it at either cash assumption. So the window and the cash reachability decide the verdict, not the trailing peak. Li Lu, the stock fell while trailing profit more than doubled — what is Mr. Market's opposing view?

<details>
<summary>Evidence and turn notes</summary>

confidence medium · 2026-11-24T10:15:00+08:00

**Evidence**
- EV 565.5亿 with all cash deducted; mid-cycle core EBIT 61.8亿 (harvest median of oi_core_pretax, an EBIT proxy; the bottom-up rebuild from DuckDB expense lines gives 60.85亿 excl other income and 61.51亿 incl, so the proxy gap is 0.95亿 and closable locally) yields 10.93% pre-tax, 8.2% after tax at 25% _(source: derived: calc.enterprise_value)_
- EV 681.39亿 if only half the cash and trading assets are ever recoverable; same EBIT 61.8亿 yields 9.07% pre-tax, 6.8% after tax; rebuilt decade-wide mid EBIT 38.57亿 yields 5.11% / 4.25% after tax at the two EVs and fails the 6% bogey _(source: derived: calc.enterprise_value)_
- Trailing parent NI 132.67亿 vs 49.90亿 a year earlier = 2.66x, +166% — more than doubled, not tripled _(source: derived: calc.pct_change)_
- Cash is not in the investor's pocket: value it by management's deployment history, and EV at par overstates upside when the cash cannot be unlocked — the availability check behind the half-vs-full range _(source: SRC source-files/csinvesting/Lecture 11-Balance-Sheet-Analysis-Duff-Phelps-ROE-vs-ROC.pdf pp.1-2 (I. CASH; Flaw in Using Enterprise Value))_

</details>

### Li Lu (李录, Himalaya Capital)

The opposing view: 2026's margin is a borrowed cost windfall, and alumina prices will take it back. The local test fits — 9M revenue up 19.4% year-on-year while cost of sales fell 4.1%, so the gain is cost-side, not price-side. Megastudy's lesson applies: the market's bear case can be right. The stock's 36% fall says traders believe it. I cannot refute it locally: no alumina series here. Joel, your harvest window excludes 2026 — does adding the windfall as permanent double-count the cycle?

<details>
<summary>Evidence and turn notes</summary>

confidence medium · 2026-11-24T10:20:00+08:00

**Evidence**
- 9M2026 vs 9M2025 (year-on-year, cumulative): revenue 526.16亿 vs 440.72亿 = +19.4%; cost of sales 357.59亿 vs 372.90亿 = a 4.1% decline; the margin gain is cost-side _(source: S2 raw_income 9M2026/9M2025 (DuckDB, report_type='1', deduped; query in workpaper Appendix D))_ — {"rev_9M26": 526.16, "rev_9M25": 440.72, "cost_9M26": 357.59, "cost_9M25": 372.9}
- Stock decline 36% YTD: 32.84元 at 20251231 to 21.01元 at the S1 quote 2026-11-20 _(source: derived: calc.pct_change)_
- Bear case: the 2026 cost windfall reverses when alumina prices recover; unverified, no local commodity price series _(source: KB H-000807-001)_
- Megastudy: the market's opposing view (free government service) was real and revenue fell — a cheap stock can deserve its price; discover and test the bear case before calling it a bargain _(source: SRC source-files/Li Lu/Li Lu_CBS Lecture Notes.pdf pp.4-5 (What's wrong? Why is the company so cheap?))_

**Challenges**
- → Joel Greenblatt: The harvest-only window keeps the cost-depression years and drops the cost-windfall year; adding 2026 as permanent would double-count one cost cycle

</details>

### Joel Greenblatt

Fair challenge — the window is truncated: the 2021–22 cost depression and the 2026 cost windfall are two sides of one cycle, and my harvest band keeps only the downside side. Asking what a defensible solution looks like without external prices: the mechanical median stands, labelled truncated, until the alumina series says otherwise. I concede the higher mid-cycle is an argued override, not a finding. Stephen, strip the hoard and its carry — what does the operating business alone yield?

<details>
<summary>Evidence and turn notes</summary>

confidence medium · 2026-11-24T10:25:00+08:00

**Evidence**
- Harvest window FY2021-25 is truncated for a full cost cycle (no cost-windfall year inside); calc.normalized_band docstring requires a full cycle or a truncated label _(source: derived: calc.normalized_band)_

**Concessions**
- ← Li Lu (李录, Himalaya Capital): The harvest band is truncated on the upside; the mechanical median 44.12亿 stands only as a labelled base until the alumina price series verifies persistence

_[reasoning method, not evidence — richard-hamming · 2.2]_

</details>

### Stephen Penman

My own headline mixed financing into operations: the hoard's bank carry sits inside that 6.1%. Strip the cash and its income — I assume 2% pre-tax carry, an assumption, not a reported yield — and the operating business yields about 7.9% with no growth; deducting minorities' book share of the cash, a rough proxy, puts it near 7.7%. So even ex-cash the price only meets my hurdle at the mid band, and the basis matters. Jeff, does management's record say the hoard ever reaches owners?

<details>
<summary>Evidence and turn notes</summary>

confidence medium · 2026-11-24T10:30:00+08:00

**Evidence**
- Like-for-like: earnings 44.12亿 less after-tax carry on 211.79亿 net cash at an assumed 2% pre-tax yield, over ex-cash price 728.62-211.79 = 516.83亿, gives 7.92% zero-growth (1.5% carry case: 8.08%; workpaper Appendix C) _(source: derived: calc.like_for_like_earnings)_
- Minority basis sensitivity: proxy minorities' share of net cash by their book-equity share 48.67 / 469.57 = 10.4%; parent-attributable cash 189.85亿, ex-cash yield 7.66% — below the 8% hurdle; a rough proxy, not a reported cash split _(source: derived: calc.like_for_like_earnings)_
- Net cash 211.79亿 at 2026Q3 (cash 193.71 + trading 38.07 less interest-bearing debt 19.99); the 2% pre-tax carry is an assumption — FY2025 reformulated net financial income was only 0.4亿 after tax _(source: S1 balancesheet 20260930 EV items)_ — {"cash": 193.71, "trading": 38.07, "debt": 19.99}

**Concessions**
- ← Joel Greenblatt: The cash-availability range is the right frame: the headline zero-growth return needed the same operating/financing split before it could be quoted

</details>

### Jeff Bezos

Partly — payout reached 40% last year, the first real turn toward owners. Per share, harvest free cash averaged 1.78元 a year over 2021–25, about 8.5% of today's price; the peak year flatters that yield. And owners diluted themselves via placements to fund the build-out, with no buybacks. Li Lu, what document closes your bear case?

<details>
<summary>Evidence and turn notes</summary>

confidence medium · 2026-11-24T10:35:00+08:00

**Evidence**
- FY2025 payout 40.0%: dividend 24.24亿 / parent NI 60.55亿 _(source: derived: calc.fcf_conversion)_
- Harvest FCF per share 1.78元/yr (308.57亿 over 5 years on 34.6796亿 shares) = 8.47% of the 21.01元 price; decade placements 87.4亿 vs dividends 57.73亿, shares +33%, no buybacks (workpaper Appendix F) _(source: derived: calc.per_share)_
- Free cash flow per share is the ultimate measure; dilution and capital needs decide whether earnings growth creates value — the 2004 letter's test applied to the placement-funded build-out _(source: SRC source-files/Jeff Bezos/Amazon Shareholder Letter 2004.html (Our Most Important Financial Measure: Free Cash Flow Per Share))_

</details>

### Li Lu (李录, Himalaya Capital)

Two documents: an alumina spot and contract series, and the related-party plus dividend notes in the annual report. Until then the bear case stands unrefuted, and I won't pretend otherwise. The floor limits the damage: net cash plus half the fixed assets and half the intangibles, 80% of inventory, less operating payables and minorities — about 272亿, 37% of the cap, haircuts stated. So my question to you, the user: would you hold a capped-capacity harvester at the ex-cash no-growth yield we just computed while the hoard may stay inside the group?

<details>
<summary>Evidence and turn notes</summary>

confidence medium · 2026-11-24T10:40:00+08:00

**Evidence**
- Asset floor 271.93亿 = net cash 211.79 + 50% x (fix_assets_total 192.50 + cip_total 4.70 = 197.20, DuckDB 20260930) + 50% x intangibles 26.42 + 80% x inventory 39.29 + receivables 28.03 - operating payables 62.46 (Sept26 notes+accounts 54.11 + FY2025 other payables 8.35, labelled lag: Sept26 oth_payable null) - minorities 48.67; 37.3% of cap 728.62亿; all lines 2026Q3 except other payables _(source: derived: calc.per_share)_
- The bear case and the hoard's reachability close only with the alumina price series and the FY2025/2026 related-party and dividend notes; the controller question is unverified _(source: KB F-000807-003)_

</details>

### Stephen Penman

The scan's receivables line before we close: 12.47亿 at Sept25 to 15.99亿 at Sept26, against 9M revenue up 19.4% — a small gap, and the scary year-end-to-Q3 jump is mostly seasonal collection, not new credit risk. I count them at face in the floor; the aging note would confirm. Warren, ready to close us out?

<details>
<summary>Evidence and turn notes</summary>

confidence medium · 2026-11-24T10:45:00+08:00

**Evidence**
- AR+notes 12.47→15.99亿 (+28.2%) vs 9M revenue 440.72→526.16亿 (+19.4%): gap 8.8pp, excess 1.10亿 (calc.growth_gap); the FY2025→Sept26 +365% compares year-end 3.44亿 with a Q3 point — seasonal, same-window FY2024 3.44 → Sept25 12.47 _(source: derived: calc.growth_gap)_
- Receivables are seasonal: accounts_receiv 3.44亿 FY2024, 12.47亿 Sept25, 3.44亿 FY2025, 15.99亿 Sept26 — year-end collection points, Q3 build points _(source: DuckDB raw_balancesheet accounts_receiv 20241231/20250930/20251231/20260930 (workpaper divergence scan))_ — {"fy2024": 3.44, "sept25": 12.47, "fy2025": 3.44, "sept26": 15.99}

</details>

### Warren Buffett

My (c) remains a guess between harvest spend and depreciation — the relining note would close it, and at depreciation-level (c) owner earnings equal the 44.1亿 median. So: a good business in harvest, at a fair mid-cycle price, cheap only if the windfall persists or the hoard reaches owners. I concede the mechanical median is the defensible base; the argued higher mid-cycle needs evidence we don't have. Medium confidence until alumina prices, the capex note and the payout plan are verified.

<details>
<summary>Evidence and turn notes</summary>

confidence medium · 2026-11-24T10:50:00+08:00

**Evidence**
- Owner earnings a+b-c with (c) guessed between harvest spend 8.5亿/yr and depreciation 18.6亿/yr; at (c) = depreciation owner earnings equal the 44.12亿 median (calc.owner_earnings, workpaper Appendix H) _(source: estimate (labelled in text))_
- Owner earnings are reported earnings plus depreciation less the capitalized spend needed to hold volume and competitive position; (c) must be a guess and cash flow a+b without (c) is meaningless in manufacturing _(source: SRC source-files/Warren Buffett/Berkshire Hathaway Shareholder Letter 1986.html (owner-earnings appendix, a+b-c))_

**Concessions**
- ← Joel Greenblatt: The mechanical harvest median 44.12亿 is the defensible base; an argued mid-cycle of 55-60亿 needs alumina-persistence evidence this panel does not have

</details>

## Disagreements

- **Normalized mid-cycle earnings: mechanical harvest median ~44亿 vs an argued 55-60亿** — narrowed
  - Joel Greenblatt: mechanical median 44.12亿, window labelled truncated, until alumina persistence is verified
  - Warren Buffett: harvest free cash suggests more owner cash; concedes the median is the defensible base without the capex note
  - Li Lu (李录, Himalaya Capital): adding the 2026 windfall as permanent double-counts one cost cycle
  - _resolution_: Narrowed to two missing facts: the alumina spot/contract series (does any of the 2026 cost windfall persist) and the annual-report capex / pot-relining note (where (c) sits). Conclusion uses the mechanical median.
- **Reachability of the 211.8亿 net-cash hoard under a state controller** — open
  - Joel Greenblatt: show EV at full vs half cash recovery rather than a flat haircut
  - Li Lu (李录, Himalaya Capital): related-party alumina purchases and policy reinvestment could trap the cash; unverified
  - _resolution_: Needs the FY2025/2026 related-party note and the dividend plan; both EV cases and the like-for-like ex-cash yield are shown so the answer does not depend on assuming reachability.

## Conclusion

**Answer (medium confidence):** Yunnan Aluminium is a good business in harvest, not a great one: a cost-position commodity smelter whose decade splits into a capital-hungry build-out (FY2016-20 parent profit 6.99亿 on capex 167.3亿) and a cash-rich harvest (FY2021-25 profit 223.1亿, free cash 308.6亿). The decade's cash backs the profit (10y FCF 260.8亿 = 1.13x parent NI 230.1亿), but harvest capex at 0.47x depreciation means today's free cash overstates owner cash unless maintenance is genuinely cheap. At 728.6亿 (S1 quote 2026-11-20, 21.01元) the price is not buying the 2026 peak: on the mechanical harvest median 44.1亿 it pays 6.1% with no growth and needs 4.6% perpetual growth at an 8% hurdle; stripping the 211.8亿 hoard and its assumed carry, the operating business yields about 7.9% with no growth, or about 7.7% once minorities' book share of the cash is deducted — at or below the hurdle, not above it. The insight to remember: the market's 36% fall against trailing profit up ~166% is a bet that the cost-side windfall reverses, and the price already sits at mid-cycle no-growth, so the upside depends on alumina persistence or the hoard reaching owners, not on the boom continuing. Scorecard: business type GOOD in harvest (commodity spread, no franchise moat); cash backing YES over the decade (1.13x) but current FCF flattered by deferred maintenance; return driver margin and turnover up on a growing base over FY2016-25 (RNOA 5.0% to 28.6%, NOA 170.5亿 to 254.3亿), with base shrinkage (291.6亿 to 254.3亿) only in FY2021-25; leverage gone; cheap or not FAIR at mid-cycle no-growth — the ex-cash operating yield meets the 8% hurdle only at the mid band and only on the consolidated-cash basis; floor about 272亿 (37% of cap) with stated haircuts protects roughly a third of the price. Confidence medium: the mid-cycle base is mechanical, the carry yield and maintenance (c) are labelled assumptions, and the bear case is unrefuted locally.

**What would change our mind**
- An alumina spot/contract series showing cheap alumina persisting into 2027 would lift normal earnings above the 44.1亿 median toward 55亿 and make the price cheap at zero growth
- The annual-report capex / pot-relining note showing maintenance (c) near harvest spend rather than depreciation would raise owner earnings above the median
- A dividend or buyback plan releasing the 211.8亿 hoard would let the cash count at par and lift the ex-cash operating yield into the price
- Recurring Yunnan power rationing or an alumina price spike would push normal earnings below the band low 33.2亿 and break the floor story

**Open questions**
- Alumina spot and contract price series (external commodity data): does any of the 2026 cost windfall persist into mid-cycle?
- FY2025/2026 annual-report related-party note and dividend plan: is the 211.8亿 hoard reachable by minority owners, or trapped in group purchases and policy reinvestment?
- Annual-report capex note and pot-relining (大修) treatment: where does maintenance (c) sit between harvest spend 8.5亿/yr and depreciation 18.6亿/yr?
- FY2021 impairment 19.85亿 detail: how much of the later RNOA rise is bleed-back from a written-down book?
- FY2023 revenue -12%: was it dry-season power rationing (MD&A), and does it recur?
- AR2026 aging note and year-end collection pattern: is the Sept26 15.99亿 collectable at face, and how much of the FY2025-to-Sept26 jump is seasonal?

## Thinkers consulted (reasoning methods, not evidence)

- richard-hamming · 2.2 — System-test rerun: the conclusion risks repeating the prior session's; reframed the important problem as 'what normalization is defensible without external prices' instead of re-answering 'is it cheap', which produced the truncated-window concession and the mechanical-median base
- declined — the open cash-reachability disagreement needs the related-party note and dividend plan, not a reasoning method

## Candidate questions for the next round

- Round 2: read the alumina price series and 2027 contract assumptions against the harvest band — does any of the 2026 windfall belong in normal earnings?
- What do the FY2025 related-party note and the 2026 dividend plan say about the 211.8亿 hoard's reachability?
- What is maintenance capex per the annual-report capex note — does (c) sit near depreciation or near harvest spend?

## Knowledge candidates (to be validated before entering knowledge/)

- [fact, high] 000807.SZ FY2019 S1/S2 share-count mismatch (31.28亿 vs 26.07亿) is a listing lag: the FY2019 placement (parent ~21.11亿) raised share capital within FY2019 but the new shares listed in 2020, so daily_basic at 20191231 still showed the old count _(source: S1 balancesheet.total_share FY2019 + S2 raw:cash_from_equity_issuance / raw:minority_equity_contributions FY2019 (workpaper §0))_
- [fact, medium] 000807.SZ 9M2026 margin spike is cost-side: revenue +19.4% YoY (526.16亿 vs 440.72亿) while cost of sales -4.1% (357.59亿 vs 372.90亿); cumulative gross margin 15.39% to 32.04% _(source: S2 raw_income 9M2026/9M2025 DuckDB deduped (workpaper Appendix D))_
- [fact, medium] 000807.SZ receivables are seasonal: accounts_receiv 3.44亿 FY2024, 12.47亿 Sept25, 3.44亿 FY2025, 15.99亿 Sept26; same-window Q3 YoY +28.2% vs revenue +19.4% (gap 8.8pp, excess 1.1亿) — the year-end-to-Q3 +365% is a window artifact _(source: DuckDB raw_balancesheet accounts_receiv + raw_income revenue (workpaper divergence scan))_
- [hypothesis, low] Part of the 2026 alumina-cost windfall persists into mid-cycle, lifting normal parent NI above the harvest median 44.12亿 toward 55亿; the harvest-only band is truncated on the upside _(source: panel round 1 (Greenblatt concession, Li Lu challenge); KB H-000807-001)_
- [method, medium] For a state-controlled harvester with an idle hoard, show EV at full vs partial cash recovery and value the operating business ex-cash like-for-like, instead of a flat cash haircut or a headline yield that keeps the carry in earnings _(source: SRC Lecture 11 pp.1-2 + joel-greenblatt card 1.1; panel round 1)_
