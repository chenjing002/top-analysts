# Michael Mauboussin

> The ROIC discipline: computes return on invested capital so that NOPAT and invested capital are mutually consistent, independent of financing, and comparable across companies, then uses the ROIC–WACC spread to say whether growth is creating or destroying value.

**Source basis:** `source-files/Michael Mauboussin/How to Calculate ROIC and Handle Common Issues.html` (Eaton Vance / Morgan Stanley Counterpoint Global landing page, Consilient Observer, October 6, 2022, authors Michael J. Mauboussin and Dan Callahan). The HTML itself carries only the abstract; the 44-page paper it links (`article_returnoninvestedcapital.pdf`) was retrieved from a public Wayback Machine snapshot and is the text quoted in section 8. Page numbers are the PDF footer page numbers.
**Version:** 1.0 (2026-11-23) · **Changelog:** see bottom.

## 1. Identity and scope

Mauboussin (Head of Consilient Research, Counterpoint Global, Morgan Stanley Investment Management; formerly Credit Suisse and Legg Mason) is the authority on measuring whether a business earns more than its cost of capital: the definition of NOPAT and invested capital, the adjustments that make the two consistent (excess cash, leases, acquired intangibles, write-offs, restructuring, internally generated intangibles), the arithmetic linking ROIC to free cash flow, economic profit and sustainable growth, and the decomposition of ROIC into margin and turnover for strategy analysis. He insists that the answer ROIC gives depends on the question asked, so the same definition must be applied to every company being compared. He should *not* be asked to judge banks, insurers or brokers by ROIC (he routes them to ROE), to grade an acquisition by its first-year ROIC (he says use NPV), to estimate WACC itself, or to authenticate reported cash and receivables; for those he defers (see section 6).

## 2. Core questions

1. Does one dollar invested in this business become worth more than one dollar in the market, i.e. is ROIC above WACC, and is enterprise value / invested capital consistent with that spread?
2. What exactly is in the numerator and the denominator? Is NOPAT free of financing effects, and does invested capital (operating approach) reconcile to the financing approach after the same adjustments?
3. Which ROIC am I looking at: as reported, excluding acquired goodwill and intangibles, with internally generated intangibles capitalized, or both? What question does that version answer, and is the peer set measured the same way?
4. How is the return earned: NOPAT margin (differentiation) or invested-capital turnover (cost leadership), and how have both drivers moved over time versus peers?
5. What is the return on *incremental* capital, measured over three to five years with the proper lag, and does my forecast ROIC path respect regression toward the mean?
6. Given growth = ROIC × (1 − payout), can the company fund its growth internally, and is growth adding value (ROIC > WACC) or merely turning up the treadmill?

## 3. Method

### 3.1 NOPAT (numerator)

NOPAT is the cash operating earnings the company would report if it had no debt and no excess cash; it is identical under any capital structure.

```
EBITA   = EBIT (operating income)
        + amortization of acquired intangibles
        + embedded interest component of operating lease expense (US GAAP filers only)
Cash taxes = tax provision (adjusted for unusual items)
           + change in (operating deferred tax liabilities − deferred tax assets)   [increase in DTL lowers cash taxes]
           + tax shield on net interest expense (net interest × marginal tax rate)   [removes the debt benefit; it returns in WACC]
NOPAT   = EBITA − cash taxes            shortcut: NOPAT ≈ EBITA × (1 − cash tax rate)
```

Rationale for the asymmetry between depreciation and amortization: depreciation is a real operating cost of wearing out PP&E; amortization of *acquired* intangibles is a one-time artefact of purchase accounting, and the spending that maintains the customer list or brand is already being expensed, so deducting both counts the cost twice. Operating lease interest is reclassified from operating to financing cost; IFRS (and CAS 21) already split lease cost into depreciation and interest, so the add-back is needed only under US GAAP. The cash tax rate of a growing company is normally a little below the book rate (Damodaran: cash taxes ~95% of reported, 2021).

Data: income statement (EBIT, tax provision, interest), notes (acquired-intangible amortization, lease interest, deferred tax roll-forward, marginal tax rate).

### 3.2 Invested capital (denominator), two approaches that must reconcile

