# Proposal: Add Buffett’s great, good and gruesome business test

**Status:** applied
**Kind:** improvement
**Filed:** 2026-11-23 by Codex, user-requested source-maintenance update (no company research session)
**Target:** experts/warren-buffett.md → §3 Method; supporting source-basis/version metadata, append-only §8 anchors and §9 changelog
**Evidence:**
- User explicitly requested incorporating the newly added `source-files/Warren Buffett/Businesses – The Great, the Good and the Gruesome.md`. This is source-driven maintenance, not a claim of observed discussion weakness; no round references are invented. All additions carry new §8 source anchors.
- Source pp. 6–8: enduring moat and manager independence; See’s operating capital and cash release; FlightSafety’s reinvestment needs; airline growth with poor economics; three savings accounts. Existing §3 Step 2 measures capital needs but does not articulate this three-way distinction or its contrasting cases.
- Source p. 8 and following text: errors of omission at See’s / television station and the ownership surrendered for Dexter. Existing §3 Steps 4 and 7 discuss allocation and price but omit these newly supplied counterchecks.

## Change

One source-integration change to §3, with supporting metadata and anchors. Existing §8 anchors and §6 blind spots remain intact. Exact patch:

```diff
--- a/experts/warren-buffett.md
+++ b/experts/warren-buffett.md
@@ -3,7 +3,8 @@
 > Converts reported accounting into "owner earnings" and intrinsic value, then asks whether a durable franchise run by owner-minded managers is available at a sensible price — and refuses to pay for anything else.
 
 **Source basis:** `source-files/Warren Buffett/Berkshire Hathaway Shareholder Letter 1986.html` (incl. Appendix "Purchase-Price Accounting Adjustments and the 'Cash Flow' Fallacy"), `Berkshire Hathaway Shareholder Letter 1994.html`, `The Security I Like Best - Warren Buffett.md` (four 1951–1957 *Commercial and Financial Chronicle* articles: GEICO, Western Insurance Securities, Oil and Gas Property Management, Home Protective), `The Security I Like Best - verified data.md` (figure-checked index of the same articles).
-**Version:** 1.0 (2026-11-23) · **Changelog:** see bottom.
+**Additional source:** `source-files/Warren Buffett/Businesses – The Great, the Good and the Gruesome.md` (2007 business-economics discussion and adjoining mistakes; source page markers 6–8).
+**Version:** 1.1 (2026-11-23) · **Changelog:** see bottom.
 
 ## 1. Identity and scope
 
@@ -34,6 +35,15 @@
 - ROE on beginning equity, computed over a 5–10-year run, with leverage checked separately: "businesses earning good returns on equity while employing little or no debt." Scott Fetzer: earnings rose from $40.3m (1986) to $79.3m (1994) while book value went from $172.6m to $94.0m because $634m of dividends were paid out — the ideal pattern. Check that the pattern is not produced by "a cyclical peak in earnings, a monopolistic position, or leverage", sale-and-leasebacks or receivable sales.
 - Incremental capital need: compare growth in earnings with growth in (equity + net debt). Businesses that "improved the earnings of their businesses dramatically while, except in the case of insurance, utilizing little additional capital" create unrecorded goodwill; those that must retain everything to grow (Western Insurance: premium volume up 550% "has required an increase in surplus of 350%") pay low dividends and should be priced on earnings power, not payout.
 
+#### Great, good or gruesome: what does growth leave for the owner? (GGG, pp. 6–8)
+
+Apply this distinction to the full ten-year record before celebrating growth. The categories describe business economics; investment attractiveness still depends on price (Step 7).
+
+- **Great:** an enduring advantage protects exceptional returns while growth needs little additional operating capital. Slow physical growth is no disqualification: See’s sold 16m pounds in 1972 and 31m in 2007, roughly 2% annual growth as reported in GGG. Over that interval, annual pre-tax earnings rose from under $5m to $82m while required operating capital rose from $8m to $40m. Cash sales eliminated receivables and a short production/distribution cycle kept inventories low. Ask what concrete operating feature makes cash available to owners. (GGG, p. 7, See’s paragraphs.)
+- **Good:** a durable advantage and attractive returns can still require substantial new capital to grow. FlightSafety’s annual pre-tax operating earnings rose from $111m in 1996 to $270m in 2007, while net fixed assets rose from $570m to $1.079bn. Its $159m earnings gain required a $509m increase in that asset base; regulated utilities illustrate the same need to invest more to earn more. Capital intensity alone does not make a business bad. (GGG, pp. 7–8, FlightSafety and utilities.)
+- **Gruesome:** rapid growth requires repeated capital injections yet produces inadequate earnings, with no durable competitive advantage. Airlines are the source example. Ask whether expanding the business compounds the owners’ wealth or merely increases the amount they must fund. Growth itself cannot rescue poor economics. (GGG, p. 8, airlines and savings-account comparison.)
+- **Keep the capital and tax bases explicit.** These are whole-business, pre-tax illustrations, not parent-shareholder ROE or standardized after-tax ROIC. See’s $25m acquisition price is distinct from its $8m operating capital in 1972; a high operating return is not the buyer’s return on the price paid. FlightSafety’s cumulative $1.635bn capex less $923m depreciation equals $712m (calculated), not the $509m net-fixed-asset increase. The excerpt does not reconcile that difference: do not label either difference maintenance capex or infer an unexplained balancing item. For an A-share application, reconcile fixed assets (固定资产), working capital (营运资本), acquisitions and disposals from the notes; have Penman check the accounting basis and Mauboussin check incremental-return measurement. (GGG, pp. 7–8; reconciliation procedure is an application of the source, not a quoted rule.)
+
 ### Step 3 — Identify and size the moat
 
 - Prefer **quantified** advantages: cost ratio vs. peers (GEICO expense + loss-adjustment ratio 23.5% of premiums; combined ratios of Western Fire/Casualty 88.6%/91.1% vs. industry 92.6% over 1948–52), market share trend (Western's share of industry premiums 0.05% → 0.41%), penetration (Buffalo News Sunday penetration 83%), unit-volume growth (World Book, Kirby four straight years), customer franchise (See's product "personality").
@@ -41,12 +51,17 @@
 - Franchise test via tax/pricing incidence: strong unregulated franchises keep tax cuts and price rises; "price-competitive" industries pass them through. Commodity economics (insurance pricing, airlines, "not more statesmen, but less corn") mean profits only under shortage; a high-cost player in an unregulated commodity business must cut costs "or face extinction" (USAir).
 - Is the moat widening? GEICO's expense ratio fell 24.1% → 23.5%; management "continually widens the moat by driving down costs still more".
 
+- **Test endurance, not just today’s high return.** An advantage that must be rebuilt continuously in a rapidly changing industry is not an enduring moat. Ask whether the franchise survives the departure of its star manager: the source contrasts a star surgeon’s practice with the institutional reputation of the Mayo Clinic. Good management adds value, but a business that needs a superstar to earn great results does not itself qualify as great. (GGG, p. 6, enduring-moat and manager-dependence paragraphs.)
+
 ### Step 4 — Judge management as capital allocators
 
 - Does retained capital earn more than its cost? Any decision — including buybacks and mergers — must "increase per-share intrinsic value and avoid moves that decrease it." Reject the EPS-accretion test for M&A: the acquirer "typically gives up more intrinsic value than it receives." Issue shares only when receiving "as much in intrinsic business value as we give."
 - Compensation: bonus tied to the unit the manager controls; a charge on incremental capital employed and an equal credit on capital released; options whose strike does not rise with retained earnings reward managers for treading water and give them a motive to suppress dividends.
 - Candor: watch for euphemism ("reserve strengthening" = "correction of previous untruths"), earnings smoothing, and managers who "describe almost every compensation plan as aligning the interests of management with those of shareholders".
 - Evidence of ownership: insider holdings (GEICO 1950: 16 directors "owned approximately one-third of the outstanding stock"), long tenure, simple agreements.
+
+- **Let surplus earnings leave the business.** There is no obligation to reinvest where cash was earned. See’s generated $1.35bn cumulative pre-tax earnings through 2007 while requiring only $32m additional operating capital since 1972; Berkshire could deploy the remainder elsewhere after corporate taxes. Do not call the pre-tax remainder an after-tax distribution. Limited internal reinvestment opportunities can be a strength when managers redeploy or return the surplus sensibly. (GGG, p. 7, organic growth and See’s.)
+- **Count the ownership surrendered in a stock acquisition.** Dexter cost $433m in Berkshire shares in 1993, representing 1.6% of Berkshire. Its supposed durable advantage disappeared; the source later values that surrendered interest at about $3.5bn. This is the opportunity cost measured at the source’s later valuation, not an additional cash payment or the original accounting purchase price. Test both the acquired moat and the intrinsic value of the ownership given away. (GGG, after p. 8 marker, Dexter confession.)
 
 ### Step 5 — Look-through earnings for holding/investment-heavy companies (1994)
 
@@ -66,6 +81,8 @@
 - The 1951–57 articles show the price discipline: GEICO at ~8× depressed earnings with "the major portion of growth" ahead; Western at "less than twice earnings" and a 55% discount to adjusted book; Home Protective at under 4× earnings on $1,100 of assets per share; O&G at $5m market value against reserves worth ~$150m gross. Growth is paid for only when the record proves it is "legitimate" (unit volume and policyholders, not price inflation) and the multiple does not already embed it.
 - Price, don't time: "Why scrap an informed decision because of an uninformed guess?" Buy when fear peaks; add to existing holdings before hunting new ones.
 - Size and simplicity filters: the big idea "can usually be explained in a short paragraph"; a single durable key factor is as good as a complex thesis.
+
+- **Check errors of omission as well as overpayment.** Buffett almost lost See’s by refusing to move above $25m when the seller wanted $30m; he also declined a $35m television station with little reinvestment need and strong cash generation. Revisit an anchored purchase-price ceiling when the evidence supports durable owner earnings, while retaining the sensible-price requirement. These retrospective successes do not justify paying any multiple for a great business. (GGG, pp. 8 onward, See’s and television-station confessions.)
 
 ### A-share application notes
 
@@ -268,6 +285,24 @@
 - Letter 1986, Appendix → "the accountants' job is to record, not to evaluate. The evaluation job falls to investors and managers."
 - Letter 1986, Appendix → "accounting is but an aid to business thinking, never a substitute for it."
 
+**Great, good and gruesome businesses; capital allocation mistakes**
+
+GGG = `Businesses – The Great, the Good and the Gruesome.md`, the supplied 2007 discussion. Page references use the embedded page-end markers 6, 7 and 8; the last confessions follow marker 8. Figures are USD, pounds denote physical candy volume, and “last year” in the See’s discussion is read as 2007 alongside the explicitly dated FlightSafety comparison. This excerpt supplies no full capital roll-forward.
+
+- GGG, p. 6, opening criteria → “a business we understand”; “favorable long-term economics”; “able and trustworthy management”; “a sensible price tag”.
+- GGG, p. 6, enduring moat → “A moat that must be continuously rebuilt will eventually be no moat at all.”
+- GGG, p. 6, management dependence → “if a business requires a superstar to produce great results, the business itself cannot be deemed great.”
+- GGG, p. 7, organic growth → “There’s no rule that you have to invest money where you’ve earned it.”
+- GGG, p. 7, See’s volume and acquisition paragraphs → 16m pounds (1972), 31m (2007); $25m purchase price, $8m operating capital, under $5m annual pre-tax earnings at purchase.
+- GGG, p. 7, See’s operating cycle → “the product was sold for cash”; “the production and distribution cycle was short”.
+- GGG, p. 7, See’s subsequent results → $82m annual pre-tax earnings, $40m required capital; $32m incremental capital and $1.35bn cumulative pre-tax earnings; subsequent deployment after corporate taxes.
+- GGG, pp. 7–8, FlightSafety → 1996/2007 pre-tax operating earnings $111m/$270m; net fixed assets $570m/$1.079bn; cumulative depreciation $923m and capex $1.635bn; stated increments $159m earnings/$509m investment.
+- GGG, p. 8, utilities → “we will invest many billions to make it.”
+- GGG, p. 8, gruesome savings account → “requires you to keep adding money at those disappointing returns.”
+- GGG, p. 8, See’s and television-station confessions → See’s asking price $30m versus $25m ceiling; television station offered for $35m, with virtually no capital investment required.
+- GGG, after p. 8 marker, Dexter → $433m paid in Berkshire stock in 1993, 25,203 A shares / 1.6% ownership; later opportunity cost approximately $3.5bn; the assessed durable advantage vanished.
+
 ## 9. Changelog
 
 - 1.0 (2026-11-23): initial distillation from the 1986 and 1994 Berkshire letters and the four 1951–1957 "Security I Like Best" articles plus their verified-data index. A-share application notes are the distiller's mapping of the method onto CAS statements, not source claims.
+- 1.1 (2026-11-23): expanded §3 from the newly supplied great/good/gruesome discussion: capital needs of growth, moat endurance, external redeployment, stock-acquisition opportunity cost and omission errors; appended §8 anchors with explicit tax/capital bases. Proposal: `observer/proposals/2026-11-23-warren-buffett-business-economics.md`.
```

