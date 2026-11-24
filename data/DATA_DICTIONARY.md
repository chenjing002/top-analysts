# bme.duckdb — Data Dictionary for Equity Research Queries

> **Default fact-sheet source is now local JSON, not this database.** `data/fetch.py` reads the
> agent-friendly JSON of AshareValueLine (S1) and business-model-explorer (S2): per-company files
> with `years` and `metrics[key].values` (S2, keys such as `raw:revenue`, `oi_after_tax`, `rnoa`,
> `reoi`, `implied_g_reoi`) in yuan. S2 JSON metric names match the table columns below; it has no
> quarterly rows, filing dates, reverse curve or flags. This dictionary applies to `--duckdb`
> supplements and direct SQL.

Source database: `/Users/lin/Desktop/business-model-explorer/data/bme.duckdb` (DuckDB, ~1.7 GB, **read-only**).
Built by the project at `/Users/lin/Desktop/business-model-explorer/` from Tushare raw financial statements for 5,580 listed A-share companies (SSE/SZSE/BSE, FY2008–2026Q3) plus Penman-style reformulated statements, ratios, residual income and valuation tables. Metric definitions below quote the project docs (`docs/module-02…12.md`, `AGENTS.md`); everything marked *verified* was checked against the database on 2026-11-23 for 600519.SH (贵州茅台) and 000333.SZ (美的集团).

---

## 1. Connecting, units, dates, company lookup

**Connect** (the system `duckdb` CLI is too old; use the project venv, always `read_only=True`):

```bash
/Users/lin/Desktop/business-model-explorer/.venv/bin/python -c "import duckdb; con=duckdb.connect('/Users/lin/Desktop/business-model-explorer/data/bme.duckdb', read_only=True); print(con.execute(\"SELECT ts_code,name,industry FROM raw_stock_basic WHERE symbol='600519'\").fetchall())"
```

**Units** (`AGENTS.md`, `docs/chinese-display-and-units.md`): all money is **人民币元 (CNY yuan)** — raw statements, std_facts (`unit = 'CNY_yuan'`; per-share lines `'CNY_yuan_per_share'`), reformulated tables, model values, `market_cap`. Display convention is 亿元 = value / 1e8. Prices and per-share values are 元/股; share counts are shares. Returns/ratios are decimals (0.25 = 25%); days are days; multiples are plain multiples. **Exception:** `raw_daily_basic` keeps Tushare's native units — `total_mv`/`circ_mv` in **万元**, `total_share`/`float_share` in **万股** (verified: 600519.SH 2025-12-31 `total_mv` 172,460,149.47 万元 = `market_snapshot_annual.market_cap` 1,724,601,494,694 元). `market_snapshot_annual` and `valuation_annual` are already converted to 元 / 股.

**Dates:** all date columns are VARCHAR `'YYYYMMDD'` (`end_date = '20241231'`, `trade_date = '20231229'`, `f_ann_date = '20250403'`). Fiscal year = calendar year; annual rows have `end_date LIKE '%1231'`. Provenance timestamps (`_fetched_at`, `finished_at`) are ISO-8601 UTC strings.

**Company lookup** via `raw_stock_basic` (5,580 rows, all `list_status='L'`; no delisted companies):

```sql
SELECT ts_code, symbol, name, industry, market, list_date FROM raw_stock_basic
WHERE symbol = '600519' OR name LIKE '%茅台%';      -- returns ts_code '600519.SH' (symbol is the 6-digit code)
```
`industry` is Tushare's 110-value classification (e.g. 白酒, 家用电器, 电气设备) — the only peer-group key available. Suffix `.SH` = SSE, `.SZ` = SZSE, `.BJ` = BSE (BSE codes renumbered to 920xxx).

**Universe per layer:** raw statements cover 5,576 companies (all comp_type, incl. banks/insurers/brokers). Derived tables (`std_facts` … `valuation_annual`) cover the **5,479 companies whose latest `analysis_log` status is `ok`**; 97 financial-format companies and 4 new listings are excluded (see §4). Annual derived tables run FY2008–FY2025 (≥4,095 companies/year from FY2014; 5,479/year FY2022–2025).

---

## 2. Table reference

Key: (PK) = row key as verified by uniqueness checks. Column notes quote the project docs; "undocumented" = not defined in docs and only inferred from data.

### 2.1 raw_stock_basic — company master (Tushare `stock_basic`)
| column | 中文 | note |
|---|---|---|
| ts_code (PK) | 股票代码 | e.g. `600519.SH` |
| symbol | 6位代码 | `600519` |
| name | 股票简称 | 贵州茅台 |
| fullname / enname | 公司全称 / 英文名 | |
| industry | 所属行业 | Tushare industry (110 values) |
| area | 地域 | province |
| market | 市场 | 主板 / 创业板 / 科创板 / 北交所 |
| exchange | 交易所 | SSE / SZSE / BSE |
| list_status, list_date, delist_date | 上市状态/日期 | all `L` |
| is_hs | 沪深港通标的 | H / S / N |
| act_name, act_ent_type | 实控人 / 实控人类型 | e.g. 地方国企, 自然人 |
| `_row_hash`, `_fetched_at`, `_source_url`, `_api_params` | provenance | present on every raw_* table |

### 2.2 raw_income / raw_balancesheet / raw_cashflow — Tushare statements verbatim
Rows are stored **append-only**: every revision (`update_flag`, `f_ann_date`, wider field set) is a new row, so `(ts_code, end_date)` is **NOT unique** (600519.SH FY2024 has 3 identical income rows; 000333.SZ FY2023 has an update_flag 0 and 1 row). Always dedupe — rule used by the project (`module-02`): "Preferred row per (ts_code, end_date, report_type): update_flag desc, f_ann_date desc, fetch time desc". Income and cash-flow values are **cumulative year-to-date** (Q3 row = 9 months). Only `report_type = '1'` (合并报表, consolidated) exists; parent-only/restated types 6/4/5 were never returned by the vendor.

