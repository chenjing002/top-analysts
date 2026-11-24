# Proposal: joel-greenblatt — 营业利润 or another line used as EBIT/OI without the rebuild the card requires

**Status:** applied
**Kind:** improvement
**Tag:** joel-greenblatt/ebit-proxy
**Filed:** 2026-11-24 by scripts/improve.py (threshold: `ebit-proxy` on joel-greenblatt in 2 rounds)
**Target:** experts/joel-greenblatt.md → §3.10, "EBIT from PRC statements" bullet (append)
**Evidence:**
- 000807.SZ/2026-11-23-05 r1 · joel-greenblatt · t3,t8 — "营业利润 used as EBIT without the card's core-EBIT rebuild; gap small here [88.9 vs 86.5] but the definitional step was skipped" — [low]
- 000807.SZ/2026-11-24-01 r1 · joel-greenblatt · t4 — "Recurring: 2026-11-23-05 r1 t3,t8. Card 1.1 bottom-up EBIT skipped as 'expense detail not in local data'; DuckDB raw_income has the lines. Observer rebuild: har" — [low]

## Change

Append to the §3.10 "EBIT from PRC statements" bullet:

> Before declaring the rebuild impossible, check the local data layer: DuckDB `raw_income`
> carries `sell_exp`, `admin_exp`, `rd_exp` and `biz_tax_surchg`, so the bottom-up build is
> closable for any S2-covered company. A proxy is allowed only with the gap quantified against
> that rebuild in the same evidence item — never on a "not in local data" claim that the local
> data contradicts. [observer-added, from 000807.SZ/2026-11-23-05 r1 and 2026-11-24-01 r1]

Rationale: the card already mandates the rebuild (§3.10); both cited rounds skipped it, the
second with a false data-availability claim. The addition closes the escape hatch, not the
method.

## Risk

Low. The rule does not forbid proxies — it forbids unquantified ones and false availability
claims. Where the expense lines genuinely are absent (raw-statement-only sectors), the proxy
with a stated gap remains allowed. No §8 anchor is touched; the addition is an A-share
application note, consistent with the existing unanchored §3.10 extensions.

## Validation

Independent reviewer, 2026-11-24 (had not read the discussion; read only the cited evidence).

1. Cited statements or source evidence show the claim: **pass** — log.jsonl carries both occurrences (000807.SZ/2026-11-23-05 r1 t3,t8 and 2026-11-24-01 r1 t4, marked recurring); the observer note's weakness and Resolution item 4 confirm the skip and the false "not in local data" claim; read-only DuckDB query confirms `raw_income` has `sell_exp`, `admin_exp`, `rd_exp`, `biz_tax_surchg` (the round JSON now shows the post-fix rebuild with the gap quantified, consistent with the Resolution).
2. No contradiction with §8 anchors or §1 scope: **pass** — changelog 1.0 states the A-share application notes are "written by the distiller, not sourced from the lectures", so §3.10 is an explicitly unanchored system extension; the addition enforces the rebuild §3.10 already mandates and fits §1 ("takes reported cash and EBIT as the starting point and adjusts"); no §8 anchor touched. Caveat: "closable for any S2-covered company" is slightly strong — schema presence does not guarantee populated values; the Risk section's escape clause (proxy with stated gap where lines are genuinely absent) covers this.
3. Not already covered by another expert: **pass** — the target card mandates the rebuild but has no data-layer check and no proxy-with-quantified-gap rule; Penman's §3.10 rebuilds OI (a different measure) and does not close this escape hatch. The addition is genuinely new enforcement, not a restatement.
4. `scripts/validate.py` passes on a scratch copy: **pass** — repo baseline 0 errors (6 pre-existing report-only warnings on pre-2026-11-24 rounds); scratch copy with the sentence appended to the §3.10 bullet: 0 errors, same 6 warnings. Prose-only append to an existing bullet, `[observer-added]` marker present, no structural break.
**Verdict:** validated — the recurring miss and the false data-availability claim are documented in two rounds, the local data contradicts the claim, and the clause adds enforcement the card lacks without touching any source anchor.

## Applied

2026-11-24: edit applied to the target card, version bumped to 1.2, changelog recorded. Independent validation above. Commit hash: pending (publication not authorized this session).
