---
name: observe
description: Run the Observer on a round, or validate and apply pending proposals to expert role files. Usage: /observe <ts_code> <session_id> <round> | /observe proposals
---

Arguments: `$ARGUMENTS`. Protocol in `observer/OBSERVER.md`; orchestrator steps in `CLAUDE.md` §3 and §6.

- `<ts_code> <session_id> <round>`: spawn one subagent with `observer/OBSERVER.md`, the round JSON, the
  session fact sheet and the participating experts' role files. It writes `observer/round-NN.md` in the
  session folder and, when it has two cited instances, a proposal in `observer/proposals/` with status
  `proposed`. Then `scripts/sync.sh "<ts_code> <session_id> observer round NN"`.
- `proposals`: for each `observer/proposals/*.md` with status `proposed`, spawn a *fresh* reviewer with
  only the proposal, the target role file and the cited round files. It fills `## Validation` and sets
  status `validated` or `rejected`. For each validated proposal (max one per expert per session) apply
  the change to the role file, bump the version, add the §9 changelog line naming the proposal file,
  set status `applied` with the commit hash after `scripts/sync.sh "apply proposal <file>"`.

Report: verdicts, weaknesses by severity, proposals filed/validated/applied, and the suggested next question.