Common header columns: `ts_code`, `ann_date` 公告日期, `f_ann_date` 实际公告日期, `end_date` 报告期, `report_type` 报告类型 (always '1'), `comp_type` 公司类型 ('1' 一般工商业, '2' 银行, '3' 保险, '4' 证券, '7' 其他), `end_type` 报告期类型 ('1' Q1, '2' H1, '3' Q3, '4' FY; '0'/NULL for odd periods — verified against end_date month), `update_flag` 更新标识 ('0' original disclosure, '1' revised — both kept).

**raw_income** (97 columns) — key lines:
`total_revenue` 营业总收入 · `revenue` 营业收入 · `int_income` 利息收入 · `oper_cost` 营业成本 · `total_cogs` 营业总成本 · `biz_tax_surchg` 税金及附加 · `sell_exp` 销售费用 · `admin_exp` 管理费用 · `rd_exp` 研发费用 · `fin_exp` 财务费用 · `fin_exp_int_exp` 财务费用-利息费用 · `fin_exp_int_inc` 财务费用-利息收入 · `assets_impair_loss` 资产减值损失 · `credit_impa_loss` 信用减值损失 · `invest_income` 投资收益 · `ass_invest_income` 对联营企业和合营企业的投资收益 · `fv_value_chg_gain` 公允价值变动收益 · `oth_income` 其他收益 · `asset_disp_income` 资产处置收益 · `operate_profit` 营业利润 · `non_oper_income` 营业外收入 · `non_oper_exp` 营业外支出 · `total_profit` 利润总额 · `income_tax` 所得税费用 · `n_income` 净利润 · `n_income_attr_p` 归母净利润 · `minority_gain` 少数股东损益 · `t_compr_income` 综合收益总额 · `compr_inc_attr_p` 归母综合收益 · `basic_eps` 基本每股收益 (元/股). `ebit`, `ebitda` are vendor-calculated ("opaque definitions — tagged, not for analytical use").

**raw_balancesheet** (162 columns) — key lines:
`money_cap` 货币资金 · `trad_asset` 交易性金融资产 · `notes_receiv` 应收票据 · `accounts_receiv` 应收账款 · `accounts_receiv_bill` 应收票据及应收账款 (combined display field — never add to the granular ones) · `receiv_financing` 应收款项融资 · `prepayment` 预付款项 · `oth_receiv` 其他应收款 · `inventories` 存货 · `contract_assets` 合同资产 · `oth_cur_assets` 其他流动资产 · `total_cur_assets` 流动资产合计 · `lt_eqt_invest` 长期股权投资 · `fix_assets` 固定资产 · `cip` 在建工程 · `use_right_assets` 使用权资产 · `intan_assets` 无形资产 · `goodwill` 商誉 · `total_assets` 资产总计 · `st_borr` 短期借款 · `notes_payable` 应付票据 · `acct_payable` 应付账款 · `adv_receipts` 预收款项 · `contract_liab` 合同负债 · `payroll_payable` 应付职工薪酬 · `taxes_payable` 应交税费 · `oth_payable` 其他应付款 · `non_cur_liab_due_1y` 一年内到期的非流动负债 · `lt_borr` 长期借款 · `bond_payable` 应付债券 · `lease_liab` 租赁负债 · `total_liab` 负债合计 · `minority_int` 少数股东权益 · `total_hldr_eqy_exc_min_int` 归母所有者权益 · `total_hldr_eqy_inc_min_int` 所有者权益合计. Bank/insurer/broker lines (`depos` 吸收存款, `cash_reser_cb`, `rsrv_insur_cont`, `client_depos` …) are populated only for financial companies or groups with finance subsidiaries.

**raw_cashflow** (101 columns) — key lines:
`c_fr_sale_sg` 销售商品提供劳务收到的现金 · `c_paid_goods_s` 购买商品接受劳务支付的现金 · `c_paid_to_for_empl` 支付给职工的现金 · `c_paid_for_taxes` 支付的各项税费 · `n_cashflow_act` 经营活动产生的现金流量净额 (CFO) · `c_pay_acq_const_fiolta` 购建固定无形长期资产支付的现金 (capex) · `n_recp_disp_fiolta` 处置固定无形长期资产收回的现金净额 · `c_paid_invest` 投资支付的现金 · `c_disp_withdrwl_invest` 收回投资收到的现金 · `n_cashflow_inv_act` 投资活动现金流量净额 · `c_recp_borrow` 取得借款收到的现金 · `c_prepay_amt_borr` 偿还债务支付的现金 · `c_pay_dist_dpcp_int_exp` 分配股利利润或偿付利息支付的现金 (dividends AND interest combined under CAS) · `incl_dvd_profit_paid_sc_ms` 子公司支付少数股东的股利 · `n_cash_flows_fnc_act` 筹资活动现金流量净额 · `eff_fx_flu_cash` 汇率变动对现金的影响 · `n_incr_cash_cash_equ` 现金及现金等价物净增加额 · `c_cash_equ_end_period` 期末现金及现金等价物 · `n_depos_incr_fi` 客户存款和同业存放款项净增加额 (finance-subsidiary deposit flows sit INSIDE CFO). Indirect-method supplemental block: `net_profit` 净利润, `depr_fa_coga_dpba` 固定资产折旧等, `amort_intang_assets` 无形资产摊销, `lt_amort_deferred_exp` 长期待摊费用摊销, `use_right_asset_dep` 使用权资产折旧, `decr_inventories` 存货的减少, `decr_oper_payable` **经营性应收项目的减少** (Tushare misnomer: it is receivables, not payables), `incr_oper_payable` 经营性应付项目的增加, `im_net_cashflow_oper_act` 间接法 CFO. `free_cashflow` is vendor-calculated — do not use.

