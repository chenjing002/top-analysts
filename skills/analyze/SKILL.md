---
name: analyze
description: Start, continue, or close a multi-expert research session on a Chinese A-share company. Use when asked to analyze a company or run another round of an existing panel.
---

# Analyze an A-share company

Read `AGENTS.md` for the shared evidence rules and `sessions/SCHEMA.md` for the output format.
Use the user's company name or code, round count, or session reference. Examples include
`analyze 600519`, `分析 美的集团`, `analyze 600519 --rounds 2`, and `analyze continue`.

## 1. Prepare the session

- For a new session, run `python3 data/fetch.py <code|name>`. It reads the local JSON of the two
  data projects, with no network and no database: S1 is AshareValueLine
  (`/Users/lin/Desktop/AshareValueLine/_site/api/v1/a_share/companies/<ts_code>.json`), S2 is
  business-model-explorer (`/Users/lin/Desktop/business-model-explorer/build/pages/
  business-model-explorer[-data]/api/v1/companies/<ts_code>.json`; SZ companies sit in the `-data`
  site). Names and codes resolve through the BME `companies.json` index. The default output is
  `data/cache/<ts_code>/`. Use a new `YYYY-MM-DD-NN` session ID and put the fetched artifacts in
  `sessions/<ts_code>/<session_id>/data/`. You can use `--out` directly when the full ticker and
  session ID are known. Outputs: `factsheet.md`, `factsheet.json`, and the two raw JSON copies
  `avl_raw.json` (S1) and `bme_raw.json` (S2), both in yuan as published.
- Both folders are build products. The sheet's Sources section states the S1 version and quote date
  and the S2 export time; if either looks stale, say so and rebuild the source project before
  relying on it. `--years 0` returns every S2 year in the JSON (FY2014 onward).
- **Data scope.** Work from the local data layer: S1 (`avl_raw.json`), S2 (`bme_raw.json`) and the
  fact sheet. S2 JSON is annual only. For the latest quarters the sheet carries S1's `period_trend`
  (营业收入 YTD, 存货, 应收账款) and single-quarter revenue. When a live question needs 归母净利润,
  CFO, capex or OI by quarter, the required-return reverse curve, `raw_daily_basic`, or S2 history
  before FY2014, rerun with `--duckdb` using
  `/Users/lin/Desktop/business-model-explorer/.venv/bin/python` (reads `bme.duckdb`, see
  `data/DATA_DICTIONARY.md`) or query `raw_income`, `raw_balancesheet` and `raw_cashflow` directly
  (cumulative within a year, `report_type='1'`; dedupe by `update_flag DESC, f_ann_date DESC,
  _fetched_at DESC`). Do not search the web or download filings unless the user asks. A gap that
  only outside material can fill goes to `open_questions` with the document that would close it.
  Say so when a figure is not in the local data.
- If a source file is missing the fetcher says so and the sheet carries that source as unavailable;
  an empty cross-check with one source unavailable is an unperformed check. Otherwise use a supplied
  or existing fact sheet for the same ticker and state its as-of date and any missing checks. If no
  usable sheet exists, ask for the sheet or the data needed for the question.
- Read the cross-check first. Resolve or explain any comparable S1/S2 mismatch over 1% that touches
  a series the story rests on, in the round-one workpaper, before the panel speaks. If it cannot be
  explained from the data, it becomes the opening topic, because an unexplained mismatch taints every
  series built on it. A mismatch in a series nobody will use is a one-line note, not a topic.
  Banks, insurers, and brokers (`comp_type` 2/3/4/7) have raw S2 statements only.
  Disclose that coverage and use S1 plus raw statements with sector-appropriate measures.
- Read `knowledge/playbook.md`, `knowledge/methods/`, and the company's `knowledge/facts/` and
  `knowledge/hypotheses/` files if present; cite entries as `KB F-…`, `KB M-…`, `P-…`. Run
  `python3 scripts/improve.py report` and show the trend table to the user: it lists recurring
  weaknesses to avoid this round and any proposals waiting (`drafting` ones are yours to fill,
  see §3 step 6). When the run repeats a company
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
implied expectations. In a new session also include `warren-buffett`: round one's first job is his
great, good or gruesome verdict on the business. Pick the others by what the 10-year record shows — the series that moved,
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

