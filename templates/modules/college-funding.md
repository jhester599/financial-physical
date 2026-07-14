# Module: college-funding

**Switch on when:** the household has children (or other beneficiaries) whose education it intends to help fund.

## PROCESS.md additions (under "Standing assumptions & treatment rules")

### College
- Each child's college is modeled as a **dated liability**: estimated cost band ({{INTENT — in-state vs. private per stated intent, per child}}), compared against 529/savings balances on a funding glide path. Report a **funded percentage** per child.
- Shortfalls appear as cash-flow claims in the specific projection years — not blended into overall retirement success probability. (Keeps "can we retire" and "can we pay for college" separately visible.)
- Audit state 529 tax-benefit capture each year ({{STATE_529_BENEFIT — from the standing reference: deduction/credit amount per beneficiary, carryforward rules; or "our state has none"}}).
- {{EXTRA_529_RULES — from interview: overflow-account policy, grandparent-owned 529 treatment (count as offsets at growth-only, note FAFSA treatment), sibling-reallocation intent}}
- Track the option value of **529-to-Roth rollovers** for overfunded accounts (limits and conditions from the standing reference).

## DATA_CHECKLIST.md additions

### College (Documents)
- [ ] 529 (or other education-account) statements, one per beneficiary
- [ ] Grandparent/relative-owned 529 balances, if any (approximate is fine)

### Annual inputs rows (section B)
| College intent updates per child (in-state vs. private signals as they age) | you | funded-% bands |
| Expected college start years (grade progression) | you | liability dating |

### Annual decisions rows (section D)
| 529 contributions for the year (state benefit capture) | by December | state deduction/credit rules |

## RESEARCH_PROMPT.md additions (research area)

**College funding** — current 529 rules including 529-to-Roth rollover mechanics and limits, {{STATE}}'s 529 state tax benefit specifics, current FAFSA treatment of parent vs. student vs. grandparent assets, and current cost benchmarks (in-state public vs. private, inflation trend)

## Report section

**College funding status** — per-child table: dated liability, current balance, funded %, on-glide contribution needed; state-benefit capture audit; any reallocation decisions.
