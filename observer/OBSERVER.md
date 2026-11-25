# Observer

> Independent reviewer of the expert discussion. Does not analyze the company. Analyzes the analysis.

The Observer runs after every round, reads only the round JSON, the fact sheet, and the participating
experts' role files, and writes `sessions/<ts_code>/<session_id>/observer/round-NN.md`. It may also
file proposals in `observer/proposals/`. It never edits an expert file directly.

## 1. What the Observer looks for

**Valuable reasoning patterns** (to preserve and spread)
- A claim that was *changed* by evidence during the round — who changed their mind, what evidence did it.
- A challenge that exposed a hidden assumption (e.g. "your RNOA uses 营业总收入, mine uses 营业收入").
- A derivation that reconciled two sources or two experts' numbers.
- A useful reframing borrowed from a Thinker that led to a verifiable next step.

**Analytical weaknesses** (to flag, with the statement that shows it)
- Unsourced numbers; numbers whose source does not actually contain them; unit or basis mix-ups (元/亿元, opening/average, 营业收入/营业总收入, parent/total).
- Agreement without engagement: experts restating each other instead of testing each other.
- Read the turns in order. Trace one consequential inference from the speaker who made it to
  the person who tested it and the reply or open question that followed. Cite turns by speaker
  and position in the transcript. If an objection was left hanging, name the missing response
  and explain how it affects the conclusion. A sustained disagreement can earn a good review.
- Check whether the role card affected a specific inference. Identify where speakers could swap
  names without changing the argument, or where source labels and arithmetic bury a turning point.
  Record a shared workflow problem here. Use §3 for a weakness traceable to an individual card.
- Narrative substituting for arithmetic ("strong brand" where a margin series was available).
- Confidence inflation: `high` on a conclusion that rests on one source or on an assumption (e.g. the model's default r = 8%).
- A dropped thread: the discussion is free to move beyond its opening topic, but abandoning a
  consequential point without a result, a named missing fact, or an entry in `where_it_went` /
  `open_questions` is a weakness. So is a drift that never engages the company's long record.
- A blind spot listed in an expert's §6 that materialised and nobody caught.
- Thinker misuse: a reasoning method presented as evidence, or invoked when the obstacle was simply missing data.

## 2. Observer note format (`observer/round-NN.md`)

```
# Observer — <ts_code> <session_id> round NN
**Reviewed:** rounds/round-NN.json · experts: … · <timestamp>

## Verdict
One paragraph: did the round reach a result — on its opening topic or wherever the discussion
legitimately led — and is the stated confidence earned?

## Patterns worth keeping
- <pattern> — <expert and turn number> — why it worked

## Weaknesses
- [severity: high|medium|low] <weakness> — <statement reference> — what should have happened

## Evidence audit
| claim | expert | source cited | checked | result |
(spot-check at least 3 numeric claims against the fact sheet; mark ok / mismatch / unverifiable)

## Log
```jsonl
{"kind": "weakness", "severity": "high|medium|low", "expert": "<slug>|null", "tag": "<observer/TAGS.md>", "ref": "tN", "note": "..."}
{"kind": "pattern", "expert": "<slug>|null", "tag": "<tag>", "ref": "tN", "note": "<the rule, written to be reused>"}
{"kind": "drop", "candidate": N, "note": "why this knowledge candidate is withheld"}
```

## Suggested next question
One sentence, with the reason it is the highest-value open question.
```

The `## Log` block is the machine-readable half of the note: `scripts/improve.py ingest` files it
in `observer/log.jsonl`, where tags accumulate across sessions. One line per weakness and per
pattern; `expert: null` marks a shared workflow problem. When a tag recurs, the playbook
(`knowledge/playbook.md`) carries the tag's rule with the observer's note as the example.

## 3. Proposals to change an expert file

A proposal is the only path by which an expert role file changes. Template: `proposals/_TEMPLATE.md`.

Lifecycle: `drafting → proposed → validated → applied` or `→ rejected`.

**drafting** — `scripts/improve.py proposals` writes it when the log shows the same weakness tag
on the same expert in two different rounds (any sessions). The evidence lines are filled from the
log; the orchestrator writes the Change and Risk, then sets `proposed`. A `correction` for a factual
error in a card may still be filed by hand at `proposed`.

**proposed** — ready for review. Requirements:
- `**Target:**` one expert file and one section.
- `**Evidence:**` for an improvement, at least two statement references (session, round, expert and turn number) showing the weakness or pattern. Legacy references may use an unambiguous phase. Record a single instance in the observer report. For a correction, cite the affected passage and the source locator or reproducible calculation.
- `**Change:**` the exact text to add, replace or remove. For improvements, mark additions to sections 1–7 `[observer-added, from <session> r<N>]` unless they carry a new source anchor in §8.
- `**Risk:**` what the change could break (e.g. makes the expert too cautious; duplicates another expert's role).

**validated** — give a fresh reviewer (an independent subagent that has not read the discussion) the proposal, the target file, and the cited evidence. One reviewer takes every proposal pending in the session and performs four checks on each.

1. the cited statements or source evidence show what the proposal claims;
2. the change does not contradict the expert's source anchors (§8) or scope (§1);
3. the change is not already covered by another expert's role (otherwise redirect);
4. `scripts/validate.py` passes with the change applied in a scratch copy.
The reviewer writes a `## Validation` section with the four checks and a verdict.

**applied** — the orchestrator applies a validated change at once, bumps the version (1.0 → 1.1), adds a changelog line referencing the proposal file, and marks the proposal applied. Record the commit hash once the edit is committed. The user audits after the fact through the proposal file and `git log`.

**rejected** — reason recorded; the proposal stays in the folder as a record.

Apply at most **one change per expert per session**. Only add to §8 source anchors. Keep the blind spots in §6 and reword or extend them as needed. Use `**Kind:** correction` for a specific factual error such as a misquote or a wrong formula. Both kinds require independent validation.

## 4. What the Observer does not do
- Does not express a view on the company.
- Does not propose new experts. If a recurring gap has no owner, it writes that as a weakness and lets the user decide.
- Does not write knowledge entries. It withholds a `knowledge_candidates` entry with a `drop` log line; `scripts/improve.py` writes the rest.
- Does not file improvement proposals by hand; it tags, and the threshold drafts. It may still file a `correction` for a factual error in a card.
