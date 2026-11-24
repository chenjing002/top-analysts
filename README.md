# Top Analysts — multi-expert equity research on Chinese listed companies

A minimal multi-agent research system. Eight investment experts, distilled from their own writings,
examine one A-share company **grounded in its 10-year financial record**. Any expert can open a
round with whatever the record made them notice; the discussion evolves from there: they state
positions with sourced evidence, challenge each other, record disagreements, and reach a
conclusion with an honest confidence level.
An independent Observer reviews each round and proposes validated improvements to the expert role
files. Verified findings go to a shared, provenance-tagged knowledge base. Published rounds appear in
the [discussion archive](https://chenjing002.github.io/top-analysts/).

## The experts

| file | distilled from | contributes |
|---|---|---|
| `experts/stephen-penman.md` | Penman, *What Matters in Company Valuation* (2002) + Penman & Pope book site | reformulated statements, RNOA, residual income, reverse-engineering the price. **Always on the panel.** |
| `experts/warren-buffett.md` | Berkshire letters 1986 & 1994; *The Security I Like Best* (1951–57) | owner earnings, economics vs accounting, moat and capital allocation, insurance float |
| `experts/michael-mauboussin.md` | Mauboussin & Callahan, *ROIC* (2022) | NOPAT / invested capital reconciliation, goodwill & intangibles, ROIC–growth–value |
| `experts/jeff-bezos.md` | Amazon 2004 (and 1997) shareholder letters | free cash flow per share, the growth-destroys-cash machine example, operating cycle |
| `experts/rockwood.md` | *Media Accounting* (Rockwood Notes, 2025) + Netflix IR content-accounting deck | capitalized-and-amortized assets: cash spend vs amortization, restating operating cash flow |
| `experts/joel-greenblatt.md` | Columbia value-investing lectures (csinvesting.org) | EBIT/EV and EBIT/tangible capital, normalizing earnings, retail unit economics, how to grill a thesis |
| `experts/li-lu.md` | CBS lecture notes; Timberland case (中文) | fear-by-fear verification, governance and controller analysis, cheap-for-a-reason vs misunderstanding |
| `experts/joekray-mond.md` | 22 historical micro-cap / OTC case studies | setup taxonomy of extraordinary outcomes, at-purchase snapshots, base rates and survivorship |

`Thinkers/` (Hamming, Tukey) are not experts. They supply reasoning methods, used only when analysis
stalls, and always labelled "reasoning method, not evidence".

## Data

Two primary sources, always cross-checked (`data/fetch.py`):

- **S1** [AshareValueLine](https://chenjing002.github.io/AshareValueLine/) — 10-year annual indicators,
  quarterly revenue, full balance sheet, business segments, current quote. Amounts in 亿元.
- **S2** `bme.duckdb` — Tushare raw statements 2008–2025 plus Penman-style reformulation, ratios,
  working capital, cash reconciliation, residual income and valuation reverse-engineering for ~5,500
  companies. Amounts in yuan. Definitions in `data/DATA_DICTIONARY.md`.

The fact sheet lists every figure with its source. A mismatch > 1% between sources is resolved or
explained in the round-one workpaper before the panel speaks; an unexplained one opens the round.

## Running an analysis

Open this repository and ask `analyze 600519` or `分析 美的集团`. The shared entry point is
[`AGENTS.md`](AGENTS.md). The [Analyze skill](skills/analyze/SKILL.md) runs the panel, and the
[Observe skill](skills/observe/SKILL.md) audits a round or reviews a proposed expert edit.

| Where you work | How to use it |
|---|---|
| Codex | Open this repository as the workspace. Use `$analyze` or `$observe`, or ask in plain language. Codex discovers both skills through `.agents/skills/`. |
| Claude Code | Open this repository and use `/analyze` or `/observe`. `CLAUDE.md` imports `AGENTS.md`, and `.claude/skills/` exposes the shared skills. |
| ChatGPT or another agent | Ask it to read `AGENTS.md` and the relevant file in `skills/`. If the chat has no workspace access, attach those files, the relevant expert cards, and the fact sheet. For a round audit, include `observer/OBSERVER.md` and the round JSON. A GitHub-connected chat can retrieve the files once they are pushed to a repository it can access. |

Both native skill directories link to `skills/`. Edit the visible files there to update both tools.
If your checkout does not resolve symlinks, open the visible files directly. Live fetch and SQL
require the local data setup below. A chat can work from a supplied fact sheet.

Manual steps:

```bash
# fact sheet only
/Users/lin/Desktop/business-model-explorer/.venv/bin/python data/fetch.py 600519

# publish an authorized round (stages all changes, commits, and pushes main)
scripts/sync.sh "600519.SH 2026-11-23-01 round 1: <question>"

# validation only
python3 scripts/validate.py
```

## Self-improvement, controlled

The system learns one round at a time, through a loop of deterministic scripts and one independent
judgment:

1. **Gate.** `scripts/check_round.py` reads the round JSON against the session's local data: every
   figure with an S1/S2 source must exist there, every `derived:` figure must recompute from its
   formula and inputs (the formulas live in `scripts/calc.py`, with doctests), every figure spoken in
   a turn must have an evidence item, amounts are in 亿, and `high` confidence cannot rest on a model
   default. Rules are listed in [`skills/analyze/CHECKLIST.md`](skills/analyze/CHECKLIST.md). Errors
   block `scripts/sync.sh`.
2. **Observe.** The Observer reviews the round and tags each weakness and each pattern worth keeping
   with the vocabulary in [`observer/TAGS.md`](observer/TAGS.md), in a `## Log` block.
3. **Ingest.** `scripts/improve.py ingest` files the tags in `observer/log.jsonl`, three numbers per
   round in `observer/metrics.jsonl`, and the surviving knowledge candidates in `knowledge/` (an
   unverified fact enters as a hypothesis). A pattern or a shared pitfall seen in two rounds becomes a
   rule in [`knowledge/playbook.md`](knowledge/playbook.md), which every expert reads at session start.
4. **Propose.** `scripts/improve.py proposals` drafts a card change when the same weakness tag recurs
   on the same expert in two rounds, with the evidence filled from the log. The orchestrator writes the
   change, a fresh reviewer that has not read the discussion runs the four checks in
   [`observer/OBSERVER.md`](observer/OBSERVER.md#3-proposals-to-change-an-expert-file), and a
   validated change is applied with a version bump and changelog line — one change per expert per
   session, auditable in `git log`. Cards stay source-based; cross-expert lessons live in the playbook.
5. **Measure.** `scripts/improve.py report` shows the trend (check errors, weaknesses by severity,
   knowledge cited) and the recurring tags, so the next round starts knowing what to avoid.

Knowledge is admitted by `knowledge/README.md` rules: one line, one claim, with id, date, confidence,
and source. Hypotheses live apart from facts and can never be `high` confidence.

## Site

`site/` is a dependency-free static viewer (one HTML, one CSS, one JS; markdown rendered client-side).
`.github/workflows/pages.yml` copies `site/`, `sessions/`, `experts/`, `knowledge/`, `Thinkers/` and
`observer/` into the Pages artifact on every push to `main`. Search covers company, code, question,
expert, conclusion and (when fewer than 400 rounds) full statement text.

Not investment advice. The archive is a record of a research *process*.
