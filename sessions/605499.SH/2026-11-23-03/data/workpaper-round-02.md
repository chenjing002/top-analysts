# Workpaper — round 2 (not shown in the chat view)
Topic: where 2026 growth comes from and whether the margin rise is pricing power or cost relief.
Sources: S1 `avl_raw.json` main_business P (product) and D (region), periods 20231231–20260630; S2 raw_income / raw_balancesheet (report_type 1, latest filing per end_date). 亿元 unless stated.

## Correction to round 1
Round 1 said "2026 product split is not in local data." That was wrong: S1 main_business carries **20260630** (H1 2026) as well as 20250630. The fact sheet only prints the latest annual, which hid it. The H1 split is used below; Q3-only product split is still not available locally.

## H1 product split (S1 main_business.P)
| line | H1 2025 rev | H1 2026 rev | yoy | GM H1 2025 | GM H1 2026 |
|---|---|---|---|---|---|
| 能量饮料 | 83.61 | 89.37 | +6.9% | 50.6% | 54.7% |
| 电解质饮料 | 14.93 | 16.72 | +12.0% | 32.1% | 40.6% |
| 茶饮料 | (in 其他) | 10.58 | n/a | — | 23.7% |
| 其他饮料 | 8.77 | 7.59 | −13.5% | 15.4% | 26.0% |
| 其他 | 0.06 | 0.17 | — | — | — |
| total | 107.37 | 124.43 | +15.9% | 45.1% | 48.4% |

- Tea was inside 其他饮料 before 2026 (FY2025 其他饮料 19.86 includes tea; no separate tea line in 2023–2025). Comparable "tea + other drinks" bucket: 8.83 → 18.35, **+108%**. Treat the −13.5% on 其他饮料 alone as a reclassification artifact, not a decline.
- Growth contribution of the +17.06 H1 gain: energy +5.76 (34%), electrolyte +1.79 (10%), tea+other +9.52 (56%).
- Energy share of sales: 77.9% (H1 2025) → 71.8% (H1 2026); FY2023 it was 91.8% (东鹏特饮 103.36 / 112.63).
- Electrolyte deceleration: FY2025 +118% → H1 2026 +12%. The 2025 "second curve" is stalling harder than the flagship in relative terms.
- Two-year energy growth: H1 2024 东鹏特饮 68.55 → H1 2026 89.37 = +30% (≈14%/yr), vs FY2017–25 company CAGR 28%.

## Gross margin: cost relief, not proven pricing power
Energy GM by period: FY2023 45.4% → FY2024 48.3% → FY2025 50.8% → H1 2026 **54.7%** (record high). Overall H1 GM 45.1% → 48.4%. Every line's GM rose. With flagship revenue growth at +6.9%, a 4-point GM jump is more consistent with cheaper inputs (PET, sugar — hypothesis, not verifiable locally) than with price increases. No volume/price split exists in S1/S2 → open question: interim report cost note and any price action.
Q3 2026 overall GM 45.7% (round 1 workpaper) vs H1 48.4% — the margin cushion already narrowed in Q3. Mix (tea at 23.7% GM growing fastest) works the other way once cost relief fades.

## Region (S1 main_business.D) — reclassification caveat
H1 2025 uses old regions (广东 25.46, 广西 7.40, 华东 15.36, 华北 17.08, 华中 13.77, 西南 12.82, 重客及其他 12.53, 线上 2.90). H1 2026 uses 战区 (华南 31.76, 华东 21.07, 华北 17.41, 华中 28.44, 华西 20.96, 其他 4.61). 重客/线上 (15.43 in H1 2025) appears folded into 战区/其他 (4.61) in H1 2026, so region growth rates are not like-for-like. Tentative only: 华南 ≈ 广东+广西 32.85 → 31.76 (−3%) even though ~10 亿 of key-account/online sales may have been re-allocated into the regions — home-market weakness is possible but not provable locally. Low confidence; needs the interim report segment note.

## Normalizing the cost windfall (reverse-curve sensitivity)
TTM energy revenue = FY2025 155.99 + H1 2026 89.37 − H1 2025 83.61 = 161.75; TTM energy GP 85.76 → TTM energy GM 53.0%. Assume the windfall reverts to FY2025's 50.8% (assumption; FY2024 was 48.3%, FY2023 45.4%): pretax drop 161.75 × (53.0% − 50.8%) = 3.59; after tax at 21.4% = 2.83. Core TTM NOPAT 46.01 → 43.18.
Reverse curve (EV 693.2, NOA 45.2, RE0 = core − r·NOA): implied g at 8% = 1.78% (vs 1.4% unadjusted); at 10% = 3.81% (vs 3.4%). So stripping the trailing cost windfall raises the growth the price needs by ~0.4 pt. Forward risk is larger if the H1 run-rate (54.7%) is the base that normalizes; Q3 GM already 45.7% (round 1) shows the cushion fading.

## What this does to round 1's hypothesis
Round 1 knowledge candidate: "a flat 2026 energy line would explain the stall." **Partly rejected**: energy grew +6.9% in H1, not flat; the sharper deceleration is electrolyte (+118% → +12%). The Q3 stall (+0.75% total) comes after H1 +15.9%, so it is a Q3-specific break, not a gradual H1 fade. Q3 product split unavailable → the Q3 mechanism stays open. The "mix dilutes margin" worry is deferred, not confirmed: cost relief currently masks the mix shift.