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
      observer/round-01.md           Observer notes on that round, with a ```jsonl log block (observer/TAGS.md)
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

One round starts from one opening topic — raised by whichever expert saw it — and the discussion
may evolve from there; `question` records where it started, `where_it_went` records where it led.
Write turns in spoken order. Each number a speaker reports needs an entry in that turn's
`evidence`, with a source and, for a calculation, the formula and inputs. Keep the spoken text
conversational and in plain language, with the working in `data/workpaper-round-NN.md`; turn
length follows the content. A question or reply introducing no new figures can carry an empty
evidence list. Earlier rounds use `opening`, `rebuttal` and `closing` as phase labels. Readers
render all turns in array order.

```json
{
  "round": 1,
  "session_id": "2026-11-23-01",
  "ts_code": "600519.SH",
  "started_at": "...", "ended_at": "...",
  "question": "The opening topic, as the initiating expert put it.",
  "initiated_by": "stephen-penman",
  "why_this_question": "One or two sentences: why it matters now and what raised it — a prior round, or something in the 10-year record.",
  "where_it_went": "Optional: one or two sentences on how the discussion moved beyond the opening topic.",
  "participants": ["stephen-penman", "warren-buffett"],
  "statements": [
    {
      "expert": "stephen-penman",
      "phase": "discussion",
      "timestamp": "...",
      "text": "The statement, in the expert's voice. Markdown allowed.",
      "evidence": [
        {"claim": "RNOA fell from 183% to 123% between FY2023 and FY2025",
         "source": "S2 ratios_annual basis=average", "values": {"2023": 1.83, "2025": 1.228}},
        {"claim": "Implied growth 1.1% at r = 8% on normalized E = 55",
         "source": "derived: scripts/calc.py implied_growth_re",
         "formula": "r - (E - r*B)/(P - B)", "inputs": {"P": 728.62, "B": 420.9, "E": 55, "r": 0.08},
         "result": 0.0107},
        {"claim": "Alumina spot price fell about 40% in 2025",
         "source": "hypothesis (labelled in text)", "unverifiable": "no local commodity price series"}
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
  "thinkers_consulted": [
    {"thinker": "richard-hamming", "method": "2.5", "used_for": "..."},
    {"thinker": null, "declined_because": "the open disagreement needs a document, not a method"}
  ],
  "knowledge_candidates": [
    {"kind": "fact | method | hypothesis", "text": "...", "source": "...", "confidence": "high | medium | low"}
  ]
}
```

### Evidence fields and the gate

`scripts/check_round.py` reads every round (see `skills/analyze/CHECKLIST.md`). It verifies
`values` (or the figures in `claim`) against the session's local data for `S1`/`S2` sources,
recomputes `derived:` items from `formula` + `inputs` against `result`, and requires every 亿, %,
× or 元 figure spoken in `text` to have an evidence item in the same turn (or an earlier turn of
the round when quoting a colleague). Fields:

- `values` — the figures as numbers, keyed by anything readable; in 亿 for amounts, decimals for rates.
- `formula`, `inputs`, `result` — for `derived:` sources; the formula is plain arithmetic over the
  input names (`+ - * / ** ( )`, `sum`, `min`, `max`, `abs`), preferably the one in `scripts/calc.py`.
- `unverifiable` — a short reason when the figure cannot be checked locally (an estimate, outside
  data, a document not in the data layer). It must also be labelled in the spoken text.

`thinkers_consulted` carries each method used, or a `declined_because` entry when a stall signal
(open disagreement, unexplained S1/S2 mismatch, a conclusion repeating the previous round,
single-quarter evidence at high confidence) fired and the panel chose not to consult a method.

### Source labels
- `S1 <block>` — AshareValueLine (e.g. `S1 annual.归母净利润`, `S1 main_business.P`)
- `S2 <table>` — bme.duckdb (e.g. `S2 ratios_annual basis=average`, `S2 reformulated_bs`)
- `AR <year> <section>` — the company's annual report (年度报告), when an expert reads it directly
- `SRC <file> <locator>` — a passage read from `source-files/` in that turn (section, letter year, page or heading)
- `KB <id>` — an entry in `knowledge/`
- `derived: <formula>` — computed from the above; state the formula

Phrase judgments and hypotheses as the speaker's interpretation. Give verifiable claims a
corresponding source in the same turn's evidence notes.
