---
name: analyze
description: Start, continue, or close a multi-expert research session on a Chinese A-share company. Use when asked to analyze a company or run another round of an existing panel.
---

# Analyze an A-share company

Read `AGENTS.md` for the shared evidence rules and `sessions/SCHEMA.md` for the output format.
Use the user's company name or code, round count, or session reference. Examples include
`analyze 600519`, `分析 美的集团`, `analyze 600519 --rounds 2`, and `analyze continue`.

## 1. Prepare the session

- For a new session, run `data/fetch.py <code|name>` to resolve the ticker through DuckDB's
  `raw_stock_basic`. The default output is `data/cache/<ts_code>/`. Use a new `YYYY-MM-DD-NN`
  session ID and put the fetched artifacts in `sessions/<ts_code>/<session_id>/data/`. You can
  use `--out` directly when the full ticker and session ID are known.
- On the original workstation, run the fetcher and read-only DuckDB queries with
  `/Users/lin/Desktop/business-model-explorer/.venv/bin/python`. The fetcher uses the local
  `bme.duckdb` listed in `data/DATA_DICTIONARY.md` and needs network access for AshareValueLine.
  Use `python3` for rendering, indexing, and validation.
- **Data scope.** Work from the local data layer: S1 (`avl_raw.json`), the fact sheet, and S2
  `bme.duckdb`. The `raw_income`, `raw_balancesheet` and `raw_cashflow` tables hold quarterly
  filings (cumulative within a year, `report_type='1'`) up to the latest filed quarter, which can be
  later than the annual `duckdb_last_end`; check `SELECT DISTINCT end_date` first. Do not search the
  web or download filings unless the user asks. A gap that only outside material can fill goes to
  `open_questions` with the document that would close it. Say so when a quarterly figure is not in
  the local tables.
- When live data is unavailable, use a supplied or existing fact sheet for the same ticker and state
  its as-of date and any missing checks. If no usable sheet exists, ask for the sheet or the data
  needed for the question. An empty cross-check with one source unavailable is an unperformed check.
- Read the cross-check first. Any comparable S1/S2 mismatch over 1% takes priority as the first
  panel question. Banks, insurers, and brokers (`comp_type` 2/3/4/7) have raw S2 statements only.
  Disclose that coverage and use S1 plus raw statements with sector-appropriate measures.
- Read company facts and hypotheses in `knowledge/` if present. Write `session.json` with the
  user's request verbatim, selected expert slugs and versions, and a one-line reason for each pick.
- For `continue`, choose the most recent open session for the named company or the only open session.
  Resolve ambiguity when several companies have open sessions and none was named. Read the session
  and prior rounds. For an open session with zero rounds, use the first-round question rules.

## 2. Choose the panel

Choose three experts, with a fourth when the question requires one. Always include `stephen-penman`
for accounting, residual income, and implied expectations. Pick the others by the evidence gap.

| Signal in the fact sheet or question | Expert |
|---|---|
| Pricing power, durability of returns, maintenance capital, insurance float | `warren-buffett` |
| Goodwill, acquisitions, excess cash, leases or R&D complicate comparable ROIC | `michael-mauboussin` |
| Cash trails earnings, working capital expands, capex rises or shares dilute | `jeff-bezos` |
| Capitalized content, software, development costs or other judgmentally amortized assets | `rockwood` |
| Normalized EBIT/EV, retail unit economics, cyclicality or special situations | `joel-greenblatt` |
| Governance, related parties, an untested bear case or a need for primary verification | `li-lu` |
| Micro-cap discounts, hidden assets, controlling holders or historical analogues | `joekray-mond` |

Add an expert mid-session only when `open_questions` names a gap that only that role covers. Record
the reason and the role version.

## 3. Run one round

1. **Set the question.** In round one, resolve the cross-check mismatch if present. Otherwise pick the
   single question whose answer most affects the valuation. For later rounds, use the top-ranked
   `next_question_candidates` item unless the user redirects.
2. **Work up the series first.** Before the discussion, build the multi-year and single-quarter
   series the question depends on from S1/S2 (de-cumulate quarters, bridge balance-sheet and equity
   movements, split growth into price, volume and mix where the data allow, and reconcile S1 to S2).
   Put the SQL and formulas in the turn evidence. Treat a bridge that does not close as a finding.
   Check that earlier rounds' derived figures use comparable share counts and definitions, and
   correct them in the round when they do not.
