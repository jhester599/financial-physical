# Module: employer-stock-concentration

**Switch on when:** any single stock (usually an employer's) is a meaningful share of household assets — as a screening rule, >10% of investable assets, or any concentrated position the household is worried about. Almost always paired with the equity-compensation module.

## PROCESS.md additions (under "Standing assumptions & treatment rules")

### Concentration
- **Measure total exposure honestly**: shares in every account (check inside 401(k)s — employer-stock funds hide there) + vested and unvested equity awards + any deferred-compensation balance that is an unsecured employer liability + human-capital dependence (salary streams from the same employer). Report it as % of investable assets and % of net worth, with and without unvested awards.
- **Stress test annually**: what a severe drawdown in the concentrated position (e.g., −50% to −60%) does to the retirement math and the earliest feasible age.
- **Concentration policy:** {{CONCENTRATION_POLICY — target ceiling as % of investable, deadline, and whether further purchases are frozen; set at interview or "to be set in first review"}}.
- **Diversification order (cheapest tax first):** (1) inside tax-advantaged accounts — selling employer stock inside a 401(k)/IRA is tax-free; (2) charitable gifts of lowest-basis lots if the household gives anyway; (3) loss or near-zero-gain lots in taxable; (4) gain-budgeted taxable tranches sized annually; (5) deliberate holds. Before selling low-basis employer stock held *inside* a 401(k), check **NUA (net unrealized appreciation)** treatment first — it can change the answer.
- Maintain a **lot table** (refreshed each year from cost-basis exports) ranking taxable lots by tax cost per dollar diversified. Verify dividend reinvestment is OFF for the concentrated position (wash-sale hygiene and no auto re-buying).

## DATA_CHECKLIST.md additions

### Concentrated position (Documents)
- [ ] Cost-basis export for every account holding the position (per-lot detail)
- [ ] Retirement-plan holdings detail (does employer stock sit inside the 401(k)? share count + basis)

### Annual inputs rows (section A)
| New lots acquired (vests/purchases), lots disposed | broker export | lot-table refresh |
| Dividend reinvestment status for the position | broker settings | should be OFF |
| In-plan employer stock: count + blended basis | plan export | concentration + NUA status |

### Annual decisions rows (section D)
| Sale tranche size for the year (per lot ranking) | annually, after vest/bonus timing is known | income picture, lot table, gain budget |

## RESEARCH_PROMPT.md additions (research area)

**Concentrated stock management** — frameworks for sizing acceptable single-company concentration (including unvested equity and deferred-comp exposure), staged diversification approaches, tax-efficient unwind strategies, current NUA rules, and exchange funds / other deferral vehicles with their costs and criticisms

## Report section

**Concentration & stress test** — the honest exposure measure (table: by account, vested/unvested/deferred/human capital), policy vs. actual, the drawdown stress result, and the **lot disposition framework** (ranked channels + this year's tranche recommendation).
