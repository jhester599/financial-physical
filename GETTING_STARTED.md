# Getting Started — Step by Step (Claude Code track)

This walkthrough assumes nothing. If you've used GitHub and Claude Code before, the [README quick start](README.md#quick-start-claude-code-track) is all you need.

> **Don't want to install anything?** There are two lighter options: a one-hour **Quick Physical** that works in any AI chat (`chat/QUICK_PHYSICAL_PROMPT.md`), and a full **chat track** that runs the whole system in claude.ai with no installs (`chat/CHAT_GETTING_STARTED.md`). The README's "Three ways to run it" table compares them. This guide covers the deepest option: Claude Code working in a folder on your computer.

## Step 1 — Get Claude

1. You need a **paid Claude subscription** — the **Pro** plan ($20/mo) is enough. It includes both things this system uses: **Claude Code** (Claude working in a folder on your computer) and **Research** (Claude doing cited web research in a chat).
2. Sign up at [claude.ai](https://claude.ai) if you haven't.
3. Install **Claude Code**: follow the official quickstart at [code.claude.com/docs/en/quickstart](https://code.claude.com/docs/en/quickstart). The **desktop app** (Mac/Windows) is the easiest route if you don't live in a terminal — it can open a folder and chat with you about the files in it, which is exactly what we need.

## Step 2 — Get this template onto your computer

**Path A — you don't use GitHub (most people):**

1. On this template's GitHub page, click the green **Code** button → **Download ZIP**.
2. Unzip it somewhere that makes sense long-term, e.g. `Documents/financial-physical`. This folder will accumulate years of reports — treat it like a filing cabinet, not a temp folder.
3. That's it. You never need GitHub again. (Someone can also just send you the ZIP.)

**Path B — you use GitHub:**

1. Click **"Use this template"** → **"Create a new repository"** at the top of the template's page.
2. Name it what you like, and make it **Private**. (The template contains no personal data, but your copy will accumulate reports about your finances — even rounded ones belong in a private repo.)
3. Clone your new repo to your computer.

> **Either path: check your backup story.** If the folder lives only on one laptop, a dead disk loses your history. Path B users are covered by GitHub. Path A users: put the folder somewhere your normal backup covers (Time Machine, OneDrive, iCloud Drive, etc.). The `data/` folder holding raw statements is the sensitive part — if your backup is a cloud-sync service and that makes you uncomfortable, you can exclude `data/` and re-download statements when needed; everything else (methodology, reports) is rounded and redacted by design.

## Step 3 — Run the setup interview (once, ~1–2 hours)

1. Open Claude Code in your folder (desktop app: open the folder; terminal: `cd` into it and run `claude`).
2. Open `SETUP_PROMPT.md` in any text editor. Copy everything **below the horizontal line**.
3. Paste it to Claude and follow along. It will interview you about your household, income, accounts, and goals, then write your personalized methodology files. You don't need documents in hand — good guesses are fine.
4. At the end you'll have a `NEXT_STEPS.md` note. Follow it.

## Step 4 — The facts refresh (~15 minutes of your time)

1. Open a **regular Claude chat** (claude.ai or the app — not Claude Code) and turn on **Research**.
2. Paste everything below the line in your generated `RESEARCH_PROMPT.md`. Research runs take a while; come back when it's done.
3. Save the output as `research/STANDING_REFERENCE_2026.md` (use the current year) in your folder.

This step exists because tax rules and contribution limits change every year and AI models' built-in knowledge goes stale — the annual review **refuses to run** without a current-year reference, on purpose.

## Step 5 — Gather your documents (an afternoon)

Work through your generated `DATA_CHECKLIST.md`:

1. Download recent statements for each account on the list.
2. **Black out account numbers and Social Security numbers** (any PDF editor, or even a marker + rescan). Balances and transactions stay — they *are* the analysis.
3. Put everything in the `data/` folder.
4. Export 12 months of credit-card and bank transactions (CSV exports from your bank's website) into `data/` too.
5. Fill in `data/notes.md` (the setup session started it for you).

## Step 6 — Run your first annual review (~2–3 hours, interactive)

1. Open Claude Code in your folder again. If you can, switch to the strongest model available (`/model`).
2. Paste everything below the line in `ANNUAL_REVIEW_PROMPT.md`.
3. Claude will check your documents against the checklist, walk through the annual questions with you, then build the analysis step by step — balance sheet first, then spending, then projections — checking with you at each stage.
4. The output is `reports/2026-annual-review.md` — your first financial physical.

**Optional but recommended:** run the peer review (`PEER_REVIEW_PROMPT.md` in a fresh Research-enabled chat, attaching your draft report) and let a second Claude try to poke holes in the first one's work before you call it final.

## Every year after

The routine is: **facts refresh → gather documents → run review → (peer review) → file the report**. Each year gets faster because the checklist is stable, the notes carry forward, and the report compares against last year automatically — including a scorecard of whether last year's recommendations actually happened.

## Troubleshooting

- **"Claude says the standing reference is missing/stale."** That's the staleness gate working. Do Step 4 for the current year.
- **"Claude can't see my files."** Make sure you opened Claude Code *in the folder* (the folder name should show in the session), and that files are in `data/`, not on your desktop.
- **A number looks wrong.** Say so, and ask Claude to show the calculation and which document it came from. Claude can misread statements — this is why the process shows intermediate results and why the disclaimer says verify before acting.
- **PDF build fails.** The report is the `.md` file — HTML/PDF are conveniences. See `scripts/build_report.py --help`, or just skip it.

## Cost & privacy, honestly

- **Cost:** a Claude Pro subscription. Heavy review sessions can bump into Pro's usage limits — if that happens, split the review across a couple of days or upgrade for the month.
- **Privacy:** your statements stay in a folder on your machine. During a session, the content Claude reads is processed by Anthropic's API in the moment — the same trust decision as pasting anything into a Claude chat; consumer plans aren't used for model training without opt-in, but read Anthropic's current privacy policy and decide for yourself. What this system adds on top: the files never get uploaded to any cloud storage or repository, account numbers are redacted before Claude ever sees them, and anything committed/shared uses rounded figures only.
