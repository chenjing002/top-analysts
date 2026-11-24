# Proposal: Define a defensible surplus-cash haircut

**Status:** applied
**Kind:** correction
**Filed:** 2026-11-23 by Codex during role-card review
**Target:** experts/joel-greenblatt.md → §3.10 A-share application notes
**Evidence:**
- The last sentence of the Enterprise value bullet calls `$1–2 on the dollar` a haircut. At the upper end, this doubles the estimated value of cash and subtracts the larger amount from EV. The first part of the bullet and §4 call for assessing availability and use before taking cash at face value.
- `source-files/csinvesting/Lecture 7-Students Grilled on Their Investment Presentations.pdf`, p. 34, discusses cash and the value of the earnings stream in general terms.

## Change

Replace the last sentence of the Enterprise value bullet with the following.

> For 存贷双高 (large cash alongside large interest-bearing debt), check the annual-report notes for restrictions and availability before subtracting excess cash. If availability is uncertain, show EV under a range of recoverable excess-cash assumptions and label them as analyst scenarios.

## Risk

Cash adjustments will vary with the company's disclosures. Showing the assumptions and corresponding EVs keeps the calculation comparable and auditable.

## Validation

Independent review 2026-11-24 (reviewer did not read any discussion rounds; judged from the proposal, the card, the csinvesting transcripts and the protocol only).

1. Cited statements or source evidence show the claim: yes — The current sentence is internally inconsistent on its face: a "haircut" cannot land at $1–2 *on the dollar* (100–200% of face). The transcripts show where the wording came from: Lecture 11, p.2 (already anchored in §8) values a $5 excess-cash pile "as low as $1 or $2 or at full value", i.e. 20–40 cents on the dollar up to par, depending on management's deployment record — "$1–2 on the dollar" is a garbled copy of "$1 or $2 [of $5]". Lecture 7, p.34 is correctly described by the proposal as general ("cash is cash, and you are valuing the earnings stream"); it is not the operative anchor, Lecture 11 pp.1–2 is. The replacement follows the first part of the same bullet (strip restricted 货币资金 first, then only the excess over 1–2% of sales — Lecture 7 p.2 and p.36) and §4 ("balance-sheet cash at face value until its use is known"). It also drops the unsupported claim that 存贷双高 is "exactly" the case Greenblatt haircuts: his discount is for cash management sits on earning 1–2%, not for cash whose availability is in doubt.
2. No contradiction with §8 anchors or §1 scope: yes — Reading annual-report notes for restrictions is "takes reported cash as the starting point and adjusts" (§1) and "reads footnotes for aberrations, not fraud" (§6.7), not auditing. A range of EV scenarios is consistent with Lecture 11 p.2 ("I may value it as low as $1 or $2 or at full value") and p.2 ("You can't immediately unlock the value of the excess cash"). No new anchor is added and none is removed. Note: the replacement no longer states Greenblatt's own deployment-based range in this bullet; that teaching remains in §2 Q4, §3.1, §4, §6.7 and §7, so the card does not lose it.
3. Not already covered by another expert: yes — Penman §3.10 treats 存贷双高 as an earnings-quality red flag and classifies 货币资金 as a financial asset in NFO; he does not haircut cash inside an EV for an EBIT/EV yield. Buffett has no EV construction. The point is Greenblatt-specific EV construction, so it is not a duplicate; the "restricted cash" check overlaps Penman's 受限资金 carve-out only at the level of reading the same footnote.
4. `scripts/validate.py` passes on a scratch copy: yes — Change applied verbatim to a scratch copy of experts/, observer/, knowledge/, Thinkers/, sessions/, scripts/; `validate: 0 errors, 6 warnings` (the six warnings are the expected pre-2026-11-24 check_round reports).

**Verdict:** validated — the current sentence misstates Lecture 11 p.2 ($1–2 of every $5, not $1–2 on the dollar) and the replacement is consistent with the bullet, §4 and the §8 anchors without duplicating another role. Follow-up for the orchestrator, outside this proposal's scope: §7 "Excess cash — valued between $1 and full value per dollar" carries the same garble and should read "between roughly 20–40 cents and full value per dollar (Lecture 11, p.2: $1–2 of $5)"; file as a separate correction.

## Applied

Applied 2026-11-24 by the orchestrator: `experts/joel-greenblatt.md` version 1.0 → 1.1, changelog line added. The reviewer's follow-up on §7 is filed as `observer/proposals/2026-11-24-joel-greenblatt-excess-cash-vocabulary.md` (one change per expert per session). Commit: 10fe8a0.
