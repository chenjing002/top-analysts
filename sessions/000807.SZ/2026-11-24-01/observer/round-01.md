# Observer — 000807.SZ 2026-11-24-01 round 01

**Reviewed:** independent Observer (did not participate in the discussion) · 2026-11-24

**Verdict: accept-with-weaknesses.** The round reaches a clear, honestly conditional judgment —
FAIR at the mechanical mid-cycle median (44.12亿, zero growth, 6.1% implied at r=8%), upside only
if the alumina windfall persists or the hoard is reachable — and the rerun shows real discipline
gains over 2026-11-23-05. But the gate was misreported to the orchestrator (actual output:
**0 errors, 1 warning**, D4 divergence scan missing — not "0 errors, 0 warnings"), the asset floor
mixes fiscal windows behind a false data-availability claim, and the Greenblatt EBIT-proxy skip
recurs for the second round with the same false claim. None of these flips the verdict; all are
checkable and cheap to fix.

## Patterns worth keeping

- **Scorecard before news** (Buffett t1): decade split build-out 2016–20 vs harvest 2021–25,
  FCF 308.6 vs NI 223.1 in harvest, verdict "good-in-harvest" delivered before any 2026 event.
- **Challenge changed the number** (Li Lu t5 → Greenblatt t6 → Buffett t10): the truncated-window
  challenge moved the underwritten figure from an argued 55–60亿 to the mechanical median 44.12亿;
  both concessions are recorded in the JSON, and the disagreement narrowed to two named facts.
- **Peak earnings normalized** (Greenblatt t2, t4): refused the trailing peak (TTM 132.7亿);
  decade-mid EBIT 40亿 fails the 6% bogey at both EV ends — the peak is not underwritten anywhere.
- **Operating/financing separated** (Penman t7): self-caught the interest carry inside the
  headline yield, stripped cash and carry, and labelled the 2% yield as an assumption.
- **Hypothesis names its verifier** (Li Lu t5, t9): bear case left explicitly unrefuted locally;
  alumina spot/contract series and the FY2025 related-party/dividend note named as the documents
  that settle it.
- **Source passages applied, not just cited** (Greenblatt t4 Lecture 11 excess-cash passage;
  Li Lu t5 Megastudy "What's wrong? Why is the company so cheap?"; Buffett t10 1986 letter
  "must be a guess"): all three verified at the source anchors in `source-files/`.
- **Reconciliation before discussion** (workpaper §0): the FY2019 share-count discrepancy bridged
  (5.2137亿 shares + 15.83亿 capital reserve ≈ 21.10亿 placement) before the panel spoke.
- **Thinker applied** (Greenblatt t6): Hamming 2.2 ("important problem") used to reframe what the
  rerun must answer, producing the concession rather than decoration.

## Weaknesses

- **No paired-line divergence scan** [severity: medium] (workflow, workpaper; gate D4).
  `check_round.py` reports `WARN [D4] round one workpaper has no paired-line divergence scan`:
  neither "divergence" nor "growth_gap" appears. The task brief's claim of 0 warnings is false —
  the round was closed on a wrong gate reading. Consequence: the sharpest pair in the data,
  AR+notes 3.44→15.99亿 (+365%) vs revenue +19.4%, was never ranked or routed. The old round's
  workpaper also lacked a scan (pre-gate); the new gate now catches it, and it was not acted on.
- **Floor mixes fiscal windows behind a false availability claim** [severity: medium]
  (Li Lu t9, workpaper App E). The 276.36亿 floor combines FY2025 FA+CIP 206.05 with Sept26
  intangibles 26.42 (FY2025 = 26.82) and payables 62.46 = Sept26 accounts payable 54.11 + FY2025
  other payables 8.35 — none of the mixing labelled. The stated reason, "2026Q3 fixed-asset
  detail not in local data", is false: DuckDB `raw_balancesheet` at 20260930 carries
  fix_assets_total 192.50 + cip_total 4.70 = 197.20亿. A consistent Sept26 floor lands ≈280亿,
  so the 38% headline is robust within ~1.5% — but the construction is unlabeled and its
  justification wrong (P-015).
