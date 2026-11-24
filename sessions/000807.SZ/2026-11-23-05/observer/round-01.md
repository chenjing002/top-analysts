# Observer — 000807.SZ 2026-11-23-05 round 01
**Reviewed:** rounds/round-01.json · experts: warren-buffett (1.1), stephen-penman (1.0), joel-greenblatt (1.0), jeff-bezos (1.0), li-lu (1.0) · 2026-11-23T22:53−08:00

## Verdict
**Accept with weaknesses.** The round reached a clear result on its opening topic: a good-in-harvest,
cost-advantaged commodity smelter whose 2026 earnings are a cost-driven cyclical peak, priced at
21.01 at roughly 12–13× mid-cycle parent profit (55–60亿) with ~no growth implied at an 8% hurdle,
net cash equal to 29% of market cap, and an asset floor near 36% of cap. The medium confidence is
earned: the normalized-E band and owner-earnings range are labelled estimates, the r=8% and 25%
tax defaults cap confidence at medium, and the two swing facts (alumina-price persistence, cash
reachability under a state controller) are honestly left open with named missing documents. Every
numeric claim spot-checked (18 of 18, several re-derived from S2 read-only queries) reconciles.
The one material defect is presentational but pervasive: the spoken English text systematically
says "billion" where the amounts are 亿 (0.1 billion), a 10× mislabel in every discussion turn.
The evidence values, workpaper, and conclusion are all correct in 亿, so no calculation or
conclusion changes — but the transcript as written misinforms an English reader by an order of
magnitude and must not be published as-is without a units pass.

## Patterns worth keeping
- **Scorecard before news, and the decade split in two** — Buffett turn 1 — the GGG verdict was
  delivered off the full ten-year record (7.0亿 profit on 167.3亿 capex 2016–20 vs 223.1亿 on
  42.6亿 2021–25) before any 2026 event, exactly the round-one workflow rule.
- **A challenge that changed the number the panel underwrites** — Buffett turn 1 → Penman turn 2
  → disagreement "RNOA 28.6% as evidence of quality" (resolved) — the RNOA was decomposed into
  margin, turnover and base shrinkage (2021 impairment 19.85亿 verified in S2 raw_income), and
  the panel switched from trailing RNOA to a normalized band. Penman's concession is recorded.
