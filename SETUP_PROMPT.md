# SETUP_PROMPT.md — One-Time Setup Interview

**When to use:** once, when you first get this template (and again only if your situation changes drastically — new marriage, business sale, retirement).

**How to use:** open Claude Code (or Claude Desktop) in this folder, copy everything below the line, and paste it to Claude. Budget 1–2 hours. You don't need any documents in hand yet — reasonable guesses are fine; everything gets validated with real documents during the annual review.

---

You are setting up a personalized annual household financial review system for me. This folder is a template: it contains skeleton documents and a module library in `templates/`, and your job today is to interview me and then generate my personalized versions of four files: `PROCESS.md`, `DATA_CHECKLIST.md`, `RESEARCH_PROMPT.md`, and `PEER_REVIEW_PROMPT.md`.

Work conversationally and in plain language — assume I am comfortable with my own finances but not necessarily with git, financial jargon, or AI tools. Explain any term of art the first time you use it.

## Step 0 — Preflight (do this before the interview)

1. Verify the `data/` folder exists (create it if missing).
2. Check whether this folder is a git repository (`git rev-parse --is-inside-work-tree`).
   - **If yes:** verify `.gitignore` exists and covers `data/`, `*.pdf` (except `reports/*.pdf`), `*.csv`, `*.xlsx`, and similar statement formats. Fix it if not. Tell me: methodology and reports will be version-controlled; raw data never will be.
   - **If no:** that's completely fine — say so explicitly. Everything works from a plain folder. Skip all git-related steps in the generated documents (use the "no-git" variants noted in the templates), and tell me my archive is simply the dated files in `reports/` and `research/`.
3. Explain the privacy model to me in 3–4 plain sentences: what goes in `data/` (statements, notes — never uploaded or committed), what I should redact first (account numbers, SSNs), what gets saved outside `data/` (methodology, rounded-figure reports), and the rule that reviews run locally on this machine — never upload `data/` files to a web/cloud session.
4. Read `templates/PROCESS.template.md`, `templates/DATA_CHECKLIST.template.md`, `templates/RESEARCH_PROMPT.template.md`, `templates/PEER_REVIEW_PROMPT.template.md`, and skim the module files in `templates/modules/` so you know what you'll be assembling.

## Step 1 — The interview

Interview me across the areas below. Go section by section, a few questions at a time — not one giant questionnaire. Where my answer switches a module on, note it. Where I'm unsure, record the uncertainty rather than forcing an answer (the annual review validates everything against real documents anyway).

**A. Household**
- Who is in the household? (single / couple; names or initials as I prefer for documents; ages)
- Children or other dependents? Ages? Anyone else you help support financially?
- State of residence, and any plans to move (state taxes matter).

**B. Income**
- Employment for each earner: employer type, W-2 / self-employed / business owner / retired.
- Base pay, and whether there is **variable compensation** (bonus/commission) → *variable-compensation module*.
- **Equity compensation** — RSUs, stock options, ESPP, performance shares? → *equity-compensation module*.
- A **nonqualified deferred compensation plan**? → *deferred-compensation module*.
- **Self-employment or business income**? → *self-employment module*.
- **Pension or annuity**, current or future? → *pension-income module*.

**C. Accounts & assets** (approximate balances fine; ranges fine)
- Retirement accounts: 401(k)/403(b)/457, IRAs (traditional/Roth), HSA. Old accounts at former employers?
- Taxable brokerage and cash accounts. Roughly how much cash do you keep, and is that deliberate?
- Any **concentrated position** — employer stock or any single holding that's a big share of your money? → *employer-stock-concentration module*.
- Crypto, private investments, rental property, other unusual assets.

**D. Home & debts**
- Rent or own? If own: rough value, mortgage balance and rate → *home-mortgage module*.
- Other debts: auto, student loans, HELOC, credit cards carried.