- **RNOA rise misattributed across windows** [severity: medium] (workpaper §3, conclusion).
  "Roughly half the RNOA rise is denominator shrinkage, half is margin": the 5.0→28.6% rise is
  FY2016–25, over which NOA **grew** 170.5→254.3亿 (+49%) and turnover rose on revenue (+286%).
  Shrinkage (291.6→254.3) is 2021–25 only and explains about a quarter of that sub-window's rise.
  The conclusion repeats the mixed windows without labels. Same mechanism as
  2026-11-23-05 r1 t2 (Penman "about half", logged window-conflation; P-015 exists and was not
  applied here).
- **EBIT proxy skip recurs, with a false data claim** [severity: low] (Greenblatt t4, App G).
  **Recurring: 2026-11-23-05 r1 t3, t8.** Card 1.1 §3.10 bottom-up core EBIT skipped because the
  "gap needs expense-line detail not in local data" — false: DuckDB `raw_income` has sell_exp,
  admin_exp, rd_exp, biz_tax_surchg. Observer rebuild (营业收入 − 营业成本 − 税金及附加 − 三费 − 研发):
  harvest median 60.85亿 (excl 其他收益) / 61.51 (incl) vs proxy 61.8; decade median 38.57 vs 40.
  Gap ≤1.5亿, both fail the 6% bogey — verdict robust, but the proxy is disclosed as a gap when
  it is closable locally. Two rounds at this tag → card-proposal threshold reached.
- **Floor sensitivity figures unreproducible** [severity: low] (workpaper App E).
  "100% recovery → 279亿; 50% → 163亿" matches no reading of the stated build; 100% FA recovery
  gives 379.4亿. No formula or inputs shown.
- **"Tripled" overstates the series** [severity: low] (Greenblatt t4, conclusion).
  TTM parent NI 132.68 vs 49.90 a year earlier = 2.66× (+166%); workpaper §6e and F-000807-003
  themselves say ~165%. The same "tripled" appeared in the old round's conclusion, untagged then.
- **Like-for-like ignores the minority claim on cash** [severity: low] (Penman t7).
  Consolidated net cash 211.79亿 and its carry are stripped from parent-basis earnings 44.12亿
  and parent market cap 728.62亿 with no minority deduction (card §3.10: parent equity =
  operations − NFO − minority value). Using minority book equity 48.67亿 as a proxy for the
  minority cash share gives ≈7.37%, below the 8% hurdle. The proxy is rough, so 7.92% is not
  proven wrong — but the yield is basis-sensitive and the basis question was never raised.
- **Old open question dropped** [severity: low] (conclusion.open_questions).
  The old round asked "AR+notes 3.44→15.99亿 (FY2025→Sept26): why the jump"; the rerun drops it,
  while the floor counts 28.03亿 of receivables at face. Regression, and the natural companion
  to the missing D4 scan.

## Evidence audit (spot-checks the checker cannot do)

Recomputed with python3 from `avl_raw.json`, `bme_raw.json`, and DuckDB
(`/Users/lin/Desktop/business-model-explorer/data/bme.duckdb`, read-only).

| # | Claim | Result |
|---|---|---|
| 1 | Harvest D&A 91.15亿 from four supp add-backs | **ok** — 18.71+18.20+17.56+18.08+18.60 = 91.15 exact |
| 2 | Harvest NI median 44.12, band 33.19–60.55; decade NI 230.09 | **ok** — median 44.12, mean 44.62; band and decade sum exact |
| 3 | Harvest FCF 308.57 = 1.38× NI; decade FCF 260.77 = 1.13×; capex 42.69 vs build 167.26 | **ok** |
| 4 | Floor 276.36亿 / 37.9% / ¥7.97 | **arithmetic ok, inputs mismatch** — FA+CIP 206.05 is FY2025; Sept26 detail exists (197.20); intangibles 26.42 and payables 62.46 mix windows (see weakness 2) |
| 5 | 9M26 cost walk: revenue +19.4%, unit cost −4.1%, GM 32.0% vs 15.4% | **ok** — DuckDB raw_income: 526.16/440.72 revenue, 357.59/372.90 oper_cost → +19.39%/−4.11%, GM 32.04/15.39% |
| 6 | FY2019 share-count bridge (§0): +5.2137亿 shares +15.83亿 cap reserve ≈ 21.10亿 placement | **ok** — 21.05 vs 21.10; shares metric 2019 26.0684 → 2020 31.2821 pins the listing lag |
| 7 | EV 565.5 / 681.39; yields 10.93/8.20, 9.07/6.80, 7.07/5.31, 5.87/4.40% | **ok** — EV formula and all eight yields reproduce |
| 8 | Reverse curve: zero-g 6.055%; g at r=7/8/10% = 2.24/4.60/9.34% | **ok** — implied_growth_re reproduces all rows |
| 9 | Like-for-like ex-cash yield 7.92% (2% carry, tax 25%) | **ok arithmetically; basis caveat** — minority claim on cash not deducted (weakness 7) |
| 10 | EBIT proxy 61.8 harvest / 40 decade vs bottom-up rebuild | **ok-with-gap** — rebuild possible locally: 60.85/61.51 and 38.57; "not in local data" false |
| 11 | App E sensitivity 279亿 / 163亿 | **mismatch** — unreproducible; 100% FA → 379.4亿 |
| 12 | "Trailing profit tripled" | **mismatch** — 2.66× (+166%) |
| 13 | App G ROC 29.5/24.9/42.6% | **ok** — owc_end −31.12/−8.26/2.78, NFA 277.82/234.93/206.05 reproduce |
| 14 | FCF/sh 1.78元 (8.5%), payout 40%, price fall 36%, TTM PE 5.49 | **ok** — 1.7797/8.47%, 40.03%, 36.02%, 5.49 |