1. **Read the business first, then the news.** A new session's round one is a business-overview
   round, not a reaction to the latest quarter. Before anyone speaks, write the **business
   scorecard** at the top of `data/workpaper-round-01.md`: one line per question, each with its
   few anchor numbers over the full 10 years.
   1. **What kind of business?** Great, good or gruesome (`experts/warren-buffett.md` §3 Step 2):
      compare the 10-year rise in operating profit with the rise in capital it needed (fixed assets
      plus working capital), and whether cash was left for owners.
   2. **Does cash back the profit?** Ten-year free cash flow (operating cash flow less capex)
      against net profit, capex against depreciation and amortization (折旧摊销), and the
      cash-conversion ratio. Say what part of capex looks like maintenance and what part looks like
      growth, labelled as an estimate.
   3. **What drives the return?** DuPont: net margin × asset turnover × equity multiplier, 10 years.
      Add Penman's RNOA/OPM/ATO when net operating assets are large enough to read; when the fact
      sheet suppresses RNOA (net operating assets near zero or negative, as with large customer
      advances), say so and rely on the three-factor DuPont plus the operating-margin and
      working-capital lines.
   4. **Is it cheap, and what is the floor?** Market value, book value, price to book, earnings yield
      and free-cash-flow yield at the S1 quote date. Then open the book: how much is cash and
      financial assets, receivables, inventory, fixed assets, goodwill and intangibles, less debt
      and customer advances. Give a rough floor (net cash plus tangible assets, with the haircut
      stated) and say whether it protects the downside. End with what the price assumes
      (the reverse curve).
   5. **What did management do with the cash?** Ten-year payout, buybacks, issuance and share count.
   6. **Where does the story bend or break trend?** The headline numbers (about five) and the
      one-line verdict.
   7. **Which paired lines diverged, and whose question is each?** Read the fact sheet's
      paired-line divergence scan (`calc.growth_gap`): every row pairs a line with the line it
      should follow across all three statements — cost of sales, selling and admin expense and tax
      against revenue or pre-tax profit; receivables, inventory, payables, customer advances,
      other receivables, fixed assets and intangibles against the flow that drives them; cash
      collected, cash paid, CFO, capex, dividends and borrowings against revenue, cost of sales,
      net income, D&A and capex. Take the three to five largest **excess moves in 亿** (not the
      largest percentages: a small base makes any move look huge) and the gaps that changed sign
      between years. Write one line per item: the pair, the gap and both absolute changes, what
      would be surprising about it, and the colleague whose lens owns it:

      | pair that diverged | owner |
      |---|---|
      | CFO vs net income, cash collected vs revenue, tax or minority leakage, any accrual line | `stephen-penman` |
      | receivables, inventory, payables or advances vs their flow; dividends or borrowings vs CFO and capex | `jeff-bezos` |
      | capex vs D&A, fixed assets vs revenue, cost of sales vs revenue (pricing power or cost position) | `warren-buffett` |
      | goodwill or intangibles vs revenue, cash vs interest-bearing debt (存贷双高), capitalized development | `michael-mauboussin` / `rockwood` |
      | other receivables vs revenue, prepayments vs cost of sales, minority share of profit, related-party channels | `li-lu` |
      | a cost line that jumped or collapsed in one year (reclassification, windfall, cycle) | `joel-greenblatt` |

      These lines are the round's question menu: the opener may start from the largest one, and
      the ones not reached go to `next_question_candidates` with the pair named. A divergence
      that the data already explains (a reclassification visible in the series, a disposal) is a
      one-line note, not a question.

   This record, not the latest quarter, is what the panel reads. Below the scorecard, keep the supporting series and calculations as
   a reference appendix. Compute more only when a live question needs it: de-cumulate quarters,
   bridge balance-sheet or equity movements, split growth into price, volume and mix, reconcile S1
   to S2. Stop a calculation when its answer cannot change the conclusion. A bridge that does not
   close is a finding only if it affects the story; otherwise note it in the appendix. In later
   rounds, extend the workpaper with what the live topic needs and correct earlier derived figures
   that used non-comparable share counts or definitions. The latest quarter or news item enters
   round one only if it changes the scorecard's verdict; otherwise it is queued for round two.
