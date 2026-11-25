# Proposal: stephen-penman — one sentence mixes two periods or windows

**Status:** validated
**Kind:** improvement
**Tag:** stephen-penman/window-conflation
**Filed:** 2026-11-25 by scripts/improve.py (threshold: `window-conflation` on stephen-penman in 2 rounds)
**Target:** experts/stephen-penman.md → §4
**Evidence:**
- 000807.SZ/2026-11-23-05 r1 · stephen-penman · t2 — "'about half' conflates the full decade [~49% margin] with 2021–25 [~84% turnover] and the bleed-back size is unknown" — [low]
- 000915.SZ/2026-11-25-01 r1 · stephen-penman · t7 — "Recurring [000807.SZ/2026-11-23-05 r1]. Says the price assumes 'this broken year' lasts, but TTM parent profit 2.8亿 still holds three pre-break quarters and the" — [medium]

## Change

Add one bullet at the end of §4 Evidence standards:

> - **One window per figure.** A trailing-twelve-month figure names the quarters it contains. When the latest quarter breaks from the others (a loss, a deduction, a sign change), show that quarter beside the TTM and never call the TTM "this year" or "the broken year". A ratio computed over a decade is not attributed to a sub-period (or the reverse); when a comparison crosses windows, name both in the same sentence. [observer-added, from 000915.SZ/2026-11-25-01 r1 and 000807.SZ/2026-11-23-05 r1]

## Risk

Adds words to valuation turns already near the 110-word cap; the quarter list can sit in evidence while the turn names the break. Penman may lean on single quarters more than his card's forward-earnings anchor intends; the bullet asks only that the break be shown, not that it replace the TTM. It does not overlap any other expert: Tukey/P-014 cover single-quarter inference, not window labelling.

## Validation

Reviewed 2026-11-25 by an independent reviewer (did not read the discussion).

1. Cited statements or source evidence show the claim: **pass, with a caveat.** 000807.SZ/2026-11-23-05 r1 t2 (low): "about half" mixed the full-decade ~49% margin with 2021-25 ~84% turnover; the log and observer note confirm it, and it was fixed. 000915.SZ/2026-11-25-01 r1 t7 (medium): "this broken year" and "holds at 8% or 12%" against a TTM that still holds three pre-break quarters (1.27, 1.11, 1.13) plus a loss quarter (-0.67); confirmed in the observer note as reviewed (fixed afterwards, see Resolution W1). The two instances differ in kind (decade vs sub-period ratio; TTM vs latest quarter), and the first is low severity, so evidence is thinner than for the other proposal; the bullet does cover both patterns.
2. No contradiction with §8 anchors or §1 scope: **pass.** Penman's forward-earnings anchor is untouched; the bullet asks to show the break beside the TTM, not replace it. No source anchor needed because it is an evidence-hygiene rule.
3. Not already covered by another expert: **pass, mild concern.** No other card has window labelling (Li Lu uses TTM but has no such rule; Tukey/P-014 cover single-quarter inference). AGENTS.md "Shared rules" already require stating period and scope, so this is arguably a panel-wide rule better placed in the playbook than in one card. It is accepted here because both log hits are Penman's.
4. `scripts/validate.py --quiet` on a scratch copy with the Change appended to §4: **passes (exit 0).** Only pre-existing WARN lines for pre-2026-11-24 rounds.
Optional tightening: drop the sentence quoting "this year"/"the broken year" (it targets one round's wording); keep "name the quarters in a TTM, show a breaking quarter beside it, name both windows when crossing".
**Verdict:** validated. Priority 2.
## Applied

—