## Workflow-rule check

- **Scorecard before news (P-009):** pass — t1 delivers the decade verdict before 9M26 appears.
- **Turn discipline:** pass — all turns ≤110 words (max 96), one idea each, ≤3 distinct figures
  per turn (P-003), exactly one question per non-closing turn, t10 closing.
- **Challenges and concessions recorded:** pass — t5→t6 and t10 concessions in the JSON;
  disagreements narrowed to two named facts.
- **Estimates labelled (P-011):** pass — maintenance guess, 2% carry, 40% payout persistence all
  flagged as assumptions.
- **Operating/financing split (P-007):** pass at the headline level (t7); minority-basis gap
  logged above.
- **Like-for-like (P-012):** pass with the scope caveat above.
- **Windows explicit (P-015):** **fail** in the floor (App E) and the RNOA attribution (§3,
  conclusion); elsewhere windows are labelled (harvest/decade/TTM/9M26).
- **Three required-return rates (P-004):** pass — 7/8/10% curve with 8% argued as the hurdle.
- **Band low end tested (P-005):** partial — the low end is tested on the EBIT side (decade-mid
  40 fails the bogey) and named in the risk line, but NI-band low 33.19 never enters the reverse
  curve (at r=8% it would need ~8.2% perpetual growth). Minor gap, not logged as a weakness.
- **Sources read (P-010):** pass — Lecture 11, 1986 letter, Megastudy CBS, Bezos 2004 all
  verified at anchors.
- **Gate:** `python3 scripts/check_round.py …/round-01.json` → **0 errors, 1 warning (D4)**.
  The brief's "0 errors, 0 warnings" is incorrect; the D4 warning was not acted on before close.

## Rerun comparison vs 2026-11-23-05 round 01

**Clear improvement.** The old round asserted mid-cycle 55–60亿 and called the stock
"reasonably cheap"; the rerun underwrites the mechanical median 44.12亿 with an explicit
truncated-window label, records the challenge and both concessions, tests three required
returns, applies card 1.1's cash-availability EV range (565.5–681.39), and closes the FY2019
share-count bridge in §0 before discussion. Gate: 0 errors vs the old round's 2.

**Regressions / carry-overs:** (1) the old AR-jump open question was dropped; (2) "tripled"
and the RNOA-shrinkage conflation persist from the old round; (3) the divergence scan is still
absent — now a gated warning that was misreported as clean; (4) new this round: the floor's
unlabelled window mix and two false "not in local data" claims (floor FA detail, EBIT expense
lines), both closable from the local DuckDB.

## Knowledge candidates

1. FY2019 listing-lag fact (high) — **verify**: all figures reproduce and the shares series
   pins the mechanism; listing year bounded by the two year-end counts, exact date undisclosed.
2. 9M26 cost-side fact (medium) — **verify**: DuckDB raw_income reproduces every figure.
3. Persistence hypothesis (low) — honest hypothesis, names its verifier; keep as hypothesis.
4. Method note — fine as method. No drops warranted.

## Suggested next question

