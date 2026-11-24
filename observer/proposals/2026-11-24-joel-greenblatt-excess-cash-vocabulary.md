# Proposal: Fix the excess-cash valuation range in §7

**Status:** proposed
**Kind:** correction
**Filed:** 2026-11-24 by the orchestrator, from the independent reviewer's follow-up on `2026-11-23-joel-greenblatt-cash-haircut.md`
**Target:** experts/joel-greenblatt.md → §7 Vocabulary and formulas, "Excess cash" entry
**Evidence:**
- Affected passage (§7): "valued between $1 and full value per dollar depending on management's deployment record" — "$1 per dollar" is full value, so the range collapses; the wording is a garbled copy of the source.
- `source-files/csinvesting/Lecture 11 … .pdf`, pp.1–2 (already anchored in §8): Greenblatt values a $5 excess-cash pile "as low as $1 or $2 or at full value", i.e. roughly 20–40 cents on the dollar up to par, depending on whether management will deploy or return it.

## Change

```
- - **Excess cash** — cash above ~1–2% of sales operating need; valued between $1 and full value per dollar depending on management's deployment record.
+ - **Excess cash** — cash above ~1–2% of sales operating need; valued between roughly 20–40 cents and full value per dollar depending on management's deployment record (Lecture 11, p.2: "$1 or $2 or at full value" of a $5 pile).
```

## Risk

None to the method; this restores the source's range. It must wait for the next session because §3.10 of the same card was changed on 2026-11-24 (one change per expert per session).

## Validation

(filled by the independent reviewer; required before status → validated)

1. Cited statements or source evidence show the claim: —
2. No contradiction with §8 anchors or §1 scope: —
3. Not already covered by another expert: —
4. `scripts/validate.py` passes on a scratch copy: —
**Verdict:** —

## Applied

—
