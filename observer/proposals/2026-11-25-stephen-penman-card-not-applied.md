# Proposal: stephen-penman — the expert skipped a step their own card requires

**Status:** applied
**Kind:** improvement
**Tag:** stephen-penman/card-not-applied
**Filed:** 2026-11-25 by scripts/improve.py (threshold: `card-not-applied` on stephen-penman in 2 rounds)
**Target:** experts/stephen-penman.md → §3.3
**Evidence:**
- 000915.SZ/2026-11-25-01 r1 · stephen-penman · t1,t11 — "The card nets operating liabilities as interest-free financing, but the GREAT verdict and RNOA 102% were not split: half of the NOA fall is OL growth [4.6 to 6." — [medium]
- 605499.SH/2026-11-23-02 r1 · stephen-penman · t8 — "residual earnings charged on reported TTM profit including about 3.7 pretax of fair-value and investment gains; the card's core-vs-unusual split was not done" — [medium]

## Change

Add one bullet at the end of §3.3 Profitability analysis, after the "Separate **core (recurring) OI**…" bullet:

> - **Apply both splits before a verdict, not only in the workpaper.** Before RNOA or a shrinking NOA is cited as evidence of a capital-light or "great" business, split ΔNOA into ΔOA and ΔOL and say in the same turn how much of the release is operating-liability growth (taxes, payroll, advances, accrued charges) that can reverse; when OL/NOA is above about 0.5, quote the return on operating assets beside RNOA. Before residual earnings are charged on reported or TTM profit, remove unusual and fair-value items so RE runs on core earnings. [observer-added, from 000915.SZ/2026-11-25-01 r1 and 605499.SH/2026-11-23-02 r1]

## Risk

Mostly a restatement of rules already in §3.3 (OLLEV, core vs unusual), made operative. It could lengthen turns. It could also make the expert discount every OL-funded business, although stable OL float (a durable customer-advance model) is legitimate value; the bullet asks for disclosure, not a haircut. It does not overlap Bezos's float lens, which judges whether float is good, not how RNOA is measured.

## Validation

Reviewed 2026-11-25 by an independent reviewer (did not read the discussion).

1. Cited statements or source evidence show the claim: **pass.** Log lines for 000915.SZ/2026-11-25-01 r1 (t1,t11) and 605499.SH/2026-11-23-02 r1 (t8) match the proposal. The 000915 observer note (as reviewed, before the Resolution) records that about half of the NOA fall (12.21 to 8.55亿) was OL growth (4.6 to 6.4亿) that unwound (NOA +6.12亿) and that RNOA 102% and GREAT were never split; 605499 t8 charged RE on reported TTM profit holding about 3.7亿 pretax fair-value and investment gains, and Penman himself called those gains a drag in t6. Both weaknesses were real as reviewed. Caveat: the 000915 gap is partly a Buffett t1 claim; the Penman fault is the missing application of OLLEV.
2. No contradiction with §8 anchors or §1 scope: **pass.** Consistent with HTML Ch 6 ("Operating liabilities lever the profitability of operations and can add value"), Ch 10 and §3.8 (core vs unusual); the bullet asks for disclosure, not a haircut, which keeps the Ch 6 "can add value" reading. Stays within accounting reformulation.
3. Not already covered by another expert: **pass.** Bezos's card has no float lens on RNOA measurement; Mauboussin excludes non-operating items for NOPAT/ROIC but not for residual earnings or ΔNOA/ΔOL. Overlap is only with Penman's own §3.3 (OLLEV, core vs unusual), which is the point: the card states the rules but the expert skipped them twice.
4. `scripts/validate.py --quiet` on a scratch copy with the Change inserted after the core-OI bullet: **passes (exit 0).** Only pre-existing WARN lines for pre-2026-11-24 rounds.
Optional tightening: two rules in one bullet; could split "ΔNOA into ΔOA/ΔOL" and "core RE" into two sentences-as-bullets, and define "OL/NOA above about 0.5" as OLLEV (the card's term).
**Verdict:** validated. Priority 1 if only one change per expert is applied this session (two medium-severity hits, Penman-specific, directly operationalises existing card text).
## Applied

2026-11-25 — experts/stephen-penman.md 1.1 → 1.2, §3.3 bullet added verbatim; changelog line added. Commit: recorded after publish.
