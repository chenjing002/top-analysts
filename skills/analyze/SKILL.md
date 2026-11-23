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
- Read the cross-check first. Resolve or explain any comparable S1/S2 mismatch over 1% that touches
  a series the story rests on, in the round-one workpaper, before the panel speaks. If it cannot be
  explained from the data, it becomes the opening topic, because an unexplained mismatch taints every
  series built on it. A mismatch in a series nobody will use is a one-line note, not a topic.
  Banks, insurers, and brokers (`comp_type` 2/3/4/7) have raw S2 statements only.
  Disclose that coverage and use S1 plus raw statements with sector-appropriate measures.
- Read company facts and hypotheses in `knowledge/` if present. When the run repeats a company
  after changes to the workflow or role cards, start a fresh session ID and delete the superseded
  session only when the user asks. The goal of such a run is to test the system, so record
  `run_purpose` and the git revision of the workflow files in `session.json`, and compare the new
  rounds with the old on the dimensions the user named. Write `session.json` with the
  user's request verbatim, selected expert slugs and versions, and a one-line reason for each pick.
- For `continue`, choose the most recent open session for the named company or the only open session.
  Resolve ambiguity when several companies have open sessions and none was named. Read the session
  and prior rounds. For an open session with zero rounds, use the first-round question rules.

## 2. Choose the panel

Choose three to five experts. Always include `stephen-penman` for accounting, residual income, and
implied expectations. Pick the others by what the 10-year record shows — the series that moved,
broke trend, or diverged from each other are the signals.

| Signal in the 10-year record or question | Expert |
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

1. **Read the big picture first, then go deep only where it pays.** For a new session, before
   anyone speaks, write a one-page decade read at the top of `data/workpaper-round-01.md`: what kind
   of business this is, what the 10 years show (growth, margins, returns on capital, cash conversion,
   capex against depreciation, share count, capital allocation), where the story bends or breaks
   trend, and the few headline numbers (about five) that carry that story. This record, not the
   latest quarter, is what the panel reads. Below it, keep the supporting series and calculations as
   a reference appendix. Compute more only when a live question needs it: de-cumulate quarters,
   bridge balance-sheet or equity movements, split growth into price, volume and mix, reconcile S1
   to S2. Stop a calculation when its answer cannot change the conclusion. A bridge that does not
   close is a finding only if it affects the story; otherwise note it in the appendix. In later
   rounds, extend the workpaper with what the live topic needs and correct earlier derived figures
   that used non-comparable share counts or definitions.
2. **Let an expert open.** Give the panel the fact sheet, the decade workpaper, the data
   dictionary, relevant company knowledge and prior rounds. Each speaker has their full role card.
   When the host supports and authorizes delegation, keep a separate context for each expert.
   Each panelist reads the 10-year record through their own lens; whoever saw the most
   consequential thing opens the round with it — the thing that changes how the business or its
   price should be understood: a puzzle, a break in a long series, an assumption the record
   contradicts, a question to a specific colleague. Prefer a question about what the business is
   and where it is heading over a question about how one figure was computed. A question or tentative explanation
   is enough to begin. In round one the unexplained cross-check mismatch, if any, opens instead.
   In later rounds an expert may pick up a `next_question_candidates` thread, answer a standing
   objection, or open something new the record justifies — unless the user redirects. Record the
   opening topic as the round's `question` and the opener as `initiated_by`. Leave subsequent
   topics, speakers and the outcome open.
3. **Follow the exchange one turn at a time.** Share the conversation so far, including the latest
   turn, before generating the next contribution. Follow the inference that matters most to the investment judgment and that someone can test.
   Keep the group at the level of business and valuation insight. When a dispute is only about
   arithmetic, a definition or a data detail, one speaker states which way it was settled and what
   it does to the conclusion (usually nothing), the detail goes to the workpaper, and the chat moves
   on. Do not spend more than a turn or two on a point that cannot move the conclusion.
   Any panelist can enter, return, or sit a point out. Give the person whose premise was challenged
   room to answer. Draw on the part of their card that changes how they read this particular fact.
   For instance, two experts may accept the same number and disagree about what caused it. Let
   them work out which observation would distinguish their explanations and check it if the data
   are available. A speaker may introduce a hypothesis the brief or role card never mentions.
   Keep it provisional until a test distinguishes it from the alternatives. A question, concession
   or reason for holding a view can each stand as a whole turn. The discussion may move to an
   adjacent topic when the reasoning leads there; follow it, and record the move in
   `where_it_went` rather than forcing the thread back. Move on when a point has a result
   or further progress depends on a named missing fact.

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

   Append each turn to `statements[]` in spoken order with `phase: "discussion"`.

   **Chat register.** The round is read as a group chat, so write each turn as one person talking
   to the others, in clear accessible language: no tables, no formulas, no SQL, no field names and
   no source codes in `text`. Length follows the content — a one-line question and a worked
   argument are both fine turns, but every turn carries one main idea and answers the previous one
   before it adds anything. Lead with the point, then give the one to three numbers that make it
   convincing, rounded and with their period. Name accounting terms in plain words so a reader
   outside finance can follow, without blunting the analysis. Intermediate arithmetic stays in the
   workpaper. The turn's `evidence[]` carries one short item per figure the
   reader may want to check, with a short source label such as `S2 raw_income FY2016–FY2025`.
   A question can have empty evidence. Identify assumptions in the spoken text. Run-level notes on
   how the system performed belong in `session.json` `run_notes`, not in the chat.
   If reasoning stalls despite usable evidence, consult a method in `Thinkers/README.md`, attach
   its required label in the turn record, and return to verification.
4. **Close the round.** If the conclusion relies on an objection raised in the last turn, give
   the affected speaker a chance to address it or record how the unresolved point limits the answer.
   Record disagreements as open, narrowed, or resolved, with the evidence that
   shifted them. Write the conclusion — covering where the discussion actually went, not only the
   opening topic. Start it with the big-picture verdict in two or three plain sentences: what
   the business is, what the decade says, what the price implies, and the insight a reader
   should remember. Then give the handful of numbers that anchor it. Add what would change it, open questions, ranked next questions, Thinkers
   consulted, and knowledge candidates. Use the lowest confidence of the evidence the
   conclusion depends on. High confidence requires a direct statement line or two independent
   sources. A finding that depends on an S2 default (r = 8%, g = 3%, or tax = 25%) is at most medium.
5. **Save and review.** Write `rounds/round-NN.json`, run `python3 scripts/render_round.py <file>`,
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
