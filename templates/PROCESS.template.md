<!-- SKELETON — the setup interview (SETUP_PROMPT.md) fills placeholders, splices module
     blocks at the MODULE markers, deletes unused markers, and writes the result to
     /PROCESS.md. Do not edit generated content back into this skeleton. -->

# PROCESS.md — Methodology & Standing Assumptions

This document is the analytical contract for each annual review. Claude should read it in full before touching any data. Changes to methodology belong here, with a dated entry in the Decision Log.

**Companion document:** `research/STANDING_REFERENCE_[YEAR].md` carries the current-year external facts — tax law, contribution limits, healthcare rules, withdrawal-rate research, state specifics — refreshed annually via `RESEARCH_PROMPT.md` **before** the review starts (required pre-req). PROCESS.md says *how we analyze*; the standing reference says *what the current rules are*. Where the two conflict, the newer standing reference wins on external facts and this document wins on household treatment rules.

*This analysis is educational decision support, not financial, tax, or legal advice. Verify figures before acting; seek professional review for large or irreversible decisions.*

## Scope

{{HOUSEHOLD_SCOPE — who is covered: earners, dependents, all accounts including dormant prior-employer plans}}

## Standing priorities (set {{SETUP_YEAR}})

{{PRIORITIES — ranked 1..N from interview section H; #1 is the analytical spine}}

## Core methodology

The spine of every review: **household balance sheet → spending analysis → projection → recommendations.**

1. **Account inventory & balance sheet.** Every account with balance, owner, tax treatment (taxable / traditional / Roth / HSA{{/ NQDC if module on}}), allocation, and fees where available.
2. **Spending analysis.** 12 months of bank/credit-card transactions, categorized. Output feeds the projection's baseline spending assumption. Discretionary capital projects (renovations, vehicles, trips) are broken out as separate lines so they do not inflate recurring spend. Apply a **rigorous recurring-vs-non-recurring screen**: classify every material transaction as persisting into retirement or not, and show the excluded items so the screen is auditable.
3. **Projection.** Savings rate (derived from real history where available, not just assumed), growth assumptions, target retirement spending → success probability under multiple market scenarios (Monte Carlo or equivalent). Report retirement-date sensitivity to key assumptions, the **distribution of outcomes** (10th/50th/90th percentile wealth at key ages), the **failure shape** (median/earliest failure age), and the **implied withdrawal rate vs. published benchmarks** from the standing reference.
4. **Recommendations.** Ordered by expected impact, each with commentary on rationale and tradeoffs.

## Standing assumptions & treatment rules

### Retirement timing
- **Headline scenario:** {{RETIREMENT_HEADLINE — e.g., "both retire at 62" / "no target set — compute the feasible-age frontier each year"}}. Always show a sensitivity table extending/advancing retirement year by year around the headline.
- **Earliest-feasible-age analysis:** each year, compute the earliest retirement age at which the plan still succeeds at a {{SUCCESS_BAR — e.g., 90%}} bar, with the cost of earlier exits quantified.

<!-- MODULE: variable-compensation -->
<!-- MODULE: equity-compensation -->
<!-- MODULE: deferred-compensation -->
<!-- MODULE: self-employment -->
<!-- MODULE: pension-income -->

### Social Security
- **Headline treatment:** {{SS_HEADLINE — e.g., "$0 assumed (conservative)" or "75% of scheduled benefits"}} — set by preference during setup; revisit annually.
- **Always show sensitivity at 0% / 75% / 100% of scheduled benefits side by side**, so the cost of the chosen assumption stays visible.
- Claiming strategy: {{SS_CLAIMING — decided age or "analyze annually"}}. Use actual SSA statements when provided; otherwise estimate from earnings history; recompute the benefit for earnings stopping at the modeled retirement age.

### Housing
{{HOUSING_TREATMENT — homeowner: see home-mortgage module; renter: "Rent flows into baseline spending; model rent inflation explicitly; no home equity on the balance sheet. Revisit if a purchase becomes a goal (model as a dated scenario, not baseline)."}}

<!-- MODULE: home-mortgage -->

### Cash & emergency fund
- Target: {{EF_TARGET — months of baseline spending and where it sits}}. Each review checks the actual cash trend against the target and flags sustained drift in either direction.

<!-- MODULE: college-funding -->
<!-- MODULE: employer-stock-concentration -->

### Tax optimization
- Audit actual contributions against the household funding priority waterfall ({{WATERFALL — e.g., "401(k) match → HSA → 401(k) max → Roth IRA → taxable"}}), using current-year limits from the standing reference — **verify limits each year, never reuse stale figures**.
- {{TAX_NOTES — household-specific items from setup: backdoor Roth in use? pro-rata exposure? state deductions to capture?}}

### Insurance & estate (gap-check only)
- Flag status of life/disability/umbrella coverage vs. household needs, beneficiary designations, wills{{, and guardianship if minor children}}. Identify gaps; do not draft documents.
- Include a quantified **survivor scenario**: what happens financially if either adult dies this year.

### Fixed household preferences (set at interview; change only via decision log)
{{FIXED_PREFERENCES — from interview section F, one per line, each dated}}

<!-- MODULE: advisor-crosscheck -->
<!-- MODULE: early-retirement-bridge -->

## Report structure (`reports/YYYY-annual-review.md`)

1. Executive summary
2. **Key metrics dashboard** — one column per year, appended annually; the longitudinal spine of the review (assets, spend, success %, earliest feasible age, open risk flags{{, module metrics}})
3. **Actions & decisions for [YEAR]** — prioritized, deadline-flagged list of what to actually do this year; one line each + a short rationale
4. **What changed since last report** — new facts, law/market changes, household changes, each tagged with whether it alters the analysis; includes the scorecard of last year's Actions (Year 1: baseline statement)
5. Assumptions used this year (explicit table)
6. Household balance sheet & year-over-year changes
7. Spending analysis
8. Projection with Social Security sensitivity (0/75/100), outcome distribution, failure shape, implied withdrawal rate vs. benchmarks
{{MODULE_REPORT_SECTIONS — one numbered section per active module, from the module files}}
- Tax optimization audit
- Insurance & estate gap-check (incl. survivor scenario)
- Recommendations with commentary (ordered by impact)
- Items to revisit next year — split into **data to gather** vs. **decisions to score**
- **Glossary of acronyms** — update whenever new terms enter the report

Reports use **rounded figures** (nearest $1k, or $0.1M above $1M); **never account numbers**. Year 2+ reports must open with a scorecard of last year's actions (adopted / declined / deferred, and outcome). Cadence: {{CADENCE — e.g., "annually each January, after the standing-reference refresh"}}.

**Peer review (optional, recommended):** after the draft is complete, run `PEER_REVIEW_PROMPT.md` in a fresh Research-enabled chat (attach report + PROCESS.md + standing reference); adjudicate findings before finalization — accepted findings become decision-log entries.

**Finalization:** {{FINALIZATION — git users: "annotated tag `YYYY-final` on the final commit (optionally a GitHub Release with the PDF)"; no-git users: "save the final report and a dated PDF/HTML copy in `reports/`; that is the permanent archive"}}. Markdown is the source of truth; `python scripts/build_report.py reports/[YEAR]-annual-review.md` builds the shareable HTML/PDF.

Workpapers (spend-screen outputs, projection scripts) are preserved in `data/[YEAR]/workpapers/` — never committed — for exact reproducibility at the next review.

## Decision log

| Date | Decision |
|------|----------|
| {{SETUP_DATE}} | Initial setup: scope, priorities, and module selection per setup interview |
{{INITIAL_DECISIONS — one dated row per standing decision made during setup}}
