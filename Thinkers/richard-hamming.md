# Richard Hamming

> Helps when an analysis is stuck because the *question* is wrong, the data is trusted too much, or the analyst has quietly optimized a component instead of the whole.

**Source basis:** `source-files/Thinkers/Ricahrd Hamming/The Art of Doing Science and Engineering.md` (chapters 1, 5, 13, 16, 20, 25–30).

Hamming is not an investor. He supplies *style of thinking*—his own phrase for the book's content. Everything below is a reasoning method, not evidence. Any hypothesis it produces must go back to filings, cash-flow reconciliation, and primary sources before it counts.

## 1. When to consult

- Two reputable sources give incompatible numbers for the same quantity (e.g., segment margins in the 10-K vs. the investor deck) and you are about to "average" them.
- You have re-run the same valuation three times with more inputs and the answer keeps coming back the same—yet you still do not believe it.
- Management, a sell-side consensus, or your own prior says something is "impossible" (cannot lose share, cannot cut the dividend, cannot be disrupted) and you have not inspected the assumptions behind the impossibility.
- You are tuning one metric (ROIC, FCF yield, a DCF terminal value) to perfection while the thesis as a whole has drifted out of view.
- A headline statistic (TAM, market-share claim, growth rate) feels plausible but you have never checked whether it is even arithmetically compatible with other known numbers.
- You are about to accept a time series (inventory days, unemployment-like macro indicators, "adjusted" EBITDA) across a period where the definition of the thing measured may have changed.
- You have a model whose output matches your prior suspiciously well and you cannot say what would have falsified it.
- A KPI the company reports (or that you track) is shaping behavior—theirs or yours—more than it is describing reality.

## 2. Methods

### 2.1 Back-of-the-envelope compatibility check

- **What it is.** Hamming observes that great scientists do quick quantitative modeling far more often than ordinary ones: take two claimed figures, build the simplest model that links them, and see whether they are compatible. The point is not precision but a "feeling for the truth or falsity of what was claimed" and discovering "which factors you were inclined not to think about." First use definite numbers you have a feel for, then redo it with parameters.
- **How to apply.** A company reports revenue up 18% and operating cash flow down 12%. Before building a thesis, write the simplest bridge: revenue growth × historical cash-conversion rate should give roughly expected OCF; the gap is the quantity to explain. Then parameterize: how many days of receivables stretch, or how much inventory build, would it take to produce the gap? If 25 extra DSO days is needed and reported DSO rose by 6, the stated explanation ("timing") cannot be the whole story—you now know which line items to verify in the cash-flow statement and footnotes.
- **What it is NOT.** Not a valuation, not an estimate you may cite. It tells you *which* question to ask the filings, not the answer. If the envelope says "compatible," that is weak evidence of nothing; proceed to verification anyway.

### 2.2 "If I had a solution, what would it look like?"

- **What it is.** Hamming's stated move when stuck: ask what the solution *must* involve. "What must the solution involve? Are there conservation laws which must apply? Is there some symmetry? How does each assumption enter into the solution, and is each one really necessary? Have you recognized all the relevant factors?" The question is designed to expose approaches "you had subconsciously ignored."
- **How to apply.** You cannot decide whether rising reported earnings with falling operating cash flow is benign. Ask: if the benign explanation were true, what would the evidence necessarily look like? A conservation law applies—cash does not disappear; it must be in working capital, capex, acquisitions, or financing. A benign story (growth-driven working-capital build) predicts: receivables growing in line with revenue, inventory turns stable, no change in revenue-recognition policy, the gap reversing within a few quarters. Write that checklist *before* you look, then check each item. A malign story predicts the opposite pattern plus a policy change in the notes. You have turned a feeling into a falsifiable spec.
- **What it is NOT.** Not permission to fit the problem to the answer you like. Hamming notes "maybe the problem needs to be altered to fit the solution! That has happened!"—he reports it as a hazard, not a technique. The specification you write must be committed before you open the data.

### 2.3 Invert the problem

