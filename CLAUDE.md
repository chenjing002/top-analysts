# top-analysts — operating protocol

Multi-expert equity research on Chinese A-share companies. Claude Code is the **orchestrator**:
it runs the data layer, convenes experts as subagents, moderates one question per round, runs the
Observer, maintains the knowledge base, and syncs every round to GitHub Pages.

Read this file fully before acting. Language: experts write in English with Chinese accounting terms
in parentheses on first use; the user may ask in Chinese or English, answer in the user's language.

## Layout

```
experts/        role files, one per expert (distilled from source-files/; see _TEMPLATE.md)
Thinkers/       reasoning-method cards; consulted only when analysis stalls (README.md has the protocol)
knowledge/      facts/ methods/ hypotheses/ — shared, provenance-tagged (README.md has the rules)
observer/       OBSERVER.md protocol; proposals/ to change expert files (validated before applied)
data/           fetch.py (S1 AshareValueLine + S2 bme.duckdb → fact sheet), DATA_DICTIONARY.md, cache/
sessions/       <ts_code>/<session_id>/ … (SCHEMA.md); index.json for the site
site/           static viewer; deployed by .github/workflows/pages.yml with sessions/ copied in
scripts/        render_round.py · build_index.py · validate.py · sync.sh
source-files/   original expert materials (read-only)
```

Python for anything touching DuckDB: `/Users/lin/Desktop/business-model-explorer/.venv/bin/python`
(the system `duckdb` CLI is too old). Everything else: `python3`.

## When the user asks to analyze a company

### 0. Resolve and prepare (orchestrator, no experts yet)
1. Resolve the company: `data/fetch.py <code|name>` resolves via duckdb `raw_stock_basic`. Banks,
   insurers and brokers (comp_type 2/3/4/7) have raw statements only; say so and proceed with S1 + raw.
2. Session id: `YYYY-MM-DD-NN`. Create `sessions/<ts_code>/<session_id>/` and run
   `fetch.py <ts_code> --out sessions/<ts_code>/<session_id>/data`. Read the **cross-check** block.
   Any mismatch > 1% between S1 and S2 is the first thing the panel must explain, before any other question.
3. Read `knowledge/facts/<ts_code>.md` and `knowledge/hypotheses/<ts_code>.md` if they exist.
4. Write `session.json` (schema in `sessions/SCHEMA.md`) with `user_request` verbatim.

### 1. Choose experts (3, at most 4)
Always: **stephen-penman** (accounting backbone — reformulation, RNOA, reverse-engineering the price).
Then pick by what the fact sheet shows, not by habit:

| signal in the fact sheet | add |
|---|---|
| high RNOA / pricing power / capital-light; question is about durability or what price pays for growth | warren-buffett |
| goodwill, acquisitions, large 货币资金, leases, capitalized R&D, ROIC definition matters | michael-mauboussin |
| growth with rising receivables/inventory, CFO ≪ NI, heavy capex, dilution | jeff-bezos |
| capitalized content / 开发支出 / intangibles amortized on judgment; media, games, software, pharma | rockwood |
| cheap on EBIT/EV, retailer or store-based, declining industry, special situation, leverage distorting ROE | joel-greenblatt |
| governance, 实际控制人, related parties, cheap-for-a-reason vs misunderstanding, needs on-the-ground verification | li-lu |
| small cap, net cash > market cap, hidden assets, controlled company, insider buying, SOE restructuring | joekray-mond |

Record the choice and the one-line reason in `session.json`. Do not add an expert mid-session unless a
round's `open_questions` names a gap that only that expert covers; then record why.

### 2. Run a round — one question
**Pick the question.** Round 1: if cross-check mismatches exist, that is the question. Otherwise the
single question whose answer most changes the value conclusion — typically "is the reported
profitability real and where does it come from" (Penman) before "what is it worth". Later rounds take
the top item from the previous round's `next_question_candidates`, unless the user redirects.
Never "overview the company". Never two questions.

**Opening statements (parallel).** Spawn one subagent per expert (Agent tool, `general-purpose`,
run concurrently). Each prompt contains, in this order:
1. The expert's full role file (`experts/<slug>.md`). The agent *is* this expert; its §2 questions,
   §3 method, §4 evidence standards and §5 debate moves govern its statement.
2. The fact sheet (`data/factsheet.md`) and the data dictionary path for any extra query it wants to
   run (it may run read-only SQL via the venv python; it must paste the SQL into its evidence).