2. **Let an expert open.** Give the panel the fact sheet, the decade workpaper, the data
   dictionary, relevant company knowledge and prior rounds. Each speaker has their full role card.
   When the host supports and authorizes delegation, keep a separate context for each expert.
   Each panelist reads the 10-year record through their own lens; whoever saw the most
   consequential thing opens the round with it — the thing that changes how the business or its
   price should be understood: a puzzle, a break in a long series, an assumption the record
   contradicts, a question to a specific colleague. Prefer a question about what the business is
   and where it is heading over a question about how one figure was computed. A question or tentative explanation
   is enough to begin. In round one the unexplained cross-check mismatch, if any, opens instead; otherwise Buffett opens
   with the great/good/gruesome verdict and the single scorecard line that most surprised him, and
   the rest of the round works through valuation and floor, cash and returns in turn.
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

   **Chat register.** The round is read as a group chat: short, clear, one idea per turn, in the
   words a smart non-specialist uses. Aim for two to four sentences (about 40 to 90 words); a
   one-line question or concession is a whole turn, and a turn may run longer only when a worked
   argument cannot be split. Each turn answers the previous one first, then adds one point with at
   most one to three rounded numbers and their period. No tables, formulas, SQL, field names or
   source codes in `text`. Name accounting terms in plain words. Intermediate arithmetic stays in
   the workpaper; the turn's `evidence[]` carries one short item per figure, with a source label such
   as `S2 raw_income FY2016–FY2025`. A computed figure uses the function in `scripts/calc.py`
   (`python3 scripts/calc.py implied_growth_re price=… book=… earnings_next=… r=…`) and carries
   `formula`, `inputs` and `result`; a figure that cannot be checked locally carries
   `unverifiable` with the reason. Identify assumptions in the spoken text. Run-level notes on how
   the system performed belong in `session.json` `run_notes`, not in the chat.

   **Keep asking.** The panel makes progress by questions. Every turn except a closing one ends
   with one question — to a named colleague, or to the user when the answer depends on their
   horizon, risk tolerance or knowledge — and the next speaker answers it before adding anything.
   A good question is single, concrete and answerable from the data or from a named missing fact
   ("Is the 2023 rise in fixed assets growth capex or catch-up?", not "What about capital
   allocation?"). The sharpest questions name two lines that should move together and did not,
   with the gap in both percentage and 亿 ("Cash paid to suppliers rose 45亿 more than cost of
   sales last year — prepaying alumina, or inventory built in transit?"), and go to the colleague
   whose lens owns the pair (the table in step 1.7). Do not let an income-statement thread run the
   whole round when the scan shows a balance-sheet or cash-flow gap of the same size; the next
   speaker may cross statements by naming the pair. A growth rate spoken for a small line carries
   its absolute change in the same sentence. Do not stack questions in one turn. Aim for eight to twelve turns per round, one
   topic at a time; when a new topic opens, record it in `where_it_went` or queue it as the next
   round's question instead of running two threads at once.
   If reasoning stalls despite usable evidence, consult a method in `Thinkers/README.md`, attach
   its required label in the turn record, and return to verification. Four stall signals are
   detected by the checker (open disagreement, unexplained S1/S2 mismatch on a cited series, a
   conclusion repeating the last round, single-quarter evidence under high confidence); when one
   fires, the round either consults a method or records `{"thinker": null, "declined_because": …}`
   in `thinkers_consulted`.
4. **Close the round.** If the conclusion relies on an objection raised in the last turn, give
   the affected speaker a chance to address it or record how the unresolved point limits the answer.
   Record disagreements as open, narrowed, or resolved, with the evidence that
   shifted them. Write the conclusion — covering where the discussion actually went, not only the
   opening topic. Start it with the big-picture verdict in two or three plain sentences: what
   the business is, what the decade says, what the price implies, and the insight a reader
   should remember. Then give the handful of numbers that anchor it. Add what would change it, open questions, ranked next questions (at most three, each single and
   answerable, the first being what to ask next round or what the user should tell us), Thinkers
   consulted, and knowledge candidates. After round one, the conclusion also states the scorecard
   verdict in one line each: business type, cash backing, return driver, cheap or not and the floor. Use the lowest confidence of the evidence the
   conclusion depends on. High confidence requires a direct statement line or two independent
   sources. A finding that depends on an S2 default (r = 8%, g = 3%, or tax = 25%) is at most medium.
5. **Gate, save and review.** Write `rounds/round-NN.json` and run
   `python3 scripts/check_round.py <file>` (rules in `skills/analyze/CHECKLIST.md`). Fix every
   error and the warnings you can; a gated round with errors cannot be published. Then run
   `python3 scripts/render_round.py <file>` and update the session's `rounds` and
   `question_queue`. Run the `skills/observe/SKILL.md` round review with the exact round inputs,
   read its verdict before the next round, and fix what it finds in the round file (record the
   resolution at the end of the observer note). Run `python3 scripts/validate.py`.
6. **Improve.** Run `python3 scripts/improve.py ingest <round.json>`: it files the observer's
   tagged findings in `observer/log.jsonl`, the round's three numbers in `observer/metrics.jsonl`,
   writes the surviving knowledge candidates into `knowledge/` (an unverified fact becomes a
   hypothesis), and promotes playbook entries. Then `python3 scripts/improve.py proposals`. For
   each proposal it leaves at `drafting`, read the cited turns and the target section, write the
   Change and Risk, set `proposed`, and hand it to the Observe workflow's proposal review (an
   independent reviewer; apply on `validated`). If the ingest reports a workflow pitfall promoted
   to the playbook, add the rule to `CHECKLIST.md` and, when it can be computed, to
   `scripts/check_round.py`. Report the trend line (errors, weaknesses, knowledge cited) with the
   round result.

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
