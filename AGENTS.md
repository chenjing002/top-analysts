# Top Analysts

This repository runs multi-expert equity research on Chinese A-share companies, one question per
round. Expert statements use English, with Chinese accounting terms in parentheses on first use.
Answer the user in their language.

## Start here

Open the relevant workflow from the repository root. Plain-language requests work on any host
with access to the files.

| Request | Workflow |
|---|---|
| Start, continue, or close a company analysis | [Analyze](skills/analyze/SKILL.md) |
| Audit a completed round or review expert proposals | [Observe](skills/observe/SKILL.md) |

| Path | Contents |
|---|---|
| [`experts/`](experts/) | Eight source-based role cards. See the [expert directory](README.md#the-experts) and [role template](experts/_TEMPLATE.md). |
| [`Thinkers/`](Thinkers/README.md) | Reasoning methods to consult when analysis stalls. |
| [`knowledge/`](knowledge/README.md) | Shared facts, methods, and hypotheses with provenance. |
| [`observer/`](observer/OBSERVER.md) | Review protocol and versioned proposals for changes to role cards. |
| [`data/`](data/DATA_DICTIONARY.md) | Fact-sheet generator and S1/S2 definitions. |
| [`sessions/`](sessions/SCHEMA.md) | Session and round schema. `sessions/index.json` feeds the site. |
| `site/`, `scripts/` | Static viewer, renderer, index builder, validator, and publishing script. |
| `source-files/` | Expert source material. Treat it as read-only. |

## Shared rules

- Ground every discussion in the company's long financial record — the full 10-year S1 annual
  blocks and the S2 series over the same recent 10 years (older S2 history back to FY2008 is
  queried only when a live question needs it). A recent quarter is read against the decade that
  produced it, never as the default subject on its own.
- Big picture first. Every round and every conclusion leads with the insight that matters for the
  investment judgment — what the business is, what the decade shows, what the price assumes — and
  backs it with a few anchor numbers. Detailed calculations and reconciliations support that story
  in the workpaper; they do not become the discussion unless they change the conclusion.
- Discussion turns read as a group chat: plain, conversational, in clear accessible language.
  Length follows the content — a turn can be a one-line question or concession, or a worked
  argument that takes the space it needs. Explain what each number means in plain words;
  calculations, SQL and source detail go in the round's workpaper, not in the spoken text.
- Any expert may initiate a topic, and the discussion follows the reasoning wherever it leads.
  Record where it went; do not force it back to the opening topic.
- Use expert cards as analytical lenses. Attribute new judgments to the panel or its simulated
  roles. Quote the original writers only when the wording can be verified at a source anchor.
- Separate company evidence, calculations, assumptions, and hypotheses. Label every reported
  number with a source and cite the inputs to derived numbers. For annual reports, cite the year
  and section actually read. Put missing evidence and unverified channel checks in `open_questions`.
- State the period, tax basis, capital basis, and ownership scope when comparing returns. Penman’s
  RNOA, Mauboussin’s ROIC, and Greenblatt’s tangible-capital return use different definitions.
- S2 amounts are in yuan and the fact sheet converts them to 亿元. S1 amounts are already in 亿元.
  S1 revenue is 营业收入. S2 uses 营业总收入 in ratios and valuation tables and 营业收入 in
  `working_capital` and `reformulated_is`. State which definition you used.
- State the S1 quote date in price claims. Use S2 year-end prices for historical work.
  Treat S2 point values such as `v_per_share` and `v_to_p` as scenarios with fixed inputs.
  For valuation, use the reverse curve (implied growth across required returns) and justify the inputs.
- Use the [proposal process](observer/OBSERVER.md#3-proposals-to-change-an-expert-file) for changes
  to expert role cards. Keep the scope of changes tied to the research or maintenance request.
- Run `python3 scripts/validate.py` after changing structured project files. Publish only when
  authorized for the session. `scripts/sync.sh` stages the entire working tree and pushes `main`.