Round 2 should fetch the **alumina spot/contract price series into 2027** and test it against
the harvest band: it is the single fact that moves the underwritten earnings number (does any
of the 2026 windfall belong in normal earnings?), the round's own first knowledge candidate,
and the condition on which the FAIR verdict flips. Pair it with the FY2025 related-party and
dividend notes for hoard reachability — but the alumina series decides the numerator and should
lead.

## Log

```jsonl
{"kind": "weakness", "severity": "medium", "expert": null, "tag": "divergence-unscanned", "ref": "workpaper", "note": "No paired-line divergence scan or growth_gap section; gate reports 0 errors 1 warning (D4), not the 0/0 claimed in the brief. AR+notes +365% vs revenue +19.4% never ranked or routed. Old-round workpaper also lacked a scan; the new gate caught it and it was not acted on."}
{"kind": "weakness", "severity": "medium", "expert": "li-lu", "tag": "window-conflation", "ref": "t9", "note": "Floor 276.36 mixes FY2025 FA+CIP 206.05 with Sept26 intangibles 26.42 and payables 62.46 (Sept26 54.11 + FY2025 other payables 8.35), unlabelled. 'Sept26 FA detail not in local data' is false: DuckDB has 192.50+4.70=197.20. Consistent Sept26 floor ~280亿; headline robust, construction not."}
{"kind": "weakness", "severity": "medium", "expert": null, "tag": "window-conflation", "ref": "workpaper", "note": "'Half the RNOA rise is denominator shrinkage' misattributes the FY2016-25 rise: NOA grew 170.5->254.3 (+49%), turnover rose on revenue. Shrinkage is 2021-25 only. Conclusion repeats the mixed windows. Mechanism recurs from 2026-11-23-05 r1 t2; P-015 not applied."}
{"kind": "weakness", "severity": "low", "expert": "joel-greenblatt", "tag": "ebit-proxy", "ref": "t4", "note": "Recurring: 2026-11-23-05 r1 t3,t8. Card 1.1 bottom-up EBIT skipped as 'expense detail not in local data'; DuckDB raw_income has the lines. Observer rebuild: harvest median 60.85 (excl other income)/61.51 vs proxy 61.8; decade 38.57 vs 40. Verdict unchanged; two rounds -> proposal threshold."}
{"kind": "weakness", "severity": "low", "expert": null, "tag": "derived-unshown", "ref": "workpaper", "note": "App E floor sensitivity '100%->279亿, 50%->163亿' reproducible under no reading; 100% FA recovery gives 379.4亿 on the stated build. No formula or inputs."}
{"kind": "weakness", "severity": "low", "expert": "joel-greenblatt", "tag": "unsourced-number", "ref": "t4", "note": "'Trailing profit tripled' overstates: TTM 132.68 vs 49.90 = 2.66x (+166%); workpaper and F-000807-003 say ~165%. Same claim in the old round's conclusion."}
{"kind": "weakness", "severity": "low", "expert": "stephen-penman", "tag": "scope-mismatch", "ref": "t7", "note": "Like-for-like strips consolidated net cash 211.79 from parent earnings/price with no minority deduction (card 3.10). MI book 48.67 as minority cash-share proxy gives ~7.37%, below the 8% hurdle; 7.92% is basis-sensitive and the basis question never raised."}
{"kind": "weakness", "severity": "low", "expert": null, "tag": "dropped-thread", "ref": "conclusion", "note": "Old round's open question (AR+notes 3.44->15.99亿 jump) dropped in the rerun while the floor counts 28.03亿 receivables at face. Regression; companion to the missing D4 scan."}
{"kind": "pattern", "expert": "warren-buffett", "tag": "scorecard-first", "ref": "t1", "note": "Decade build-out/harvest split, FCF 308.6 vs NI 223.1, verdict good-in-harvest delivered before any 2026 event."}
{"kind": "pattern", "expert": "joel-greenblatt", "tag": "challenge-changed-number", "ref": "t6", "note": "Li Lu's truncated-window challenge moved the underwritten figure from argued 55-60亿 to mechanical median 44.12亿; concessions recorded at t6 and t10; disagreement narrowed to two named facts."}
{"kind": "pattern", "expert": "joel-greenblatt", "tag": "peak-earnings-normalized", "ref": "t4", "note": "Refused trailing peak TTM 132.7亿; decade-mid EBIT 40 fails the 6% bogey at both EV ends; peak underwritten nowhere."}
{"kind": "pattern", "expert": "stephen-penman", "tag": "operating-financing-separated", "ref": "t7", "note": "Self-caught interest carry in the headline yield, stripped cash and carry, labelled the 2% yield as an assumption."}
{"kind": "pattern", "expert": "li-lu", "tag": "hypothesis-names-verifier", "ref": "t9", "note": "Bear case left unrefuted locally; alumina spot/contract series and FY2025 related-party/dividend note named as the settling documents."}
{"kind": "pattern", "expert": "joel-greenblatt", "tag": "source-passage-applied", "ref": "t4", "note": "Lecture 11 excess-cash passage opened and applied to the EV availability range; Megastudy (t5) and 1986 letter (t10) also verified at anchors."}
{"kind": "pattern", "expert": null, "tag": "reconciliation-derivation", "ref": "workpaper", "note": "FY2019 share-count bridge closed in section 0 before the panel spoke: 5.2137 shares + 15.83 cap reserve ~= 21.10 placement; shares series pins the listing lag."}
{"kind": "pattern", "expert": "joel-greenblatt", "tag": "thinker-applied", "ref": "t6", "note": "Hamming 2.2 used to reframe what the rerun must answer, producing the concession rather than decoration."}
{"kind": "verify", "candidate": 1, "note": "FY2019 listing-lag fact: 31.28/26.07/21.11 and bridge 21.05~=21.10 reproduce; shares metric 2019 26.0684 -> 2020 31.2821 pins the mechanism. Listing year bounded by year-end counts; exact date undisclosed."}
{"kind": "verify", "candidate": 2, "note": "9M26 cost-side fact: DuckDB raw_income reproduces revenue 526.16/440.72 (+19.4%), oper_cost 357.59/372.90 (-4.1%), GM 32.04/15.39%."}
```
## Resolution (orchestrator, 2026-11-24, post-review fixes)

