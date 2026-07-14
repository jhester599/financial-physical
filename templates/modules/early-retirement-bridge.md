# Module: early-retirement-bridge

**Switch on when:** retirement before 65 (Medicare) is a target or a live possibility. This is the module that makes early-retirement math honest.

## PROCESS.md additions (under "Standing assumptions & treatment rules")

### Early-retirement bridge (retirement → Medicare at 65 → RMDs)
- **Healthcare bridge:** model self-funded health coverage explicitly from retirement age to 65 as a dedicated spending line, using current marketplace benchmarks from the standing reference. Show it both **with and without premium subsidies** (subsidy rules change; the plan shouldn't depend on them) — a banded estimate is honest, a single number isn't.
- **Account-access sequencing:** map which money is *reachable* in each bridge year — taxable first; then penalty-free early-access paths for retirement accounts where needed (Rule of 55 for the final employer's 401(k), 72(t)/SEPP, Roth contribution basis); {{BRIDGE_INCOME — pension/NQDC/other income streams that arrive during the bridge, if any}}. The projection must show a **funding map**: which account pays for which years.
- **Low-income window planning:** the years between retirement and Social Security/RMDs are typically the household's lowest-bracket years — analyze **Roth conversions** to fill low brackets annually, weighing conversion taxes against future RMDs and (if subsidies matter) the income-level interaction with healthcare subsidies. Target bracket: {{CONVERSION_TARGET — e.g., "top of the 12%/22%/24% bracket — decided annually"}}.
- **Sequence-of-returns protection:** the bridge years carry the plan's concentrated sequence risk. Match the de-risking to the accounts that actually fund the bridge (a spending sleeve of safer assets in the accounts tapped first) rather than de-risking the whole portfolio — accounts untouched for 20+ years can stay growth-heavy.
- Longer horizons need lower withdrawal rates: benchmark the plan's implied rate against the standing reference's early-retirement (35–50 year) research, not the 30-year "4% rule."

## DATA_CHECKLIST.md additions

### Annual inputs rows (section B)
| Health coverage intent for the bridge (marketplace / retiree plan / spouse's plan / COBRA start) | you | bridge cost line |
| Final-employer 401(k) plan: does it allow Rule-of-55 withdrawals / partial withdrawals? | SPD — *needed once* | access sequencing |

## RESEARCH_PROMPT.md additions (research areas)

**Early-retirement healthcare bridge** — current marketplace subsidy structure (cliffs/phase-outs), income-management strategies, and realistic cost benchmarks for pre-Medicare coverage at the household's ages

**Roth conversion window planning** — bracket-filling strategies for the years between early retirement and RMDs, and interactions with healthcare subsidies and Medicare premium surcharges (IRMAA)

## Report section

**Bridge plan** — funding map (which account funds which years), healthcare bridge cost band, Roth-conversion plan for the current/coming year, and the access-path checklist (Rule of 55 / 72(t) / Roth basis) with what's confirmed vs. assumed.