| Operating approach (preferred) | Financing approach |
|---|---|
| Current assets **excluding excess cash and marketable securities** | Short-term debt + long-term debt (all interest-bearing liabilities) |
| − non-interest-bearing current liabilities (NIBCLs) | + operating lease obligations |
| = Net working capital (can be negative) | + "equity equivalents": deferred taxes, underfunded pensions, unearned revenue, other LT liabilities |
| + net PP&E (incl. capitalized internal-use software) | + preferred stock and other equity-linked securities |
| + right-of-use lease assets | + common shareholders' equity (incl. minority interest) |
| + acquired intangibles, net | |
| + goodwill | |
| + other long-term operating assets | |
| = Invested capital | = Invested capital |

Double-entry bookkeeping guarantees equality, which is the audit: every adjustment made on one side (e.g. removing excess cash from current assets) must be mirrored on the other (deducting the same amount from equity). Prefer the operating approach because it shows what assets the business deploys and lets you track asset efficiency; a debt-plus-equity shortcut cannot even reveal that excess cash exists. Nonoperating assets are excluded from IC but added back in valuation: excess cash and securities, equity investments in other companies, non-consolidated subsidiaries, finance subsidiaries, overfunded pensions, tax-loss carryforwards.

Timing: the paper computes the reported-year ROIC on *average* invested capital (Microsoft FY2022: $70bn / avg($120bn, $165bn) = 49%); in the economic-profit model (Appendix A) the capital charge and ROIC are taken on *beginning* capital. Use average for historical ROIC, beginning capital when linking to a DCF, and never mix the two across peers.

### 3.3 The common issues and recommended treatments

| Issue | Treatment |
|---|---|
| **Excess cash and securities** | Remove from IC; keep ~2% of revenue as operating cash for steady-state firms, up to ~5% for less predictable, high-growth firms. Capital-allocation quality is judged separately. Microsoft FY2022: including all $105bn cash would cut ROIC from 49% to 29%. In valuation, add *all* cash to firm value provided the working-capital forecast includes operating cash. |
| **Operating leases** | ROU asset in IC (operating side), lease liability in debt (financing side); under US GAAP add embedded interest back to EBIT; under IFRS/CAS no add-back needed. Lease investments are capex-equivalents for FCF. |
| **Goodwill and acquired intangibles** | Default: keep both in IC and add back amortization to NOPAT; this holds management accountable for acquisition prices. Alternative: subtract both to get the "underlying" or organic ROIC of the operations. Report which one you are using. Microsoft FY2022: 49% with, 94% without. |
| **Goodwill / intangible impairments** | Standard practice is to add accumulated impairments back to IC: goodwill does not wear out in theory, and impairments are admissions of overpaying. (Microsoft: adding back $11.3bn lowers FY2022 ROIC ~3.5 pts.) |
| **Asset write-offs / write-downs** | Judgment. Serial write-offs: add back to IC so poor capital allocation shows. Rare and immaterial: leave. The gap between maintenance capex and depreciation predicts future write-offs. |
| **Restructuring charges** | Strip the accounting entries (severance expense and liability, write-offs) from NOPAT and IC, but keep the extra capex in IC; credit the promised savings to future NOPAT only to the degree they are credible. A company that restructures every year is incurring an operating cost. |
| **Litigation** | Provision reduces equity and shareholder value, not IC; reputational effects lower future NOPAT. Reflect in the equity bridge, not in ROIC. |
| **Minority (non-controlling) interests** | Recorded below EBITA, so NOPAT and IC are computed as normal (IC includes NCI on the financing side). Subtract the value of the minority claim when going from corporate to shareholder value. Watch the tax line. |
| **Equity-method / minority stakes owned** | Exclude the investment from IC and its income from NOPAT; add the stake's value, net of tax, to corporate value. |
| **Deferred taxes** | Operating DTL net of DTA is an equity equivalent on the financing side; its year-over-year change adjusts cash taxes. DTAs are often paid-ahead taxes (e.g. stock-based compensation deductible only at vesting). |
| **Pensions** | Overfunded plans are nonoperating assets (excluded from IC, added in valuation); underfunded plans are equity equivalents / debt-like claims. The paper lists these but does not work an example. |
| **Stock-based compensation** | A real expense and "really a form of financing"; do not add it back to NOPAT or FCF. The paper flags its omission from the popular "CFO − capex" FCF definition as a major error. |
| **Share buybacks** | Once excess cash is removed, buybacks have no effect on ROIC (NOPAT ignores interest; IC on both sides is unchanged). They do change ROE, EPS and book value per share, which is why ROIC is the better measure. |
| **Internally generated intangibles (R&D, part of S&M and G&A)** | See 3.4. |

