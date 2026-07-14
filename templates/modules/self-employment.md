# Module: self-employment

**Switch on when:** any earner has self-employment, freelance, or closely-held business income.

## PROCESS.md additions (under "Standing assumptions & treatment rules")

### Self-employment / business income
- **Model income as a distribution, not a number:** use a conservative baseline ({{SE_BASELINE — e.g., "trailing 3-year average" or "worst recent year"}}) with sensitivity at the recent average; never project the best year forward.
- **Retirement-plan structure is an annual audit item:** is the current vehicle (solo 401(k) / SEP-IRA / SIMPLE) still the right one for the income level and any backdoor-Roth strategy? *Note: SEP/SIMPLE balances break the backdoor Roth's pro-rata math — if backdoor Roths are in use, plan structure must account for it.*
- **Quarterly estimated taxes**: verify safe-harbor compliance each year (no penalties) and that the cash reserve for taxes is segregated from spendable income in the cash-flow model.
- Separate **owner's compensation from business value**: if the business itself has sale value, carry it on the balance sheet at a conservative, haircut value and never count it in retirement funding until a sale is concrete (then model as a dated scenario).
- QBI deduction eligibility and phaseouts are re-checked annually from the standing reference.

## DATA_CHECKLIST.md additions

### Business / self-employment (Documents)
- [ ] Prior-year Schedule C / K-1 / business P&L
- [ ] Business retirement-plan statement (solo 401(k)/SEP/SIMPLE)
- [ ] Estimated-tax payment records for the year

### Annual inputs rows (section A)
| Business income: prior-year actual + current-year run rate | P&L / you | income distribution |
| Plan contributions made (employee + employer side) | plan statement | waterfall audit |
| Business value change, if material | you (conservative) | balance sheet (non-funding) |

## RESEARCH_PROMPT.md additions (research area)

**Self-employment planning** — current-year solo 401(k)/SEP/SIMPLE contribution limits and deadlines, QBI deduction rules and phaseouts, self-employment tax treatment, estimated-tax safe harbors, and retirement-plan choices that preserve backdoor-Roth eligibility

## Report section

*(Business income appears in the income model and assumptions; plan-structure findings appear in the tax audit. Add a standalone section only if a business sale scenario is live.)*
