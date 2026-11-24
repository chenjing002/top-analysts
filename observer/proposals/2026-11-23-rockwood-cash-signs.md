# Proposal: Use consistent signs in the content cash-flow bridge

**Status:** applied
**Kind:** correction
**Filed:** 2026-11-23 by Codex during role-card review
**Target:** experts/rockwood.md → §3.3 Restate the cash flow statement
**Evidence:**
- §3.3 describes Netflix cash content spend as `$(132B)`. Its FCF formula then subtracts content capex without specifying a sign conversion. Given adjusted OCF of $142B, literal substitution yields $274B before PP&E capex, while reported OCF before that capex is $10B.
- `source-files/Rockwood/media-accounting.md`, Netflix section, reports the $10B, $142B, and $(132B) figures for 2011–2024. The Disney section uses the cash-spend magnitude from the footnote and adds it to reported OCF.

## Change

Replace the formula block in §3.3 with the following.

```text
Reclassified spend = magnitude of the cash outflow included in reported OCF
                     Netflix: negate the sum of the two signed content cash-flow lines
                     Disney FY24: use the footnote spend of 23,435 million dollars
Adjusted OCF       = Reported OCF + Reclassified spend
Content capex      = Reclassified spend, shown as a positive outflow
Adjusted FCF       = Adjusted OCF − PP&E capex − Content capex
                     PP&E capex is a positive outflow separate from content capex.
```

## Risk

This convention applies only to content cash outflows moved from operating to investing. Check for overlap with other capex lines when adapting the bridge to a new company.

## Validation

Independent review 2026-11-24 (reviewer had not read any discussion rounds; judged from the proposal, `experts/rockwood.md`, `source-files/Rockwood/media-accounting.md`, `observer/OBSERVER.md` §3 and `experts/stephen-penman.md` §3.9).

1. Cited statements or source evidence show the claim: yes — `media-accounting.md`, Netflix section, states cumulative 2011–2024 "(Adjusted) operating cash flow was $142B compared to as-reported OCF of $10B" and "Cash content spend was $(132B)"; Disney section states "$23.4 billion under 'Spending'" and "$37.4 billion adjusted" (image 08: Spending 23,435; 13,971 + 23,435 = 37,406). The current §3.3 block mixes conventions: its Adjusted OCF line subtracts the content lines (which only works if they are read as signed, negative CF lines), its Disney bracket adds a positive magnitude (13,971 + 23,435), and its Adjusted FCF line subtracts "Content capex" while the paragraph below quotes that quantity as "$(132B)". Literal substitution of the negative figure gives 142 − (−132) = 274 before PP&E capex, not 10. The proposed block fixes the magnitude as positive: Netflix 10 + 132 = 142 and 142 − 132 = 10 before PP&E capex; Disney 13,971 + 23,435 = 37,406. Both reproduce the source.
2. No contradiction with §8 anchors or §1 scope: yes — §8 anchors ("Cash content spend was $(132B)", "$37.4 billion adjusted", "same bottom line numbers whether you move the lines around or not") are untouched and still consistent; the change is a presentation fix inside the statement-rebuilding scope of §1. §7's "Adjusted OCF" entry keeps the "Reported OCF − (Additions + Change in liabilities)" wording, which remains correct when the lines are read as signed and matches the new "negate the sum of the two signed lines" instruction. Minor loss: the replacement block drops the parenthetical "(= reported FCF; the total is unchanged …)"; the point survives in §5, §6 ("Reclassification is cosmetic to FCF") and §8, so it is not a contradiction.
3. Not already covered by another expert: yes — `stephen-penman.md` §3.9 treats FCF only for liquidity and default (Treasurer's rule) and defines no operating-to-investing content bridge; no other card in `experts/` mentions adjusted OCF, content capex or this reclassification.
4. `scripts/validate.py` passes on a scratch copy: yes — change applied to the scratch `experts/rockwood.md` exactly as written; `validate: 0 errors, 6 warnings` (the warnings are the expected pre-2026-11-24 check_round reports).
**Verdict:** validated — the source figures confirm the sign ambiguity in the current §3.3 block, the replacement makes the magnitude convention explicit and reproduces 10 + 132 = 142, 142 − 132 = 10 and 13,971 + 23,435 = 37,406, and nothing in §8 or §1 is contradicted.

## Applied

Applied 2026-11-24 by the orchestrator: `experts/rockwood.md` version 1.0 → 1.1, changelog line added. Commit: see git log (recorded after commit).
