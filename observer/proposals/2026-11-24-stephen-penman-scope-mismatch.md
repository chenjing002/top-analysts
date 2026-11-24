# Proposal: stephen-penman — parent vs total, pre- vs post-bonus shares, consolidated vs segment

**Status:** applied
**Kind:** improvement
**Tag:** stephen-penman/scope-mismatch
**Filed:** 2026-11-24 by scripts/improve.py (threshold: `scope-mismatch` on stephen-penman in 2 rounds)
**Target:** experts/stephen-penman.md → §3.10, new bullet after "Market data"
**Evidence:**
- 000807.SZ/2026-11-24-01 r1 · stephen-penman · t7 — "Like-for-like strips consolidated net cash 211.79 from parent earnings/price with no minority deduction [card 3.10]. MI book 48.67 as minority cash-share proxy " — [low]
- 605499.SH/2026-11-23-02 r1 · stephen-penman · t1 — "share count 5.2→7.3 includes a ×1.30 bonus step; read as dilution before the step was identified" — [low]

## Change

Add a bullet at the end of §3.10 (after "Market data"):

> **Scope checks before quoting a yield or per-share figure.** State the basis on every such
> figure: parent vs consolidated, pre- vs post-bonus shares. When consolidated net cash is
> stripped for a like-for-like or ex-cash yield, minorities own part of that cash: deduct their
> share from both the cash and its carry (book-equity share as a labelled proxy when no better
> split exists) and show the yield on both bases. When share count jumps, identify 送转
> (bonus/transfer) steps before calling it dilution. [observer-added, from
> 000807.SZ/2026-11-24-01 r1 and 605499.SH/2026-11-23-02 r1]

Rationale: §3.10 already states the minority deduction for equity value (CSE = NOA − NFO −
minority) but never extends it to cash-stripped yields; the 605499 round read a ×1.30 bonus step
as dilution. One basis-discipline bullet covers both cited misses.

## Risk

Low to medium. The minority book-equity share is a rough proxy for the minority cash share and
could mislead if quoted as precise; the text therefore requires labelling it a proxy and showing
both bases rather than a single "corrected" number. No §8 anchor is touched.

## Validation

Independent reviewer, 2026-11-24 (had not read the discussion; read only the cited evidence).

1. Cited statements or source evidence show the claim: **pass** — log.jsonl carries 000807.SZ/2026-11-24-01 r1 t7 (consolidated net cash 211.79 stripped from parent earnings/price, no minority deduction) and 605499.SH/2026-11-23-02 r1 t1 (×1.30 bonus step in 5.2→7.3 read as dilution); the observer note's weakness 7 and Resolution item 7 confirm both, and the current t7 shows the post-fix minority-proxy sensitivity (10.4% book share → 7.66%, labelled rough). Two rounds, same expert and tag; the third scope-mismatch line (605499.SH/2026-11-23-03) is `expert: null` and correctly not counted.
2. No contradiction with §8 anchors or §1 scope: **pass** — §8 states explicitly "The A-share mapping in 3.10 is this system's extension and has no source anchor" (§6 repeats it); the bullet extends the card's existing minority treatment (CSE = NOA − NFO − 少数股东权益; parent equity = operations − NFO − minority value) to cash-stripped yields, within §1's accounting-rigor scope. The book-equity proxy is required to be labelled and both bases shown, consistent with the card's evidence standards.
3. Not already covered by another expert: **pass** — the card covers minority deduction for equity value and parent-basis market data, but never for stripped cash and its carry, and nowhere identifies 送转 steps; Greenblatt's EV bullet adds minorities at book for EV, a different calculation that does not cover Penman's like-for-like yield. The shared basis-discipline rule in AGENTS.md exists, but the card-level mechanics are new and useful.
4. `scripts/validate.py` passes on a scratch copy: **pass** — repo baseline 0 errors (6 pre-existing report-only warnings on pre-2026-11-24 rounds); scratch copy with the new bullet appended after "Market data" in §3.10: 0 errors, same 6 warnings. Prose-only bullet, `[observer-added]` marker present, no structural break.
**Verdict:** validated — both cited misses are documented in the log and observer note, and one basis-discipline bullet genuinely extends the card's minority and per-share rules without contradicting any anchor.

## Applied

2026-11-24: edit applied to the target card, version bumped to 1.1, changelog recorded. Independent validation above. Commit hash: 4bb967b3becb94012b0311cc21c613452c390f32.