- **What it is.** When blocked, Hamming inverted the formulation: lacking an "acre of programmers," he asked why the machine itself could not do the detail work, turning a defect into an asset. "When stuck, often inverting the problem and realizing the new formulation is better represents a significant step forward." He also changed a problem from "getting answers" to "demonstrating something," which changed what counted as success.
- **How to apply.** Your question "is this stock cheap?" keeps producing the same inconclusive answer. Invert: "what would have to be true for the current price to be *fair*?" Back out the implied growth, margin, and duration from the price; now the analysis is a verification task—are those implied figures consistent with the company's history, its industry, and the cash-flow trend you already distrust? Or invert the burden: instead of proving earnings quality is good, list what you would need to see to prove it is *bad*, and go look for exactly that.
- **What it is NOT.** Not a reason to abandon the original question. Inversion produces a *new question*, which still requires the same financial verification. It is also not "contrarianism"—the inverted question may well confirm the consensus.

### 2.4 Inspect the assumptions behind any "impossible"

- **What it is.** "All impossibility proofs must rest on a number of assumptions which may or may not apply in the particular situation." Hamming's own failure: he remembered the FFT was a "bad idea" but forgot *why*—the reason was his equipment at the time, and equipment changed. His rule: when you know something cannot be done, "also remember the essential reason why," so that when circumstances change you re-examine instead of repeating the verdict.
- **How to apply.** The thesis rests on "this incumbent cannot be displaced—switching costs are too high." Write down the exact assumptions that make that true (customer integration depth, contract length, regulatory moat, no substitute at comparable price). Then for each assumption ask what has changed since it was first established. If the "cannot" was established in 2016 and two of its four supports have since eroded, you no longer have a moat argument; you have a hypothesis to test against churn data, pricing disclosures, and competitor filings.
- **What it is NOT.** Not an argument that every moat is fragile or every consensus is wrong. Hamming's companion rule is that an expert saying something *can* be done "is probably correct." The method is asymmetric: it targets confident negatives, not all claims.

### 2.5 Distrust the data, test for consistency first

- **What it is.** "Data is generally much less accurate than it is advertised to be." Hamming learned "never to process any data until I had first examined it carefully for errors," and to "pretest it for consistency and outliers at a minimum." Specific hazards: measuring instruments trusted because they carry a label; the same machine that produces the activity also records it; definitions that change silently over time (his inventory-reporting and poverty-line examples); careful estimates combined with wild guesses, with the reliability of the careful part transferred to the sum.
- **How to apply.** Reported earnings rise, OCF falls. Before interpreting, test consistency: does the cash-flow statement tie to balance-sheet changes? Did the company change inventory method, revenue recognition, or segment definitions in the period (the "definition drift" hazard)? Is the earnings figure "adjusted" by the same management whose incentives it serves (the machine recording itself)? Is your model combining audited numbers with a management growth target and treating the blend as audited? Only after these checks does the earnings/OCF divergence become a fact worth explaining rather than an artifact to be cleaned.
- **Inspect the definition, not just the number.** Hamming's companion rule from the information-theory chapter: "the initial definitions determine what you find," and definitions "should be inspected, not only when first proposed, but much later, when you see how they are going to enter into the conclusions drawn." Ask of any metric: who defined it, under what conditions, and to get what result? "Adjusted EBITDA," "organic growth," and "core earnings" are definitions first and measurements second.
- **What it is NOT.** Not a license for nihilism ("all data is bad, so use intuition"). Hamming's answer to bad data is *more careful* verification, smaller well-chosen samples, and explicit tracking of each input's reliability—not less verification. Hamming's rule ("90% of the time, the next independent measurement will fall outside the previous 90% confidence limits") is a memorable exaggeration, by his own admission, not a statistic.

### 2.6 You get what you measure / don't optimize the component

