# Module: pension-income

**Switch on when:** any earner has a defined-benefit pension (current or from a former employer) or an annuity, or expects one.

## PROCESS.md additions (under "Standing assumptions & treatment rules")

### Pension / annuity income
- Model pension income as an **income floor** in the projection — it reduces the portfolio withdrawal needed and materially changes safe-withdrawal math (flexible spending strategies pair best with a solid floor).
- **Record the key terms here once confirmed from plan documents:** {{PENSION_TERMS — benefit formula or promised amount, earliest/normal start ages, COLA or fixed, survivor options, lump-sum option availability}}.
- **Start-age and form elections are analyzed, not defaulted:** when the election approaches, compare start ages and single-life vs. joint-survivor forms (and lump sum, if offered) against household longevity, the survivor scenario, and bracket management. Until then, model the {{DEFAULT_ELECTION — e.g., "joint-and-survivor at normal retirement age"}} as baseline.
- A fixed (non-COLA) pension **loses real value** — model it in nominal terms with explicit inflation erosion, never as a constant real income.
- If the sponsor is a private employer, note PBGC guarantee limits vs. the promised benefit.

## DATA_CHECKLIST.md additions

### Pension / annuity (Documents)
- [ ] Annual pension benefit statement (accrued benefit, projected benefit)
- [ ] Plan summary — *needed once: formula, start ages, survivor options, lump-sum availability, COLA*
- [ ] Annuity contract summary, if any

### Annual inputs rows (section A)
| Accrued/projected benefit update | plan statement | income floor |
| Election windows approaching? | plan / HR | triggers the election analysis |

## RESEARCH_PROMPT.md additions (research area)

**Pension & annuity elections** — current frameworks for lump-sum vs. annuity decisions (interest-rate sensitivity of lump sums), single vs. joint-survivor election analysis, PBGC guarantee limits, and how pension floors interact with safe-withdrawal-rate research

## Report section

*(No standalone section by default — the floor appears in the projection and the survivor scenario. Add one in election years.)*
