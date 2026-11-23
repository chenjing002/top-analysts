# John W. Tukey

> Helps when an analysis is stuck because the analyst is answering a precise but wrong question, is reading a raw noisy series as if it were signal, or has let one outlier or one favored "expression" of the data dominate the conclusion.

**Source basis:** `source-files/Thinkers/Ricahrd Hamming/JOHN TUKEY Work on Time Series and Spectrum Analuysis.pdf` — D. R. Brillinger, "John W. Tukey's Work on Time Series and Spectrum Analysis," *Annals of Statistics* 30(6), 2002, pp. 1595–1618. Secondary: Hamming, *The Art of Doing Science and Engineering*, ch. 25 and 30 (Hamming's observations of Tukey's working habits).

Tukey was a statistician, not an investor. The source is a survey of his *time-series* work, so the methods below are those the source actually documents: the maxim on approximate answers, exploratory "detective work," prewhitening, robust/resistant estimation, bounding estimates, multiple expressions of the data, and the overt/covert work cycle. Ideas often attributed to Tukey that this source does **not** contain (e.g., "the data may not contain the answer," box plots, the full EDA toolkit) are not claimed here. All methods are reasoning aids, not evidence.

## 1. When to consult

- Your model produces a sharp, confident number but you suspect the question it answers ("what is fair value under these exact assumptions?") is not the question that matters ("is this business getting better or worse?").
- A single quarter, one-off item, or one extreme data point is driving the whole conclusion (an impairment, a litigation charge, a channel-stuffed quarter).
- You are staring at a raw series—monthly revenue, weekly web traffic, daily price—and "seeing" a trend or cycle you cannot defend.
- Two sources (reported earnings vs. operating cash flow; GAAP vs. adjusted; company vs. competitor disclosures) disagree, and you want to know whether the disagreement is real or within the noise.
- You have only looked at the data one way (one metric, one scale, one time window) and the conclusion feels fragile.
- You have fitted a tidy few-parameter model (constant growth, mean-reverting margin) with no theory to justify it, and are about to extrapolate.
- You have been iterating the same analysis for days without alternating between "look for anything surprising" and "estimate the specific thing."
- The thing you most need to know is the *relationship* between two series (price vs. cost, bookings vs. revenue), but you have been analyzing each in isolation.

## 2. Methods

### 2.1 Approximate answer to the right question

- **What it is.** Tukey's most quoted maxim: "Far better an approximate answer to the right question, which is often vague, than an exact answer to the wrong question, which can always be made precise." The source traces it to his 1947 work on linearizing supersonic-flow equations—replacing an exact but intractable formulation with a guessed form fitted to known solutions. Late in life he said the hard questions were no longer "how to solve it" but "how to formulate it."
- **How to apply.** Reported earnings up, operating cash flow down. The precise-but-wrong question is "what is the exact P/E or EV/EBITDA?"—answerable to two decimals, meaningless if earnings quality is in doubt. The right, vaguer question is "is the business generating more or less cash per unit of economic activity than two years ago?" An approximate answer—cash conversion ratio across several years, with a range rather than a point—tells you whether the earnings number should be trusted at all. Write the right question in one sentence first; then accept an approximate answer to it over a precise answer to the substitute.
- **What it is NOT.** Not an excuse for sloppiness or for refusing to compute. The maxim is about *question selection*, after which Tukey was exacting about computation. Nor does it authorize vague conclusions in the final write-up—the verdict must still be verified in the financials.

### 2.2 Quantitative detective work before estimation

- **What it is.** Tukey ordered the analyst's tasks: "The first task of the analyst of data is quantitative detective work.... His second task is to extract as clearly as possible what the data says about certain specified parameters. His later tasks are to assess the contributions to the uncertainties." The typical pattern of data analysis is "try, look, and try something a little different." Hamming's observation of Tukey adds the habit behind it: turning new information over repeatedly to build many retrieval "hooks."
- **How to apply.** Before modeling the earnings/OCF gap, plot it. Lay out eight to twelve quarters of revenue, net income, OCF, receivables, inventory, payables, and capex side by side; look for the quarter where the series diverged and what else moved then (a new segment, an acquisition, a policy change in the notes). Only then specify the parameter to estimate (e.g., "how much of the gap is receivables stretch?"). Detective work finds *where* to look; estimation measures *how much*. Doing them in the wrong order means estimating the wrong parameter precisely.
- **What it is NOT.** Not an invitation to story-tell from a picture. Detective work generates suspects, not convictions; each suspect is a hypothesis to verify in the filings. Tukey paired exploration with explicit assessment of uncertainty—step three is mandatory.