- **What it is.** Two linked systems rules. First: "the way you choose to measure things controls to a large extent what happens"—his example is quarterly bottom-line focus producing short-termist companies; and "accuracy of measurement tends to get confused with relevance of measurement." Second: "If you optimize the components, you will probably ruin the system performance." Solutions that solve "the wrong problem correctly" are common; a good solution "should bring further understanding of the problem."
- **How to apply.** You have spent two days perfecting the WACC and terminal multiple. Step back: what is the *system* question—whether the business earns its cost of capital durably, or whether the price offers a margin of safety given what you do not know? If the earnings/OCF gap is unexplained, a precise terminal value is a component optimized while the system is broken. Separately, ask what management is measured on (EPS targets? revenue growth? adjusted EBITDA?) and whether the metric you distrust is exactly the one their compensation rewards—that is the "you get what you measure" prediction, and it tells you where to look for pressure on the numbers.
- **What it is NOT.** Not an excuse to skip rigorous component work. Hamming insists systems engineering "must be built on a solid ground of classical simplification to definite problems." The method decides *which* precise work matters now; it does not replace it.

## 3. Anti-patterns this thinker warns against

- **Solving the wrong problem correctly.** A rigorous model of an irrelevant question. Ask "What is the total problem in which this part is to fit?" before refining.
- **The Rorschach simulation.** Adjusting model parameters until the output matches what you wanted, then treating the output as evidence. Hamming: "Did he merely find what he wanted to find, or did he get at 'reality'?" Traditional science has safeguards (pre-registration, blinding) that analysts routinely skip.
- **Never saying "there is no signal."** In the random red/green-light experiment, no Bell Labs scientist ever concluded there was no pattern. Analysts are trained to find stories; they are rarely trained to say "this is noise."
- **"Get more data" as avoidance.** Hamming calls it "a favorite trick of people in charge who do not want to bear the responsibility." Sometimes the decision needs a reframed question, not another dataset.
- **Expert certainty without inspecting the basis.** The two faults of experts: "(1) the expert is certain they are right, and (2) they do not consider the basis for their beliefs and the extent to which they apply to new situations." Includes yourself. Ask "What would you accept as evidence you are wrong?"
- **Confusing accuracy with relevance.** Grabbing the hard, measurable number (reported EPS) over the soft, relevant one (durability of the franchise).
- **Combining careful estimates with wild guesses** and inheriting the reliability of the careful part.
- **Tuning for low variance and calling it accuracy.** Experimenters adjust equipment "so you get consistent runs" and hand the statistician low-variance data; the claimed precision is an artifact. A model whose inputs were adjusted until the outputs looked stable has the same problem.
- **Horizon bias in forecasts.** "Short-term predictions are always optimistic and long-term predictions are always pessimistic"—compounding is hard to grasp, so multi-year growth and multi-year erosion are both routinely underestimated; near-term guidance is routinely over-believed.
- **Definition drift in time series.** Comparing "adjusted" figures or segment data across periods where the definition changed without saying so.
- **Monomaniacal pursuit.** If a question has produced the same answer repeatedly, Hamming's creativity chapter says temporary abandonment often works better than more force; return with a changed formulation.
- **Not tolerating ambiguity.** Great people "can both believe and disbelieve at the same time." Holding a thesis and its falsifier simultaneously is a skill, not a failure of conviction.

## 4. Worked invocation (protocol trace)

A compressed example of the README protocol using this file. Company X: reported EPS +22% YoY for three quarters; operating cash flow -9% over the same period; management cites "timing of collections."

1. **Obstacle.** Conflicting evidence; two re-reads of the 10-Q produced the same "probably timing" conclusion I do not trust.
2. **Thinker / method.** Hamming 2.2 ("what would a solution look like?") then 2.5 (consistency test).
3. **Apply 2.2.** If "timing" were true, the data must show: DSO up but inventory turns and payables stable; no revenue-recognition policy change in the notes; the gap reversing within two quarters; no change in the proportion of revenue from new, long-dated contracts.
4. **Apply 2.5.** Check consistency before interpreting: does ΔOCF reconcile to Δworking capital on the balance sheet? Did any definition change (segment, "adjusted" bridge, contract-asset classification)?
5. **Output.** `[reasoning method, not evidence — Hamming 2.2/2.5]` Hypothesis: the gap is driven by growth in contract assets (unbilled revenue) rather than receivables; this would be inconsistent with "collection timing." Specific items to verify: contract-asset roll-forward note, revenue-recognition policy section, DSO vs. unbilled-days split.
6. **Return to verification.** Pull the notes; compute unbilled days for six quarters; compare to peers. Record confirm / refute / open. Nothing above is evidence until that step completes.

