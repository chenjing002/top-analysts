# Observer tags

Controlled vocabulary for the `## Log` block in every observer note. `scripts/improve.py` reads
those lines into `observer/log.jsonl`, counts them across sessions, and acts on thresholds:

- a **weakness** tag on the same expert in two different rounds drafts a proposal for that card;
- a **weakness** tag with `expert: null` (a workflow problem) in two rounds becomes a playbook
  pitfall, and a candidate for a new `check_round.py` rule;
- a **pattern** tag in two rounds becomes a playbook entry every expert reads at session start.

Use the tag that names the mechanism, not the symptom. Add a tag here before using it; an
unknown tag is a validation warning. `Check` names the deterministic rule that already catches it.

## Weakness tags

| tag | meaning | default target § | check |
|---|---|---|---|
| `units` | 亿 written as billion/million; 元 vs 亿元; wrong scale | — (workflow) | U1 |
| `unsourced-number` | a figure with no evidence item, or whose source does not contain it | §4 Evidence standards | N1, N4 |
| `derived-unshown` | a computed figure without formula and inputs | §4 | N3 |
| `cash-split` | operating and financial items not separated before a ratio or a valuation | §3 Method | — |
| `like-for-like` | basis mismatch: cash stripped from price but its income kept in earnings; TTM vs annual; pre- vs post-raise | §3 | — |
| `required-return-unargued` | r (or g, tax) taken as given and never argued although the answer depends on it | §3 | C1 |
| `default-confidence` | `high` on a result that rests on a model default or an estimate | §4 | C1 |
| `ebit-proxy` | 营业利润 or another line used as EBIT/OI without the rebuild the card requires | §3 | — |
| `window-conflation` | one sentence mixes two periods or windows | §4 | — |
| `single-quarter-read` | one quarter drives the inference; seasonal or lumpy base ignored | §4 | T4 |
| `selective-evidence` | the series that fits is cited, the one that does not is left out | §4 | — |
| `assumption-as-finding` | an estimate or scenario spoken as a fact | §4 | — |
| `narrative-for-arithmetic` | a qualitative claim where a series was available | §5 | — |
| `card-not-applied` | the expert skipped a step their own card requires | §3 | — |
| `scope-mismatch` | parent vs total, pre- vs post-bonus shares, consolidated vs segment | §7 | — |
| `confidence-inflation` | stated confidence above what the evidence supports (other than defaults) | §4 | — |
| `multi-idea-turn` | more than one idea or more than three figures in a turn | — (workflow) | D1 |
| `question-discipline` | no question, or several, in a non-closing turn | — (workflow) | D2 |
| `challenge-unrecorded` | a challenge or concession made in text but absent from `challenges[]`/`concessions[]` | — (workflow) | — |
| `concession-without-referent` | a concession answering a claim nobody made | §5 | — |
| `dropped-thread` | a consequential point abandoned without result or open question | — (workflow) | — |
| `agreement-without-engagement` | restating instead of testing a colleague | §5 | — |
| `thinker-missed` | a stall signal fired and no method was consulted or declined | — (workflow) | T1–T4 |
| `scorecard-missing` | round one skipped a scorecard line | — (workflow) | D3 |
| `divergence-unscanned` | round one's workpaper has no paired-line divergence scan, or items without an owner | — (workflow) | D4 |
| `percent-without-base` | a growth rate spoken for a small line or a mismatched pair without its absolute change | §4 | — |
| `statement-blind-spot` | a top-five balance-sheet or cash-flow excess move in the scan that no turn asked about | — (workflow) | — |
| `source-not-opened` | a role card quoted without reading the `source-files/` passage | §8 | — |
| `knowledge-overreach` | a knowledge candidate that embeds inference in a fact | — (workflow) | C2 |

## Pattern tags (worth spreading)

The meaning is written as the rule the playbook will carry; the observer's note supplies the example.

| tag | meaning |
|---|---|
| `scorecard-first` | Open round one with the business verdict off the full ten-year record, before any recent event. |
| `challenge-changed-number` | Challenge the figure a colleague underwrites, not the narrative; when the challenge lands, switch figures and record who conceded. |
| `disagreement-narrowed` | Narrow a real disagreement to the missing fact and name the document or series that settles it; do not paper over it. |
| `peak-earnings-normalized` | Refuse a trailing multiple for a cyclical or a windfall margin; bracket a normal band and test the low end against the hurdle. |
| `hypothesis-names-verifier` | State a hypothesis together with the document or series that would settle it and when it can be checked. |
| `cross-expert-cover` | When a colleague skips a step from their own card, do it and say whose step it was. |
| `point-to-point-honesty` | Label a price or series move as two points, not a path, when the daily series is not in the data. |
| `base-rate-labelled` | Use a prior from a card as a prior, say so, and name the local evidence that would move it. |
| `reconciliation-derivation` | Reconcile two sources or two experts' numbers with a bridge that closes before reading either. |
| `thinker-applied` | When a stall signal fires, apply one named Thinker method and bring back a verifiable next step. |
| `operating-financing-separated` | Take financial assets, debt and their income out of operations before any return or valuation. |
| `source-passage-applied` | Read the source passage in the turn and apply its test to this company, labelling the result plausible or proven. |
| `divergence-routed` | Ask about two lines that should move together and did not, with the gap in both percent and 亿, and put it to the colleague whose lens owns the pair. |

## Log line format

Inside the observer note, a fenced block:

~~~
```jsonl
{"kind": "weakness", "severity": "high", "expert": null, "tag": "units", "ref": "t1-t14", "note": "every spoken amount said billion for 亿"}
{"kind": "weakness", "severity": "low", "expert": "stephen-penman", "tag": "window-conflation", "ref": "t2", "note": "'about half' mixes the decade and 2021–25"}
{"kind": "pattern", "expert": "joel-greenblatt", "tag": "peak-earnings-normalized", "ref": "t3,t8", "note": "Refuse the trailing EBIT/EV of a cyclical; bracket a normal-year band and test that the low end clears the hurdle."}
{"kind": "drop", "candidate": 3, "note": "fact embeds the alumina hypothesis"}
```
~~~

`kind` is `weakness`, `pattern`, `drop` (a knowledge candidate to withhold, 1-based index) or `verify`
(a candidate whose every figure the evidence audit reproduced; counts as verified for `improve.py`).
`severity` is `high|medium|low` for weaknesses. `expert` is a slug or `null` for a shared workflow
problem. `ref` cites turns as `tN`. A pattern `note` describes the instance in one sentence; the playbook
entry is the tag's rule (the meaning column) followed by that instance as its example.