### 2.3 std_facts — long-form standardized facts (37.4 M rows)
One row per fact. (PK) `(ts_code, end_date, report_type, concept, period_kind)` — verified unique for point/cumulative facts. Built from the *preferred* raw row only, so it is already deduplicated.
| column | meaning |
|---|---|
| statement | `balancesheet` / `income` / `cashflow` |
| concept | snake_case standardized name from `config/mapping_tushare.yml` (230 mapped fields), e.g. `revenue`, `total_revenue`, `cost_of_goods_sold`, `operating_profit_reported`, `net_income_parent`, `inventory`, `ppe`, `cash_and_equivalents`, `deposits_taken`, `cfo`, `capex_paid`, `supp_depreciation` (supp_* = indirect-method block) |
| raw_field | Tushare column it came from (`source_row_hash` links to the exact raw row) |
| label_zh | Chinese statement caption (the authoritative display name) |
| penman_class | **default** Penman class, "EDITABLE defaults, not truth". BS: `operating_asset` / `financial_asset` / `operating_liability` / `financial_obligation` / `equity` / `minority_interest` / `subtotal` / `presentation_combined` (Tushare combined display fields that overlap granular fields — never sum with them). IS: `operating_income` / `operating_expense` / `financing` / `tax` / `subtotal` / `per_share` / `other_comprehensive` / `minority`. CF: `operating` / `investing` / `financing` / `fx` / `subtotal` / `supplemental` |
| note | judgment note from the YAML (e.g. 货币资金 "May contain operating cash"; 长期股权投资 "Associates/JVs; judgmental"; finance-subsidiary items) |
| value | yuan (or 元/股 for per_share) |
| value_type | `reported` (verbatim) or `calculated` (derived single quarters) |
| period_kind | `point` (BS), `cumulative` (IS/CF as reported, YTD), `single_quarter` (Qn = cum Qn − cum Qn−1; "Per-share fields never differenced") |
| basis | always `'consolidated'` here (the opening/average distinction lives in `ratios_annual.basis`) |
| update_flag, f_ann_date | of the preferred raw row |
| mapping_version | `'1'` |

