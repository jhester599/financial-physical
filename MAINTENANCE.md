# Maintaining this template

Light-duty by design. Two rituals keep it alive:

## 1. Annual seed refresh (each year, ideally by January)

The bundled `research/STANDING_REFERENCE_[YEAR]_SEED.md` is what lets new users start without running Research. It expires yearly. To refresh:

1. Run a Research-enabled Claude chat with `templates/RESEARCH_PROMPT.template.md`'s structure, using a **generic archetype** (no state section — the seed stays state-neutral) and attaching the prior seed.
2. Generalize: no household specifics, module sections tagged *[module: …]*, every current-year figure flagged **[TIME-SENSITIVE]**, provenance note dated.
3. Commit as `research/STANDING_REFERENCE_[YEAR]_SEED.md` (keep prior years — they're harmless history), update the year references in `README.md`, both `SETUP_PROMPT`s, and the Quick Physical's fact card + vitals where figures changed.
4. Add a CHANGELOG entry.

**Off-cycle:** if major legislation lands (the ACA-subsidy question is the current watch item), patch the affected seed section rather than waiting for January.

## 2. Feedback loop

- Users can open GitHub Issues; the most common report will be "the interview didn't handle my situation" — those usually become a new module or a new interview question.
- Real-user confusion in GETTING_STARTED is a bug; fix the doc, not the user.
- Keep `templates/` generation-compatible: the setup prompts read those files, so renaming placeholders or module section headers is a breaking change — note it in the changelog if unavoidable.

## Versioning

Human-readable versions in `CHANGELOG.md` (1.x). No tags/releases required; `main` is always the recommended version.
