# Thinkers

Thinkers are **not** investment experts. They supply reasoning methods that an analyst (an `experts/` persona) consults when analysis stalls: conflicting evidence, uncertainty about how to proceed, or a question that keeps producing the same answer.

> When analysis stalls, improve the way experts think—not merely the amount of information they collect.

A borrowed method is a way of asking; it is never a fact. Anything a thinker produces must be labeled `[reasoning method, not evidence]` and must return to financial verification before it enters a conclusion.

## Index

| Thinker | File | Named methods | Consult when… |
| --- | --- | --- | --- |
| Richard Hamming | [richard-hamming.md](richard-hamming.md) | 2.1 Back-of-the-envelope compatibility check · 2.2 "If I had a solution, what would it look like?" · 2.3 Invert the problem · 2.4 Inspect the assumptions behind any "impossible" · 2.5 Distrust the data, test for consistency first · 2.6 You get what you measure / don't optimize the component | Two sources give incompatible numbers; the same valuation keeps returning the same answer you don't believe; a thesis rests on "cannot happen"; you are polishing one metric while the whole thesis drifts; a time series may have changed definition; a model's output matches your prior too well; a KPI is shaping behavior more than describing it. |
| John W. Tukey | [john-tukey.md](john-tukey.md) | 2.1 Approximate answer to the right question · 2.2 Quantitative detective work before estimation · 2.3 Prewhitening (remove the known, examine the residual) · 2.4 Robust/resistant estimation · 2.5 Bounding estimates ("touch estimation") · 2.6 Multiple expressions, then alternate overt/covert analysis | Your model gives a precise answer to what may be the wrong question; one quarter or one item drives the whole conclusion; you "see" a trend in a raw noisy series; earnings and cash flow disagree and you don't know if it's noise; you've looked at the data only one way; you've fitted a tidy model with no business theory; you need the relationship between two series, not each in isolation. |

## Protocol: how an expert invokes a thinker

1. **State the obstacle** in one sentence: what is stuck and why (conflicting evidence / no path forward / same answer repeating).
2. **Pick one thinker** (two at most) whose "consult when…" column matches the obstacle. Do not browse all of them.
3. **Apply one named method** from that file, following its "How to apply" step literally, including the "What it is NOT" guardrail.
4. **Produce an output of exactly one kind:** a reframed question, a new falsifiable hypothesis, or a specific line item / document to verify.
5. **Label it** `[reasoning method, not evidence]` with the thinker and method number, e.g. `[reasoning method, not evidence — Hamming 2.3]`.
6. **Return to financial verification:** take the reframed question or hypothesis to filings, cash-flow reconciliation, footnotes, or primary sources. The thinker's output has no evidentiary weight of its own.
7. **Record the result** in the analysis: whether verification confirmed, refuted, or left open the hypothesis. If the method produced nothing useful, say so and stop; do not stack thinkers to force an insight.

Do not use a thinker to: justify a conclusion already reached, replace a number you could look up, or add rhetorical authority ("as Tukey said…") to an unverified claim.

## Source files

`source-files/Thinkers/Ricahrd Hamming/` — *The Art of Doing Science and Engineering* (Hamming, full text, markdown); Brillinger, "John W. Tukey's Work on Time Series and Spectrum Analysis," *Annals of Statistics* 2002 (PDF). Both thinker files cite chapter/page and line numbers so quotes can be checked.
