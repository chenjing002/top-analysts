# Round checklist

Deterministic rules every round must meet. `scripts/check_round.py <round.json>` enforces the ones
with a check id; `scripts/validate.py` runs it for every round and `scripts/sync.sh` refuses to
publish a gated round with errors. Rules without an id are checked by the Observer and logged
with the tag in brackets (see `observer/TAGS.md`). When a tagged workflow pitfall reaches the
playbook, add a rule here and, where it can be computed, a check in `check_round.py`.

## Numbers (errors)

- **N1** A figure with an `S1`/`S2` source exists in the session's `factsheet.json`, `avl_raw.json`
  or `bme_raw.json` within 1%. Quarterly or DuckDB-only figures are warnings: the workpaper shows the query.
- **N2** A `derived:` figure carries `formula` + `inputs` and recomputes to `result` within 1%. Use
  the function in `scripts/calc.py` and name it in the source (`derived: calc.implied_growth_re`).
- **N3** A derived figure without formula and inputs is a warning. Add them or mark `unverifiable`.
- **N4** Every 亿, %, ×, 元 or decimal figure spoken in `text` has an evidence item in that turn, or
  in an earlier turn of the round when quoting a colleague. Round in speech, not in evidence.
- **U1** Amounts are written in 亿 in English text. "billion" and "million" are errors unless they
  are dollar figures quoted from a source.

## Confidence (errors)

- **C1** A turn or conclusion at `high` must not rest on a default or an estimate: r = 8%, g = 3%,
  tax = 25%, "assume", "estimate". Cap at `medium` and say which input would lift it.
- **C2** A `fact` knowledge candidate at `high` has every figure verified locally; otherwise it goes
  in as a hypothesis at `low`.

## Discussion (warnings)

- **D1** Turns run to at most 110 words. [multi-idea-turn]
- **D2** Every non-closing turn ends with exactly one question. [question-discipline]
- **D3** Round one's conclusion carries the scorecard: great/good/gruesome, cash backing, return
  driver, cheap or not, floor. [scorecard-missing]
- **D4** Round one's workpaper carries the paired-line divergence scan (`## Divergence scan`
  heading, or a line per pair under scorecard item 7) with an owner for each item.
  [divergence-unscanned]
- **D5** Round one estimates what the two or three assets that dominate book are worth, not only
  what they carry: the workpaper shows `calc.revalued_book` (or an `asset worth` section) with
  each asset's carrying value, worth and basis, and the conclusion says what they are worth
  against the price. [asset-worth-missing]
- A growth rate spoken for a line smaller than about a tenth of revenue, or for a pair whose two
  lines differ by an order of magnitude, carries its absolute change in the same sentence
  (`calc.growth_gap` `excess_a`). [percent-without-base]
- A round's questions span the statements the scan flagged: when a balance-sheet or cash-flow
  excess move ranks among the five largest and nobody asks about it, log the miss. Plan the turn
  order from the scan before the opener speaks so that at least one balance-sheet and one cash-flow
  item from the top five gets a question; an item the round cannot reach becomes the first
  `next_question_candidates` entry, with the pair named (P-021; 000002.SZ and 000915.SZ r1).
  [statement-blind-spot]
- A consequential point raised in a turn — a precedent in the data, a colleague's figure, a test
  someone proposed — is used, answered, or carried to `open_questions` / `next_question_candidates`
  by the end of the round; before writing a test or threshold, check whether the record already
  ran it once (e.g. a prior dip and recovery) and say what differs (P-020). Observer-checked.
  [dropped-thread]
- Challenges and concessions made in the text are recorded in `challenges[]` / `concessions[]`.
  [challenge-unrecorded]
- A spoken estimate carries its assumption in the same sentence as the number: a floor names its
  haircut, a cause read from one line item says so, an annualized yield names the part that is
  fair-value marks. The workpaper label is not enough; the spoken figure is what gets quoted.
  [assumption-as-finding]
- A spoken multiplier word (doubled, tripled, quadrupled) is a figure: it needs an evidence item
  with the matching ratio within rounding ("tripled" for 2.66× is a miss; say "more than doubled"
  or give the percent). Observer-checked. [unsourced-number]

## Financial definitions (Observer-checked)

- Separate operating from financial items before any return or valuation: excess cash, trading
  financial assets and their income are financing (Penman §3.1). [cash-split]
- Like for like: if cash leaves the price or the book, its after-tax income leaves the earnings
  (`calc.like_for_like_earnings`); TTM against TTM; pre-raise against pre-raise. [like-for-like]
- 营业利润 is not EBIT. Rebuild core EBIT or OI before an EBIT/EV yield, or disclose the proxy and
  the gap in the same evidence item. [ebit-proxy]
- A required return is an input to argue, not a constant. State the hurdle, show the answer at two
  others (the reverse curve), and say which one the conclusion uses. [required-return-unargued]
- Cyclicals: never a trailing multiple alone; a normalized band (`calc.normalized_band`) with the low
  end tested against the hurdle. [peak-earnings-normalized]
- One quarter proves nothing: read it against the same quarter of prior years and the seasonal
  base before inferring. [single-quarter-read]
- State scope on every comparison: parent vs total, pre- vs post-bonus shares, 营业收入 vs 营业总收入,
  begin vs average basis. [scope-mismatch]
- A floor or write-down percentage names its base and its end point: full book or tangible book,
  over which assets, and whether it reaches the price or zero. A magnifier names its base (EV /
  market cap, assets / book, or 1% of assets over market cap); do not speak two in one round
  without saying which is which. Pair a figure only with the gap it was computed from (P-017,
  P-012; 000002.SZ/2026-11-25-01 r1). [like-for-like] [scope-mismatch]
- An asset's worth names its basis (market price, rent over a stated yield, selling price less
  cost to finish, a multiple of its own earnings), the parent's share and the tax on a sale, and
  is spoken as an estimate. A write-down that reaches the price is not a worth estimate; it says
  how wrong book must be, not how wrong it is. [assumption-as-finding] [scope-mismatch]

## Stall signals (warnings — consult a Thinker or record `declined_because`)

- **T1** A disagreement closes `open` → Hamming 2.3 (invert) or Tukey 2.5 (bounding).
- **T2** An S1/S2 cross-check differs by more than 1% on a series the round cites → Hamming 2.5.
- **T3** The conclusion overlaps the previous round's by more than 60% → Hamming 2.2.
- **T4** Single-quarter evidence under a high-confidence conclusion → Tukey 2.4.

## Before the Observer runs

```
python3 scripts/check_round.py sessions/<ts>/<sid>/rounds/round-NN.json
```

Fix every error and every warning you can; mark the rest `unverifiable` with a reason. Then run
the Observe workflow, then `python3 scripts/improve.py ingest <round.json>` and
`python3 scripts/improve.py proposals`.