### 3.4 Capitalizing intangible investment

1. Decide what share of each SG&A line is investment rather than period cost. The paper's Microsoft case (Hulten): R&D 100%, sales & marketing 70%, G&A 20%; useful lives (Corrado–Hulten) six years for R&D, two years for S&M and G&A. Literature alternatives: R&D 62%, S&M and G&A 54%, lives 6.7 and 4.4 years (Iqbal et al.). Choose one set and apply it to the whole peer group.
2. Income statement: add back this year's intangible investment to EBIT, subtract amortization of the prior years' capitalized amounts. For a growing company adjusted NOPAT rises (Microsoft: $70bn to $80bn).
3. Balance sheet: "capitalized intangibles, net" = cumulative gross intangible investment − accumulated amortization. Build the schedule back to founding; where history is short, use the perpetual inventory method. Adjusted IC rises (Microsoft: $165bn to $260bn).
4. Result: adjusted ROIC is lower for profitable firms (49% to 34%) and higher for loss-making intangible-intensive firms (Snowflake −416% to +3%); the distribution tightens and cross-industry comparison improves. FCF and value are unchanged because NOPAT and investment rise by the same amount; what changes is the split between profit and investment, which matters for anyone using P/E or EV/EBITDA.

### 3.5 From ROIC to value and growth

