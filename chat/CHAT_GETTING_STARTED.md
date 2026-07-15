# The Chat Track — Financial Physical without Claude Code

This track runs the whole system in **regular Claude chats** (claude.ai or the mobile/desktop apps) using a **Claude Project** as your filing cabinet. No terminal, no git, no installs. You give up some depth (see "Honest tradeoffs" below) but keep the core: a personalized methodology, an annual report, and a system that remembers year to year.

**Not sure which track you want?** See "Three ways to run it" in the [README](../README.md).

## What you need

- A **Claude Pro** subscription (Projects and Research are included).
- The files from this template (Download ZIP → unzip; you'll upload a few files from it).
- Your documents, when review time comes.

## One-time setup (~1–2 hours)

1. **Create a Project** at claude.ai → Projects → "Financial Physical". Projects give every conversation inside them access to shared "project knowledge" files — that's where your methodology will live.
2. **Set the Project's custom instructions** (Project page → "Set custom instructions") — paste this; it makes every conversation in the Project behave, even quick one-off questions:

   > This project is our household's annual financial review system. Always: treat PROCESS.md in project knowledge as the methodology contract; take tax figures and limits only from the standing reference in project knowledge (flag anything it doesn't cover as "verify" — never quote limits from memory); use plain language and define jargon; use rounded figures and never account numbers in anything meant to be saved; if you spot an account number in an upload, tell me immediately. This is educational decision support, not financial, tax, or legal advice.

3. **Add the starter files to project knowledge:** everything in the template's `templates/` folder (the four skeletons + the `modules/` files), plus `research/STANDING_REFERENCE_2026_SEED.md`.
4. **Run the setup interview:** start a new conversation in the Project, and paste everything below the line in `chat/CHAT_SETUP_PROMPT.md`. Claude interviews you and then produces your four personalized documents (PROCESS.md, DATA_CHECKLIST.md, RESEARCH_PROMPT.md, PEER_REVIEW_PROMPT.md).
5. **Save the outputs twice:** download each generated document to a folder on your computer (your permanent archive), **and** add each to project knowledge (so future conversations can see them). You can remove the `templates/` skeleton files from project knowledge afterwards — they've done their job.

## The annual review (chat edition)

1. **Facts refresh:** in 2026 you can skip this — the seed reference in project knowledge covers it. From 2027: new conversation (Research ON), paste your `RESEARCH_PROMPT.md`, save the output to your folder and replace the old reference in project knowledge.
2. **Gather your numbers** per your DATA_CHECKLIST. You have two options, and can mix them:
   - **Type them in** (most private): current balance per account, rough monthly spending, debts. The checklist tells you what's needed.
   - **Upload redacted statements** (most accurate): black out account numbers/SSNs first. See the privacy note below.
3. **Run the review:** new conversation in the Project, paste everything below the line in `chat/CHAT_ANNUAL_REVIEW_PROMPT.md`, then provide your numbers/documents as it asks.
4. **Save the report** it produces to your folder as `reports/[YEAR]-annual-review.md`, and add it to project knowledge (it's next year's comparison baseline).
5. **Optional peer review:** fresh conversation *outside* the Project (fresh eyes on purpose), Research ON, attach the draft report + your PROCESS.md + the reference, paste `PEER_REVIEW_PROMPT.md`. Bring findings back to finalize.

## Privacy in the chat track — read this

The chat track's privacy model is **different** from the Claude Code track, and you should choose it knowingly:

- In the Code track, your statements sit in a local folder and are read in place. In the chat track, anything you upload or type **is stored in that conversation (and project knowledge, if you add it there) until you delete it**.
- Either way, content you share is processed by Anthropic in the moment — the same trust decision as anything you've ever pasted into Claude. Consumer plans aren't used for model training without opt-in, but read the current privacy policy and decide for yourself.
- Practical hygiene: **redact account numbers and SSNs before uploading anything**; prefer typing summary numbers over uploading raw statements when precision doesn't matter; **delete data-heavy conversations** after you've saved the report; keep raw statements OUT of project knowledge (only methodology, references, and finished reports belong there).

## Honest tradeoffs vs. the Code track

- **Transaction-level spending analysis is the big loss.** A year of raw bank CSVs is more than a chat can comfortably chew through. Workarounds, in order of quality: (a) use your bank's/card's own category-summary export for 12 months and upload that; (b) upload 2–3 representative months of transactions and extrapolate; (c) type in your own spending estimate — the review will flag it as unaudited and treat it more conservatively.
- **Projections are coarser.** Claude chat can run analysis on your numbers, but the Code track's saved workpapers and rerunnable scripts don't exist here. Expect scenario tables rather than full Monte Carlo fan charts.
- **You are the filing system.** Nothing auto-saves; the routine of downloading outputs to your folder and updating project knowledge is manual. The upside: it's just files in a folder — no tooling to learn.
- **Session limits.** A full review may not fit one conversation. That's fine — the review prompt is designed in stages; start a new conversation in the Project and say where you left off (project knowledge carries the context).

## Using another AI (ChatGPT, Gemini, …)

These prompts are plain text — nothing about them is locked to Claude. The full tracks assume two features: a **project/workspace with persistent file knowledge** and a **cited deep-research mode**; if your tool has equivalents (e.g., ChatGPT Projects + deep research), the prompts adapt with minor wording changes. Two honest cautions: we only test this with Claude, and whichever model you use, **the annual facts-refresh step matters more than the model brand** — never let any model quote tax figures from its training memory.

If you just want to try the idea with any AI in an hour, that's exactly what `chat/QUICK_PHYSICAL_PROMPT.md` is for.