## Risk

This overlaps Greenblatt’s reinvestment economics and Mauboussin’s incremental returns. Keep Buffett’s distinctive classification around owner cash and concrete source cases; delegate standardized return measurement rather than import their formulas. Do not equate business quality with a good investment at any price, compare pre-tax whole-business examples to after-tax shareholder returns, or silently reconcile the FlightSafety asset discrepancy. The 2007 dating is explicit in FlightSafety and contextual for See’s; the excerpt’s later opportunity cost is not a present-day valuation.

## Validation

Independent reviewer: `review_buffett_update`, 2026-11-23. Reviewed the original role card, exact proposal patch, candidate, supplied source excerpt and the overlapping roles; this review did not edit the role card.

1. **Cited source evidence supports the change: yes.** Checked all 11 new quoted fragments against whitespace-normalized source text; each matches and is no longer than 25 words. Verified See’s volume, earnings, purchase-price and operating-capital figures; FlightSafety’s figures; and the See’s / television-station / Dexter confessions. Independently calculated $1,635m − $923m = $712m, $1,079m − $570m = $509m, $270m − $111m = $159m and $40m − $8m = $32m. Candy-volume CAGR is approximately 1.91%, consistent with the source’s rounded 2%. Page-end markers support the locators. FlightSafety explicitly identifies 2007; the candidate transparently describes See’s “last year” dating as contextual. It distinguishes pre-tax earnings from after-tax funds and the later Dexter opportunity cost from original consideration. The FlightSafety capital discrepancy is left unreconciled, as it must be from this excerpt. This is the user’s explicit source-maintenance request, so validation uses source evidence rather than inventing research-round weakness references.
2. **No contradiction with existing scope or anchors: yes.** The changes deepen §3’s existing franchise-economics, capital-allocation and owner-earnings method. The sensible-price requirement remains explicit, so omission examples do not license paying any valuation. No technology-investing authority is inferred from the source’s Microsoft / Google aside. Verified that the original §8 anchor block remains intact and §6 blind spots are unchanged. The patch matches the candidate exactly; the sole substantive target is §3, with necessary source metadata, new anchors, version and changelog support.
3. **Distinct contribution rather than reassignment to another role: yes.** Greenblatt already measures reinvestment economics, Mauboussin measures incremental returns, Penman handles statement articulation, and Bezos tests capital-intensive growth with unit NPV. None supplies Buffett’s source-specific three-account classification, See’s / FlightSafety contrast, manager-independent moat test and ownership-surrender / omission cases as one owner-cash framework. The candidate explicitly delegates standardized measurement and reconciliation rather than copying their formulas or numerical hurdles. Some economic overlap is intentional corroboration from Buffett’s own newly supplied source, not a new generic mandate.
4. **Scratch-copy validation: yes.** Copied the validation-relevant repository directories to `/private/tmp/buffett-independent-review-8njv951u`, applied the exact candidate to `experts/warren-buffett.md`, and ran `python3 scripts/validate.py`: **0 errors, 0 warnings**.

**Verdict:** validated — source-supported, appropriately scoped enrichment of §3; ready for the orchestrator to apply as version 1.1. No publication or commit was performed by the reviewer.

## Applied

Applied by Codex on 2026-11-23: `experts/warren-buffett.md` version 1.0 → 1.1, following the independent validation above. Commit: not committed. No publication performed.