## 5. Pairing note

Hamming and Tukey were colleagues and the two files are complementary, not interchangeable. Use Hamming when the stall is about the *question, the assumptions, or the system* (wrong problem, unexamined "impossible," metric gaming). Use Tukey when the stall is about *how to look at the data* (noise vs. signal, outliers, which expression, what to remove first). If both apply, run Hamming first to fix the question, then Tukey to examine the data; do not run them in parallel to manufacture agreement.

## 6. Source anchors

File: `The Art of Doing Science and Engineering.md` (line numbers from the markdown).

| Chapter | Line | Quote |
| --- | --- | --- |
| 1 Orientation | 161 | "Style of thinking is the center of the course." |
| 1 Orientation | 213 | "you get a good feeling for the truth or falsity of what was claimed, as well as realize which factors you were inclined not to think about" |
| 1 Orientation | 254 | "Short-term predictions are always optimistic and long-term predictions are always pessimistic." |
| 5 History of computer applications | 544 | "The purpose of computing is insight, not numbers." |
| 13 Information theory | 1946 | "All definitions should be inspected, not only when first proposed, but much later, when you see how they are going to enter into the conclusions drawn." |
| 13 Information theory | 1948 | "the initial definitions determine what you find, much more than most people care to believe" |
| 16 Digital filters—III | 2445 | "when you know something cannot be done, also remember the essential reason why" |
| 20 Simulation—III | 2840 | "you are seldom taught to replace a nice theory with nothing but randomness!" |
| 20 Simulation—III | 2842 | "'Get more data,' they say." (described as "a favorite trick of people in charge who do not want to bear the responsibility") |
| 20 Simulation—III | 2846 | "Did he merely find what he wanted to find, or did he get at 'reality'?" |
| 25 Creativity | 3238 | "When stuck I often ask myself, 'If I had a solution, what would it look like?'" |
| 25 Creativity | 3258 | "If you cannot drop a wrong problem, then the first time you meet one you will be stuck with it for the rest of your career." |
| 26 Experts | 3284 | "All impossibility proofs must rest on a number of assumptions which may or may not apply in the particular situation." |
| 26 Experts | 3290 | "If an expert says something can be done he is probably correct, but if he says it is impossible then consider getting another opinion." |
| 26 Experts | 3312 | "What would you accept as evidence you are wrong?" |
| 27 Unreliable data | 3340 | "data is generally much less accurate than it is advertised to be" |
| 27 Unreliable data | 3358 | "never to process any data until I had first examined it carefully for errors" |
| 27 Unreliable data | 3374 | "you adjust for low variance; what else can you do? But it is this low-variance data you turn over to the statistician" |
| 27 Unreliable data | 3378 | "90% of the time, the next independent measurement will fall outside the previous 90% confidence limits!" |
| 27 Unreliable data | 3384 | "Careful estimates are combined with wild guesses, and the reliability of the whole is taken to be the reliability of the engineering part." |
| 27 Unreliable data | 3394 | "This is a problem in all time series. The definition of what is being measured is constantly changing." |
| 28 Systems engineering | 3450 | "If you optimize the components, you will probably ruin the system performance." |
| 28 Systems engineering | 3536 | "I have seen many, many solutions offered which solved the wrong problem correctly." |
| 29 You get what you measure | 3546 | "the bottom line of the profit and loss statement every quarter ... produces a company interested mainly in short-term profits" |
| 29 You get what you measure | 3554 | "Accuracy of measurement tends to get confused with relevance of measurement" |
| 30 You and your research | 3656 | "When stuck, often inverting the problem and realizing the new formulation is better represents a significant step forward." |
| 30 You and your research | 3670 | "Great people can tolerate ambiguity; they can both believe and disbelieve at the same time." |
