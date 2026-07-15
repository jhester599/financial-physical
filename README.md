# Financial Physical 🩺💰

An annual household financial review — a **"financial physical"** — that you run with an AI assistant, using your own documents. Once a year you gather your statements, sit down with Claude for an afternoon, and walk away with a written report: where you stand, what changed since last year, and a prioritized list of actions.

This is a **template**. It doesn't come with a methodology baked in — your first session is a guided interview where Claude learns your situation (your income sources, accounts, family, goals) and writes a personalized methodology just for you. A renter with a pension gets a different checkup than a homeowner with stock compensation. After setup, the same annual routine works for both.

## Three ways to run it — pick your track

| | ⚡ Quick Physical | 💬 Chat track | 🖥️ Claude Code track |
|---|---|---|---|
| **What it is** | One-prompt mini-review in a single sitting | The full system, run in regular Claude chats using a Claude Project | The full system, run by Claude Code in a folder on your computer |
| **You need** | Any capable AI chat (Claude, ChatGPT, Gemini…) | Claude Pro (claude.ai — no installs) | Claude Pro + Claude Code installed |
| **Personalization** | Generic — you type in your numbers | Personalized methodology via the setup interview | Personalized methodology via the setup interview |
| **Depth** | Snapshot + simple projection + top actions | Full report; coarser projections, summary-level spending | Full report; transaction-level spending audit, deepest analysis |
| **Data handling** | Type summary numbers into a chat | Type numbers and/or upload redacted documents to your Project | Raw documents stay in a local folder, read in place |
| **Start here** | [`chat/QUICK_PHYSICAL_PROMPT.md`](chat/QUICK_PHYSICAL_PROMPT.md) | [`chat/CHAT_GETTING_STARTED.md`](chat/CHAT_GETTING_STARTED.md) | [`GETTING_STARTED.md`](GETTING_STARTED.md) |

**Not sure?** Do the Quick Physical this weekend — it takes an hour (10 minutes of it with the [fill-in worksheet](chat/QUICK_PHYSICAL_WORKSHEET.md)), gives you a vitals scorecard, and tells you whether the full version is worth your time — [see a fictional example of its output](examples/EXAMPLE-quick-physical-output.md). You can graduate tracks any time; they share the same methodology files. And you don't need to run any Research step your first year: a **pre-built 2026 reference** ships in [`research/STANDING_REFERENCE_2026_SEED.md`](research/STANDING_REFERENCE_2026_SEED.md).

> **⚠️ Important disclaimer — read this first**
>
> This is an **educational decision-support tool, not financial, tax, or legal advice**. Claude is a language model: it can make arithmetic mistakes, misread documents, and cite outdated rules. The methodology here is designed to reduce those risks (current-year fact refreshes, adversarial peer review, explicit assumptions), not eliminate them. **Verify any number before acting on it**, especially tax figures. For large or irreversible decisions — retirement dates, pension elections, large stock sales, estate documents — get professional review. If you have a financial advisor, use this as a second opinion and discussion agenda, never as a replacement.

## What you get

- **A written annual report** with an executive summary, a metrics dashboard that grows one column per year, a prioritized action list with deadlines, an explicit assumptions table, and a scorecard of how last year's recommendations turned out.
- **A retirement projection** with sensitivity analysis (what if Social Security pays less? what if returns disappoint? what if you retire two years earlier?).
- **A spending analysis** built from your real transactions, separating recurring living costs from one-time projects.
- **A tax checkup** against current-year rules and contribution limits — refreshed every year, never from the model's memory.
- **An accumulating system**: each year's decisions get logged, each year's report compares against the last. It gets more valuable the longer you run it.

## How it stays private

