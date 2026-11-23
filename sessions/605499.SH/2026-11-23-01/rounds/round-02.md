# Round 2 — Did consumers buy fewer energy drinks in the third quarter, or did shops and distributors order less?

**Session** 605499.SH / 2026-11-23-01 · **started** 2026-11-23T05:15:00-08:00 · **ended** 2026-11-23T05:18:58-08:00
**Participants** Stephen Penman, Warren Buffett, Jeff Bezos, Li Lu (李录, Himalaya Capital)

> The round-one review left a specific operating question open. The company’s half-year and nine-month product disclosures now let the panel isolate the summer quarter and test what weaker revenue says about demand.

## Discussion

_Simulated expert perspectives._

### Li Lu (李录, Himalaya Capital)

Last round I said a decline in the core drink would make me take the slowdown more seriously. We now have one. Dongpeng’s energy-drink revenue fell 8.6% year over year in the third quarter. Suppose a shop sold just as many bottles this summer and ordered fewer because it had cases left over. Which part of the evidence would look different?

<details>
<summary>Evidence and turn notes</summary>

**Evidence**
- Q3 energy-drink revenue fell 8.56% year over year. _(source: Eastroc operating disclosures 2026-097 (https://static.cninfo.com.cn/finalpage/2026-10-30/1225640897.PDF) and 2026-074 (https://static.cninfo.com.cn/finalpage/2026-07-31/1225449598.PDF) §I(a), product revenue from principal activities (主营业务收入), RMB 万元. For each year subtract H1 from 9M, then divide the 2026 quarter by the 2025 quarter and subtract one.)_ — {"FY2026": "1,277,960.86 − 893,661.56 = 384,299.30", "FY2025": "1,256,315.56 − 836,051.10 = 420,264.46"}

</details>

### Stephen Penman

Dongpeng’s third-quarter sales through distributors fell 4.9% year over year. That makes your explanation plausible. But the distributor figure includes tea and every other drink, while the energy-drink figure includes every channel. To test your shop example, I’d follow the same pack through the same shops. How many bottles crossed the till, and how many cases were left on the shelf?

<details>
<summary>Evidence and turn notes</summary>

**Evidence**
- Q3 distribution revenue fell 4.88% year over year. Product and channel figures are separate totals. _(source: Eastroc operating disclosures 2026-097 (https://static.cninfo.com.cn/finalpage/2026-10-30/1225640897.PDF) and 2026-074 (https://static.cninfo.com.cn/finalpage/2026-07-31/1225449598.PDF) §I(a–b), distribution (经销), all products, RMB 万元. Formula: (9M26 − H126) / (9M25 − H125) − 1.)_ — {"FY2026": "1,537,980.18 − 1,047,598.69 = 490,381.49", "FY2025": "1,450,484.51 − 934,966.38 = 515,518.13"}

</details>

### Warren Buffett

Was the usual bottle cold and available at its usual price? Management says new products briefly drew attention away from the core. A shopper who finds only tea in the cooler tells us little about loyalty to the energy drink. If customers passed it up even where price, promotion and availability held steady, I’d take the threat to the franchise much more seriously.

<details>
<summary>Evidence and turn notes</summary>

**Evidence**
- Management attributed some weakness to resources diverted to new products. The cooler example is a hypothesis. _(source: Q3 2026 issuer results-call record, Q1: https://dataclouds.cninfo.com.cn/shgonggao/investor/2026/20261030/0f98e991ba3a99661bcda766b181883e.pdf)_

</details>

### Jeff Bezos

I thought customer advances might tell us whether dealers were pulling back. Contract liabilities (合同负债) barely moved from June to September and ended 43% above the previous September. I’m less worried about customers withdrawing funding across the business. But a dealer could keep the same money on account and switch the next order from energy drinks to tea. Warren, I’d want to see what that dealer reordered after the usual bottle went back in the cooler.

<details>
<summary>Evidence and turn notes</summary>

**Evidence**
- The group advance balance rose 42.86% year over year and fell 0.77% from June. Order switching is hypothetical. _(source: S2 raw_balancesheet, consolidated, RMB yuan. SQL: SELECT DISTINCT end_date, contract_liab FROM raw_balancesheet WHERE ts_code='605499.SH' AND report_type='1' AND end_date IN ('20250930','20260630','20260930') ORDER BY end_date. Changes: Sep26/Sep25 − 1 and Sep26/Jun26 − 1.)_ — {"Sep2025": 3562994166.81, "Jun2026": 5129597311.04, "Sep2026": 5090207385.53}

</details>

### Warren Buffett

Jeff, the first reorder might just fill an empty shelf. What interests me is when the shop asks for the next case. Dongpeng says it tracks stock and sales through linked codes. Could we see how quickly those first cases sold at the usual price, alongside the same weeks last year?

<details>
<summary>Evidence and turn notes</summary>

**Evidence**
- The issuer describes using linked codes for channel inventory and retail movement. The repeat-order test is a proposal. _(source: 2026 interim report, core competitiveness, 渠道力, 精细化渠道管理驱动效能提升: https://static.cninfo.com.cn/finalpage/2026-07-31/1225449594.PDF)_

</details>

### Li Lu (李录, Himalaya Capital)

I’d narrow my bear case. The drop in energy-drink revenue makes me worry about the core product, but I can’t yet say regular buyers walked away. If the usual bottle stayed cold, in stock and at the same effective price, and the same stores still sold fewer of them, I’d put more weight on weaker demand. If those stores sold as many bottles while dealers ran down stock, I’d withdraw that inference.

## Disagreements

- **How far does the core revenue decline support a consumer-demand bear case?** — narrowed
  - Li Lu (李录, Himalaya Capital): Core weakness deserves more weight now that it is visible in product revenue.
  - Stephen Penman: Separate product and channel totals leave retail units and downstream inventories unidentified.
  - Warren Buffett: Availability, promotion and the speed of the next sale matter for a claim about customer preference.
  - Jeff Bezos: The advance balance weakens a broad funding-withdrawal story and leaves room for changes in product orders.
  - _resolution_: The panel established weaker recognized energy-drink revenue. Retail demand, channel inventory changes and execution can coexist. Their relative contributions remain open.

## Conclusion

**Answer (low confidence):** Dongpeng recorded lower energy-drink revenue in the summer quarter. The panel has low confidence about the cause. Dealers could have worked through existing stock, consumers could have bought fewer bottles, or the product could have been harder to find. Company-wide advances and distributor sales cannot distinguish these explanations for the core drink.

**What would change our mind**
- Stable register units with a larger channel inventory drawdown than in the comparison period would favor an ordering adjustment.
- Lower unit sales at comparable outlets with the usual pack in stock, on comparable display and at comparable effective prices would strengthen the demand explanation.

**Open questions**
- Which stores and distributor depots report matched energy-drink units, receipts, inventory and stockouts for comparable summer weeks? Coverage and sample representativeness are unverified.
- How did realized prices, pack mix and promotions affect the translation from revenue to unit shipments?
- Does the same pattern persist after normal replenishment resumes?

## Candidate questions for the next round

- What do comparable-store energy-drink till units, stockouts and channel stock movements show during the summer versus the same weeks last year?
- Establish what the 2026 share-count increase was (issue type, date, price, proceeds) and rebuild EV, NOA and the reverse curve at 20260930 on a like-for-like definition.
- Explain the coexistence of 62.73 亿 short-term borrowings with 207.18 亿 of financial assets after an apparent equity raise.
- Estimate the return on incremental capital for the 22.7 亿 capex and 14.14 亿 在建工程 if growth stays near zero.

## Knowledge candidates (to be validated before entering knowledge/)

- [fact, medium] Q3 2026 energy-drink revenue from principal activities fell about 8.6% year over year. _(source: Eastroc operating disclosures 2026-097 (https://static.cninfo.com.cn/finalpage/2026-10-30/1225640897.PDF) and 2026-074 (https://static.cninfo.com.cn/finalpage/2026-07-31/1225449598.PDF) §I(a), 9M less H1 for each fiscal year (turn 1).)_
