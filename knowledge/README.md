# Shared knowledge base

Everything an expert learns during a session that is worth keeping, written so a future session can
trust it without re-deriving it. Three directories, three levels of trust:

| dir | contains | admission rule |
|---|---|---|
| `facts/<ts_code>.md` | verified company-specific facts | reproducible from S1/S2/annual report; checked by a second expert or by a query in the round |
| `methods/*.md` | reusable analytical methods and checks | used in ≥1 round, produced a result that changed or sharpened a conclusion, and written generally enough to apply to another company |
| `hypotheses/<ts_code>.md` | unverified but promising claims | anything an expert believes but could not verify in-session; **never** confidence `high` |

Each entry is one line, one claim, in this exact form (validated by `scripts/validate.py`):

```
- [F-600519-001] (2026-11-23, confidence: high, source: S2 ratios_annual basis=average FY2016–FY2025) RNOA fell from 227% (FY2019) to 123% (FY2025) while OPM held at ~50%; the decline is entirely asset turnover (ATO 4.58 → 2.50), i.e. NOA grew faster than sales. Session 600519.SH/2026-11-23-01 r1.
- [M-001] (2026-11-23, confidence: medium, source: sessions 600519.SH/2026-11-23-01 r1) When RNOA falls with stable OPM, decompose ΔNOA into operating-asset lines (S2 reformulated_bs_components) before concluding "returns are eroding" — the cause is usually a balance-sheet build, not a margin problem.
- [H-600519-001] (2026-11-23, confidence: low, source: inference from S1 存货 growth) Inventory growth above sales growth since FY2021 reflects deliberate aging of base liquor, not demand weakness. Test: 年报 note on 库存商品 vs 半成品 split.
```

ID prefixes: `F-<ts_code 6 digits>-NNN` facts, `M-NNN` methods, `H-<6 digits>-NNN` hypotheses. IDs are never reused.

Rules
1. **Provenance or nothing.** `source:` names the table/block/report section. "Analyst estimate" is not a source; it goes to hypotheses.
2. **Confidence means something.** `high` = two independent sources agree or a direct statement line; `medium` = one source, or a derivation with a stated formula; `low` = inference.
3. **Promotion, not accumulation.** A hypothesis moves to facts only when a later round verifies it; the old line is deleted, not kept. A fact that is contradicted is removed and the removal noted in the session's summary.
4. **Dates are facts too.** Every entry says which fiscal years it covers. Facts about a company rot; the date tells the reader how old the evidence is.
5. **No duplication of the fact sheet.** Numbers that `data/fetch.py` reproduces on demand do not belong here. Keep what required judgment or cross-referencing to establish.
6. **Capture at session close**, from each round's `knowledge_candidates`, after the Observer has reviewed the round. The orchestrator writes entries; it never writes an entry no expert proposed.
7. **Cap.** Keep each `facts/<ts_code>.md` under 40 entries and `methods/` under 60 total. Beyond that, consolidate; do not append.

Experts read `facts/<ts_code>.md`, `hypotheses/<ts_code>.md` and `methods/` at the start of every session. They cite knowledge entries as `KB F-600519-001`.
