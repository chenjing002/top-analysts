# Proposal: <short title>

**Status:** proposed
**Kind:** improvement | correction
**Filed:** YYYY-MM-DD by <reviewer or Observer; session/round if applicable>
**Target:** experts/<slug>.md → §<n> <section name>
**Evidence:**
- <ts_code>/<session_id> r<N> · <expert> · turn <N> — "<≤30-word excerpt>" — what it shows
- <ts_code>/<session_id> r<N> · <expert> · turn <N> — "<≤30-word excerpt>" — what it shows

For a correction, replace the two round references with the affected passage and a source locator or reproducible calculation.

## Change

Exact text. Use a diff-like form:

```
- old line (if replacing)
+ new line [observer-added, from <session> r<N>]
```

## Risk

What this could make worse, and why it is still worth doing.

## Validation

(filled by the independent reviewer; required before status → validated)

1. Cited statements or source evidence show the claim: yes/no — note
2. No contradiction with §8 anchors or §1 scope: yes/no — note
3. Not already covered by another expert: yes/no — note
4. `scripts/validate.py` passes on a scratch copy: yes/no
**Verdict:** validated | rejected — reason

## Applied

(filled by the orchestrator) version a.b → a.c, commit <hash>, date.
