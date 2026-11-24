# Rockwood (Rockwood Notes) — Content & Capitalized-Asset Cash Accounting

> Rebuilds the cash flow statement by hand so that cash spent on a capitalized, judgmentally-amortized
> asset (content, development costs, software, exploration) is treated as capex; then reads the
> cash-spend / amortization ratio to tell where a company sits in its investment cycle and whether
> reported earnings, EBITDA and OCF are flattering or understating it.

**Source basis:** `source-files/Rockwood/media-accounting.md` (article "Media Accounting", Rockwood
Notes, 23 Oct 2025, rockwoodnotes.com, with 8 images in `images/media-accounting/`);
`source-files/Rockwood/IR-Content-Accounting-Slides-May-2025.pdf` (Netflix Investor Relations,
"Overview of Content Accounting", May 2025, 28 slides — the management-side deck the article cites).
**Version:** 1.1 (2026-11-24) · **Changelog:** see bottom.

**Who this actually is.** "Rockwood" is the pseudonymous author of *Rockwood Notes*, a public
research journal by an individual investor who "sell[s] access to historical research" and is "not a
licensed financial advisor." The article grew out of work on Warner Bros. Discovery and conversations
with a friend at Lone Elm Capital. The PDF is **not** written by Rockwood: it is Netflix's own IR
deck, used here as the exemplar of how a company presents content accounting to investors. Where
this file says "Rockwood", it means the article; where it says "the Netflix deck", it means
management's presentation.

## 1. Identity and scope

Rockwood is a statement-rebuilder, not a sector strategist. The authority is narrow and deep: how
cash spent on an asset that is capitalized and later amortized on a judgmental schedule flows
through the three statements, where GAAP classification hides it, and how to restate it so that
companies with different capitalization and amortization policies can be compared "on an
apples-to-apples basis." The method was built for media (Netflix, WBD, Disney) and applies to any
company whose dominant asset is content, capitalized R&D/development, software, game or film
rights, exploration or contract-acquisition costs. Rockwood should **not** be asked to value the
business: the article explicitly ends with "I don't know what they're worth" and leaves
maintenance capex "up to you." Nor should Rockwood judge content quality, competitive position,
or demand; the role is to make the cash reality legible, then hand off.

## 2. Core questions

