---
name: observe
description: Audit a completed Top Analysts research round or independently review pending proposals to change expert role cards.
---

# Observe a research round

Read `AGENTS.md` and `observer/OBSERVER.md`. Identify the round from the user's request, for
example `observe 600519.SH 2026-11-23-01 1`. Use `observe proposals` for pending role-card changes.

## Review a round

- Resolve the round JSON, the session fact sheet and the participating role cards. Give those inputs
  and `observer/OBSERVER.md` to an independent reviewer when the host supports and authorizes one.
- Write the verdict, evidence spot checks, weaknesses and suggested next question in
  `sessions/<ts_code>/<session_id>/observer/round-NN.md`. Follow the proposal criteria in the
  Observer protocol for any proposed role-card change. Return the verdict, severity of weaknesses,
  proposals filed, and next question.
- Check the workflow rules the round should have met: in round one, the business scorecard
  (great/good/gruesome, 10-year FCF vs profit, capex and depreciation, DuPont, valuation against
  book and the downside floor) was done before the news topic; turns are short, one idea each, and
  end with one concrete question; the round stayed on one topic. Report each miss as a weakness.
- If an independent reviewer is unavailable, do a self-review and label it as such. Leave any
  proposals pending independent validation. If the inputs are supplied in chat, return the review
  there when the host has no writable checkout.
- Publish a standalone review only when authorized, using `scripts/sync.sh` after checking the
  scope of the changes it will stage. The Analyze workflow handles publishing for reviews run within a round.

## Review proposals

- For each pending proposal, give a fresh reviewer the proposal, target role card and cited rounds
  or source evidence. Follow the four validation checks in `observer/OBSERVER.md` and record
  `validated` or `rejected` with the rationale. Leave the status pending if a fresh reviewer or
  the required evidence is unavailable.
- Apply validated edits through the same protocol, observing its one-change-per-expert limit. Bump
  the version, record the proposal in the changelog, and validate the repository. Record the commit
  hash when one exists. Report the proposals filed, validated, rejected, or applied.
