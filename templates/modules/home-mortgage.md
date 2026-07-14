# Module: home-mortgage

**Switch on when:** the household owns its home (or other non-rental real estate). Renters get the skeleton's rent treatment instead.

## PROCESS.md additions (fills the "Housing" slot)

### Real estate
- Primary home on the balance sheet at a **conservative value** (county assessor / online-estimate midpoint), net of mortgage. **{{FUNDING_TREATMENT — default: "Excluded from retirement funding assets — treated as a contingency reserve (downsizing option)"; override if the household plans to sell/downsize as part of the plan, in which case model it as a dated event}}**
- **Mortgage payoff vs. carry:** while a mortgage exists, analyze payoff vs. carry annually (rate vs. expected after-tax portfolio return, liquidity cost, refinance outlook) and give an explicit recommendation.
- Property tax, insurance, and maintenance flow into baseline spending; use a maintenance reserve of ~1% of home value/year if actuals aren't available.
- Renovation projects are **discretionary capital outlays**, separate from recurring spend.
- Speculative property ideas (second home, land) are modeled as **scenarios**, not baseline — showing the impact of locked capital on retirement date and success probability.

## DATA_CHECKLIST.md additions

### Home & mortgage (Documents)
- [ ] Mortgage statement (balance, rate, escrow detail)
- [ ] HELOC statement, if any

### Annual inputs rows (section B)
| Home value | county assessor / online midpoint | balance sheet |
| Planned renovation phases + costs | you | capital-outlay lines |

### Annual decisions rows (section D)
| Mortgage payoff / refi check | annual, while a mortgage exists | balance, rate, refi market |

## RESEARCH_PROMPT.md additions (research area)

*(Usually covered by the federal/state tax sections — mortgage-interest deductibility at the household's income, property-tax deduction caps. Add a dedicated line only if a purchase/sale/1031 decision is live.)*

## Report section

*(No standalone section — home value and mortgage appear in the balance sheet; the payoff-vs-carry recommendation appears in Recommendations.)*