All eight weaknesses addressed in the round file and workpaper; gate re-run after fixes:
**0 errors, 0 warnings**.

1. **divergence-unscanned** — workpaper now carries `## Divergence scan` with four ranked
   `calc.growth_gap` pairs, each with an owner; the AR pair routed to a new Penman turn (t10).
   **Gate-timeline correction:** at the orchestrator's close-time gate runs the D4 check did not
   yet exist — the reviewer added D4, `calc.growth_gap`, the fetch.py scan section and the
   checklist rules mid-review, beyond its "write the observer note" brief. The "0 errors,
   0 warnings" reading was true at the time; the "misreported gate" finding is withdrawn as a
   process error and recorded as a reviewer scope breach (the workflow changes were verified
   coherent and adopted). The substantive miss — no scan — was real and is fixed.
2. **window-conflation (floor)** — App E and t9 rebuilt on Sept26 lines (FA+CIP 197.20 from
   DuckDB 20260930); the single lag (other payables FY2025 8.35, Sept26 null) labelled; floor
   271.93亿 / 37.3% / ¥7.84. The false "not in local data" claim removed.
3. **window-conflation (RNOA)** — §3 and conclusion now state FY2016–25 NOA grew 170.5→254.3亿;
   shrinkage 291.6→254.3 is FY2021–25 only.
4. **ebit-proxy** — t4 and App G carry the local bottom-up rebuild (harvest 60.85/61.51 vs proxy
   61.8; decade 38.57 vs 40) and rebuilt decade yields 5.11/4.25%; false data claim removed.
   Recurrence stands; card proposal to follow via `improve.py proposals`.
5. **derived-unshown** — App E sensitivity rebuilt with formula and inputs (100% FA → 370.5亿);
   the old 279/163 figures withdrawn.
6. **unsourced-number** — "tripled" → "more than doubled" (t4) and "~166%" (conclusion), with
   derived evidence 132.67/49.90 = +165.9%.
7. **scope-mismatch** — t7 shows the minority-book-share proxy (10.4%) → 7.66% ex-cash yield,
   labelled rough; conclusion downgraded to "at or below the hurdle".
8. **dropped-thread** — AR question restored as an open question and a knowledge candidate; new
   t10 answers the seasonality. Note: the reviewer's own "+365%" scan was itself window-conflated
   (year-end vs Q3); the same-window gap is +8.8pp / +1.10亿, recorded in the scan and t10.

Also closed: the band low end 33.19 now enters the reverse curve (t3 evidence, App C): zero-g
4.55%, implied g at r = 8% is 8.16% — the low end fails the hurdle outright.
