# Module: variable-compensation

**Switch on when:** a meaningful share of any earner's pay is variable — bonus, commission, profit-sharing — such that assuming it (or ignoring it) would materially change the savings model.

## PROCESS.md additions (under "Standing assumptions & treatment rules")

### Variable compensation
- **Baseline conservatively, show upside as sensitivity.** Model the variable component at {{BASELINE — e.g., "the plan's target payout" or "a conservative floor such as the worst year in the last five"}}; always show a sensitivity line at the trailing multi-year average of *actual* payouts.
- **Maintain a payout history table** (year, payout vs. target) in `data/notes.md`; append each year and recompute the trailing average used in sensitivity. {{HISTORY_SOURCE — where actuals come from: comp statements, public filings, etc.}}
- Savings from variable comp are **lumpy** — map when it pays out and where it goes (retirement plan deferrals, taxable investing, spending), so the projection's contribution timing is realistic.
- If any employer-stock or deferred-comp exposure shares the same performance driver as the bonus (same company results), treat them as **correlated in stress tests** — a bad company year hits both.

## DATA_CHECKLIST.md additions

### Annual inputs rows (section A)
| Prior-year actual bonus/commission — append to history table, recompute trailing average | comp statement | sensitivity line |
| Current-year target/plan structure changes | employer | payout model |
| Where variable comp was directed (deferrals, investing, spending) | statements | contribution timing |

## RESEARCH_PROMPT.md additions (research area)

*(Usually none needed — variable comp is a modeling treatment, not a rules area. Include a research line only if the comp has unusual tax mechanics.)*

## Report section

*(No standalone section — the history table and sensitivity lines appear inside the projection and assumptions sections.)*
