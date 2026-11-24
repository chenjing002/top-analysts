# Proposal: li-lu — carry the assumption in the sentence that carries the number

**Status:** rejected
**Kind:** improvement
**Tag:** li-lu/assumption-as-finding
**Filed:** 2026-11-24 by scripts/improve.py (threshold: `assumption-as-finding` on li-lu in 2 rounds); Change written by the orchestrator
**Target:** experts/li-lu.md → §4 Evidence standards
**Evidence:**
- 605499.SH/2026-11-23-03 r3 · li-lu · turn 9 — "the cash flow shows an exchange loss of about 2 亿 … That makes me think it could be an offshore listing, but I am guessing" — a cause inferred from one line item; labelled, but the label sits two sentences after the figure and the inference still enters the round's governance reading
- 605499.SH/2026-11-23-04 r1 · li-lu · turn 7 — "Year-end plus the raise gives about 17 yuan a share, 15% of the price … count plants at half cost. At full cost it is 22 to 24 yuan, 19–21%" — the floor is quoted as a percentage before the haircut that produces it is stated; the observer notes "16%" can be quoted as a fact

## Change

Add one bullet to §4 Evidence standards, after **Standard of proof**:

```
+ - **A spoken estimate carries its assumption in the same sentence.** [observer-added, from 605499.SH/2026-11-23-03 r3, 2026-11-23-04 r1] When a figure he speaks is a scenario (a floor at a stated haircut) or a cause read from one line item (an FX loss, a single provision), the assumption or the single-source nature is stated before or with the number, and the document that would turn it into a fact is named in the same turn. The workpaper label is not enough: the spoken figure is what gets quoted.
```

## Risk

Could make Li Lu hedge every number and lengthen turns; the rule is limited to scenarios and single-item inferences, which his own §4 already treats as weak evidence ("a single quarter in either direction" is discounted). It does not change what he accepts as evidence, only where the label sits.

## Validation

Independent review 2026-11-24 (reviewer had not read the rounds; judged from the two cited turns, the two observer notes, the card, OBSERVER.md §3, AGENTS.md shared rules and skills/analyze/CHECKLIST.md).

1. Cited statements or source evidence show the claim: **no (one of two)** — 2026-11-23-04 r1 turn 7 does show it: "about 17 yuan a share, 15% of the price" and "18.5, 16%" are spoken two sentences before "count plants at half cost" and the prepayment deduction; the full-cost alternative follows and confidence is `low`, but the percentage can be lifted without its haircut, as the observer said (medium). 2026-11-23-03 r3 turn 9 does **not** show it: the sentence that carries the 2 亿 opens with "There is a hint it may be foreign money", the label "but I am guessing" is the very next sentence (not two sentences later as the Evidence line says), and the verifying document is named in the same turn ("Until we read the issue document"). That turn already meets the proposed bullet word for word, and the observer note rated it low with "No action needed beyond the existing label." One genuine instance is below the two-round threshold that drafts an improvement.
2. No contradiction with §8 anchors or §1 scope: **yes** — the bullet is in the spirit of §1(d) intellectual honesty and §8 p.6 ("Both are possible") / p.7 ("Do I know enough to be entitled to an opinion?"). One misfit, not a contradiction: "the document that would turn it into a fact" has no referent for a floor at a stated haircut, which is a scenario by construction and never becomes a fact.
3. Not already covered by another expert: **no — redirect to the workflow** — no other card carries this wording, but the mechanism is not traceable to anything in the Li Lu card (nothing in §3–§5 induces figure-before-assumption ordering), and the same tag drafted a parallel proposal against michael-mauboussin on the same day, which is the OBSERVER.md §1 signature of a shared workflow problem. The verifier-naming clause duplicates playbook P-002 (`hypothesis-names-verifier`); the substance is in AGENTS.md ("Separate company evidence, calculations, assumptions, and hypotheses") and CHECKLIST C1. What is missing is a placement rule for spoken text, and that belongs in skills/analyze/CHECKLIST.md Discussion rules (e.g. "A scenario or single-item inference is spoken with its assumption in the same sentence as the figure" [assumption-as-finding]) or a playbook pitfall with `expert: null`, where every expert reads it, not in one card.
4. `scripts/validate.py` passes on a scratch copy: **yes** — change applied after **Standard of proof** in a scratch copy under scratchpad/lilu-review/; `validate: 0 errors, 6 warnings`, all six the expected pre-2026-11-24 check_round report-only warnings.
**Verdict:** rejected — only one of the two cited turns shows the weakness (r3 turn 9 already labels the inference before the figure and names the verifying document, as the observer itself recorded), so the evidence threshold is not met; and the weakness is a speech-placement rule shared with the Mauboussin proposal filed the same day, so its home is CHECKLIST.md / the playbook, not the Li Lu card. Re-file against the workflow; if Li Lu alone shows a second genuine instance, a card proposal can be drafted then.

## Applied

—
