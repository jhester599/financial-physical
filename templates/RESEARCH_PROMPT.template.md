<!-- SKELETON — the setup interview writes the archetype block (generic, no personal data),
     sets the state, includes module-conditional research areas, and writes the result to
     /RESEARCH_PROMPT.md. -->

# RESEARCH_PROMPT.md — Annual Standing-Reference Refresh (Required Pre-Req)

**This is a required prerequisite of the annual review.** Before running `ANNUAL_REVIEW_PROMPT.md`, a current-year `research/STANDING_REFERENCE_[YEAR].md` must exist; the review stops if it's missing or stale.

To refresh: copy everything below the line into a fresh Claude chat with **Research enabled**, and **attach the prior year's edition** so the report is an update, not a rebuild (first year: run it without an attachment). Save the output as `research/STANDING_REFERENCE_[YEAR].md`{{ and commit it | git only}}. Re-run annually, and off-cycle after major tax legislation.

---

Research current best practices, rules, and strategy frameworks for the household archetype below. The report will serve as a standing reference for annual financial reviews, so cite sources with dates and clearly separate durable frameworks from time-sensitive figures and rules. If a prior edition is attached: preserve its structure, re-verify every **[TIME-SENSITIVE]** figure from primary or named sources rather than carrying it forward, and open with a short **"What changed since the prior edition"** summary of the deltas that most affect the plan.

## Household archetype (generic — no personal data)

{{ARCHETYPE_BLOCK — 4–7 bullets describing the household in generic terms: earner structure,
compensation types, dependents, state, account types in use, retirement horizon, whether a
professional advisor is involved. NO names, employers, or dollar amounts.}}

## Research areas

1. **Retirement withdrawal & projection methodology** — current state of safe withdrawal rate research (static vs. dynamic/guardrails approaches), Monte Carlo assumption debates, sequence-of-returns risk mitigation, and equity glide path recommendations near retirement
2. **Federal tax landscape for the current year** — brackets and rules following the most recent major tax legislation; what changed versus prior law; current status of provisions affecting retirement-account strategy, deductions, and capital gains at this household's income level
3. **{{STATE}} state tax specifics** — current income tax structure and legislative trajectory, treatment of retirement income, and local/municipal tax considerations
4. **Account contribution & drawdown strategy** — current-year contribution limits across account types; current research on taxable/traditional/Roth withdrawal ordering, including blended and tax-bracket-aware approaches
{{MODULE_RESEARCH_AREAS — numbered continuation, one per active module, from the module files
(e.g., NQDC distribution strategy, concentrated-stock management, Roth conversion windows,
ACA bridge, 529 rules for {{STATE}}, pension/annuity election frameworks, self-employment
retirement plans & QBI)}}

## Output requirements

- Markdown, organized by the numbered sections above
- Within each section: durable principles first, then current-year specifics flagged **[TIME-SENSITIVE — verify annually]**
- Cite sources with publication dates; prefer primary sources (IRS, SSA, healthcare.gov, state revenue departments, academic and practitioner research)
- Close with: (a) the ten findings most likely to change a household plan, and (b) a checklist of items to re-verify at every annual review
