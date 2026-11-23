# Session storage schema

```
sessions/
  index.json                         built by scripts/build_index.py — the site reads this
  <ts_code>/                         e.g. 600519.SH
    <session_id>/                    e.g. 2026-11-23-01  (date + sequence)
      session.json                   metadata (below)
      data/factsheet.md              evidence sheet from data/fetch.py (S1 + S2, cross-checked)
      data/factsheet.json
      data/avl_raw.json
      data/workpaper-round-01.md     SQL, series and bridges behind round 1 (not shown in the chat view)
      rounds/round-01.json           one file per round (schema below)
      rounds/round-01.md             rendered by scripts/render_round.py — never hand-edit
      observer/round-01.md           Observer notes on that round
      summary.md                     written when the session closes
```

## session.json

```json
{
  "session_id": "2026-11-23-01",
  "company": {"ts_code": "600519.SH", "name": "贵州茅台", "industry": "白酒"},
  "started_at": "2026-11-23T10:00:00+08:00",
  "status": "open | closed",
  "user_request": "the user's original request, verbatim",
  "experts": ["stephen-penman", "warren-buffett", "michael-mauboussin"],
  "expert_versions": {"stephen-penman": "1.0", "warren-buffett": "1.0", "michael-mauboussin": "1.0"},
  "expert_selection_reason": {
    "stephen-penman": "accounting and implied expectations",
    "warren-buffett": "durability of pricing power",
    "michael-mauboussin": "comparability of returns on invested capital"
  },
  "data": {"avl_version": "20261121_201610", "duckdb_last_end": "20251231", "factsheet_generated_at": "..."},
  "question_queue": ["candidate questions not yet taken up"],
  "run_purpose": "optional: why this run exists, e.g. a re-run to test workflow changes",
  "run_notes": ["optional: what this run showed about the system, not about the company"],
  "rounds": 1
}
```

## rounds/round-NN.json

One round follows one question. Write turns in spoken order. Each number a speaker reports needs
an entry in that turn's `evidence`, with a source and, for a calculation, the formula and inputs.
Keep the spoken text focused on what those facts imply: conversational, under about 110 words per turn, at most two evidence items, with the working in `data/workpaper-round-NN.md`. A question or reply introducing no new
figures can carry an empty evidence list. Earlier rounds use `opening`, `rebuttal` and `closing`
as phase labels. Readers render all turns in array order.

```json
{
  "round": 1,
  "session_id": "2026-11-23-01",
  "ts_code": "600519.SH",
  "started_at": "...", "ended_at": "...",
  "question": "The single question this round examines.",
  "why_this_question": "One or two sentences: why it matters now and what prior round raised it.",
  "participants": ["stephen-penman", "warren-buffett"],
  "statements": [
    {
      "expert": "stephen-penman",
      "phase": "discussion",
      "timestamp": "...",
      "text": "The statement, in the expert's voice. Markdown allowed.",
      "evidence": [
        {"claim": "RNOA fell from 183% to 123% between FY2023 and FY2025",
         "source": "S2 ratios_annual basis=average", "values": {"2023": 1.83, "2025": 1.228}}
      ],
      "challenges": [{"to": "warren-buffett", "point": "..."}],
      "concessions": [{"to": "warren-buffett", "point": "..."}],
      "confidence": "high | medium | low",
      "thinker_used": null
    }
  ],
  "disagreements": [
    {"topic": "...", "positions": {"stephen-penman": "...", "warren-buffett": "..."},
     "status": "open | resolved | narrowed", "resolution": "..."}
  ],
  "conclusion": {
    "answer": "The panel's answer to the round question, with the confidence stated.",
    "confidence": "high | medium | low",
    "what_would_change_our_mind": ["..."],
    "open_questions": ["..."]
  },
  "next_question_candidates": ["..."],
  "thinkers_consulted": [{"thinker": "richard-hamming", "method": "...", "used_for": "..."}],
  "knowledge_candidates": [
    {"kind": "fact | method | hypothesis", "text": "...", "source": "...", "confidence": "high | medium | low"}
  ]
}
```

### Source labels
- `S1 <block>` — AshareValueLine (e.g. `S1 annual.归母净利润`, `S1 main_business.P`)
- `S2 <table>` — bme.duckdb (e.g. `S2 ratios_annual basis=average`, `S2 reformulated_bs`)
- `AR <year> <section>` — the company's annual report (年度报告), when an expert reads it directly
- `SRC <file> <locator>` — a passage read from `source-files/` in that turn (section, letter year, page or heading)
- `KB <id>` — an entry in `knowledge/`
- `derived: <formula>` — computed from the above; state the formula

Phrase judgments and hypotheses as the speaker's interpretation. Give verifiable claims a
corresponding source in the same turn's evidence notes.
