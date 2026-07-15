# Standing Reference — 2026 SEED EDITION (generalized)

**What this is.** A pre-built edition of the annual "standing reference" — the current-year external facts (tax law, contribution limits, healthcare rules, withdrawal-rate research) that every review needs. It ships with the template so **first-year users don't have to run the Research step before their first review**.

**What it is not.** It is *generalized*: it covers federal rules and durable planning frameworks for common situations, but **not your state's taxes** and not every module's niche. It was distilled in **July 2026** from a Research-verified edition; anything flagged **[TIME-SENSITIVE]** can change with legislation.

**How to use it:**
- **2026 reviews:** use this file as-is; it satisfies the review's staleness gate. For state specifics, ask your review session to look up (or you verify) your state's income-tax treatment of retirement income and its 529 benefit — the two state facts most plans need.
- **2027 and later:** this edition is stale — run your generated `RESEARCH_PROMPT.md` in a Research-enabled chat to produce `research/STANDING_REFERENCE_[YEAR].md`. That personalized refresh also covers your state and your modules properly.
- Sections marked *[module: …]* only matter if that module is in your PROCESS.md — skip freely.

---

## 1. Retirement withdrawal & projection methodology

**Durable principles.** Sequence-of-returns risk — poor returns early in retirement permanently impairing a portfolio because withdrawals sell at depressed prices — is concentrated in the first 5–10 years after retirement. Kitces & Pfau (*Journal of Financial Planning*, Jan. 2014) found a *rising* equity glide path — entering retirement with reduced equity and increasing it over the first 10–20 years (the "bond tent") — outperformed static and declining paths in worst-case periods.

The 4% rule (Bengen, 1994) is a research reference point, not a spending strategy. Dynamic approaches — Guyton-Klinger guardrails, Vanguard dynamic spending, RMD-based — allow higher starting withdrawals in exchange for spending flexibility; they pair best with a solid income floor (Social Security, pension) so downward adjustments don't cut into basic needs.

Historical backtesting (Bengen) and forward-looking Monte Carlo (Morningstar) genuinely disagree because they use different inputs; neither is definitive. For retirements longer than 30 years (early retirees), most research recommends a lower starting rate (~3.25–3.5%) plus dynamic adjustment.

**[TIME-SENSITIVE]**
- Morningstar "The State of Retirement Income: 2025" (Dec. 3, 2025): base-case safe starting withdrawal rate **3.9%** for 30 years at 90% success (up from 3.7%); guardrails strategies supported a **5.2%** starting rate; a 30-year TIPS ladder supported 4.5%.
- Bengen's updated research (*A Richer Retirement*, 2024): historical SAFEMAX **4.7%** with a diversified mix; ~4.2% at 50 years.
- Equity valuations entering 2026 were historically elevated (Shiller CAPE ~42 mid-2026, second-highest reading in 140+ years) — a reason to lean toward the conservative end of the range above.

## 2. Federal tax landscape for 2026

**Durable principles.** Seven progressive brackets; separate long-term capital-gains brackets; parallel systems (AMT, the 3.8% Net Investment Income Tax) catch higher earners. Marginal rate ≠ effective rate.

**[TIME-SENSITIVE]** The One Big Beautiful Bill Act (OBBBA, Pub. L. 119-21, July 4, 2025) made the TCJA-era structure permanent. Key 2026 parameters (IRS Rev. Proc. 2025-32):
- Rates permanent: 10/12/22/24/32/35/37%. Top bracket from $640,600 single / $768,700 MFJ.
- Standard deduction: $16,100 single / $32,200 MFJ.
- Long-term capital gains: 0% to $49,450 single / $96,700 MFJ; 15% to $545,500 / $600,050; 20% above. NIIT adds 3.8% above $200k single / $250k MFJ MAGI (thresholds not inflation-indexed).
- SALT cap: $40,400 for 2026, phasing back toward $10,000 above ~$505k AGI; scheduled to revert after 2029.
- AMT exemption $90,100 single / $140,200 MFJ; phaseouts lowered and steepened for 2026 — more upper-income filers affected.
- Estate/gift exemption: $15M per individual.
- Roth conversion mechanics unchanged; permanence of lower brackets removes "convert before sunset" urgency and favors multi-year pacing. Recharacterization remains prohibited.

## 3. Contribution limits for 2026 **[TIME-SENSITIVE]**

- 401(k)/403(b) elective deferral: **$24,500**; catch-up (50+) applies, with a "super catch-up" of **$11,250** at ages 60–63; workers earning ≥$150,000 must make catch-ups as **Roth** (SECURE 2.0 mandate).
- Total defined-contribution (415(c)) limit: **$72,000** — the ceiling that matters for after-tax "mega backdoor" strategies where a plan allows them.
- IRA/Roth IRA: **$7,500** (under 50). Direct Roth contributions phase out above **$252,000 MFJ** MAGI — higher earners use the backdoor path (watch the pro-rata rule if any pre-tax IRA balances exist).
- HSA: **$8,750** family, +$1,000 catch-up per spouse 55+.
- Verify every figure against IRS publications at review time — these are the numbers most likely to be misremembered by an AI model from training data.

