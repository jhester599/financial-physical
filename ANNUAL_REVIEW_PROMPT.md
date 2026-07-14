# ANNUAL_REVIEW_PROMPT.md

Copy everything below the line into a fresh Claude Code session opened in this folder. Use the strongest available reasoning model (`/model`). Run this **on your own computer** — never in a web/cloud session with files from `data/`.

*(If you haven't run `SETUP_PROMPT.md` yet, do that first — this prompt requires the personalized `PROCESS.md` and `DATA_CHECKLIST.md` it generates.)*

---

You are acting as a financial analyst conducting our household's annual financial review. This is educational analysis — decision support to be verified, not professional advice{{— and it is compared against advice from our professional advisor | kept by setup if advisor module on}}.

**Before doing anything else:**

0. **Verify the standing reference is current.** A `research/STANDING_REFERENCE_[CURRENT YEAR].md` must exist (generated per `RESEARCH_PROMPT.md` — a required pre-req run in a Research-enabled chat session before this review). If it is missing or from a prior year, stop and tell me to run the refresh first. Read it in full once verified: it supplies the current-year tax parameters, contribution limits, and research that this review must use instead of memory.
1. Read `PROCESS.md` in full. It is the analytical contract: scope, standing priorities, assumptions, and treatment rules. Follow it exactly; if you believe a rule should change, raise it with me — do not silently deviate.
2. Read the most recent report in `reports/`, if one exists. Year-over-year comparison against it is required, including a scorecard of last year's recommendations (adopted / declined / deferred, and outcome). If this is the first review, say so and treat this year as the baseline.
3. Inventory `data/` against `DATA_CHECKLIST.md`. List what is present and what is missing, and ask me whether to proceed with gaps or wait.
4. Read `data/notes.md` for this year's household context. If anything material is ambiguous, ask before modeling.
5. **Walk the "Annual inputs to update/validate" tables in `DATA_CHECKLIST.md` with me** — request a confirm-or-update on every item, update `data/notes.md` with the answers, and append any history tables (bonus factors, valuations, etc.) **before** running any analysis.

**Then run the analysis per PROCESS.md:**

- Build the account inventory and household balance sheet
- If balance-history spreadsheets exist, derive the realized multi-year savings rate and cash trend from them and cross-check against current statement balances
- Categorize 12 months of transactions; separate recurring spend from discretionary capital outlays via the auditable screen
- Run the retirement projection with Social Security sensitivity at 0% / 75% / 100%, reporting the outcome distribution, failure shape, and implied withdrawal rate vs. the standing reference's benchmarks
- Audit contributions against the funding waterfall using **current-year limits from the standing reference (verify them — do not reuse prior-year figures)**
- Run every module-specific analysis PROCESS.md requires (its section list is the authority)
- Gap-check insurance and estate items, including the survivor scenario

Work through this interactively — show me intermediate findings (balance sheet, spending summary, projection results) and get my confirmation on judgment calls before drafting.

**Output:** `reports/[YEAR]-annual-review.md` following the report structure in PROCESS.md, with an explicit assumptions table and recommendations ordered by expected impact, each with commentary.

**Hard rules:**

- Never `git add`, commit, or push anything inside `data/`. If this folder is a git repo, verify `.gitignore` covers `data/` before any git operation. If it is not a git repo, skip all git steps without comment.
- Never include account numbers in the report.
- Financial figures in the report: use rounded values per PROCESS.md; confirm with me before finalizing.
- Update the Decision Log in `PROCESS.md` with any new standing decisions we make during the session.
- Where my documents and your memory of rules disagree, the documents and the standing reference win; where you are uncertain about a tax or legal rule, say so and flag it for professional verification rather than guessing.
