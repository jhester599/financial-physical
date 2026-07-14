<!-- SKELETON — the setup interview fills placeholders, keeps only sections relevant to the
     household, splices module checklist blocks at the MODULE markers, and writes the result
     to /DATA_CHECKLIST.md. -->

# DATA_CHECKLIST.md — Annual Gathering List

Redact account numbers and SSNs, then place everything in `data/` (never committed, never uploaded). Claude inventories `data/` against this list at the start of each review and flags gaps before proceeding.

## Documents

### Retirement accounts
- [ ] {{RETIREMENT_ACCOUNT_STATEMENTS — one line per account from the interview: owner, type, institution}}
- [ ] Statements for any dormant prior-employer plans
- [ ] HSA statement *(if applicable)*

### Investments & cash
- [ ] Brokerage statements ({{BROKERAGE_ACCOUNTS}})
- [ ] Bank account statements
- [ ] 12 months of credit-card + bank transactions (export CSVs; a full seasonal year matters)

### Debts
- [ ] {{DEBT_STATEMENTS — mortgage, auto, student loans, HELOC as applicable}}

<!-- MODULE: equity-compensation -->
<!-- MODULE: deferred-compensation -->
<!-- MODULE: college-funding -->
<!-- MODULE: self-employment -->
<!-- MODULE: pension-income -->

### Protection & benefits
- [ ] Life insurance policy summaries ({{PER_ADULT}})
- [ ] Disability insurance summary
- [ ] Umbrella policy declarations *(if held)*
- [ ] SSA statements for each earner (ssa.gov) — feeds the Social Security sensitivity lines; until provided, estimate from earnings history

### Balance history (optional but valuable)
If you track account balances over time in a spreadsheet, include it — a multi-year balance history lets the review derive your *realized* savings rate and cash-flow patterns instead of assuming them. If you don't track one, consider starting: even an annual snapshot compounds in value.
- [ ] Balance-history spreadsheet(s), if kept

## Annual inputs to update/validate (interviewed each year; values live in `data/notes.md`)

Claude walks this list with you at the start of each review — confirm or update every item **before modeling**. Committed here are only the input names; current values stay in gitignored `data/notes.md`.

### A. Income & employment
| Input | Source | Why it matters |
|---|---|---|
| Base pay per earner | paystub | Savings model |
{{INCOME_INPUT_ROWS — module files add rows: bonus history, equity grants, deferral elections, business income}}
| Employer / role changes | you | Benefits, vesting, account tracking |

### B. Household facts & spending drivers
| Input | Source | Why it matters |
|---|---|---|
| Retirement-age intent (changed?) | you | Headline scenario |
| Planned capital outlays next 5 yrs (vehicles, projects, trips) | you | Non-recurring lines |
| {{HOUSING_INPUT — home value source, or current rent}} | {{source}} | Balance sheet / spending |
| Major life events / new or closed accounts | you | Everything |
{{HOUSEHOLD_INPUT_ROWS — module/interview-specific: dependent support, childcare trajectory, college intent}}

### C. Insurance, estate, tax status
| Input | Source | Why it matters |
|---|---|---|
| Estate docs status (wills{{, guardianship}}, POAs) | you | Top action until done |
| Beneficiary designations current? | account portals | Estate overlay |
| Coverage levels (life ×base, LTD %, umbrella) | benefits portal / declarations | Gap-check vs. targets |
| Estimated-tax / withholding on track? | transactions / CPA | Cash-flow model |
{{TAX_STATUS_ROWS — e.g., backdoor Roth executed? pro-rata clean?}}

### D. Annual decisions to make/confirm
| Decision | Cadence | Inputs needed |
|---|---|---|
| Cash/EF vs. target ({{EF_TARGET}}) | annual | cash balance trend |
{{DECISION_ROWS — module files add rows: deferral elections, sale tranches, 529 contributions, payoff checks}}

*External parameters (IRS limits, brackets, state rates, healthcare rules, withdrawal-rate research) are NOT listed here — they come from the annual `research/STANDING_REFERENCE_[YEAR].md` refresh, which is a required pre-req.*

## Free-text notes (`data/notes.md`)

Copy this template into `data/notes.md` and update annually:

```markdown
# Household Notes — [YEAR]

## Ages & timing
- Adult ages:
- Target retirement age(s):
{{KIDS_LINE — kids' ages and expected college start years, if applicable}}

## Income
{{INCOME_LINES — one line per earner and income type from the interview}}

## Retirement target
- Annual spending target (today's dollars) or % income replacement:

## Large planned outlays (next 5 years)
- (projects, vehicles, trips, tuition, etc.)

## Risk & preferences
- Target stock/bond allocation:
- Behavior in last major drawdown:
- Emergency fund target (months) and where cash sits:

{{ADVISOR_SECTION — if advisor-crosscheck module on: what the advisor covers, notable recommendations this year}}

## Benefits & estate
- Estate status: wills / {{guardianship /}} beneficiary designations current? (Y/N + notes)
- Unusual employer benefits:

## Changes since last review
- (job changes, new accounts, closed accounts, major life events)
```