## 4. Roth conversion window planning *[module: early-retirement-bridge]*

**Durable principles.** The "conversion corridor" — years between retirement and Social Security/RMDs — is when taxable income is lowest and conversions are cheapest. Converting fills low brackets now to shrink future RMDs (which begin at 73 for those born 1951–59, 75 for those born 1960+), reduces the surviving-spouse "widow's tax trap," and creates tax-free assets for heirs. Pay conversion tax from non-retirement funds.

Bracket-filling: filling to the top of the 12% bracket is the highest-value move (the 12→22% jump is the largest); households with large pre-tax balances often fill to the top of 22% or 24% if RMD projections show 24%+ later.

Critical interactions: conversions raise MAGI, which (pre-65) can cost ACA subsidies and (63+) sets Medicare IRMAA surcharges two years later. Crossing an IRMAA tier can make the effective marginal rate on the last dollars converted extremely high — but don't let IRMAA-avoidance override the lifetime-tax picture for a large pre-tax balance.

**[TIME-SENSITIVE]** 2026 MFJ bracket ceilings: 12% ≈ $100,800; 24% = $403,550. First IRMAA threshold: $218,000 MFJ / $109,000 single (2-year MAGI lookback).

## 5. Early-retirement healthcare bridge *[module: early-retirement-bridge]*

**Durable principles.** Retiring before 65 requires bridging to Medicare: ACA marketplace, COBRA (≤18 months), a spouse's plan, or part-time work with benefits. The composition of withdrawals drives ACA MAGI (Roth withdrawals and return of basis don't count; traditional withdrawals, conversions, gains, interest, dividends do). Insurers may charge a 64-year-old up to 3× a 21-year-old's premium.

**[TIME-SENSITIVE — the most volatile section in this document]**
- Enhanced premium tax credits **expired Dec. 31, 2025**, restoring the **400%-of-FPL subsidy cliff**: $1 of income above the cutoff loses ALL credits. 2026 cutoffs ≈ $62,600 (single) / $84,600 (two-person) / $128,600 (family of four). Extension legislation was in active flux in early 2026 (retroactive reinstatement possible) — **re-verify status at every review**.
- Full-price benchmarks (2026, directional): ~$1,100/month for a 62-year-old; a pre-Medicare couple should budget roughly **$25,000–$35,000/yr** at full freight. Marketplace out-of-pocket max: $10,600 individual / $21,200 family.
- If the cliff can't realistically be cleared, plan for full-freight premiums and use the low-income years for Roth conversions instead of chasing subsidies.

## 6. College funding *[module: college-funding]*

**Durable principles.** 529s grow tax-free for qualified education expenses; ownership drives financial-aid treatment; overfunding risk is mitigated by beneficiary changes, the $10k lifetime student-loan provision, and the 529-to-Roth rollover.

**[TIME-SENSITIVE]**
- **529-to-Roth rollover** (SECURE 2.0): $35,000 lifetime cap per beneficiary, into the *beneficiary's* Roth IRA; account open ≥15 years; last 5 years of contributions ineligible; each year capped at the annual Roth limit and requires the beneficiary to have earned income; no income limit. Beneficiary changes likely restart the 15-year clock (IRS guidance incomplete).
- **FAFSA (post-simplification):** parent-owned 529s are parent assets assessed at ≤5.64%; student UTMA/UGMA assets at 20%; **grandparent-owned 529s are invisible** — not reported, and distributions no longer count as student income. (~200+ private colleges use the CSS Profile, which may still count them.)
- **Your state:** most states offer a 529 deduction or credit — the amount, per-beneficiary structure, and whether it requires the in-state plan vary widely. Look yours up (state 529 program site) and record it in PROCESS.md.

## 7. Concentrated employer stock *[module: employer-stock-concentration]*

**Durable principles.** A single holding above ~5–10% of investable assets is generally considered concentrated; above ~20% warrants a written plan. For an employee, the honest measure is **total economic exposure to the employer**: vested shares (check inside the 401(k)) + unvested equity + any deferred-comp balance (an unsecured claim on the same company) + human capital (the paycheck itself). The human-capital framework (CFA Institute) is the anchor: don't let financial capital and human capital be devastated by the same event. A practical action test: if a 30–40% decline in the stock would change your retirement date or major plans, the position is too large to manage casually.

Unwind toolbox, cheapest tax first: sell inside tax-advantaged accounts (tax-free); RSUs sold at/near vest (basis ≈ vest price, little embedded gain — "sell at vest" is the default discipline); charitable gifts of lowest-basis lots; loss/low-gain taxable lots; gain-budgeted tranches sized to stay under bracket/NIIT thresholds; exchange funds (7-year lockup) for extreme cases. Check **NUA** treatment before selling low-basis employer stock inside a 401(k). Insiders: coordinate with trading windows / 10b5-1 rules.

## 8. Nonqualified deferred compensation *[module: deferred-compensation]*