- **A real disagreement, narrowed not papered over** — Bezos turn 5 (FCF/share 4.37 is the owner's
  measure) vs Buffett turn 6 (capex at 0.34× D&A defers maintenance; owner earnings ≈ NI) —
  status "narrowed" with the missing fact named (pot-relining/大修 notes). Neither side restated
  the other; the conclusion carries the caveat ("current FCF overstates owner cash if
  maintenance ≈ D&A").
- **Peak-earnings trap refused with arithmetic, not narrative** — Greenblatt turn 3 and Penman
  turn 7 — the 32.2% peak EBIT/EV yield and 18.3% peak E/P were explicitly labelled mirages and
  replaced by a 50–90亿 band against the 6% floor; the low end (6.6% after tax) was shown to
  barely pass, so the thesis is not fine-tuned at the midpoint.
- **Hypothesis discipline** — Li Lu turns 4, 9, 13 — alumina-collapse, Yunnan rationing, and the
  中铝系 controller are all labelled hypotheses/background knowledge with the verifying document
  named; he explicitly declines a strong view until the alumina series is seen ("not entitled").
  Greenblatt's §6.1 blind spot (cyclicals at peak) materialised and was caught by the panel's own
  normalization, not missed.
- **Point-to-point price honesty** — workpaper §G — the −36% is flagged as two closes, not a
  verified 2026 path, since S2 has no 2026 daily prices.

## Weaknesses
- **[major] Systematic 亿→"billion" unit mislabel in the spoken text** — every discussion turn:
  Buffett t1 "7 billion … 167 billion" (= 7.0亿 / 167.3亿, i.e. 0.7 / 16.7 billion), Greenblatt t3
  "182 billion" peak EBIT (= 181.9亿), Penman t2 "292 to 254 billion" NOA, Bezos t5 "raised 87
  billion … 212 billion of net cash", Li Lu t4/t9 "232 billion" hoard, Buffett t14 spoken verdict
  aside, the conclusion itself correctly uses 亿. All evidence[] values and the workpaper are
  correct in 亿; ratios and conclusions are unaffected. But 1亿 = 0.1 billion, so the transcript
  overstates every spoken amount 10×. The prior session (605499.SH 2026-11-23-04) used 亿 directly
  in English text — the house convention. This is a shared workflow problem (all five speakers),
  not traceable to one role card; the orchestrator should require a units pass on the transcript
  (write 亿, or convert correctly) before any publish.
- **[minor] "About half" conflates two windows, at high confidence** — Penman t2. Over the full
  decade the log decomposition is ~49% OPM / ~51% ATO (5.2→12.2%, 0.96→2.35), which supports
  "half". But the sentence anchors on 2021–2025 base shrinkage, and over that window turnover
  explains ~84% of the RNOA rise (ATO 1.44→2.35 vs OPM 11.2→12.2). The impairment bleed-back
  attribution ("today's return borrows from that charge") is directionally right but its size is
  unknown — the workpaper itself lists "which assets the 19.85亿 wrote down" as an open question.
  Confidence should have been medium on that clause, and the window stated.
- **[minor] EBIT definition step skipped** — Greenblatt t3/t8 and workpaper §4/§E use raw 营业利润
  (TTM 181.9, band basis FY2022–24 55–60) without the bottom-up core-EBIT rebuild his card §3.10
  requires (营业利润 is not EBIT). Here the gap is small and conservative (FY2025 core pretax OI
  88.9 vs 营业利润 86.5; net financial income), so the band survives, but the definitional check
  should be shown. EV also strips all cash rather than excess cash; defensible given negative OWC
  every year, and the workpaper carries the 1.5%-of-sales sensitivity (575.8) — noted, not a fault.
- **[minor] challenges[] under-recorded** — Penman t7 asks Greenblatt "does your EV yield
  double-count the cash in my book-value anchor?" and Bezos t10 asks whether the spike is rolling
  over; both are challenges in substance, answered at t8 and t11, yet both challenges arrays are
  empty. Only 2 of ~4 actual challenges are structurally recorded; the transcript is richer than
  the metadata.
- **[minor] Multi-idea turns** — Penman t7 (E/P curve + implied g + equity multiplier + a
  challenge) and Bezos t5 (placements + dilution + capex + debt repayment + FCF/share) each carry
  three or more ideas against the one-idea-per-turn rule. Every non-closing turn does end with
  exactly one concrete question (13 of 13 checked), and the round stayed on one thread.
- **[minor] Rounding/wording nits** — workpaper §C displays "60.5 − 44.0 + 116.1 = 132.7", which
  evaluates to 132.6 at the shown precision (true unrounded 132.68 → 132.7 is correct; verified in
  S2); knowledge candidate 1's FCF sub-sums −47.8/308.7 vs −47.9/308.6 from the rounded table are
  the same artifact. Li Lu t9 "dividends, up from nothing" ignores the 2017 dividend of 1.82亿 —
  the zero stretch is 2018–2020, which is what the evidence claim actually says.

## Evidence audit
Spot-checks against factsheet.md, workpaper-round-01.md, and read-only S2 (bme.duckdb) queries.
Amounts in 亿元.

| claim | expert (turn) | source cited | checked / recomputed | result |
|---|---|---|---|---|
| 10y CFO Σ 470.7 | panel / workpaper §2 | S2 cash reconciliation | S1 经营现金净额 Σ = 470.71 | ok |
| 10y capex Σ 209.9; FCF Σ 260.8; parent NI Σ 230.1 → 1.13× | Bezos t5 / workpaper §2 | S2 raw annual; S1 | Σ 209.9; 470.7−209.9 = 260.8; S1 Σ 230.11; 260.8/230.1 = 1.133 | ok |
| FY2016–20 NI 7.0 / capex 167.3; FY2021–25 NI 223.1 / capex 42.6 | Buffett t1 | S2 raw annual sums | 7.00 / 167.3; 223.11 / 42.6 | ok |
| FY2025 capex 6.4 vs D&A 18.6 = 0.34× | Buffett t1 | S2 capital & reinvestment | factsheet row 20251231: 6.4 / 18.6 = 0.344 | ok |
| NOA 291.6 (2021) → 254.3 (2025); rev 416.7→600.4 (+44%) | Penman t2 | S2 reformulated_bs | factsheet: 291.6 / 254.3; 600.4/416.7−1 = 44.1% | ok |
| FY2021 impairment 19.85 (≈ unusual pretax −20.2) | Penman t2 | S2 raw_income assets_impair_loss | duckdb: −19.849 (2021), −6.330 (2018); reformulated_is −20.2 | ok |
| GM 10.0% (2025Q1) → 31.6% (2026Q1); 9M26 rev +19.4%, cost −4.1% | Greenblatt t3 | S2 raw_income, derived | duckdb: (144.111−129.763)/144.111 = 9.96%; (163.832−112.103)/163.832 = 31.57%; 526.161/440.716−1 = +19.39%; 357.592/372.900−1 = −4.11% | ok |
| TTM parent NI 132.7; PE(TTM) 5.49 | conclusion / Li Lu t13 | workpaper §C; S1 snapshot | duckdb: 60.547−43.982+116.116 = 132.68; 728.62/132.7 = 5.49 = S1 | ok (displayed rounded bridge gives 132.6; rounding only) |
| TTM 营业利润 181.9 → 32.2% of EV | Greenblatt t3 | workpaper §C | duckdb: 86.509−62.142+157.495 = 181.86; 181.9/565.5 = 32.2% | ok |
| EV 565.5 = 728.62 + 19.99 + 48.67 − 193.71 − 38.07 | Greenblatt t3 | S1 EV items; S2 BS 20260930 | debt 6.52+13.34+0.13 = 19.99; 728.62+19.99+48.67−231.78 = 565.50 | ok |
| Net cash 211.8 (Sept26) = 29% of cap | Bezos t5 / Buffett t14 | S2 raw_balancesheet | 231.78−19.99 = 211.79; /728.62 = 29.1% | ok |
| Implied g 1.1% at r=8%, E=55, B=420.9 | Penman t7 | workpaper §E | 0.08 − (55−0.08×420.9)/307.72 = 0.0107 | ok |
| Zero-growth r = E/P: 45→6.2%, 60→8.2%, 133→18.3% | Penman t7 | workpaper §E | 45/728.62 = 6.18%; 60/728.62 = 8.23%; 133/728.62 = 18.25% | ok |
| EPS 0.043 (2016) → 1.746 (2025); shares +33% | Buffett t6 | derived, S1 | 1.11/26.07 = 0.0426; 60.55/34.68 = 1.746; 34.68/26.07−1 = 33.0% | ok |
| FCF/share −1.28 (2018), 2.25 (2025), 4.37 (TTM) | Bezos t5 | workpaper §B/§C | −33.3/26.07 = −1.277; 77.9/34.68 = 2.246; 151.5/34.68 = 4.369 | ok |
| Payout 20.2% → 32.2% → 40.0% (24.24亿 2025); zero 2018–20 | Li Lu t9 / Bezos t10 | S1 annual.分红 | 7.98/39.56 = 20.2%; 14.22/44.12 = 32.2%; 24.24/60.55 = 40.0%; S1 分红 2018–20 — | ok |
| Placements ≈87.4 (36.3 / ~21.1 / 30.0) | Bezos t5 | S2 raw_cashflow less minority | duckdb: 36.34−0.01 = 36.33; 30.07−8.96 = 21.10; 30.49−0.49 = 30.00; Σ 87.43 | ok |
| Equity multiplier 3.46 → 1.38; S1 ROE 20.06% | Penman t7 | derived; S1 | 319.27/92.4 = 3.455; 441.76/320.32 = 1.379 | ok |
| Normalized PE 12.1 / 13.2; EBIT 70 → 9.3%, EBIT 50 → 6.6% after tax | Buffett t14 / Greenblatt t8 | workpaper §E | 728.62/60 = 12.14; /55 = 13.25; 70/565.5×0.75 = 9.28%; 50/565.5×0.75 = 6.63% | ok |

SRC citations: all six marked "(read this turn)"; anchors verified on the role cards and the GGG
savings-account passage confirmed in the source file (p.8 region, "requires you to keep adding
money at those disappointing returns"). No SRC citation on an unmarked passage.

## Knowledge candidates
None to drop. All five are supported by the audited numbers or explicitly labelled as
hypothesis/method. One editorial note for the orchestrator: candidate 3 (kind: fact, medium)
embeds an interpretation — "the market prices spread normalization" — inside a fact; keep the
price/earnings path as the fact and mark that clause as panel inference (it is the alumina
hypothesis in disguise). Candidate 1's FCF sub-sums (−47.8/308.7) differ by 0.1 from the rounded
table sums (−47.9/308.6); rounding, not an error.

## Proposals filed
None. The 亿/"billion" mislabel is shared by all five speakers and contradicts an existing house
convention (605499.SH 2026-11-23-04 uses 亿 in English text), so it is a workflow weakness, not a
role-card defect; AGENTS.md already requires unit discipline. Penman's window conflation and
Greenblatt's skipped EBIT rebuild are single instances — recorded here per protocol; a proposal
needs a second instance or a factual error in a card, and neither card is wrong.

## Suggested next question
"What do AR2025's 关联方及关联交易 note and the 实际控制人 chain say about alumina purchase pricing
and the intended use of the 231.8亿 cash hoard?" — it is the highest-weighted unresolved fact that
primary documents can actually settle locally: it gates both the cash cushion (29% of market cap,
the stated margin of safety) and the quiet leak in owner earnings, whereas the alumina price
series (the panel's own top candidate) needs external data the panel does not have.

## Orchestrator resolution (post-review, same day)
- **[major] units** — fixed: all spoken amounts now written in 亿 (house convention); no "billion" remains in the transcript. Evidence values and conclusions were already correct; no numbers changed.
- **[minor] Penman window/confidence** — fixed: t2 now states "about half over the full decade … since 2021 mostly turnover", bleed-back size labelled unverified, statement confidence lowered to medium.
- **[minor] challenges[]** — fixed: Penman t7→Greenblatt (EV double-count) and Bezos t10→Greenblatt (spike rolling over) recorded.
- **[minor] EBIT proxy** — disclosed in Greenblatt t3 evidence source (营业利润 as proxy; FY2025 core pretax OI 88.9 vs 86.5); full rebuild still not done, noted.
- **[minor] knowledge candidate 3** — "market prices spread normalization" now explicitly marked panel inference.
- **[minor] Li Lu t9 wording** — "up from nothing" corrected to "back after three zero years" (2017 dividend 1.82亿 acknowledged).
- Not fixed (accepted, recorded): two multi-idea turns (Penman t7, Bezos t5); rounding display nits in workpaper §C and candidate 1 sub-sums.