"Nulls emit no fact (missing stays missing)" — an absent line is absent, never zero. Deposits/interbank items of finance subsidiaries (e.g. Moutai's 吸收存款及同业存放 → `deposits_taken`, `financial_obligation`) are flagged judgmental.

### 2.4 reformulated_bs — Penman balance sheet (all periods incl. quarters)
(PK) `(ts_code, end_date)`; rows for every balance-sheet date (quarterly), 2008–2026Q3.
```
oa  = Σ operating assets        fa = Σ financial assets
ol  = Σ operating liabilities   fo = Σ financial obligations
noa = oa − ol                   nfo = fo − fa   (negative = net financial assets)
cse_calc = noa − nfo − minority_interests   (checked against reported parent equity, R3)
```
`total_assets_reported`, `total_liabilities_reported`, `parent_equity_reported` = raw totals. Reconciliation residuals, "reported, never forced": `r1_assets_residual` = (oa+fa) − total assets; `r2_liab_residual` = (ol+fo) − total liabilities; `r3_cse_residual` = cse_calc − parent equity. Non-zero R1/R3 = unmapped or vendor-missing lines (000333.SZ: ≈ ¥11–21 bn every period, i.e. ~2% of assets left out of NOA — see §4). Conventions: "all cash = financial_asset (no invented operating-cash split)"; 长期股权投资 operating; 投资性房地产 financial; combined display fields resolved per period (`reclass_decisions.choice ∈ granular_match / combined_used`). Line-level resolved values are in `reformulated_bs_components (ts_code, end_date, concept, effective_class, value)`.

### 2.5 reformulated_is — Penman income statement
(PK) `(ts_code, end_date, period_kind)` with `period_kind ∈ cumulative / single_quarter`.
```
oi_core_pretax  = Σ operating_income − Σ operating_expense (core lines; exact term list in is_terms JSON)
unusual_pretax  = impairments + asset disposal gains + 营业外收入 − 营业外支出   (non-recurring)
oi_pretax       = oi_core_pretax + unusual_pretax
nfe_pretax      = 财务费用 − 公允价值变动收益 − 投资收益 (+ associate income if moved to operating)
tax_rate_assumed = 0.25  (statutory-rate ASSUMPTION, same for every row)
nfe_after_tax   = nfe_pretax × (1 − 0.25)
oi_after_tax    = ni_total + nfe_after_tax       (consolidated, incl. minority claims)
oi_core_after_tax = oi_after_tax − unusual_after_tax ;  unusual_after_tax = unusual_pretax × 0.75 (inferred from data; undocumented)
r4_pretax_residual = (oi_pretax − nfe_pretax) − 利润总额
```
Also `revenue` 营业收入, `total_revenue` 营业总收入, `tax_reported`, `ni_total` 净利润, `ni_parent` 归母净利润, `minority_income`, `comprehensive_income_total/parent`. `is_terms` (cumulative rows only) is a JSON of the exact signed raw concepts in each bucket — read it to see how a given company's lines were classified (verified: 000333.SZ moves `associate_investment_income` into core OI; 600519.SH puts finance-subsidiary 利息收入/利息支出 in core OI).

### 2.6 ratios_annual — Nissim–Penman decomposition (annual, two capital bases)
(PK) `(ts_code, end_date, basis)`, `basis ∈ {'average','opening'}`: `average` = capital is the mean of opening and closing balances; `opening` = prior year-end balance (verified: 600519 FY2025 opening `noa_capital` 62.44 bn = FY2024 `reformulated_bs.noa`; average = (62.44+75.42)/2). Use `average` for standard ratio analysis; `opening` matches the residual-income tables.
```
RNOA  = oi_after_tax / noa_capital = OPM × ATO
OPM   = oi_after_tax / total_revenue     ATO = total_revenue / noa_capital
OLLEV = OL_cap / noa_capital             FLEV = nfo_capital / te_capital
NBC   = nfe_after_tax / nfo_capital      Spread = RNOA − NBC
ROTCE = RNOA + FLEV × Spread   (TE = NOA − NFO = equity incl. minority; identity exact)
```
Columns: `revenue` (**= 营业总收入 total_revenue**, verified), `oi_after_tax`, `noa_capital`, `nfo_capital`, `te_capital`, `rnoa`, `opm`, `opm_core` (= oi_core_after_tax/total_revenue), `ato`, `ollev`, `flev`, `nbc`, `spread`, `rotce` (identity), `rotce_direct` (= (oi_after_tax − nfe_after_tax) / te_capital, i.e. NI_total / TE — inferred, verified numerically; kept when the identity version is suppressed), `roce_parent` = ni_parent / CSE_cap ("separate column with NO identity"), `gross_margin` = (营业收入 − 营业成本)/营业收入 ("product-business proxy"), and inverse-turnover components `inventory_to_sales`, `receivables_to_sales`, `prepayments_to_sales`, `ppe_to_sales`, `cip_to_sales`, `intangibles_to_sales`, `op_payables_to_sales`, `customer_advances_to_sales` (component / total_revenue; NULL = line not disclosed that year, "missing ≠ zero").
`ratio_flags` (comma-separated, '' when none): `no_opening_balance` (first year → all NULL), `noa_near_zero_suppressed` (|NOA_cap| < 5% of revenue → RNOA/ATO/OLLEV NULL), `nfo_near_zero_suppressed` (|NFO_cap| < 5% of revenue → NBC/Spread/ROTCE NULL), `net_financial_assets` (informational, NFO < 0 — 61,276 of 123,908 rows), `negative_noa`, `non_positive_equity_capital`, `non_positive_revenue`.

### 2.7 working_capital_annual — turnover days and operating working capital
(PK) `(ts_code, end_date)`. Average balances, 365 days. **`revenue` here = 营业收入 (`revenue`), not 营业总收入** (verified: 600519 FY2024 170.9 bn vs 174.1 bn in ratios_annual).
```
dio = 365 · inventory_avg / cogs
dso = 365 · trade_receivables_avg / revenue   (notes+accounts+combined+receivables_financing+contract assets; other_receivables excluded)
dpo = 365 · trade_payables_avg / purchases_est,  purchases_est = COGS + ΔInventory  (dpo_method = 'purchases=COGS+dInventory')
dpo_cogs = 365 · trade_payables_avg / cogs     (variant; diverges when inventory grows)
ccc = dio + dso − dpo
advance_days = 365 · customer_advances_avg / revenue  (预收+合同负债; NOT netted into ccc)
ccc_net_advances = ccc − advance_days   (inferred from data; undocumented)
owc = inventory + trade receivables + prepayments − trade payables − other op payables (salaries/taxes/other) − customer advances
owc_begin / owc_end / owc_avg ; owc_pct_sales = owc_avg / revenue ; d_owc = owc_end − owc_begin ; d_revenue
incr_owc_per_incr_revenue = d_owc / d_revenue  (NULL + flag when |Δrevenue| < 5% of revenue)
```
`wc_flags`: `no_opening_balance`, `delta_revenue_near_zero_suppressed`, `receivables_not_disclosed` (ccc NULL), `owc_components_incomplete`.

### 2.8 cash_summary_annual — earnings-to-cash reconciliation
(PK) `(ts_code, end_date)`. `ni_total` 净利润; `cfo` 经营活动现金流量净额; `capex_paid` 购建固定无形长期资产支付的现金; `asset_disposal_proceeds`; `fcf_simple` = "CFO − cash capex"; `fcf_after_disposals` = "CFO − cash capex + asset disposal proceeds" (definitions carried in `fcf_simple_def` / `fcf_after_disposals_def`); `cash_conversion` = CFO / NI (NULL when |NI| < 2% of CFO scale); `accruals` = ni_total − cfo (inferred; undocumented). CAS treatment preserved: "interest received is investing; interest + dividends paid are financing. Chinese CFO already excludes financing interest." Check residuals: `c0_supp_vs_is_ni` (supplemental NI vs IS NI), `c1_bridge_residual` (indirect bridge vs reported indirect CFO), `c2_indirect_vs_direct`. `cf_flags`: `supplemental_not_disclosed`, `ni_near_zero_suppressed`. The step-by-step bridge is in `cash_bridge_annual (step_order, concept, label, value, step_kind)`.

### 2.9 capital_summary_annual — capital employed and reinvestment
(PK) `(ts_code, end_date)`. `noa_begin`, `noa_end`, `delta_noa`; funding split `delta_noa = delta_cse + delta_mi + delta_nfo` (exact); `revenue` (= 营业总收入), `revenue_growth`, `noa_growth`; `reinvestment_rate` = ΔNOA / oi_after_tax; `capex_paid`; `da_total` = sum of **disclosed** supp_* depreciation/amortization lines (NULL + `da_not_disclosed` otherwise); `capex_to_da`; `fcf_from_oi` = "OI after tax − ΔNOA (Penman: C − I = OI − ΔNOA)"; `fcf_simple` (from 2.8); `fcf_articulation_diff` = fcf_from_oi − fcf_simple — "**expected to be nonzero**" (CAS interest classification, FX/dirty-surplus/M&A). `capex_split_note`: maintenance-vs-growth capex "NOT knowable from statements". `cap_flags`: `no_opening_balance`, `oi_near_zero_suppressed` (|OI| < 5% of revenue), `noa_base_near_zero_suppressed`, `negative_noa_base`, `da_not_disclosed`, `no_income_statement`, `no_prior_revenue`. Waterfall steps in `capital_bridge_annual`.

### 2.10 residual_income_annual — ReOI, RE and value-creation drivers (opening capital)
(PK) `(ts_code, end_date)`. `r_op_assumed` = `r_e_assumed` = **0.08 on every row** (verified) — "ASSUMPTIONS, not estimates".
```
capital_charge = r_op × noa_begin ;  reoi = oi_after_tax − capital_charge ;  reoi_core = oi_core_after_tax − capital_charge
rnoa_open = oi_after_tax / noa_begin ;  ato_open = revenue / noa_begin ;  spread_op = rnoa_open − r_op
equity_charge = r_e × cse_begin ;  re_common = comprehensive_income_parent − equity_charge  (RE uses parent COMPREHENSIVE income)
roce_open = ni_parent / cse_begin ;  spread_e = roce_open − r_e
pm = oi/revenue = pm_core + pm_unusual ;  delta_reoi = reoi − reoi_prev ;  reoi_growth, oi_growth
Value-creation bridge (exact): sales_effect = ΔRev × PM_{t−1}; core_margin_effect = Rev_t × ΔPM_core;
   unusual_effect = Rev_t × ΔPM_unusual; capital_charge_effect = −r_op × (NOA_{t−1} − NOA_{t−2})
Penman drivers: margin_effect = ΔPM × ATO_{t−1} × NOA_{t−1}; turnover_effect = PM_t × ΔATO × NOA_{t−1};
   growth_effect = s_{t−1} × (NOA_{t−1} − NOA_{t−2}); profitability_effect = margin + turnover (inferred)
```
`bridge_available` / `drivers_available` booleans. `ri_flags`: `no_opening_balance`, `no_prior_reoi` (bridge needs 3 BS years), `reoi_base_not_positive_suppressed` (reoi_growth NULL when prior ReOI ≤ 0 or < 5% of revenue — 31,512 rows), `negative_noa_base`, `noa_base_near_zero_suppressed`, `drivers_suppressed`, `non_positive_cse_base`, `no_revenue`, `bridge_unavailable_no_revenue`, `comprehensive_income_parent_missing`. `oci_note`: "剩余权益收益采用归母综合收益。归母净资产收益率仍按归母净利润计算。"

### 2.11 valuation_annual — perpetuity models and reverse engineering
(PK) `(ts_code, end_date)`. Assumptions on every row: `r_op_assumed = 0.08`, `r_e_assumed = 0.08`, `g_assumed = 0.03` (verified, uniform). Book inputs at year-end: `noa`, `nfo`, `minority_interests`, `cse`, `noa_begin`, `cse_begin`; `reoi_0` = OI_0 − r·NOA_{−1}; `re_0`; `rnoa_0` (opening RNOA); `reoi_1_rnoa` = (RNOA_0 − r)·NOA_0; `fcf_0` = `capital_summary_annual.fcf_from_oi` (verified equal).
| model | V_NOA | equity column |
|---|---|---|
| book | NOA_0 | `v_equity_book` |
| reoi_flat | NOA_0 + ReOI_0 / r | `v_equity_reoi_flat` |
| **reoi_g (primary)** | NOA_0 + ReOI_0 (1+g)/(r − g) | `v_equity_reoi_g` |
| rnoa_g | NOA_0 + (RNOA_0 − r) NOA_0/(r − g) | `v_equity_rnoa_g` |
Equity value = V_NOA − NFO_0 − MI_0 (NFO, MI at book). Equity-level: `v_equity_ri` = CSE_0 + RE_0(1+g)/(r_e − g); `v_equity_aeg` (identical by algebra, verified 0 diff); `earn_1` = r_e·CSE_0 + RE_1; `aeg_2` = g·RE_1.
Market: `trade_date`, `price` (元/股, last trading day of the fiscal year), `shares`, `market_cap` (元), `market_ev` = market_cap + nfo + minority_interests (verified). `v_per_share` = v_equity_reoi_g / shares; `v_to_p` = v_equity_reoi_g / market_cap (verified; >1 = model above market). `trailing_pe` = market_cap / ni_parent **same fiscal year** (verified); `forward_pe_market` = market_cap / earn_1; `forward_pe_model` = v_equity_ri / earn_1; `normal_pe` = 1/r_e = 12.5.
Reverse engineering (P_NOA = mcap + NFO_0 + MI_0; X = P_NOA − NOA_0; Y = mcap − CSE_0): `implied_g_reoi` = (rX − ReOI_0)/(X + ReOI_0); `implied_g_rnoa` = r − (RNOA_0 − r)·NOA_0/X; `implied_g_fcf` = (r·P_NOA − FCF_0)/(P_NOA + FCF_0) (reverse DCF, "noisy anchor"); `implied_g_equity` = (r_e·Y − RE_0)/(Y + RE_0); `implied_r_op` at g: [OI_0(1+g) + gX]/[X + (1+g)NOA_{−1}]; `implied_r_e` at g: [CI_0(1+g) + gY]/[Y + (1+g)CSE_{−1}]. `net_payout_implied` d = CI − ΔCSE; `aeg_actual` = CI_t + r_e·d_{t−1} − (1+r_e)·CI_{t−1}; `cum_div_growth` = cum-dividend comprehensive-income growth (exact formula undocumented).
`val_flags`: `no_market_data` (model values kept, market columns NULL — 11,864 rows), `no_opening_balance`, `no_balance_sheet`, `implied_g_{reoi,rnoa,fcf,equity}_undefined` (non-positive anchor or solution not below r), `rnoa_anchor_suppressed`, `market_ev_at_or_below_noa` (informational), `comprehensive_income_parent_missing`. Note the **hindsight anchor**: year-end price vs year-end book, statements published 3–4 months later; "not a point-in-time trading signal". No "today's price" valuation exists.

### 2.12 valuation_grid — sensitivity of the primary model
(PK) `(ts_code, end_date, model, r, g)`; `model` always `'reoi_g'`; r ∈ {0.06,…,0.12} step 0.01, g ∈ {−0.02, 0.00, 0.01,…,0.05} (7×7 = 49 cells/year; note −0.01 is absent). ReOI_0 recharged at each r. Columns `v_noa`, `v_equity`, `v_per_share`, `v_to_p`. Only years with market data (5,347 companies, FY2015–2025).

### 2.13 valuation_reverse_curve — implied g as a function of r
(PK) `(ts_code, end_date, r)`; r = 0.05…0.12 in 0.005 steps (15 rows/year); `implied_g_reoi`, `implied_g_rnoa`, `implied_g_fcf`, `implied_g_equity` (NULL where undefined). "Shows the (r, g) pairs that justify the price."

### 2.14 market_snapshot_annual — year-end market data in 元/股
(PK) `(ts_code, end_date)`; 5,347 companies, FY2014–2025. `trade_date` = last December trading day (e.g. `20231229` for FY2023); `close` 元/股; `shares` 总股本(股); `market_cap` 元 (= close × shares; `m1_mcap_residual_rel` ≈ 0 everywhere); `pe_reported`, `pb_reported`, `dv_ttm_reported` = Tushare's own ("based on the latest report published at that date — reference only": year-end `pe` = mcap / **prior-year** NI). A company suspended on the last December trading day has no row (and `no_market_data` downstream).

### 2.15 raw_daily_basic — Tushare `daily_basic` rows, native units
Only **December trading days** 2014–2025 (verified: every `trade_date` is in month 12; this is NOT a daily price history). `close` 元; `total_share`/`float_share` **万股**; `total_mv`/`circ_mv` **万元**; `pe`, `pe_ttm`, `pb`, `dv_ttm` vendor multiples. 5,700 ts_codes incl. 1,959 rows for codes not in `raw_stock_basic` (old BSE codes / delisted).

### 2.16 analysis_log — per-company pipeline run log
One row per (ts_code, run) — 12 runs stored, so take the **latest row per ts_code** (`QUALIFY row_number() OVER (PARTITION BY ts_code ORDER BY finished_at DESC) = 1`). `status`: `ok` (5,479 latest) / `skipped` (101 latest) / `failed` (4 historic rows only, all later re-run ok). `reason`: `financial` = latest annual `comp_type ≠ 1` ("bank 2, insurer 3, broker 4, other 7 — their statement layout needs its own mapping — not built", `error` holds e.g. `comp_type 2`); `no_annual_report` = no consolidated `****1231` balance sheet yet. `step`/`error`: failing pipeline step and exception. `n_annual`, `first_end`, `last_end`: annual coverage. `check_failures`: comma list of identity-check families with ≥ 1 failing annual row — `R1` assets, `R2` liabilities, `R3` equity (|residual| > ¥1 M), `R4` pretax classification, `L` economics-map identities (L1–L3, L5), `E` year-on-year evolution (E1–E3); families `T`, `B`, `RI`, `V` never fail. NULL = clean (5,022 companies); 457 carry failures. Per-family counts in `analysis_checks (ts_code, family, checked, failed, max_abs_residual, run_id)` — `L4` there is diagnostic only (the company's own indirect-method bridge not adding up).

Other tables (not detailed): `cash_bridge_annual`, `capital_bridge_annual`, `value_bridge_annual`, `valuation_bridge_annual` (waterfall steps), `*_checks`, `econ_map_nodes`, `econ_evolution_*`, `driver_tree_nodes`, `reclass_decisions`, `ingest_log`.

---

## 3. Definitions that differ from reported statements

- **OI after tax (税后经营收益) ≠ 营业利润.** 营业利润 (reported operating profit) includes 投资收益, 公允价值变动收益 and 财务费用. Penman OI removes them: `oi_after_tax = 净利润 + 财务费用等净金融费用 × (1 − 25%)`. For 600519 FY2024: 营业利润 ¥119.7 bn; `oi_pretax` ¥118.1 bn; `oi_after_tax` ¥88.2 bn vs 净利润 ¥89.3 bn (NFE is negative because of interest income). OI is **consolidated incl. minority claims**; it is not a parent figure.
- **Tax allocation.** Reported tax is not split; financing items are taxed at the assumed statutory **25%** (`tax_rate_assumed`), and OI absorbs the rest: OI_after_tax = NI_total + NFE_pretax × 0.75. Effective rates are not used.
- **Unusual items.** `unusual_pretax` = credit/asset impairment losses, 资产处置收益, 营业外收入 − 营业外支出 (exact set per company in `is_terms`). They stay inside OI (not in NFE); `oi_core_*`, `opm_core`, `reoi_core` exclude them. Impairment sign follows the statement layout (old CAS ≤ FY2018 expense-signed; 2019+ display sign negative = loss), decided per row from 营业总成本 when ambiguous; exceptions surface in `r4_pretax_residual`.
- **Associate/JV income** (对联营合营企业投资收益) is moved into core operating income when disclosed; the rest of 投资收益 is financing.
- **Finance-subsidiary lines in industrial groups** (Moutai, Midea …): 利息收入/利息支出 in the income statement → operating; 吸收存款及同业存放, 拆入资金 → financial obligations; 拆出资金, 发放贷款, 买入返售 → financial assets (judgmental defaults; deposit flows sit inside reported CFO).
- **NOA (净经营资产) = OA − OL**; operating liabilities (应付账款, 合同负债/预收, 应付职工薪酬, 应交税费, 其他应付款, 递延收益, 预计负债, 递延所得税负债 …) are deducted from operating assets, not treated as financing. **NFO (净金融负债) = FO − FA**; all 货币资金 is financial, so cash-rich companies have NFO < 0 (`net_financial_assets`). **CSE (归母普通股权益) = NOA − NFO − MI**, reconciled to reported 归母所有者权益 (R3).
- **RNOA** = OI_after_tax / NOA (not ROA, not ROIC on total capital); **ATO** uses 营业总收入. For cash-light, prepaid businesses NOA is tiny and RNOA huge (Moutai 123–227%); read OPM and ATO alongside it.
- **FLEV = NFO / TE** where TE = equity incl. minority — negative for net-cash companies; **NBC** = NFE_after_tax / NFO; **Spread = RNOA − NBC**; **ROTCE = RNOA + FLEV × Spread** is return on *total* equity incl. minority. **`roce_parent`** = 归母净利润 / 归母权益 is the conventional ROE and has no decomposition identity.
- **ReOI** = OI_t − r_op × NOA_{t−1} with r_op = 8% (assumption); **RE** = parent **comprehensive** income − r_e × CSE_{t−1}. The equity-level and enterprise-level values differ by construction (cash pile charged r_e at equity level, enters at book at enterprise level).
- **FCF has two definitions**: `fcf_simple` = CFO − cash capex (cash statement) and `fcf_from_oi` = OI − ΔNOA (accrual, Penman). They differ by `fcf_articulation_diff` and both are reported.
- **Revenue columns**: `ratios_annual`, `capital_summary_annual`, `residual_income_annual`, `valuation_annual` `.revenue` = **营业总收入** (`total_revenue`); `working_capital_annual.revenue` and `reformulated_is.revenue` = **营业收入**. Differences matter for groups with interest/fee income (Moutai 174.1 vs 170.9 bn).
- **Gross margin** = (营业收入 − 营业成本)/营业收入, excluding 税金及附加 — a "product-business proxy".
- **DPO** uses purchases ≈ COGS + ΔInventory, not COGS; **CCC excludes customer advances** (reported separately as `advance_days`).
- **Paired-line divergence scan** (fact sheet section, `fetch.py` `DIVERGENCE_PAIRS`, formula `scripts/calc.py growth_gap`): for each pair (A follows B) the gap is `100 × (A_t/A_t−1 − B_t/B_t−1)` in percentage points per fiscal year, and `excess_a = A_t−1 × (growth_a − growth_b)` is the part of ΔA that B's growth does not explain, in 亿. Rank by `excess_a`; the percentage alone is misleading for small lines. A cell is `—` when a base is ≤ 0 or the line is absent. Pairs mix 营业收入 (IS/BS/CF lines) and 营业总收入 (NOA); `其他应收款` prefers `*_combined`. Evidence only: a gap is a question, not a finding.

---

## 4. Known data caveats

1. **r_op, r_e, g are uniform defaults (8%, 8%, 3%), not estimates or conclusions.** No beta, no cost-of-capital model, no analyst forecasts, no explicit horizon; "a single perpetual g is the crudest scheme". Use `valuation_grid` / `valuation_reverse_curve` for sensitivity, and present `v_to_p` as conditional on these assumptions. `tax_rate_assumed` is likewise a flat 25%.
2. **Financial-format companies are excluded from every derived table.** Banks (comp_type 2, 49 companies), insurers (3, 5), brokers (4, 46) and "other" (7, 4) are only in raw_* tables; `analysis_log` marks them `skipped / financial`. Two companies whose comp_type changed historically are analysed under the industrial mapping anyway: **600816.SH** (comp_type 2 in FY2014–2021Q3 rows) and **000987.SZ** (comp_type 4 in 2017–2020Q1 rows) — treat their early years with caution.
3. **Raw tables are append-only with duplicates; only consolidated statements.** `(ts_code, end_date)` repeats across revisions and re-fetches; dedupe by `update_flag DESC, f_ann_date DESC, _fetched_at DESC` (or just use `std_facts`). `update_flag='1'` = revised disclosure (165 k of 304 k income rows). Restated comparatives are **not** stored as separate restated statements (report_type 4/5 unavailable) — a FY row reflects the vendor's latest version of that year, and `ann_date`-based point-in-time queries are "not yet built". `end_type` '0'/NULL rows (~0.1%) are odd-period/prospectus filings.
4. **Identity residuals are reported, never forced.** 457 analysed companies (8.3%) have at least one failing family in `analysis_log.check_failures`; e.g. 000333.SZ carries `R1,R3` ≈ ¥11–21 bn per period (unmapped asset lines, probably finance-subsidiary items such as `depos`/`payables` left unmapped on purpose), so its NOA and cse_calc are understated by that amount while OI is unaffected. Filter on `check_failures IS NULL` for clean cross-sections, and inspect `reformulated_bs.r1/r2/r3` and `reformulated_is.r4_pretax_residual` per company. Very large R4 values appear for a few interim/pre-IPO periods (e.g. 600941.SH 20180630, 601816.SH 20151231).
5. **Vendor data quality.** Module 15 found 167 raw rows that fail basic identities (assets = liabilities + equity, NI = 利润总额 − 所得税) across 94 companies; they are kept as is. ~80% of remaining R1–R3 residuals are "vendor rows missing several granular lines". Tushare `ebit`, `ebitda`, `free_cashflow` are opaque vendor calculations.
6. **Survivorship bias.** Only currently listed companies (`list_status='L'`); 345 delisted companies are absent. Early years are thin (FY2011: 87 companies with ratios; FY2014: 4,095).
7. **Market data is year-end only and hindsight-anchored.** `market_snapshot_annual` / `valuation_annual` use the last December trading day; `raw_daily_basic` holds December windows only — there is no daily price history and no current price. `pe_reported` is Tushare's (prior-year NI); `trailing_pe` in valuation_annual is same-year NI (also hindsight). 136 companies have no year-end price (`no_market_data`).
8. **Flags encode suppression, not errors.** NULL ratios with `*_suppressed` flags are deliberate (near-zero denominators); NULL components mean "not disclosed", never zero. Always `SELECT` the flags column with any ratio.
9. **Missing-vs-zero and quarterly limits.** `std_facts` emits no row for an undisclosed line. Ratios, WC, cash, capital, RI and valuation tables are **annual only**; `reformulated_bs` / `reformulated_is` extend to 2026Q3 and include single-quarter rows, but no trailing-4Q ratios exist.
10. **analysis_log history.** `failed` rows exist only for superseded runs (920157.BJ, 920258.BJ: "Empty inputs" at valuation; 688759.SH, 688837.SH: pre-revenue export) — all four are `ok` in the latest run. Always take the latest row per company.
11. **Undocumented columns** (inferred from data only): `unusual_after_tax`, `ccc_net_advances`, `accruals`, `profitability_effect`, `cum_div_growth` exact formula, `reoi_prev`. Treat as derived conveniences.
12. **Minor observations:** `valuation_grid` omits g = −0.01 although docs say "g ∈ −2…5%"; `raw_daily_basic` has 1,959 rows for ts_codes absent from `raw_stock_basic`; `std_facts.basis` is the literal `'consolidated'` and unrelated to `ratios_annual.basis`.

---

## 5. Ready-to-use SQL (all tested 2026-11-23)

**Q1 — 10-year ratio time series (average capital basis)**
```sql
SELECT end_date, basis, revenue, oi_after_tax, noa_capital, nfo_capital, rnoa, opm, opm_core, ato, flev, nbc, spread, rotce, roce_parent, gross_margin, ratio_flags
FROM ratios_annual WHERE ts_code = '600519.SH' AND basis = 'average' AND end_date >= '20160101' ORDER BY end_date;
```

**Q2 — Reformulated balance sheet, annual, with reconciliation residuals**
```sql
SELECT end_date, oa, ol, noa, fa, fo, nfo, minority_interests, cse_calc, parent_equity_reported, total_assets_reported, r1_assets_residual, r3_cse_residual
FROM reformulated_bs WHERE ts_code = '600519.SH' AND end_date LIKE '%1231' ORDER BY end_date;
```

**Q3 — Reformulated income statement vs reported 营业利润 (annual)**
```sql
SELECT i.end_date, i.total_revenue, i.revenue, i.oi_core_pretax, i.unusual_pretax, i.oi_pretax, i.nfe_pretax, i.tax_reported, i.nfe_after_tax, i.oi_after_tax, i.oi_core_after_tax, i.ni_total, i.ni_parent, op.value AS operating_profit_reported, i.r4_pretax_residual
FROM reformulated_is i
LEFT JOIN std_facts op ON op.ts_code = i.ts_code AND op.end_date = i.end_date AND op.concept = 'operating_profit_reported' AND op.period_kind = 'cumulative'
WHERE i.ts_code = '600519.SH' AND i.period_kind = 'cumulative' AND i.end_date LIKE '%1231' ORDER BY i.end_date;
```

**Q4 — Cash conversion and the two FCF measures**
```sql
SELECT c.end_date, c.ni_total, c.cfo, c.capex_paid, c.fcf_simple, c.cash_conversion, c.accruals, k.fcf_from_oi, k.fcf_articulation_diff, c.cf_flags
FROM cash_summary_annual c LEFT JOIN capital_summary_annual k USING (ts_code, end_date)
WHERE c.ts_code = '600519.SH' ORDER BY c.end_date;
```

**Q5 — Working-capital days and OWC intensity**
```sql
SELECT end_date, revenue, cogs, dio, dso, dpo, dpo_cogs, ccc, advance_days, ccc_net_advances, owc_end, owc_pct_sales, incr_owc_per_incr_revenue, wc_flags
FROM working_capital_annual WHERE ts_code = '000333.SZ' ORDER BY end_date;
```

**Q6 — Capital employed, reinvestment and funding split**
```sql
SELECT end_date, noa_begin, noa_end, delta_noa, delta_cse, delta_mi, delta_nfo, revenue_growth, noa_growth, reinvestment_rate, capex_paid, da_total, capex_to_da, cap_flags
FROM capital_summary_annual WHERE ts_code = '600519.SH' ORDER BY end_date;
```

**Q7 — Residual operating income and its drivers**
```sql
SELECT end_date, r_op_assumed, oi_after_tax, noa_begin, capital_charge, reoi, reoi_core, rnoa_open, spread_op, re_common, roce_open, delta_reoi, sales_effect, core_margin_effect, unusual_effect, capital_charge_effect, margin_effect, turnover_effect, growth_effect, ri_flags
FROM residual_income_annual WHERE ts_code = '600519.SH' ORDER BY end_date;
```

**Q8 — Valuation vs market and reverse-engineered growth (plus the r→g curve and the r×g grid for one year)**
```sql
SELECT end_date, price, market_cap/1e8 AS mcap_yi, v_equity_reoi_g/1e8 AS v_reoi_g_yi, v_equity_rnoa_g/1e8 AS v_rnoa_g_yi, v_equity_ri/1e8 AS v_ri_yi, v_per_share, v_to_p, implied_g_reoi, implied_g_equity, implied_r_op, forward_pe_market, trailing_pe, val_flags
FROM valuation_annual WHERE ts_code = '600519.SH' ORDER BY end_date;

SELECT r, implied_g_reoi, implied_g_rnoa, implied_g_fcf, implied_g_equity
FROM valuation_reverse_curve WHERE ts_code = '600519.SH' AND end_date = '20251231' ORDER BY r;

SELECT g, r, v_to_p FROM valuation_grid WHERE ts_code = '600519.SH' AND end_date = '20251231' ORDER BY r, g;
```

**Q9 — Peer comparison within an industry (latest fiscal year), with data-quality flag**
```sql
WITH latest AS (SELECT ts_code, status, check_failures FROM analysis_log QUALIFY row_number() OVER (PARTITION BY ts_code ORDER BY finished_at DESC) = 1)
SELECT b.ts_code, b.name, r.revenue/1e8 AS rev_yi, r.rnoa, r.opm, r.ato, r.flev, r.rotce, r.roce_parent, w.ccc, c.cash_conversion, v.v_to_p, v.trailing_pe, l.check_failures
FROM raw_stock_basic b
JOIN ratios_annual r ON r.ts_code = b.ts_code AND r.end_date = '20251231' AND r.basis = 'average'
LEFT JOIN working_capital_annual w ON w.ts_code = b.ts_code AND w.end_date = r.end_date
LEFT JOIN cash_summary_annual c ON c.ts_code = b.ts_code AND c.end_date = r.end_date
LEFT JOIN valuation_annual v ON v.ts_code = b.ts_code AND v.end_date = r.end_date
LEFT JOIN latest l ON l.ts_code = b.ts_code
WHERE b.industry = '白酒' ORDER BY r.revenue DESC NULLS LAST;
```

**Q10 — Universe screen: five consecutive years RNOA ≥ 20% and positive FCF, clean identity checks**
```sql
WITH latest AS (SELECT ts_code FROM analysis_log QUALIFY row_number() OVER (PARTITION BY ts_code ORDER BY finished_at DESC) = 1 AND status = 'ok' AND check_failures IS NULL),
win AS (SELECT r.ts_code, count(*) AS n_years, min(r.rnoa) AS min_rnoa, avg(r.rnoa) AS avg_rnoa, min(c.fcf_simple) AS min_fcf
        FROM ratios_annual r JOIN cash_summary_annual c USING (ts_code, end_date)
        WHERE r.basis = 'average' AND r.end_date BETWEEN '20210101' AND '20251231' AND r.rnoa IS NOT NULL AND r.ratio_flags NOT LIKE '%suppressed%'
        GROUP BY r.ts_code)
SELECT w.ts_code, b.name, b.industry, w.avg_rnoa, w.min_rnoa, w.min_fcf/1e8 AS min_fcf_yi, v.v_to_p
FROM win w JOIN latest USING (ts_code) JOIN raw_stock_basic b USING (ts_code)
LEFT JOIN valuation_annual v ON v.ts_code = w.ts_code AND v.end_date = '20251231'
WHERE w.n_years = 5 AND w.min_rnoa >= 0.20 AND w.min_fcf > 0
ORDER BY w.avg_rnoa DESC LIMIT 20;
```

**Bonus — balance-sheet line items with Chinese labels and Penman class (one year); and single-quarter P&L**
```sql
SELECT concept, label_zh, penman_class, value/1e8 AS value_yi, raw_field
FROM std_facts WHERE ts_code = '600519.SH' AND end_date = '20251231' AND statement = 'balancesheet'
  AND penman_class IN ('operating_asset','operating_liability','financial_asset','financial_obligation')
ORDER BY penman_class, value DESC;

SELECT end_date, revenue, oi_after_tax, ni_parent FROM reformulated_is
WHERE ts_code = '000333.SZ' AND period_kind = 'single_quarter' AND end_date >= '20250101' ORDER BY end_date;
```