**Durable principles.** NQDC is an unfunded, unsecured promise — the employee is a general creditor of the employer; balances are exposed in bankruptcy. Section 409A governs elections rigidly: deferral elections generally must precede the year compensation is earned; distribution triggers are limited to six events; changing an election requires the "12-month/5-year rule" (elect ≥12 months ahead, delay ≥5 more years); violations trigger immediate inclusion + 20% penalty. Lump sums escape credit risk sooner but stack income; installments spread brackets but extend exposure. Installments paid over **≥10 years** are taxable by the state of *residence*, not the state where earned (4 U.S.C. § 114) — relevant if relocating to a low-tax state. NQDC income occupies bracket space in early retirement that would otherwise be Roth-conversion territory — model them together.

## 9. Account drawdown sequencing

**Durable principles.** The conventional order — taxable → traditional → Roth — is a starting point, not a rule; rigid ordering often creates a mid-retirement tax spike when RMDs hit. Better: **tax-bracket-aware/blended** sequencing — in low-income years intentionally realize traditional income or conversions to fill low brackets; in high-income years draw Roth or high-basis taxable to control MAGI (ACA, IRMAA, Social Security taxability). Research (T. Rowe Price, Young & Reichenstein; TIAA Institute) shows tailored sequencing can save tens of thousands in lifetime taxes vs. mechanical ordering. Estate overlay: taxable assets get a basis step-up at death, traditional IRAs don't — bequest-minded households may draw traditional earlier. Roth withdrawals don't count toward IRMAA or Social Security provisional income — reserve Roth as the MAGI-control valve.

## 10. State taxes — NOT covered by this seed

State treatment varies enormously (no-income-tax states; flat-tax states; states that exempt Social Security or retirement income; municipal wage taxes). At minimum, establish for your state: (1) income-tax structure and rates; (2) treatment of retirement-account distributions, pensions, and Social Security; (3) the 529 benefit (section 6); (4) estate/inheritance tax, if any. Your generated `RESEARCH_PROMPT.md` covers this properly at the next refresh; until then, your review session should look these up and flag them as needing verification.

---

## The ten findings most likely to change a household plan (2026)

1. **ACA enhanced subsidies expired 12/31/2025; the 400% FPL cliff is back** — pre-Medicare healthcare is dramatically more expensive and interacts brutally with conversions/withdrawals. Highest-volatility item.
2. **OBBBA made the current brackets permanent** — Roth-conversion pacing can be smoothed over more years; no sunset deadline.
3. **Safe withdrawal rates: Morningstar 3.9% vs. Bengen 4.7%** — a genuine methodological disagreement; early retirees should plan nearer 3.25–3.5% with flexibility, especially at 2026 valuations.
4. **Total employer concentration** (vested + unvested + deferred comp + paycheck) is the honest measure, and it's usually far higher than the brokerage statement suggests.
5. **The rising-equity glide path / bond tent** directly mitigates sequence risk in the make-or-break first decade — match it to the accounts actually funding early retirement.
6. **529-to-Roth rollovers** reshape overfunding risk; grandparent-owned 529s became FAFSA-invisible.
7. **NIIT and (partially) IRMAA thresholds aren't inflation-indexed** — bracket creep pulls more households in every year.
8. **RMD ages are now 73/75** (birth-year dependent) — the conversion corridor is longer than older rules of thumb assume.
9. **Catch-up contributions changed**: ages 60–63 get a super catch-up; higher earners must make catch-ups as Roth.
10. **Tax-bracket-aware drawdown sequencing** beats mechanical ordering by years of portfolio longevity — build the income plan first, then fine-tune MAGI with taxable/Roth.

## Re-verify at every annual review

- [ ] Federal brackets, standard deduction, LTCG/NIIT thresholds, AMT, SALT cap status
- [ ] All contribution limits (section 3) against IRS publications
- [ ] ACA subsidy legislation status + your county's benchmark premiums (KFF calculator) *(if bridge module)*
- [ ] IRMAA thresholds and 2-year lookback *(if near/over 63)*
- [ ] Your state: rates, retirement-income treatment, 529 benefit, estate tax
- [ ] Withdrawal-rate research updates (Morningstar annual edition; Bengen)
- [ ] 529-to-Roth state conformity *(if college module)*
- [ ] RMD ages/rules and Social Security parameters

---

### Provenance & caveats

Distilled July 2026 from a Research-verified standing reference (primary sources: IRS Rev. Proc. 2025-32; Pub. L. 119-21; SSA; CMS; KFF; Kitces & Pfau, *JFP* Jan. 2014; Bengen, *A Richer Retirement*, 2024; Morningstar "State of Retirement Income: 2025"; CFA Institute; T. Rowe Price; 26 CFR § 1.409A-2; 4 U.S.C. § 114), then generalized: state-specific and household-specific content removed. Time-sensitive figures reflect tax year 2026 as of mid-2026; the ACA subsidy question was in active legislative flux — treat those figures as provisional. This document informs analysis; it is not tax or financial advice.