### 2.3 Prewhitening: remove what you already know before looking at what is left

- **What it is.** In spectrum estimation, Tukey found it "easier to avoid the necessity" of clever smoothing windows by preprocessing the series "to make it more like a sequence of independent identically distributed values"—removing the dominant, already-understood structure (trends, known components) so that what remains can be examined without being swamped. Detrending before analysis is the simplest case. The point generalizes: the residual after removing the expected is where the information is.
- **How to apply.** You cannot see whether OCF is weak because revenue growth mechanically consumes working capital. Prewhiten: compute what working-capital investment *should* have been given revenue growth and historical ratios (the known structure), subtract it, and examine the residual. If the residual is near zero, the gap is explained by growth; if a large residual remains, that residual—not the headline gap—is the thing to investigate (and the footnotes on receivables aging, inventory reserves, or recognition policy are where to verify it). The same move works on margins (remove known mix and input-cost effects) and on share price (remove the sector move).
- **What it is NOT.** Not a model of truth. The "known" structure you remove is itself an assumption; prewhitening can hide a real effect if you subtract too much. Tukey's own caution applies: "it does not pay to try to estimate too much detail, even if the detail is really there." State what you removed and why.

### 2.4 Robust / resistant estimation (medians, not means, when one point can lie)

- **What it is.** Tukey introduced running medians and median filtering—replacing each point with the median of its neighbors—because they "reduce spiky noise" while preserving genuine jumps. He defined robust/resistant techniques as those "that continue to work well even when there are substantial departures from the assumptions used in their construction." The motivating anecdote: "one dust speck could flatten the low portion of a naive spectrum drowning out important information." He also preferred noise *rejection* to signal *enhancement*: "far better to choose them to cancel out the noise."
- **How to apply.** A five-year average margin or growth rate is being dragged by one anomalous year (a pandemic quarter, a one-time gain, a restructuring). Replace the mean with a median or a trimmed mean and see whether the conclusion survives. For the earnings/OCF divergence: compute the cash-conversion ratio each quarter and look at the median and spread, not the sum—one quarter of channel stuffing or one large deferred-revenue inflow should not be allowed to set the picture. If the conclusion flips between mean and median, the conclusion is being made by one data point; find that point and verify it directly.
- **Signal or noise? Ask what a repetition would look like.** Tukey's working definitions: a signal is something where "a repetition would be an exact copy"; noise is something where "a repetition would have only statistical characteristics in common with the original." For a company datum, ask: if this quarter were run again under the same conditions, would this item recur in the same form (a structural cost, a contractual payment) or only in distribution (a bad-debt charge, an FX swing)? Only the first kind belongs in a run-rate.
- **What it is NOT.** Not a way to discard inconvenient data. The outlier is often the most informative observation (Tukey's own example is an anomaly discovered precisely because the method made it visible). Robustness means the *summary* is not hostage to one point; the point itself still gets investigated.

### 2.5 Bounding estimates ("touch estimation")

- **What it is.** Rather than one estimate, Tukey proposed computing two with opposite biases—"choose two windows, one with all positive side lobes and another with all negative side lobes"—so that "the difference of the corresponding spectral estimates makes clear where we ought to recalculate." The estimates are meant "to touch ... not enclose, the curve": a bracket that shows where the method itself is unreliable.
- **How to apply.** Rather than one normalized-earnings figure, compute two with known opposite biases: one treating all "non-recurring" items as truly non-recurring, one treating them as recurring; one capitalizing R&D, one expensing it; one on reported OCF, one on OCF less stock-based compensation and capitalized costs. Where the two brackets are close, the conclusion is insensitive to the judgment call and you can move on. Where they diverge widely, that is exactly the line item that needs primary-source verification—you have located the decision that matters instead of debating all of them.
- **What it is NOT.** Not a confidence interval and not a valuation range to present to a client. The bracket is diagnostic—it points at where to spend verification effort—not a statement about the probability distribution of value.

### 2.6 Multiple expressions, then alternate overt and covert analysis

- **What it is.** Tukey knew "of no field where data analysis has progressed even moderately far toward sophistication where only one expression of the data has been found worthy of being looked at"—reexpression (logs, ratios, differences, per-unit forms) is standard. He also described a work cycle: "(i) initial overt analysis, (ii) repeated covert analysis, (iii) another spell of overt analysis, and so on"—overt meaning open-ended discovery ("where the current model seems to fail most seriously"), covert meaning efficient estimation inside a settled model. And he preferred relationships over levels: "measuring relationship is almost always more rewarding than measuring relative contribution to variability."
- **How to apply.** You have looked at the earnings/OCF gap only in dollars. Reexpress: as a ratio (OCF/NI), as a per-unit figure (cash per customer or per unit shipped), as a difference from the industry median, in log growth rates. A gap that looks alarming in dollars may be flat as a ratio; or a flat ratio may hide a deteriorating per-unit trend. Then alternate: an overt pass (does any expression show something the model does not explain?), a covert pass (estimate the one parameter you now care about), another overt pass (did the estimate create a new anomaly?). Finally, analyze the *relationship*—does OCF track bookings with a lag, or has the coupling broken?
- **What it is NOT.** Not a license to try expressions until one supports the thesis (the multiplicity problem Tukey himself flagged). Decide the expressions in advance, report all of them, and treat agreement across expressions as reassurance and disagreement as a question—never as a menu.

## 3. Anti-patterns this thinker warns against

- **Reading the raw series.** "More lives have been lost looking at the raw periodogram than by any other action involving time series!" An unsmoothed, unprocessed series will show apparent cycles and trends that are noise. Smooth, detrend, and look at sampling variability before believing a pattern.
- **Few-parameter models without theory.** Tukey argued "against the use of few-parameter models ... unless there is well-grounded theory for the model." Constant-growth or mean-reversion assumptions are such models; they need a business reason, not just a good fit.
- **Overestimating detail.** "It does not pay to try to estimate too much detail, even if the detail is really there." Precision beyond what the data supports is false precision.
- **Optimism unrestrained by variability.** The analyst needs "indications of sampling variability to restrain his optimism about the reality of apparent results." Four quarters of improvement is a small sample.
- **Unexamined stationarity.** "No known phenomenon is precisely periodic" and no real series is purely stationary; a business in 2024 is not the same process as in 2019. Comparability across regimes must be argued, not assumed.
- **One expression only.** Looking at the data a single way and treating the result as settled.
- **Signal enhancement over noise rejection.** Trying to amplify the story you want rather than first removing the known contaminants.
- **Optimization as a reflex.** "To try to tell modern engineers that optimization is not the wave of the near future may perhaps be a little unpalatable"—resistant, approximate methods often beat optimal ones that assume a model that is not true.
- **Models mistaken for truth.** "Models should not be true but it is important that they be applicable." Judge a valuation model by whether it is useful for the decision, not by whether it is "correct."
- **Entering spectrum-style analysis casually.** "Spectrum analysis is to be entered upon advisedly and with care." The same holds for any sophisticated time-series or factor technique applied to financial data: the data are short, noisy, and nonstationary.

## 4. Worked invocation (protocol trace)

A compressed example of the README protocol using this file. Company Y: twelve quarters of data; net income trending up smoothly; operating cash flow erratic, with one very weak quarter (Q7) and one very strong one (Q10). The analyst has concluded "cash flow is deteriorating" twice and is not sure the conclusion is real.

1. **Obstacle.** Same answer repeating; suspicion that two extreme quarters are driving it.
2. **Thinker / method.** Tukey 2.4 (robust summary) then 2.3 (prewhiten) then 2.5 (bounding estimates).
3. **Apply 2.4.** Compute quarterly OCF/NI; compare mean (dragged by Q7) with median. If the median conversion is stable near 1.0 and only the mean falls, the "deterioration" is two data points. Investigate Q7 and Q10 individually in the filings (one large customer prepayment? a litigation settlement?).
4. **Apply 2.3.** Remove the known structure: seasonal working-capital pattern evident in Q4s and the mechanical build from revenue growth. Examine the residual series. Is there a drift left after removal?
5. **Apply 2.5.** Produce two conversion estimates with opposite biases—one treating stock-based compensation and capitalized development as cash costs, one not. If the brackets agree, the judgment call does not matter; if they diverge, that line item is the thing to verify.
6. **Output.** `[reasoning method, not evidence — Tukey 2.4/2.3/2.5]` Reframed question: "Is there a downward drift in cash conversion after removing Q7, Q10, seasonality, and growth-driven working capital?" Items to verify: Q7 and Q10 cash-flow footnotes; capitalized-software roll-forward; SBC as a share of OCF.
7. **Return to verification.** Pull the quarterly notes and recompute. Record confirm / refute / open. Until then the reframed question has no evidentiary weight.

## 5. Pairing note

Tukey and Hamming worked side by side at Bell Labs and the two files are complementary. Use Tukey when the stall is about *how to look at the data*—noise vs. signal, outliers, which expression, what to remove first. Use Hamming when the stall is about *the question, the assumptions, or the system*—wrong problem, unexamined "impossible," metric gaming, untrusted inputs. If both apply, fix the question with Hamming first, then examine the data with Tukey. Do not run them in parallel to manufacture agreement; two methods pointing the same way is still zero pieces of evidence.

## 6. Source anchors

File: `JOHN TUKEY Work on Time Series and Spectrum Analuysis.pdf` (Brillinger 2002; Annals page numbers; all quotes are Tukey's words as reproduced by Brillinger unless marked [B] for Brillinger's own text).

| Page | Quote |
| --- | --- |
| 1597 | "Far better an approximate answer to the right question, which is often vague, than an exact answer to the wrong question" |
| 1599 | "the researcher's need for indications of sampling variability to restrain his optimism about the reality of apparent results" |
| 1599 | [B] Tukey argued "against the use of few-parameter models for the power spectrum unless there is well-grounded theory for the model." |
| 1600 | "it turned out ... to be easier to avoid the necessity for their use" (on prewhitening replacing window design) |
| 1600 | [B] "In prewhitening one preprocesses the series to make it more like a sequence of independent identically distributed values" |
| 1603 | "when examined under a microscope, no known phenomenon is precisely periodic." |
| 1603 | "It may pay not to try to describe in the analysis the complexities that are really present in the situation." |
| 1603 | "it does not pay to try to estimate too much detail, even if the detail is really there." |
| 1603 | "try, look, and try something a little different as the typical pattern of data analysis." |
| 1604 | "choose two windows, one with all positive side lobes and another with all negative side lobes ... makes clear where we ought to recalculate" |
| 1605 | "I, for one, place meaningfulness and understandability before efficiency or information content." |
| 1605 | "measuring relationship is almost always more rewarding than measuring relative contribution to variability." |
| 1605 | "It is good to choose coefficients to magnify the signal, but is far better to choose them to cancel out the noise." |
| 1607 | "Models should not be true but it is important that they be applicable." |
| 1608 | signal: "a repetition would be an exact copy"; noise: "a repetition would have only statistical characteristics in common with the original." |
| 1609 | "We have gained arithmetic speed and an ability to make more subtle analysis routine, but the name of the game is still the same." |
| 1609 | "The first task of the analyst of data is quantitative detective work" |
| 1609 | "Often the purpose of good analysis is not so much to do well in catching what you want but rather to do well ... in rejecting what you don't want." |
| 1609 | "The adaptive approach is vital to learning about frequencies." |
| 1610 | "of no field where data analysis has progressed even moderately far toward sophistication where only one expression of the data has been found worthy of being looked at." |
| 1610 | "the overriding importance of noise 'rejection' over signal 'enhancement' deserves special attention." |
| 1610 | "To try to tell modern engineers that optimization is not the wave of the near future may perhaps be a little unpalatable." |
| 1610 | [B] median filters "reduce spiky noise, and they preserve jump discontinuities (edges)." |
| 1610 | "Spectrum analysis is to be entered upon advisedly and with care." |
| 1611 | "More lives have been lost looking at the raw periodogram than by any other action involving time series!" |
| 1611 | [B] "one dust speck could flatten the low portion of a naive spectrum drowning out important information." |
| 1612 | "(i) initial overt analysis, (ii) repeated covert analysis, (iii) another spell of overt analysis, and so on." |
| 1612 | "lack of gaining an understanding of where the current model seems to fail most seriously" |
| 1612 | "the most difficult questions are not 'how to solve it' but rather either 'how to formulate it,' or how do we extend applicability" |
| Hamming ch. 25, line 3248 | "he was more in the habit than I was of turning over new information again and again, so his 'hooks' for retrieval were more numerous" |