*(This section describes the Claude Code track — the most private option. The chat track's model is different and is explained honestly in [`chat/CHAT_GETTING_STARTED.md`](chat/CHAT_GETTING_STARTED.md): uploads are stored in your conversation/Project until you delete them.)*

**Your raw financial data never leaves your machine.** The system is built around one rule:

- Everything sensitive — statements, transaction exports, notes with real numbers — lives in the `data/` folder, which is **excluded from git** and never uploaded anywhere.
- What gets saved/committed is only *methodology* (how the analysis works) and *reports* (which use rounded figures and never account numbers).
- Before placing statements in `data/`, black out account numbers and SSNs. Balances and transactions stay — that's the analysis.
- During a session, Claude reads your files locally and the content it analyzes is processed by Anthropic's API in the moment — same as anything you'd paste into a Claude chat. Nothing is stored in this repository or on GitHub.
- **Always run reviews on your own computer** (Claude Code in this folder, or Claude Desktop pointed at it) — never upload `data/` files to a web/cloud session.

## What you need (Claude Code track)

1. **A Claude subscription** with Claude Code and Research included (Pro works; Max if you use Claude heavily). ~$20+/month.
2. **Claude Code** installed ([quickstart](https://code.claude.com/docs/en/quickstart)) or the **Claude Desktop app**.
3. **Your documents**: recent statements for every account, 12 months of bank/credit-card transactions, insurance summaries. (You'll get a personalized checklist during setup.)
4. **Time**: ~1–2 hours for the setup interview, an afternoon gathering documents, ~2–3 hours for the first annual review. Later years are faster.

**GitHub is optional.** If you don't use GitHub, just download this template as a folder and everything works — see [GETTING_STARTED.md](GETTING_STARTED.md).

## Quick start (Claude Code track)

**If you use GitHub:** click **"Use this template"** at the top of this page → create a **private** copy under your account → clone it to your computer.

**If you don't:** click **Code → Download ZIP** on this page, unzip it somewhere sensible (e.g., `Documents/financial-physical`), and work in that folder. No git required.

Then, either way:

1. Open Claude Code (or Claude Desktop) in the folder.
2. Open `SETUP_PROMPT.md`, copy everything below the line, and paste it to Claude.
3. Answer the interview questions. Claude writes your personalized `PROCESS.md` (your methodology), `DATA_CHECKLIST.md` (your document list), and research prompts.
4. Follow the "next steps" Claude gives you at the end — they walk you into your first annual review.

Full walkthrough with more hand-holding: **[GETTING_STARTED.md](GETTING_STARTED.md)**.

## The annual routine (after setup)

1. **Refresh the facts** *(required first step each year)*: run `RESEARCH_PROMPT.md` in a Claude chat with Research enabled; save the output as `research/STANDING_REFERENCE_[YEAR].md`. This gives the review current tax law, contribution limits, and research — the review refuses to run on a stale edition. *(For 2026 reviews you can skip this: the bundled seed edition in `research/` satisfies it, minus your state's specifics.)*
2. **Gather documents** per your `DATA_CHECKLIST.md`, redact account numbers, place in `data/`.
3. **Update your notes** file in `data/` (template in the checklist).
4. **Run the review**: open Claude Code in this folder, paste `ANNUAL_REVIEW_PROMPT.md`. Claude inventories your documents, walks the annual-inputs interview with you, runs the analysis per your `PROCESS.md`, and drafts the report interactively.
5. **Peer review** *(optional, recommended)*: run `PEER_REVIEW_PROMPT.md` in a *fresh* Claude chat with Research enabled — an independent adversarial review of the draft. Bring the findings back and adjudicate them before finalizing.
6. **Finalize**: save the report to `reports/[YEAR]-annual-review.md`; optionally build a shareable HTML/PDF with `python scripts/build_report.py`. If you use git, commit and tag `[YEAR]-final`; if not, the dated report file in `reports/` is your archive.
7. **Log decisions**: any new standing decision goes in the `PROCESS.md` decision log, so next year's review remembers.

## Folder structure

```
financial-physical/
├── README.md                    # this file
├── GETTING_STARTED.md           # step-by-step first-time walkthrough
├── SETUP_PROMPT.md              # ★ START HERE — the one-time setup interview
├── ANNUAL_REVIEW_PROMPT.md      # kickoff prompt for each year's review
├── PROCESS.md                   # (created by setup) YOUR methodology & decision log
├── DATA_CHECKLIST.md            # (created by setup) YOUR document list & annual inputs
├── RESEARCH_PROMPT.md           # (created by setup) YOUR annual facts-refresh prompt
├── PEER_REVIEW_PROMPT.md        # (created by setup) YOUR independent-review prompt
├── chat/                        # 💬 the no-installs tracks: Quick Physical + chat edition
├── templates/                   # skeletons + module library the setup interview uses
├── examples/                    # a FICTIONAL example report excerpt (not real numbers)
├── scripts/build_report.py      # optional: report markdown → HTML → PDF
├── research/                    # standing references (2026 seed edition included)
├── reports/                     # committed: one report per year (rounded figures only)
└── data/                        # ★ NEVER COMMITTED — your raw statements & notes
```

## Model guidance

Use the strongest reasoning model available for the annual review itself — it's a once-a-year task with heavy multi-document analysis, worth the best model you have access to (switch with `/model` in Claude Code). Lighter/faster models are fine for checklist edits and small updates.

## Updates & questions

The template improves over time (see [CHANGELOG.md](CHANGELOG.md)) and the bundled seed reference is refreshed annually. Updates never touch your generated files — to pick them up, re-download the prompts/seed you use, or `git pull` if you cloned. Questions, confusion, or "the interview didn't handle my situation" reports → open a GitHub Issue on this repo; that feedback is how the template gets better.

## Origin

This template is the generalized skeleton of a real household's annual-review system, built and refined through actual use — the methodology patterns (privacy-first data handling, annual fact refresh, adversarial peer review, accumulating decision log) survived a full annual cycle including an independent review. The personal details didn't come along; your setup interview writes your own.