3. **Start with one live point.** Give the panel the round question, fact sheet, data dictionary,
   relevant company knowledge and prior rounds. Each speaker has their full role card. When the
   host supports and authorizes delegation, keep a separate context for each expert. Ask the expert
   who noticed a consequential puzzle to put it to the others in a few sentences. A question or
   tentative explanation is enough to begin. Leave subsequent topics, speakers and the outcome open.
4. **Follow the exchange one turn at a time.** Share the conversation so far, including the latest
   turn, before generating the next contribution. Follow the specific inference someone can test.
   Any panelist can enter, return, or sit a point out. Give the person whose premise was challenged
   room to answer. Draw on the part of their card that changes how they read this particular fact.
   For instance, two experts may accept the same number and disagree about what caused it. Let
   them work out which observation would distinguish their explanations and check it if the data
   are available. A speaker may introduce a hypothesis the brief or role card never mentions.
   Keep it provisional until a test distinguishes it from the alternatives. A question, concession
   or reason for holding a view can each stand as a whole turn. Move on when a point has a result
   or further progress depends on a named missing fact. Carry that result into the round question.

   **Disclose sources progressively.** Speakers begin from the role card and the data. When an
   inference turns on a specific method, definition or example (for instance Buffett's owner-earnings
   test, Penman's NOA/NFO split, Li Lu's bear-case procedure, Bezos's float and free-cash-flow-per-share
   argument), the speaker opens the matching file under `source-files/<expert folder>/` listed in the
   card's source basis, searches for the passage, reads the section, and says in the turn what it
   changed in the reading of this company. Retrieve only what the current point needs. Cite it in
   `evidence[]` as `SRC <file> <section or locator>`. Quote wording only when the passage was read in
   this turn; otherwise paraphrase and mark it as from the role card. If the source does not support
   the move, say so and downgrade the claim. Each turn should end with something testable against the
   data: a prediction, a ratio, or the series that would separate two explanations. The next speaker
   runs that test, or states why it cannot be run locally.

   Append each turn to `statements[]` in spoken order with `phase: "discussion"`. Write natural
   English and keep the figures, dates and accounting distinctions the reader needs to follow the
   inference. Put source locators, calculation inputs, formulas and any query SQL in the turn's
   `evidence[]`. A question can have empty evidence. Identify assumptions in the spoken text.
   If reasoning stalls despite usable evidence, consult a method in `Thinkers/README.md`, attach
   its required label in the turn record, and return to verification.
5. **Close the round.** If the conclusion relies on an objection raised in the last turn, give
   the affected speaker a chance to address it or record how the unresolved point limits the answer.
   Record disagreements as open, narrowed, or resolved, with the evidence that
   shifted them. Write the conclusion, what would change it, open questions, ranked next questions,
   Thinkers consulted, and knowledge candidates. Use the lowest confidence of the evidence the
   conclusion depends on. High confidence requires a direct statement line or two independent
   sources. A finding that depends on an S2 default (r = 8%, g = 3%, or tax = 25%) is at most medium.
6. **Save and review.** Write `rounds/round-NN.json`, run `python3 scripts/render_round.py <file>`,
   and update the session's `rounds` and `question_queue`. Run the `skills/observe/SKILL.md` round
   review with the exact round inputs, read its verdict before the next round, and drop any
   `knowledge_candidates` the review flags as unsupported. Run `python3 scripts/validate.py`.

If delegation is unavailable, work through the roles individually and label them as simulated
perspectives. Record how the review was conducted. If the host lacks a writable checkout, return
the findings and review in the chat and identify any artifact steps that could not run.

## 4. Publish, report, and continue

- For an authorized publication, check that the changes to be staged are in scope, then run
  `scripts/sync.sh "<ts_code> <session_id> round NN: <question>"`. This renders, rebuilds the session
  index, validates, commits, and pushes. Use
  `https://chenjing002.github.io/top-analysts/#/<ts_code>/<session_id>` as the live link after
  deployment is confirmed.
- Report the question, conclusion and confidence, open disagreements, review verdict, and next
  question. Stop after one round unless the user requested more. `--rounds N` requests N rounds.
- When the user closes a session, write `summary.md` with each round's result, remaining verification,
  and any skipped steps. Capture supported knowledge using `knowledge/README.md`, set the session
  status to `closed`, and publish the closing changes if authorized. If proposals are pending at
  close, review them through the Observe workflow.
