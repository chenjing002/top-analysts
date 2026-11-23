# Top Analysts — multi-expert equity research on Chinese listed companies

A minimal multi-agent research system. Eight investment experts, distilled from their own writings,
examine one A-share company **one question per round**: they state positions with sourced evidence,
challenge each other, record disagreements, and reach a conclusion with an honest confidence level.
An independent Observer reviews each round and proposes validated improvements to the expert role
files. Verified findings go to a shared, provenance-tagged knowledge base. Every round is published to
**https://chenjing002.github.io/top-analysts/**.

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

The fact sheet lists every figure with its source. A mismatch > 1% between sources becomes the panel's
first question.

## Running an analysis

Open the repo in Claude Code and ask, e.g. `analyze 600519` or `分析 美的集团`. `CLAUDE.md` is the
orchestrator protocol: resolve company → fetch and cross-check → choose 3–4 experts → one question per
round (opening statements in parallel, rebuttals, moderator conclusion) → Observer → knowledge
candidates → sync to GitHub → Pages redeploys. `/analyze` and `/observe` are shortcuts.

Manual steps:

```bash
# fact sheet only
/Users/lin/Desktop/business-model-explorer/.venv/bin/python data/fetch.py 600519

# re-render, rebuild index, validate, commit, push
scripts/sync.sh "600519.SH 2026-11-23-01 round 1: <question>"

# validation only
python3 scripts/validate.py
```

## Self-improvement, controlled

Expert files change only through `observer/proposals/`: a proposal needs two cited instances, an
independent reviewer fills in the validation checks, and one change per expert per session is applied
with a version bump and changelog line. `scripts/validate.py` enforces structure on every push.

Knowledge is admitted by `knowledge/README.md` rules: one line, one claim, with id, date, confidence,
and source. Hypotheses live apart from facts and can never be `high` confidence.

## Site

`site/` is a dependency-free static viewer (one HTML, one CSS, one JS; markdown rendered client-side).
`.github/workflows/pages.yml` copies `site/`, `sessions/`, `experts/`, `knowledge/`, `Thinkers/` and
`observer/` into the Pages artifact on every push to `main`. Search covers company, code, question,
expert, conclusion and (when fewer than 400 rounds) full statement text.

Not investment advice. The archive is a record of a research *process*.