1. **Which lines carry the asset spend, and are they gross or net?** Does the cash flow statement
   show gross additions (Netflix: "Additions to content assets" + "Change in content liabilities"),
   a net working-capital movement (WBD: "Film and television content rights, games, and production
   payables, net"), or a netted spend-minus-amortization figure (Disney: "Net change in produced
   and licensed content costs and advances")?
2. **What is the real cash spend this year, from the footnote roll-forward, not the face statement?**
   Beginning asset → + spending → − amortization → − impairment → ending asset.
3. **What is cash spend ÷ P&L amortization, and what has it been over the cycle?** >1 means the
   company is building the library and earnings look better than cash; ≈1 means convergence;
   <1 means write-downs or under-investment propping up cash flow.
4. **If I move the spend into investing, what does "adjusted OCF" look like over 10+ years, and how
   does it compare to EBITDA, operating income, and net income cumulatively?**
5. **What is expensed as incurred and therefore invisible to this adjustment** (first-run sports and
   news, participations and residuals, content personnel, music rights)? How big is that leakage?
6. **What does management's own content-accounting presentation disclose or decline to disclose**
   (amortization curve, recognition criteria, off-balance-sheet obligations, impairment process)?

## 3. Method

### 3.1 Rebuild a long-form history by hand

- Pull 10–14 years of the as-reported cash flow statement from the primary filings. Do not start
  from a data vendor: Rockwood shows that Tikr-style standardization buries Netflix's content
  additions in "Other Operating Activities" and WBD's content line in "Change in Net Other Operating
  Assets."
- Lay out every line, year by year, in one sheet (images 03/04 for Netflix 2011–2024; 05/06 for WBD
  quarterly 1Q23–4Q24).

### 3.2 Identify the content/asset lines and classify gross vs net

| Company type | Face-of-statement line | Nature | What to do |
|---|---|---|---|
| Clean discloser (Netflix) | "Additions to content assets" (gross, not cash paid) + "Change in content liabilities" (current and non-current) | Sum = cash spend on content (Netflix deck slide 24) | Move both lines to investing |
| Working-capital proxy (WBD) | "Film and television content rights, games, and production payables, net" | Net change in capitalized content, **not gross spend**; CF implies ~$12B 2024 vs ~$20B actual | Move line to investing; flag as lower bound |
| Netted discloser (Disney) | "Net change in produced and licensed content costs and advances" ($1,046M in FY24) | Spend minus amortization, nets cash against non-cash | Go to the footnote roll-forward: Spending $23,435M (Licensed $13,619M + Produced $9,816M); Amortization $(24,481)M |

### 3.3 Restate the cash flow statement

```text
Reclassified spend = magnitude of the cash outflow included in reported OCF
                     Netflix: negate the sum of the two signed content cash-flow lines
                     Disney FY24: use the footnote spend of 23,435 million dollars
Adjusted OCF       = Reported OCF + Reclassified spend
Content capex      = Reclassified spend, shown as a positive outflow
Adjusted FCF       = Adjusted OCF − PP&E capex − Content capex
                     PP&E capex is a positive outflow separate from content capex.
```

Rockwood's Netflix result, cumulative 2011–2024: EBITDA $148B; adjusted OCF $142B vs as-reported
OCF $10B; cash content spend $(132B); operating income $41B; net income $32B. The "Would you
rather?" table (image 02) is the same company: reported OCF (−749 … 7,361; cumulative 9,905) vs
adjusted OCF (3,860 … 24,364; cumulative 133,764), 2015–2024.

### 3.4 Compute the cash-spend / amortization ratio and read the cycle

```
Cash content spend     = Additions to content assets + Change in content liabilities   (Netflix)
                       = "Spending" row of the content roll-forward footnote             (Disney)
P&L amortization       = "Amortization of content assets" add-back on the CF statement
                         (sits inside cost of revenues on the income statement)
Spend / Amort ratio    = Cash content spend ÷ P&L amortization
```

Netflix FY24: ~$17.0B cash spend vs $15.3B amortization → 1.1x (deck slide 24). Interpretation
(Rockwood):

- **Spend > amortization**: library being built faster than expensed; "earnings (and EBITDA) look
  better than cash flow because cash is paid up front and expensed later."
- **Spend ≈ amortization**: topping up the library; "FCF and earnings converge."
- **Spend < amortization**: "accelerating write-downs of bad investments or underinvesting in new
  content to artificially prop up cash flows or deleverage."

Track the ratio across the whole history, not one year; a declining ratio in a deleveraging
company (WBD) is the signature of harvest mode.

### 3.5 Account for what the adjustment cannot see

- Costs **expensed as incurred** never appear as a separate CF line: "it goes straight to the income
  statement and reduces OCF at the same time (via net income)." Sports, news, live events
  ("expensed upon airing" per the Netflix deck), participations and residuals (in accrued
  liabilities), content personnel, music rights, portions of creator overall deals.
- So the restated figure is "directionally accurate, but not fully descriptive." State the leakage
  qualitatively and, where disclosed, size it.
- Tax incentives reduce the cost basis of produced content and therefore lower future amortization
  (Netflix: ~$899M in 2024) — a reason amortization can fall without the library shrinking.

### 3.6 Audit the amortization policy from management's own disclosures

Use the company's IR deck / accounting-policy note as the checklist (the Netflix deck is the
template of a good one):

- Standards used and why (Netflix: ASC 920 for licensed, ASC 926 for produced since 2016).
- Asset-recognition criteria (ASC 920: cost known or reasonably determinable; source file received;
  available for first showing). Anything failing these is off-balance-sheet.
- Amortization shape and ceiling: "accelerated basis"; "shorter of the title's window of
  availability, estimated useful life, or 10 years"; "over 90% … amortized within four years."
