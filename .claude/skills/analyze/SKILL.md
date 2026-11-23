---
name: analyze
description: Start or continue a multi-expert analysis session on a Chinese A-share company (one question per round). Usage: /analyze 600519 | /analyze 美的集团 | /analyze 600519 --rounds 2 | /analyze continue
---

Follow `CLAUDE.md` sections 0–5 exactly. Arguments: `$ARGUMENTS`.

- A code or name starts a new session: resolve → `data/fetch.py <code> --out sessions/<ts_code>/<session_id>/data`
  → read the cross-check block → choose experts (Penman always) → write `session.json`.
- `continue` picks the most recent open session for the company named (or the only open session) and
  runs the next round on the top-ranked `next_question_candidates` item.
- `--rounds N` runs N rounds without pausing, otherwise stop after one round and report.

Per round: one question → parallel opening statements (one subagent per expert, each with its full role
file, the fact sheet, knowledge entries and prior rounds) → parallel rebuttals → orchestrator closing
(disagreements, conclusion with the *lowest* dependent confidence, next questions, knowledge candidates)
→ write `rounds/round-NN.json` → `python3 scripts/render_round.py` → Observer subagent → `scripts/sync.sh`.

Report to the user: the question, the conclusion and its confidence, open disagreements, the Observer's
verdict in one line, the next question, and the live URL
`https://chenjing002.github.io/top-analysts/#/<ts_code>/<session_id>`.
