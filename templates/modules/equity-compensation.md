# Module: equity-compensation

**Switch on when:** any earner receives RSUs, stock options, ESPP, or performance shares.
**Setup interview must capture:** which instruments; vesting schedule; what happens to unvested awards at separation/retirement (from plan documents if available — flag "to confirm from plan docs" if not); whether sales are restricted (trading windows, 10b5-1); default disposition intent (sell at vest vs. hold).

## PROCESS.md additions (under "Standing assumptions & treatment rules")

### Equity compensation
- **Model each program separately** (time-based RSUs / performance shares / options / ESPP) with its actual vesting schedule — never blend into a single "stock comp" line.
- **Separation/retirement rules drive the retirement-timing math**: model what unvested awards are forfeited vs. kept at each candidate exit date, and quantify the cost of leaving before any acceleration/retirement-eligibility threshold. *These rules must come from the actual award agreements, not memory or statement footnotes — confirm once from plan documents and record here.*
- {{VESTING_RULES — filled from interview/plan docs: schedule, retirement-eligibility terms, performance-multiplier mechanics if any}}
- **Performance awards** (if any) displayed by the broker at a floor/target multiplier must be re-valued at expected performance; show floor / expected / max lines.
- **Default disposition:** {{DISPOSITION — e.g., "sell at vest (diversification default); each January vest scored against this default in the next review"}}.
- Unvested equity counts toward employer concentration (see employer-stock-concentration module) but is **excluded from the balance sheet** until vested; model it as future income in the projection.

## DATA_CHECKLIST.md additions

### Equity compensation (Documents)
- [ ] Grant/vesting schedule showing vested + unvested tranches per program
- [ ] Equity plan documents / award agreements — *needed once, to confirm separation and retirement-eligibility rules*
- [ ] Share position + cost basis (broker export), including lots from past vests

### Annual inputs rows (section A)
| Grant value + program split this year | grant confirmation | income model |
| Vest outcomes: shares, sold-at-vest? | broker statement | disposition scorecard; new lot tracking |
| Performance factor realized (if applicable) — append to history table | company announcement | calibrates expected-multiplier line |
| Trading-window / 10b5-1 status changes | employer | sale-planning constraints |

## RESEARCH_PROMPT.md additions (research area)

**Equity compensation strategy** — current tax treatment of RSU vesting, option exercises, and ESPP (qualifying vs. disqualifying dispositions); withholding shortfall pitfalls at supplemental rates; sell-at-vest vs. hold research; 10b5-1 rule requirements after the most recent SEC amendments

## Report section

**Equity compensation** — tranche table per program (vested/unvested by year), value at floor/expected/max where performance-based, this year's vest outcomes vs. the disposition default, and forfeiture-at-exit table for the retirement-timing candidates.