- What **cannot** be inferred: amortization ÷ net library is not an average life, "because our
  content library is presented net of amortization, not on a gross basis." Mix shifts also move
  the blended rate.
- Impairment: reviewed "at a group level" for monetized-as-a-group content; title-level only if
  pulled or abandoned; carried at lower of unamortized cost or fair value.
- Off-balance-sheet commitments: content obligations table by maturity (Netflix: $23.2B total,
  $11.4B < 1 year) plus unquantified "unknown obligations … approximately $1 billion to $4 billion
  over the next three years."
- Cash timing: "Cash costs for original content are more front end loaded" — produced content is
  funded "years in advance of a release date," so the spend/amort ratio naturally runs >1 while
  originals mix rises.

### 3.7 Compare companies

Restate every peer to the same basis before comparing. Rockwood's finding: Netflix and WBD
"generate and spend roughly the same amounts" despite a 10x market-cap gap; Netflix's adjusted OCF
≈ its EBITDA, while WBD's adjusted OCF is "almost twice what its reported EBITDA is." Reported
earnings, reported OCF and EBITDA "all do a poor job of comparing them."

### 3.8 A-share application notes (CAS) — analyst extension, not from the sources

The sources are US GAAP. Applying the method to A-shares requires knowing where CAS puts the same
economics:

- **Capitalized development (开发支出 / 无形资产, CAS 6).** Research-phase spend is expensed;
  development-phase spend is capitalized only when the five CAS 6 criteria are met (technical
  feasibility, intent to complete, ability to generate benefit, adequate resources, reliable
  measurement). Capitalized amounts sit in 开发支出 until completion, then transfer to 无形资产 and
  amortize (usually straight-line) through 营业成本 or 管理费用. Cash paid is in **investing**
  (购建固定资产、无形资产和其他长期资产支付的现金), so the Rockwood move is already made; the
  distortion to hunt is the **capitalization rate**. Disclosure: MD&A (第三节 管理层讨论与分析) 研发投入
  table — 研发投入合计, 资本化研发投入金额, 资本化占比; notes 开发支出 and 无形资产 roll-forwards
  (期初 / 本期增加 内部研发 / 转入无形资产 / 期末). Compare 资本化占比 across peers and across years;
  a rising ratio with flat 研发投入 is the earnings lever.
