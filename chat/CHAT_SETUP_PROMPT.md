# CHAT_SETUP_PROMPT.md — One-Time Setup Interview (Chat Edition)

**Before pasting this:** create a Claude Project ("Financial Physical") and add to its project knowledge: the four skeletons from `templates/`, the files in `templates/modules/`, and `research/STANDING_REFERENCE_2026_SEED.md`. Full instructions: `chat/CHAT_GETTING_STARTED.md`.

Then start a **new conversation inside the Project** and paste everything below the line. Budget 1–2 hours. No documents needed yet — good guesses are fine.

---

You are setting up a personalized annual household financial review system for me, inside this Claude Project. The project knowledge contains skeleton documents (`PROCESS.template.md`, `DATA_CHECKLIST.template.md`, `RESEARCH_PROMPT.template.md`, `PEER_REVIEW_PROMPT.template.md`) and a library of module files. Your job today: interview me, then generate my four personalized documents from those skeletons and modules.

Work conversationally and in plain language — assume I'm comfortable with my own finances but not with financial jargon or AI tools. Explain any term of art the first time you use it.

**This is the chat edition** — there is no file system and no git. Instead:
- You will output each generated document as a complete, self-contained artifact/code block that I can download or copy.
- I am responsible for saving them: to a folder on my computer (my archive) and into this Project's knowledge (so future review conversations can read them). Remind me of both at the end.
- Wherever the skeletons mention git, committing, or reading files from disk, translate to the chat equivalent (saving files, project knowledge, attaching documents to conversations).

## Step 0 — Preflight

1. Confirm you can see the four skeletons and the module files in project knowledge. If any are missing, list exactly which and stop so I can add them.
2. Explain the privacy model for the chat track in 3–4 plain sentences: anything I upload or type is stored in the conversation (or project knowledge) until I delete it; I should redact account numbers/SSNs before uploading anything; raw statements should never go into project knowledge (only methodology, references, and finished reports); I can always type summary numbers instead of uploading documents.

## Step 1 — The interview

Interview me across the areas below, a few questions at a time — not one giant questionnaire. Where an answer switches a module on, note it. Where I'm unsure, record the uncertainty rather than forcing an answer (the annual review validates everything later).

**A. Household** — who's in it (single/couple; names or initials as I prefer; ages); dependents; state of residence and any plans to move.

**B. Income** — employment per earner (W-2 / self-employed / business / retired); base pay; **variable comp** (bonus/commission) → *variable-compensation module*; **equity comp** (RSUs/options/ESPP) → *equity-compensation module*; **nonqualified deferred comp** → *deferred-compensation module*; **self-employment/business income** → *self-employment module*; **pension or annuity** → *pension-income module*.

**C. Accounts & assets** (approximate balances or ranges fine) — retirement accounts incl. old-employer plans; taxable and cash accounts; any **concentrated position** → *employer-stock-concentration module*; unusual assets.

**D. Home & debts** — rent or own (if own: rough value, mortgage balance/rate → *home-mortgage module*); other debts.

**E. Goals & retirement** — target retirement age(s) or "no idea"; if pre-65 retirement is even possible → *early-retirement-bridge module*; rough annual spending if known; college intentions per child → *college-funding module*; other major goals.

**F. Risk, preferences & values** — target stock/bond mix; behavior in the last big drawdown; emergency-fund preference; anything firmly decided that the analysis should treat as fixed.

**G. Professional help** — advisor/CPA/attorney and what they cover → *advisor-crosscheck module* if an advisor exists; estate documents status.

**H. Priorities** — have me rank what matters most (retirement readiness, tax, spending clarity, debt, college, concentration, estate/insurance, simplification); top 3–4 become the standing priorities.

## Step 2 — Module selection (confirm with me)

Present a table: every module in project knowledge, on/off based on my answers, one line of reasoning each. Let me override before you generate anything. Core content (balance sheet, spending screen, projection, Social Security sensitivity, tax audit, insurance & estate gap-check, report structure) is always on — it lives in the skeletons.

## Step 3 — Generate my four documents

Assemble each from its skeleton plus the relevant sections of each switched-on module (module files are organized by target document). Fill every `{{PLACEHOLDER}}` from my answers; use the "no-git" variants throughout. Rules:

1. **PROCESS.md** — my analytical contract. Splice module blocks at the marked insertion points; delete unused markers. Initialize the **decision log** with today's date and every standing decision from this interview. Flag uncertain answers `(to validate in first review)`. Additionally, adapt the workpapers rule for chat: intermediate calculations worth keeping get pasted into the report's appendix or saved by me alongside it — there is no workpapers folder.
2. **DATA_CHECKLIST.md** — only documents that exist for my situation. Include the annual-inputs interview tables for my modules, and the `notes.md` starter template with my actual categories. Add a chat-specific line at the top: numbers can be provided by typing summaries OR uploading redacted documents, and which items truly need documents vs. which are fine typed (balances: fine typed; transaction-level spending: needs an export or bank category summary).
3. **RESEARCH_PROMPT.md** — write my household archetype block (generic — **no names, no employer names, no dollar amounts**), set the state-specific research section to my state, include module-conditional research areas, keep the skeleton's output requirements. Note at the top: for 2026, the seed reference in project knowledge already satisfies this except for state specifics.
4. **PEER_REVIEW_PROMPT.md** — fill the client-profile calibration paragraph (same generic-archetype rule); keep the panel/adversarial structure.

Show me a one-paragraph summary of each document before producing it. Then output all four, each as its own complete artifact/code block, clearly labeled with its filename.

## Step 4 — Wrap up

1. Tell me explicitly to do two things with each document: **download/save it** to my Financial Physical folder, and **add it to this Project's knowledge**. (And that I can remove the `templates/` skeletons from project knowledge now.)
2. Produce `notes.md` pre-filled from today's answers — remind me this one contains real numbers and belongs **only** in my private folder, never in project knowledge.
3. Give me a short numbered "your next steps" note: (a) for a 2026 review the seed reference suffices — from 2027, run RESEARCH_PROMPT.md in a Research-enabled chat and replace the reference in project knowledge; (b) gather numbers/documents per DATA_CHECKLIST.md; (c) start a new conversation in this Project and paste `chat/CHAT_ANNUAL_REVIEW_PROMPT.md`.
4. Restate the disclaimer: educational decision support — verify numbers before acting; professional review for big decisions.

## Hard rules for this session

- Plain language; explain jargon on first use.
- Don't invent facts about my finances — everything in the generated documents must come from my answers or be flagged as an assumption to validate.
- If I seem confused by a question, offer an example answer rather than pressing.
- Do not quote specific tax limits/brackets from memory — use the seed reference in project knowledge and cite it.
