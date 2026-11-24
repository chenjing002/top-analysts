# Proposal: michael-mauboussin — a prior is a prior, and a yield with marks in it is not income

**Status:** rejected
**Kind:** improvement
**Tag:** michael-mauboussin/assumption-as-finding
**Filed:** 2026-11-24 by scripts/improve.py (threshold: `assumption-as-finding` on michael-mauboussin in 2 rounds); Change written by the orchestrator
**Target:** experts/michael-mauboussin.md → §4 Evidence standards
**Evidence:**
- 605499.SH/2026-11-23-03 r2 · michael-mauboussin · turn 5 — "High returns regress toward the mean — that is the base rate I work from — and the newest lines are regressing fastest" — the prior is named, but "regressing fastest" is spoken as an observed speed when the local data give two-year growth, not a fade rate
- 605499.SH/2026-11-23-03 r3 · michael-mauboussin · turn 7 — "call it 2.6% on cash and more on the trading book. So they borrow cheap and lend dear, and pocket the spread" — the trading-book yield (about 7% annualized in the workpaper, partly fair-value marks) is spoken as a recurring spread; the caveat covers the loan terms, not the marks

## Change

Add one bullet to §4 Evidence standards, after the **Management claims** bullet:

```
+ - **Priors and annualized yields are labelled as such when spoken.** [observer-added, from 605499.SH/2026-11-23-03 r2, r3] Base-rate regression says returns fade; it does not say how fast this company's are fading — state the prior as a prior and name the local series (unit volume, segment growth, incremental ROIC) that would measure the speed. A yield annualized from part-year interest or a trading book that includes fair-value marks is spoken with the mark-to-market share named, never as recurring income.
```

## Risk

Overlaps the shared workflow rule that assumptions are identified in spoken text; the bullet is specific to the two tools this card relies on (base rates and return measurement) and to the failure the rounds showed. Could make the base-rate argument sound weaker than the paper intends; the prior itself is unchanged.

## Validation

Reviewed 2026-11-24 by an independent subagent reviewer (did not take part in the rounds). Read: the proposal; experts/michael-mauboussin.md §1, §3.5, §3.8, §4, §8; OBSERVER.md §3; round-02.json statements[4] and round-03.json statements[6] (text and evidence); observer/round-02.md and round-03.md Weaknesses; data/workpaper-round-03.md; AGENTS.md shared rules; skills/analyze/CHECKLIST.md; observer/TAGS.md; knowledge/playbook.md; experts/stephen-penman.md §3.1–3.3, §6.

1. Cited statements or source evidence show the claim: **partly** — r3 turn 7 shows it: the spoken text says "2.6% on cash and more on the trading book … pocket the spread" and the only spoken caveat is "the loan terms are not in our data"; the workpaper confirms the trading-book figure ("3.49 in 9M (≈7% annualized, includes marks)") and the turn's own evidence item names "fair-value gains 2.63", so the marks are labelled in evidence but not in speech. r2 turn 5 does **not** show an unlabelled prior: the prior is spoken as a prior ("that is the base rate I work from") and the turn names the local series the bullet asks for (electrolyte +118%→+12% from turn 1; energy ~14%/yr vs the company's 28%/yr, both in evidence). The observer note itself says "Properly labeled as his working base rate." The real slip in turn 5 is conflating segment-growth deceleration with return regression ("regressing fastest" on a growth series), which the proposed bullet would not have changed — the turn as spoken already satisfies it. Both tagged instances are low severity. Only one of the two evidence lines supports a card defect, so the two-statement threshold is met in count but not in substance.
2. No contradiction with §8 anchors or §1 scope: **yes** — p.8 "Historical results show that ROIC tends to regress toward the mean" and p.31 "ROIC is useful only to the degree that past results provide some guidance about the future" are consistent with stating the prior as a prior; §3.8 already excludes financial-asset income (投资收益, 公允价值变动收益) from NOPAT. Nit: the paper does give a population fade speed (quintile regression over five years, §3.5), so "it does not say how fast" holds only for *this company's* rate, as the bullet words it. Scope is not breached.
3. Not already covered by another expert: **no — covered, redirect** — the first sentence restates the existing workflow pattern tag `base-rate-labelled` in observer/TAGS.md ("Use a prior from a card as a prior, say so, and name the local evidence that would move it"), a rule meant for every expert via the playbook; Penman §6 already records "Mean reversion of RNOA is the right prior but it is a prior." The second sentence is Penman §3.2 (fair-value gains on 交易性金融资产 → NFE, not core income), playbook P-007 `operating-financing-separated` (earned in this same session, r1 and r3, and applied by Penman turn 8 to exclude the carry from core NOPAT), the CHECKLIST `[cash-split]` rule ("trading financial assets and their income are financing"), and the AGENTS.md rule to separate evidence, calculations, assumptions and hypotheses. The proposal's own Risk section concedes the overlap. The right home is the playbook/checklist, not this card.
4. `scripts/validate.py` passes on a scratch copy: **yes** — change applied exactly as written to a scratch copy under scratchpad/mauboussin-review; `validate: 0 errors, 6 warnings` (all pre-2026-11-24 check_round warnings, expected).
**Verdict:** rejected — one of the two cited turns already labels the prior as a prior and names the local series (the proposed remedy), leaving a single low-severity spoken-caveat instance; and both halves of the bullet are already owned by shared rules (`base-rate-labelled`, P-007, `[cash-split]`, AGENTS.md) and by Penman's financial-item classification, so the card is not the defect. If the `assumption-as-finding` tag recurs on this card with an instance the shared rules do not already cover, refile; meanwhile the trading-book-marks point is a candidate `[cash-split]` refinement in skills/analyze/CHECKLIST.md ("name the mark-to-market share when an annualized trading yield is spoken").

## Applied

—