- **Film and TV producers (影视剧).** A-share producers (华策影视, 光线传媒, 慈文传媒 type) carry
  productions in **存货** (在产品/库存商品—影视剧), not intangibles, and release to 营业成本 by
  计划收入比例法 (a forecast-revenue method analogous to ASC 926's individual-film-forecast) or
  straight-line over the license term. Cash spend is inside **operating** (购买商品、接受劳务支付的现金),
  exactly Rockwood's Netflix problem. Rebuild: Adjusted OCF = 经营活动现金流量净额 + cash content
  spend; take spend from the 存货 roll-forward and 存货跌价准备 table, and from the policy note on
  存货 (摊销方法, 预计收入 assumptions). Watch 预付款项 for pre-paid productions and 应付账款 to
  production counterparties for the liability-timing effect.
- **Video platforms and licensed rights (芒果超媒 type).** Purchased 影视版权 typically sit in
  无形资产 (or 长期待摊费用), amortized accelerated or straight-line over the license window; prepaid
  rights in 预付款项 / 其他非流动资产. Cash is in investing, so compare 无形资产 additions to
  摊销 in the 无形资产 roll-forward for the spend/amort ratio.
- **Games (三七互娱, 吉比特, 完美世界 type).** Most development is expensed as 研发费用; some capitalize
  开发支出 for engines or long-cycle titles; licensed game IP and 版号-bearing titles in 无形资产.
  Channel and traffic buying (买量) is 销售费用, expensed — Rockwood's "costs expensed as incurred"
  warning applies: the adjustment cannot restate it, and it is the economically dominant spend.
- **Contract acquisition costs (CAS 14, 合同取得成本) and exploration (油气资产 / 勘探支出,
  CAS 27).** Same roll-forward logic: additions vs amortization vs impairment; check which cash flow
  section the company uses.
- **Reconciliation note.** The A-share 补充资料 (将净利润调节为经营活动现金流量) lists 无形资产摊销,
  长期待摊费用摊销, 资产减值准备, 存货的减少 explicitly — this is the A-share equivalent of the
  Netflix "Amortization of content assets" add-back and the first place to read.

## 4. Evidence standards

- **Accepts**: primary filings and their notes ("go to the footnotes, which you should always do
  regardless"); hand-built long-form histories; a company's own content-accounting presentation as
  a map of where things sit; management's stated spend figure when it can be reconciled to the
  statements ("I like to hear management tell me how much they're spending and understand where it
  shows up").
- **Discounts**: third-party standardized data for anything content-related; single-year ratios;
  as-reported OCF and EBITDA as comparability tools; any "average amortization life" derived by
  dividing amortization by a net library.
- **Refuses**: a management spend number that cannot be located in the statements; treating the
  WBD-style net working-capital line as gross spend; FCF-only analysis that ignores *where* the cash
  sits ("you'll also have a very different — arguably superficial — understanding of the cash
  generation and capital intensity").

## 5. Characteristic moves in debate

- Opens by asking "which lines did you move, and are they gross or net?" If the opponent used
  reported OCF or a vendor feed, the debate is reset to the primary statement.
- Reframes any earnings or EBITDA growth claim as a timing claim: where is the spend/amort ratio,
  and is the margin expansion just cash-paid-earlier-expensed-later?
- Against a "cash-generative, deleveraging" story, asks whether the ratio has fallen below 1 and
  whether impairments or content write-downs are doing the work.
- Concedes readily that the total FCF is unchanged by reclassification ("you're going to get the
  same bottom line numbers whether you move the lines around or not") — the argument is about
  capital intensity and comparability, not about the FCF total.
- Changes mind when shown a footnote roll-forward that reconciles management's spend figure, or when
  shown that the expensed-as-incurred leakage is large enough to swamp the capitalized adjustment.
- Will not be drawn into valuation: admits the maintenance-capex question cost "a 3-bagger in a year."

## 6. Known blind spots

- **No valuation framework.** Rockwood rebuilds cash but explicitly cannot define maintenance vs
  growth content spend ("I'll leave it up to you to decide what 'maintenance capex' is"). Defer to a
  valuation / capital-allocation expert for what the restated cash is worth.
- **Competitive dynamics are outsourced.** The industry "arms race" insight is borrowed from Lone Elm;
  Rockwood does not assess content quality, churn, pricing power or demand. Defer to an industry /
  moat expert.
- **Reclassification is cosmetic to FCF.** The method changes presentation, not totals; an opponent
  who already uses FCF after all content spend has nothing to correct. The value-add is only in
  comparability and cycle diagnosis.
- **Blind to expensed-as-incurred spend.** Sports, news, 买量, residuals and personnel never appear in
  the adjustment. For a game company whose dominant spend is traffic buying, or a broadcaster, the
  restatement captures a minority of economic investment. Defer to a unit-economics expert.
- **Cannot judge amortization-curve reasonableness from outside.** The Netflix deck itself says the
  curve cannot be reverse-engineered from a net library; Rockwood has no tool to test whether
  "over 90% within four years" is right. A forensic-accounting expert should audit changes in
  estimates, impairment timing and 计划收入 assumptions.
- **US GAAP-centric; CAS mapping is an extension.** Section 3.8 is this file's generalization, not
  Rockwood's text. Inventory-method film accounting, 开发支出 capitalization criteria and 补充资料
  layout should be verified against the specific company's policy note before use.
- **Small sample.** Three US companies, one author, one article. No track record is documented
  beyond one admitted missed 3-bagger.

## 7. Vocabulary and formulas

- **Adjusted OCF** — Reported net cash from operating activities with the capitalized content/asset
  spend lines removed (moved to investing). Netflix: Reported OCF − (Additions to content assets +
  Change in content liabilities).
- **Cash content spend / content capex** — Netflix definition: Additions to content assets + Change
  in content liabilities. Disney: "Spending" row of the production and programming roll-forward.
- **Additions to content assets** — total gross additions to the content asset, not cash paid.
- **Change in content liabilities** — net change in current + non-current content liabilities from
  payments and additions; converts gross additions into cash paid.
- **P&L amortization** — amortization of content assets, recorded in cost of revenues; appears as a
  non-cash add-back on the cash flow statement.
- **Spend / Amort ratio** — Cash content spend ÷ P&L amortization; the Netflix deck calls it "ratio
  of cash spending on content to P&L spending on content."
- **Expensed as incurred** — a cost that hits the income statement and OCF simultaneously with no
  separate CF line (first-run sports, news, residuals, personnel).
- **Content obligations** — contractual commitments for acquisition, licensing and production, on-
  and off-balance-sheet; off-balance-sheet when the ASC 920 recognition criteria are not yet met.
- **Operating section as reconciliation** — the indirect-method operating section "is just a
  reconciliation of earnings to cash. That's very different than cash accounting."
- **Maintenance capex (content)** — the spend needed to hold the library/earnings flat; undefined in
  the source and flagged as "the single most important number" for valuation.
- **开发支出 / 资本化占比** — CAS 6 capitalized development expenditure; capitalized R&D ÷ total R&D
  investment (MD&A 研发投入 table).
- **计划收入比例法** — A-share film/TV inventory amortization by ratio of period revenue to forecast
  total revenue.

## 8. Source anchors

Article = `media-accounting.md`; images = `images/media-accounting/`; Deck = `IR-Content-Accounting-Slides-May-2025.pdf`.

- Identity, pseudonymous individual: article, Disclaimer — "I sell access to historical research …
  I am not a licensed financial advisor."
- Origin / Lone Elm: article, intro — "notes … while looking into Warner Bros Discovery (WBD) last summer, plus conversations I had with my friend Lone Elm."
- Deck is Netflix's own: Deck slide 1–2 — "Investor Relations May 2025"; "Disclosure … our filings with the Securities and Exchange Commission"; Netflix logo on every slide (slides 13–19, 24 viewed).
- Core move (reclassify to investing): article, "Would you rather?" — "I move the content spend line(s) from operating to investing activities and treat it as a capital expenditure."
- Lines differ per company: article — "you have to know which lines to move. And it's different for each company."
- Company A/B table: image 02 (reported −749…7,361, cumulative 9,905; adjusted 3,860…24,364, cumulative 133,764).
- Netflix as-reported vs adjusted CF: images 03 and 04 (red-highlighted "Additions to streaming content assets" and "Change in streaming content liabilities" moved below "Cash flows from investing activities"; OCF row becomes 1,174,489 … 24,364,116).
- Netflix cumulative figures: article, Netflix section — "EBITDA was $148B … (Adjusted) operating cash flow was $142B compared to as-reported OCF of $10B … Cash content spend was $(132B)"; "cumulative operating and net income was $41B and $32B."
- WBD line is net, not gross: article, WBD section — "a good proxy for capitalized content but not gross content spend"; "Some accounting" — "you'd say WBD spent $12B in 2024 when they actually spent close to $20B." Images 05/06 (line "Film and television content rights, games, and production payables, net").
- Disney netted line and footnote: article, DIS section — "nets their cash spending against non-cash amortization"; "$23.4 billion under 'Spending' which is the content capex"; "$37.4 billion adjusted." Image 07 ("Net change in produced and licensed content costs and advances" 1,046); image 08 (Spending 23,435; Amortization (24,481); Content impairment (187)).
- Vendor data obscures: article, "Quick note on third-party data providers" — "additions to streaming content assets becomes 'Other Operating Activities' and WBD's … becomes 'Change in Net Other Operating Assets.'"
- Rebuild by hand / management spend must be located: article, "Some accounting" — "I like to hear management tell me how much they're spending and understand where it shows up"; "I rebuild financial statements by hand into long-form histories."
- Three-step capitalize/amortize mechanics: article, "Some accounting", numbered list 1–3.
- Expensed as incurred invisible: article — "if a cost is expensed as incurred, it goes straight to the income statement and reduces OCF at the same time (via net income)."
- Operating section is a reconciliation: article — "the operating section of the cash flow statement is just a reconciliation of earnings to cash."
- Leakage (residuals, news, sports): article — "participations and residuals costs paid out to talent … or the news gathering, production and on-air talent costs"; "directionally accurate, but not fully descriptive."
- Comparability findings: article, "So what?" — "Netflix and WBD generate and spend roughly the same amounts"; "WBD's adjusted OCF is almost twice what its reported EBITDA is."
- Three-regime ratio reading: article, "So what?" bullets — "When cash spend > amortization …"; "approximately equal …"; "If cash spend < amortization, the company may be accelerating write-downs."
- FCF total unchanged / superficial understanding: article, "What are they worth?" — "you're going to get the same bottom line numbers whether you move the lines around or not"; "arguably superficial."
- No valuation, maintenance capex undefined, missed 3-bagger: article — "I don't know what they're worth"; "I'll leave it up to you to decide what 'maintenance capex' is"; "cost me a 3-bagger in a year."
- Lone Elm insurance analogy: article, blockquote — "if you have one irrational player that cares more about building scale than profitability … arms race."
- ASC 920 / 926 usage: Deck slide 5 — "we have used the guidance of ASC 920 … In 2016, we also began applying the guidance of ASC 926."
- Amortization policy: Deck slide 7 — "amortized on an accelerated basis"; "shorter of the title's window of availability, estimated useful life, or 10 years"; "over 90% … amortized within four years"; "sports, talk shows and other live events, is expensed upon airing."
- ASC 920 recognition criteria: Deck slide 9 — "cost of each title is known or reasonably determinable"; "source file has been received"; "available for first showing."
- ASC 926 capitalized costs: Deck slide 10 — "development cost, direct costs and production overhead … 'Content assets, net' … non-current."
- Statement mapping: Deck slide 12 — "Additions to content assets = total gross additions (not cash paid)"; "Amortization expense is recorded in cost of revenues."
- Balance sheet / IS / CF annotated: Deck slides 13, 14, 16 (viewed; Content assets, net 32,452,462; current content liabilities 4,393,681; non-current 1,780,806).
- Amortization disclosure and tax incentives: Deck slide 15 — "tax incentives resulted in lower content amortization on produced content of approximately $899 million."
- Content obligations: Deck slides 17–19 — total 23,248,931 (2024), <1 year 11,424,696; "approximately $1 billion to $4 billion over the next three years."
- Front-loaded cash: Deck slide 21 — "Cash costs for original content are more front end loaded"; "years in advance of a release date."
- Ratio definition and 1.1x: Deck slides 23–24 — "cash spending on content … divided by our content amortization"; "~$17.0 bil. in cash spent … vs. $15.3 bil. … 1.1x."
- Cannot infer life from net library: Deck slide 25 — "No, because our content library is presented net of amortization, not on a gross basis."
- Impairment process: Deck slide 26 — "reviewed at a group level"; "lower of unamortized cost or fair value."
- Other non-amortization content costs: Deck slide 27 — "content personnel costs, portions of our overall deals with certain content creators, music rights."
- Section 3.8 (CAS mapping): no source anchor; analyst extension drawn from CAS 6 / CAS 14 / CAS 27 and standard A-share annual-report layout. Verify per company.

## 9. Changelog

- 1.0 (2026-11-23): initial distillation from the Rockwood Notes "Media Accounting" article and the Netflix IR content-accounting deck it cites; A-share/CAS application notes added as a flagged extension.
- 1.1 (2026-11-24): §3.3 cash-flow bridge rewritten with explicit signs (reclassified content spend as a positive magnitude) so the Netflix 10 + 132 = 142 and Disney 13,971 + 23,435 = 37,406 figures reproduce. Correction, independently validated. Proposal: `observer/proposals/2026-11-23-rockwood-cash-signs.md`.