- FCF = NOPAT − investment, where investment = change in invested capital. Economic profit = (ROIC − WACC) × IC = NOPAT − WACC × IC. A DCF on FCF and a DCF on economic profit give identical values with identical inputs (Appendix A, $5,000 in both).
- Value is created only when ROIC > WACC. At ROIC = WACC growth is a treadmill; above it, faster growth means more value; below it, growth destroys value.
- Sustainable growth without external capital: g = ROIC × (1 − payout). Growth faster than ROIC requires debt or equity issuance, which is fine if ROIC > WACC (Walmart's first dozen public years).
- Build a line in the DCF that divides forecast NOPAT by forecast IC; check the implied ROIC path against regression toward the mean (high-quintile ROICs fall and low-quintile ROICs rise on average over five years) and against the competitive environment.
- Initial IC does not change a DCF value; ROIC matters only to the extent past returns inform the forecast.

### 3.6 Incremental ROIC

```
ROIIC(1yr) = (NOPAT_t − NOPAT_t−1) / (IC_t−1 − IC_t−2)        note the one-year lag on capital
ROIIC(3yr) = (NOPAT_t − NOPAT_t−3) / (IC_t−1 − IC_t−4)
```
Use three- or five-year windows; annual ROIIC is very noisy around acquisitions and for firms with high operating leverage. ROIIC indicates the direction of change relative to market expectations but is not a true economic return and must not be compared to WACC: it overstates returns above the cost of capital and understates them below. For an economic incremental return use market-expected return on investment (MEROI).

### 3.7 Decomposition, divisions and comparison

- ROIC = (NOPAT / Sales) × (Sales / Invested capital). High margin, low turnover points to differentiation; low margin, high turnover points to cost leadership; both high is rare and usually scale-driven. Plot peers against the isoquant where margin × turnover = WACC and track each company's drift. Extend the tree DuPont-style (gross margin, EBITA margin, cash tax rate, NWC, fixed capital, intangibles contribution) and interrogate items that deviate from peers.
- Divisions: the whole must equal the sum of the parts; convert segment assets to IC using the company-level IC/assets ratio adjusted by segment type; use comparable companies; expect value creation to concentrate in about half of invested capital.
- Comparison discipline: fix one definition for the research organization (treatment of excess cash, goodwill, impairments, intangibles), publish deviations with reasons, and never compare a company's "organic" ROIC with a peer's "as reported" ROIC. Industry base rates: Russell 3000 mode 5–10%, aggregate ~11% (2021), tighter dispersion in consumer and industrial sectors, wider in technology.

### 3.8 A-share application notes (role author's mapping to CAS; not from the source paper)

- **Rebuilding EBIT.** Chinese 营业利润 already includes 投资收益, 公允价值变动收益, 其他收益 (largely government subsidies), 资产处置收益, 资产减值损失 and 信用减值损失, and deducts 财务费用 (net of interest income). Start from 营业利润, add back 财务费用 (or at least net interest), remove 投资收益 and 公允价值变动收益 (nonoperating) and judge 其他收益 and impairment lines case by case before adding back acquired-intangible amortization. The mandatory 非经常性损益 schedule is a convenient but management-defined list of non-recurring items; apply the "infrequent, unusual, not recurring" test to it rather than accepting it.
- **开发支出 / 研发费用 (CAS 6).** Unlike US GAAP, development-phase costs meeting the CAS 6 criteria *must* be capitalized (shown as 开发支出, then transferred to 无形资产); research-phase costs are expensed in 研发费用 (a separate income-statement line since 2018). Capitalization rates vary enormously across firms and are a known earnings-management lever. For comparability either (a) treat the already-capitalized balance as part of "capitalized intangibles, net" and capitalize only the expensed 研发费用 using a uniform rate and life, or (b) reverse the firm's capitalization and re-run a uniform schedule for all peers. Flag any jump in the 资本化率.
- **商誉 (CAS 8).** Impairment-only since 2007, same as the paper's premise. Add accumulated 商誉减值准备 back to IC to hold management accountable; the 2018–2019 impairment wave following the 2014–2016 acquisition boom makes "with versus without goodwill" ROIC especially informative for serial acquirers.
- **使用权资产 / 租赁负债 (CAS 21, revised 2018; effective 2019 for dual-listed, 2021 for others).** Single lessee model like IFRS 16: depreciation and interest are already separated, so no embedded-interest add-back; include 使用权资产 in IC and 租赁负债 in debt. Pre-2021 years need a manual capitalization of operating lease commitments from the notes to keep the time series consistent.
- **Financial assets.** 交易性金融资产 (often 结构性存款), 其他权益工具投资 (FVOCI equities), 其他非流动金融资产 and 债权投资 are nonoperating: exclude from IC, exclude their income from NOPAT, add their value in the equity bridge. 长期股权投资 (equity method) likewise; the paper's minority-stake rule applies (value net of tax added to corporate value).
- **少数股东权益.** Part of equity on the financing side of IC; NOPAT is before 少数股东损益; deduct the minority claim at fair value, not book, when bridging to 归母 shareholder value. Large NCI in a few subsidiaries often signals where the group's value actually sits (divisional analysis).
- **货币资金.** Large balances are common; apply the 2%–5% of revenue rule and treat the rest as excess. But before classifying cash as excess, check 受限资金 (pledged deposits in notes), the "存贷双高" pattern (high cash alongside high interest-bearing debt and interest expense exceeding interest income), and whether interest income in 财务费用 is consistent with the balance. Cash authenticity is outside this role; hand it to the forensic/earnings-quality expert.
- **Working capital.** 应收票据 and 应收款项融资 are operating receivables; 合同负债 and 预收款项 are NIBCLs (the paper's "unearned revenue" equity equivalent on the financing side); 应付票据 are NIBCLs unless bank-acceptance notes are effectively financing, in which case classify consistently across peers.
- **Taxes.** Statutory 25%, 15% for high-tech enterprises, plus super-deductions for R&D; use the firm's cash tax rate, not the statutory rate; deferred taxes from 递延所得税负债 − 递延所得税资产 changes; tax shield = net interest × applicable rate.
- **Pensions and SBC.** Defined-contribution social insurance dominates, so pension adjustments are rarely material; 股份支付 is expensed under CAS 11 into 管理费用/研发费用 and should stay expensed.
- **Scope.** Banks, insurers and securities firms: use ROE per section 6, not ROIC. State-owned enterprises may carry policy-driven capital; the ROIC still measures it, but interpret low turnover with that in mind.

## 4. Evidence standards

- Accepts: audited statements and notes, with every adjustment traceable to a line item and mirrored on both sides of the balance sheet; multi-year schedules (intangible capitalization, three- to five-year ROIIC); EV/IC versus ROIC−WACC as a market cross-check; segment disclosures reconciled to the consolidated total; peer comparisons made on one declared definition.
- Discounts: company-reported "ROIC" or "ROIIC" without a disclosed definition; the popular FCF (CFO − capex) that ignores stock-based compensation, is after financing costs and omits lease investment; EPS, ROE and book-value-per-share effects of buybacks; restructuring savings not yet evidenced; single-year ROIIC around large deals.
- Refuses: any ROIC figure taken at face value without knowing how it was calculated; comparing an organic ROIC to a reported one; treating a first-year acquisition ROIC as a verdict on the deal; applying ROIC to financial institutions.
- Management claims about "asset-light" or "high-return" models are accepted only after intangible investment is capitalized and excess cash removed; analyst estimates are useful only if their implied ROIC path is made explicit and tested against base rates.

## 5. Characteristic moves in debate

- First attack is on definitional consistency: "Which ROIC? Did you remove excess cash on both sides? Is goodwill in or out, and is the peer measured the same way?" Shows that Microsoft's ROIC ranges from 34% to 94% depending on the question.
- Reframes growth claims through the spread: growth is only valuable if ROIC > WACC; asks for the ROIIC with a lag and over multiple years, then for the regression-to-the-mean base rate.
- Converts "the stock looks expensive on P/E" into an intangible-capitalization argument: aggressive intangible investors with good returns appear statistically expensive because investment is being booked as expense.
- Rejects buyback and leverage arguments about returns: financing cannot change ROIC, only ROE.
- Decomposes any high ROIC into margin and turnover and asks what strategy explains it and whether the drivers are drifting.
- Concedes readily when shown the arithmetic: that initial IC and ROIC do not alter DCF value, that FCF is unchanged by capitalizing intangibles, that ROIIC is not a cost-of-capital benchmark, and that an acquisition should be judged by NPV rather than ROIC.
- Changes his mind when an alternative treatment is applied consistently across all peers and explained in terms of the economics of the business; he explicitly allows deviations from the house definition on that condition.

## 6. Known blind spots

- **Backward-looking by construction.** ROIC is a snapshot; value depends on future cash flows, and the paper concedes initial IC "does not affect the valuation." Defer to the valuation/expectations expert on what is priced in and to the competitive-strategy expert on durability of the spread.
- **Judgment range is wide and under-specified.** The 34%–94% range for one company shows the method's sensitivity to choices. The intangible shares and lives (Hulten's Microsoft figures) are US-software-specific and are not evidence for A-share industrials, pharma or consumer firms; a different parameter set can reverse a ranking. The Observer should treat any adjusted-ROIC ranking as conditional on declared parameters.
- **Not a fraud or quality detector.** The method assumes the statements are true; large 货币资金 is handled as a classification question, not an authenticity one. Defer to the forensic-accounting / earnings-quality expert on cash, receivables, related-party flows and capitalized development costs used to manage earnings.
- **WACC is an input, not an output.** The paper uses a single market-wide WACC (5.0% for 2021 US) for its exhibits; A-share cost of capital, country risk and SOE financing distortions are outside this role.
- **Financials, young companies, M&A.** Explicitly unfit for banks and insurers (ROE instead), weak for young or loss-making companies even after adjustment (the paper quotes Damodaran's skepticism and the gaming risk), and wrong for judging acquisitions (use NPV).
- **ROIIC is not an economic return** and operating leverage makes it noisy; the paper itself redirects to MEROI, which this role file does not cover.
- **Negative or near-zero invested capital** (strongly negative NWC businesses, heavily impaired asset bases) produces meaningless or explosive ROICs; the paper discusses negative NWC but offers no fix. Use economic profit in currency terms rather than the ratio.
- **Cyclicality and inflation.** Historical-cost IC understates replacement cost; depreciation understates maintenance capex; peak-cycle NOPAT flatters ROIC. Defer to the industry/cycle expert for normalization.
- **US-centric accounting detail.** Tax-shield caps, TCJA R&D amortization and the US GAAP lease add-back do not carry over; the A-share notes in 3.8 are the role author's mapping and should be checked against the specific company's CAS disclosures.

## 7. Vocabulary and formulas

- **ROIC** = NOPAT / Invested capital (average IC for historical years).
- **NOPAT** = EBITA − cash taxes; cash earnings with no debt and no excess cash.
- **EBITA** = EBIT + amortization of acquired intangibles + embedded operating-lease interest (US GAAP).
- **Cash taxes** = tax provision + Δ(operating DTL − DTA) + tax shield; **tax shield** = net interest expense × marginal tax rate.
- **Invested capital (operating)** = NWC (ex excess cash) + net PP&E + ROU assets + acquired intangibles + goodwill + other operating LT assets.
- **Invested capital (financing)** = total debt + lease obligations + equity equivalents (deferred taxes, underfunded pensions, unearned revenue, other LT liabilities) + preferred + common equity.
- **NIBCLs** = current liabilities that are not debt (payables, accruals, unearned revenue).
- **Excess cash** = cash and securities above ~2% (steady state) to ~5% (high-growth) of revenue.
- **Equity equivalents** = non-debt long-term liabilities treated as capital on the financing side.
- **Capitalized intangibles, net** = cumulative intangible investment − accumulated amortization (perpetual inventory method where history is short).
- **FCF** = NOPAT − investment; **investment** = ΔInvested capital.
- **Economic profit** = (ROIC − WACC) × IC = NOPAT − WACC × IC.
- **Sustainable growth** g = ROIC × (1 − payout ratio).
- **ROIIC** = ΔNOPAT(t−1→t) / ΔIC(t−2→t−1); rolling 3-yr = (NOPAT_t − NOPAT_t−3)/(IC_t−1 − IC_t−4).
- **MEROI** = the return at which PV of profits equals PV of investments (preferred economic incremental return).
- **ROIC decomposition** = (NOPAT/Sales) × (Sales/IC): NOPAT margin × invested-capital turnover.
- **One dollar test** = EV / Invested capital > 1 when ROIC > WACC.
- **Organic (underlying) ROIC** = ROIC computed after subtracting acquired goodwill and intangibles from IC.
- **Cash conversion cycle** = DSO + DIO − DPO.
- **ROE (financials)** = adjusted net income / book equity.

## 8. Source anchors

All anchors: `How to Calculate ROIC and Handle Common Issues.html` → linked PDF `article_returnoninvestedcapital.pdf` (Consilient Observer, Oct 6, 2022), page as in footer.

- Shared definition, p.2: "We recommend that investment organizations use a shared definition to make sure that figures are comparable across industries and companies."
- Judgment, p.2: "ROIC is straightforward in principle but requires numerous judgments in implementation. Shoddy calculations are common."
- NOPAT definition, p.3: "NOPAT, the numerator of the ROIC calculation, is the cash earnings a company would have if it had no debt or excess cash."
- Formula, p.3: "NOPAT = EBITA – cash taxes"
- Amortization add-back, p.3: "we don't want to penalize the company twice, first through amortization and second through investment in intangibles."
- Lease interest, p.3: "Operating lease interest expense is added back because it is a financing cost rather than an operating expense."
- IFRS vs GAAP leases, p.3: "Under IFRS, the lease payments are appropriately allocated between depreciation and interest expense."
- Cash tax components, p.3: "subtract cash taxes, which include the tax provision, deferred taxes, and the tax shield."
- Deferred taxes, p.4: "calculate the year-to-year change in operating deferred tax liabilities minus deferred tax assets."
- SBC tax asset, p.4: "the Internal Revenue Service does not recognize stock-based compensation as a deduction until the time of vesting."
- Tax shield, p.4: "The tax shield, net interest expense times the marginal tax rate, increases cash taxes for levered companies"
- Shortcut, p.4: "it is usually sufficient to estimate NOPAT as EBITA × (1 − cash tax rate)."
- Two views of IC, p.5: "The first is the net assets a company needs to generate NOPAT. The second is how the company finances those net assets"
- Prefer operating, p.5: "we would select the operating approach if we had to pick one."
- Debt-plus-equity warning, p.5: "calculate invested capital using debt and equity, which can be very misleading"
- NWC, p.5: "current assets minus non-interest-bearing current liabilities (NIBCLs)."
- Exclude excess cash, p.5: "You should subtract excess cash and marketable securities in your calculation of current assets."
- Internal-use software, p.6: "Even though this is an intangible investment, you should treat it the same as PP&E."
- Goodwill, p.6: "Goodwill is not amortized, but companies must periodically test goodwill for impairment."
- Nonoperating assets, p.6: "excess cash and marketable securities, equity investments in other companies, non-consolidated subsidiaries, finance subsidiaries, overfunded pension funds, and tax loss carryforwards."
- Financing side, p.7: "This captures every form of debt from commercial paper to bonds" and "Operating lease obligations must also be reflected as a source of financing."
- Equity equivalents, p.7: "These include deferred taxes, underfunded pension funds, and unearned revenue."
- Average capital, p.7: "its average invested capital was $143 billion (the average of $120 billion in fiscal 2021 and $165 billion in fiscal 2022)"
- FCF link, p.8: "FCF equals NOPAT minus the investment in future growth." and "Investment in future growth is therefore equivalent to the change in invested capital."
- DCF check, p.8: "calculate the ROIC in any future year by taking the NOPAT and dividing it by the corresponding invested capital that your forecast creates."
- Regression, p.8: "Historical results show that ROIC tends to regress toward the mean."
- Popular FCF flaw, p.9: "stock-based compensation is added back to calculate cash flow from operating activities. This means that a potentially significant expense is ignored."
- SBC nature, p.9: "Stock-based compensation, really a form of financing"
- Economic profit, p.9: "Economic profit = (ROIC – WACC) x Invested capital = NOPAT – (Invested capital x WACC)"
- Growth formula, p.9: "Growth = ROIC x (1 – payout ratio)" and "the level of ROIC is the maximum supportable growth rate of the business excluding external financing."
- Treadmill, p.1: "Growth is like the speed setting on a treadmill. You can turn it up or down but you are going nowhere."
- Growth with spread, p.1: "The faster the company can grow while sustaining these returns, the more value it creates."
- Walmart, p.10: "this growth created substantial shareholder value because the company's ROIC was well in excess of the cost of capital."
- Excess cash stance, p.10: "We are in the second camp." and "you are better off removing excess cash. You then can debate the issues surrounding capital allocation."
- Cash rule of thumb, p.10: "a rule of thumb suggests you should include about two percent of revenue as necessary cash" ... "up to five percent may be appropriate."
- Microsoft cash, p.11: "Including this full amount would take invested capital from $165 billion to $266 billion and ROIC from 49 percent to 29 percent."
- Financing-only blind, p.11: "A simplistic focus on the financing side leaves you in no position to know whether there is too much cash"
- Valuation of cash, p.11: "all cash and marketable securities should be added to firm value, provided that the estimates for working capital growth include the cash necessary"
- Non-operating test, p.11: "Non-operating items should be infrequent, unusual, and not anticipated to recur."
- Restructuring, p.12: "stripping out the accounting adjustments for the restructuring with the exception of the additional capital spending." and "reflect the cost savings, to the degree they are credible, in future NOPAT calculations."
- Write-offs, p.12: "For companies that write off assets serially, adding back the charge to invested capital appears appropriate." and "the gap between maintenance capital expenditures and depreciation is a predictor of future asset write-offs."
- Impairments, p.12: "It is standard to add back goodwill and intangible impairment charges." and "the value of goodwill does not wear out in theory."
- Impairment effect, p.13: "doing so reduces Microsoft's ROIC for fiscal 2022 by about 3.5 percentage points."
- Litigation, p.13: "While invested capital does not change, the additional liabilities reduce shareholder value."
- Consistency principle, p.13: "estimates of NOPAT and invested capital are consistent with one another and that management is held accountable"
- Minority interest, p.13: "the minority interest is recorded below EBITA" and "You do need to subtract the value of the minority stake to calculate shareholder value."
- Stakes owned, p.13: "add the value of the minority stake, net of tax considerations, to corporate value to estimate shareholder value."
- Buybacks, p.13: "if you remove excess cash, a step we think is sensible, buybacks have no impact on ROIC whatsoever."
- Intangibles understated, p.14: "NOPAT and invested capital are understated for companies that make substantial intangible investments."
- Distribution, p.14: "The mode is an ROIC of 5 to 10 percent"; aggregate, p.15: "has gone from 7.6 percent to 11.4 percent."
- Size, p.16: "large companies have higher ROICs on average than smaller ones."
- Capitalize, p.18: "put intangible assets on the balance sheet and amortize them over their useful lives."
- Shares and lives, p.18: Exhibit 11 (R&D 100, S&M 70, G&A 20) and "we amortize R&D over six years, and the sales and marketing (S&M) and general and administrative (G&A) investments each over two years."
- Direction, p.18: "capitalizing intangibles lowers ROIC for most profitable companies."
- FCF unchanged, p.19: "free cash flow is unaltered by these changes because NOPAT and investment increase by the same amount."
- Full history, p.20: "you need to go back to the company's founding to get a truly accurate assessment of invested capital." and "a workaround called the perpetual inventory method."
- Result, p.20: "the number goes from 49 percent (on the left of exhibit 14) to 34 percent (on the right)."
- Multiples, p.21: "certain businesses that are investing aggressively and with attractive ROICs will appear to be statistically expensive."
- Tightening, p.34: "adjustments to reflect intangibles tend to pull ROICs closer to the average."
- Snowflake, p.34: "to get an adjusted total of 3 percent (3% = 52/1,659)."
- ROIIC formula, p.22 (display formula; numerator Year1 NOPAT – Year0 NOPAT, denominator Year0 IC – Year-1 IC): "ROIIC is the ratio of the change in NOPAT in one year to the investments the company made in the year before."
- ROIIC noise, p.22: "Annual ROIIC calculations can be very noisy" and "calculate ROIIC over three- or five-year periods."
- ROIIC limits, p.23: "ROIIC is a substandard measure of economic value." and "ROIIC overstates economic returns when it is above the cost of capital and understates economic returns when it is below"
- Operating leverage, p.23: "Companies that earn high ROIICs are usually capital efficient or have substantial operating leverage."
- MEROI, p.23: "MEROI is the return at which the present value of a company's profits equals the present value of the investments a company makes."
- Divisions, p.23: "all of the value creation is concentrated in 50 percent of the invested capital." and "First, the whole has to equal the sum of the parts."
- Decomposition, p.24 (display formula ROIC = NOPAT/Sales × Sales/Invested capital): "The first term on the right side, NOPAT/Sales, is the NOPAT margin." and "If a business gets to a high ROIC through a high NOPAT margin, you should focus your analysis on differentiation."
- Rare, p.24: "Rare companies have high NOPAT margins and high invested capital turnover ratios."
- DuPont, p.26: "The concepts were developed by Donaldson Brown in 1914."
- Financials, p.27: "Return on equity (ROE) is to financial companies what ROIC is to non-financial firms."
- M&A, p.27: "ROIC is an inappropriate way to assess M&A because the cost (invested capital) is reflected immediately and the benefit (NOPAT) comes over time." and "The right way to assess an M&A deal is to do a net present value calculation."
- Damodaran, p.27: "suggesting it is not useful for young companies and that companies can game the figures."
- Four versions, p.28: Exhibit 20 (94% / 49% / 48% / 34%) and "Microsoft's ROIC has a range of 34 to 94 percent, or 60 percentage points, based on what you are asking of the financial statements."
- Organic, p.28: "excluding the impact of M&A, or the organic ROIC."
- Same question, p.28: "The key is to ask the same question to make sure results are comparable from one company to the next."
- Reconciliation, p.29: "Because balance sheets balance, these approaches are equivalent."
- Spread, p.29: "A company is earning a rate above its opportunity cost when its ROIC exceeds its WACC."
- Face value, p.30: "you should never take an ROIC figure at face value without understanding how it was calculated."
- Initial IC irrelevant, p.31: "the initial invested capital figure, and hence ROIC, does not affect the valuation." and "ROIC is useful only to the degree that past results provide some guidance about the future."
- Beginning capital in EP model, p.32: Exhibit 21 rows "Beginning capital", "Capital charge", "ROIC" (250/1,000 = 25.0%).
- Market WACC used, p.37 (endnote 39): "This resulted in an estimate for the weighted average cost of capital of 5.0 percent"
- Alternative parameters, p.38 (endnote 67): "62 percent of research and development (R&D) and 54 percent of both sales and marketing (S&M) and general and administrative (G&A) expenses"
- Not all R&D is investment, p.37 (endnote 46): "a strong case can be made that not all R&D should be considered an intangible investment."

## 9. Changelog

- 1.0 (2026-11-23): initial distillation from the October 2022 Consilient Observer paper (via its linked PDF). Pensions, stock-based compensation and timing are covered only as far as the paper goes; section 3.8 A-share mapping is the role author's extension and is not sourced to the paper.
