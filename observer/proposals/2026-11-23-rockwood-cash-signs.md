# Proposal: Use consistent signs in the content cash-flow bridge

**Status:** proposed
**Kind:** correction
**Filed:** 2026-11-23 by Codex during role-card review
**Target:** experts/rockwood.md → §3.3 Restate the cash flow statement
**Evidence:**
- §3.3 describes Netflix cash content spend as `$(132B)`. Its FCF formula then subtracts content capex without specifying a sign conversion. Given adjusted OCF of $142B, literal substitution yields $274B before PP&E capex, while reported OCF before that capex is $10B.
- `source-files/Rockwood/media-accounting.md`, Netflix section, reports the $10B, $142B, and $(132B) figures for 2011–2024. The Disney section uses the cash-spend magnitude from the footnote and adds it to reported OCF.

## Change

Replace the formula block in §3.3 with the following.

```text
Reclassified spend = magnitude of the cash outflow included in reported OCF
                     Netflix: negate the sum of the two signed content cash-flow lines
                     Disney FY24: use the footnote spend of 23,435 million dollars
Adjusted OCF       = Reported OCF + Reclassified spend
Content capex      = Reclassified spend, shown as a positive outflow
Adjusted FCF       = Adjusted OCF − PP&E capex − Content capex
                     PP&E capex is a positive outflow separate from content capex.
```

## Risk

This convention applies only to content cash outflows moved from operating to investing. Check for overlap with other capex lines when adapting the bridge to a new company.

## Validation

Awaiting an independent reviewer.