**E. Goals & retirement**
- Target retirement age(s) — or "no idea," which is a fine answer (the review will compute feasible ranges).
- If retirement before 65 is even a possibility → *early-retirement-bridge module* (healthcare before Medicare, account-access sequencing).
- Rough annual spending, if known — or we'll derive it from transactions in the first review.
- College funding intentions for each child → *college-funding module*.
- Other major goals: home purchase, sabbatical, supporting parents, charitable giving.

**F. Risk, preferences & values**
- Target stock/bond mix, if you have one; what you did in the last big market drop.
- Emergency-fund preference (months of expenses).
- Anything you've firmly decided that the analysis should treat as fixed (e.g., "we will never sell the house," "I plan Social Security at 70").

**G. Professional help**
- Financial advisor, CPA, estate attorney? What do they cover? → *advisor-crosscheck module* if there's an advisor.
- Estate documents status: wills, guardianship (if minor children), powers of attorney, beneficiary designations.

**H. Priorities**
- Ask me to rank what matters most for this review to nail: retirement readiness, tax optimization, spending clarity, debt strategy, college, concentration risk, estate/insurance gaps, simplification. Top 3–4 become the standing priorities.

## Step 2 — Module selection (confirm with me)

Present a table: every module in `templates/modules/`, on/off based on my answers, one line of reasoning each. Let me override before you generate anything. Core content (balance sheet, spending screen, projection, Social Security sensitivity, tax audit, insurance & estate gap-check, report structure) is always on — it lives in the skeleton, not the modules.

## Step 3 — Generate my four files

Assemble each file from its skeleton in `templates/` plus the relevant sections of each switched-on module (each module file is organized by target document). Fill every `{{PLACEHOLDER}}` from my interview answers. Rules:

1. **`PROCESS.md`** — my analytical contract. Resolve all placeholders; splice module blocks at the marked insertion points; delete unused markers. Initialize the **decision log** with today's date and every standing decision made in this interview (scope, priorities, module choices, fixed preferences from section F). Where I was uncertain, write the assumption **and** flag it `(to validate in first review)`.
2. **`DATA_CHECKLIST.md`** — only documents that exist for my situation (don't list 529 statements if I have no children). Include the annual-inputs interview tables relevant to my modules, and the `data/notes.md` starter template with my actual categories.
3. **`RESEARCH_PROMPT.md`** — write my household archetype block (generic — **no names, no employer names, no dollar amounts**; e.g., "dual-income couple, one earner with RSU compensation, two children, Texas residents"), set the state-specific research section to my state, include module-conditional research areas, keep the durable output-format requirements from the skeleton.
4. **`PEER_REVIEW_PROMPT.md`** — fill the client-profile calibration paragraph (same generic-archetype rule) and keep the panel/adversarial structure from the skeleton.

Show me a summary of each file (not the full text) before writing, then write all four to the repo root. Do **not** modify anything in `templates/` — it stays pristine for re-generation.

## Step 4 — Wrap up

1. If this is a git repo: commit the four generated files with a clear message. If not: skip silently.
2. Create `data/notes.md` from the checklist's template, pre-filled with what I told you today. (This file holds real numbers — confirm it lives in `data/` and is not committed.)
3. Give me a short, numbered **"your next steps"** note (also save it as `NEXT_STEPS.md`):
   - Run `RESEARCH_PROMPT.md` in a Claude chat with **Research enabled**; save the result as `research/STANDING_REFERENCE_[YEAR].md`.
   - Gather documents per `DATA_CHECKLIST.md`, redact account numbers/SSNs, place in `data/`.
   - Open Claude Code in this folder and paste `ANNUAL_REVIEW_PROMPT.md` to run the first review.
4. Remind me of the disclaimer: this is educational decision support — verify numbers before acting, and get professional review for big decisions.

## Hard rules for this session

- Never run `git add`, `git commit`, or any git command that touches `data/`.
- Plain language; explain jargon on first use.
- Don't invent facts about my finances — everything in the generated files must come from my answers or be flagged as an assumption to validate.
- If I seem confused about a question, offer an example answer rather than pressing.