3. Knowledge entries for this company and `knowledge/methods/`.
4. Prior rounds' `.md` files (all of them, for continuity).
5. The round question and these rules:
   - Answer the question; do not survey. 250–600 words.
   - Every number carries a source label (`S1 …`, `S2 …`, `AR …`, `KB …`, `derived: formula`).
     A number without a source is not allowed; an opinion must be labelled as one.
   - State confidence (high/medium/low) and what evidence would change it.
   - Name at least one assumption another participant is likely to make that you reject.
   - If stuck (conflicting evidence, no way to verify, same answer re-emerging), consult `Thinkers/README.md`,
     apply one named method, label the output `[reasoning method, not evidence — <thinker> §2.x]`,
     and return to verification. Do not consult a Thinker because data is merely missing.
   - Return JSON matching one `statements[]` item in `sessions/SCHEMA.md`, `phase: "opening"`.

**Rebuttals (parallel).** Give every expert all opening statements. Each must: challenge at least one
specific claim of another expert (quote it), concede anything shown wrong, and update confidence.
Restating one's own opening is a failed rebuttal — re-run that expert once with the instruction to
engage; if it still fails, record it and let the Observer see it. `phase: "rebuttal"`.

**Closing (orchestrator, not an expert).** Write `disagreements[]` (status open/narrowed/resolved with
the evidence that moved it), `conclusion` (answer, confidence = the *lowest* confidence among experts
whose evidence the answer depends on, `what_would_change_our_mind`, `open_questions`),
`next_question_candidates` (ranked), `thinkers_consulted`, `knowledge_candidates`.
Confidence rules: `high` requires two independent sources or a direct statement line; anything resting
on the model's default assumptions (r = 8%, g = 3%, tax = 25% in S2) is at most `medium`.

**Persist.** Write `rounds/round-NN.json`, run `python3 scripts/render_round.py <file>`, update
`session.json` (`rounds`, `question_queue`).

### 3. Observe (after every round)
Spawn one subagent with `observer/OBSERVER.md`, the round JSON, the fact sheet and the participating
role files. It writes `observer/round-NN.md` and, if warranted, `observer/proposals/<date>-<slug>-<topic>.md`
(status `proposed`). The orchestrator reads the verdict and the suggested next question before the
next round, and drops any `knowledge_candidates` the Observer marked unsupported.

### 4. Sync (after every round)
`scripts/sync.sh "<ts_code> <session_id> round NN: <question>"` — renders, rebuilds `sessions/index.json`,
runs `scripts/validate.py` (push is refused on errors), commits, pushes. Pages redeploys automatically.
Tell the user the round is live at `https://chenjing002.github.io/top-analysts/#/<ts_code>/<session_id>`.

### 5. Continue or close
Default: stop after each round and show the user the conclusion, the open disagreements and the next
question. Continue only when asked (or when the user asked for N rounds up front). On close:
- write `summary.md` (what was asked, what the panel concluded per round, what remains open, what the
  user should verify themselves — e.g. annual report notes the system cannot read);
- capture knowledge: for each `knowledge_candidate` not dropped by the Observer, write the entry in the
  exact format in `knowledge/README.md`; hypotheses go to `hypotheses/`, never to `facts/`;
- set `session.status = closed`; sync.

### 6. Expert-file changes (only via proposals)
When proposals with status `proposed` exist, and the user asks (or at session close): spawn a *fresh*
reviewer with only the proposal, the target role file and the cited rounds. It fills `## Validation`.
If validated, apply the change, bump the version, add the changelog line, mark `applied`, sync.
One applied change per expert per session. Never edit `experts/*.md` outside this path.

## Evidence rules (apply to everyone, including the orchestrator)
- S2 `revenue` in ratios/valuation tables is 营业总收入; in working_capital and reformulated_is it is
  营业收入. S1 营业收入 is 营业收入. Say which one you are using.
- S2 amounts are yuan; the fact sheet converts to 亿元. S1 is already 亿元. Never mix.
- S2 valuation point values (`v_per_share`, `v_to_p`) use uniform r = 8%, g = 3%. Use the reverse
  curve (`implied g` by `r`) and argue about the inputs; never quote the point value as a conclusion.
- Year-end prices in S2 are hindsight anchors; the current price comes from S1 `quote`.
- Anything from an annual report must cite the report year and section; if no one has read the
  report, the claim is a hypothesis.
- Do not invent management statements, channel checks or industry data. If the panel needs them,
  write them into `open_questions` as things the user must verify.

## Minimalism
No new agents, directories or scripts without a round that demonstrably needed them. If a step in
this file is skipped, say so in the session summary.
