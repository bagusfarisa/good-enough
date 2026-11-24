# Complete Good Enough evaluation rerun

This rerun compares the published skill with the narrower SOP restart candidate. The candidate asks the agent to name a restart step the source establishes and to flag unresolved restart rules or overlaps for the procedure owner. Both versions received the same source, task, and tools for each fixture. [Published skill](https://github.com/bagusfarisa/good-enough/blob/73ea3f7/skills/good-enough/SKILL.md) · [Candidate skill](https://github.com/bagusfarisa/good-enough/blob/369a27c/skills/good-enough/SKILL.md)

## Creation results

| Check | Published skill | Candidate |
| --- | ---: | ---: |
| Original document rubric, all checks passed | 9/9 | 6/9 |
| Original documents, correct reader answers | 27/27 | 25/27 |
| Original documents, correct answers with verified evidence | 24/27 | 25/27 |
| Two-dependency brief, full rubric | 3/3 | 3/3 |
| Two-dependency brief, rubric in the first 100 words | 3/3 | 3/3 |
| One-month cash forecast, correctness in both engines | 3/3 | 3/3 |
| One-month cash forecast, median row of ending cash | 2 | 3 |
| Three-month cash forecast, correctness in both engines | 3/3 | 3/3 |
| Three-month forecast, labeled March payments subtotal | 3/3 | 2/3 |
| Three-month forecast, supported reader answers | 9/9 | 9/9 |

The three candidate document rubric failures came from the same catalog procedure fixture. Every candidate draft added a process-owner approval or handoff that the source never assigned. The published skill passed all three versions of that SOP. [Catalog source and rubric](../automated/cases.json) · [Creation scores and revisions](documents/) · [Two-dependency scores and revisions](action-grouping/)

The one-month workbook edit raised payroll from $6,000 to $7,000 and reduced ending cash from $7,000 to $6,000. The three-month edit shifted $3,000 of receipts from February to March. Every workbook recalculated the expected balances in both engines. [One-month scores and workbooks](cash-forecast/) · [Three-month scores and workbooks](financial-traceability/)

## Revision results

| Check on six existing revision fixtures | Published skill | Candidate |
| --- | ---: | ---: |
| First action from the opening | 5/12 | 7/12 |
| Complete answer from the opening | 2/12 | 4/12 |
| Complete answer from the full artifact | 11/12 | 10/12 |
| Original preservation checklist | 11/12 | 12/12 |
| Complete full answer and preservation on the same revision | 11/12 | 10/12 |
| Revised workbooks, correctness in both engines | 4/4 | 4/4 |

Four of the candidate's first-action passes came from workbooks, compared with two for the published skill. Both candidate price-import SOPs passed the original preservation checklist and supported the task in the independent usability check. Their readers missed different steps. One omitted reopening Preview and the other omitted the fresh upload. [Revision artifacts and scores](revision/)

## SOP diagnostics

| Source fidelity by fixture group | Published skill | Candidate |
| --- | ---: | ---: |
| Price import and laptop-return revisions | 2/4 | 1/4 |
| Dashboard refresh holdout | 1/2 | 2/2 |
| Three newer restart SOPs | 4/6 | 5/6 |
| Total on the six SOP revision fixtures | 7/12 | 8/12 |

Usability passed in 12/12 runs per version. Reader answers passed in 9/12 for both versions. Citation completeness was 9/12 with the published skill and 8/12 with the candidate. The independent fidelity check found material changes outside the original revision checklist. [Revision SOP diagnostics](revision/sop-diagnostics.json) · [Dashboard diagnostics and original scores](dashboard/) · [Newer SOP diagnostics](procedures/)

The rerun shows a mix of gains and losses. The candidate moved more of the revision tasks into the opening view and scored one additional fidelity pass on SOP revisions. The full-answer and preservation check was lower, and all three candidate drafts for the original catalog SOP introduced an unassigned process-owner step. The published skill keeps the existing wording.

## Coverage

Sixteen distinct fixtures produced 38 paired runs and 76 new artifacts. The original creation fixtures ran three times per condition. The revision fixtures and newer SOPs ran twice per condition.

| Suite | Fixtures | Checks |
| --- | ---: | --- |
| Original document creation | 3 | Full rubric, blind preferences, reader answers and evidence position. [Fixtures and rubric](../automated/) |
| Two-dependency approval brief | 1 | Full rubric and first 100 words. [Fixture](../action-grouping/) |
| One-month cash forecast | 1 | Formula correctness, payroll edit recalculation, and ending cash placement. [Task and inputs](../cash-forecast/) |
| Three-month cash forecast | 1 | Receipt-shift recalculation, visible March calculation, and supported reader answers. [Task, inputs, and reader rubric](../financial-traceability/) |
| Existing artifact revisions | 6 | First action, complete answers from the opening and full artifact, source preservation, and separate SOP diagnostics. [Fixtures and rubric](../revision/) · [First-action questions](../first-action/questions.json) |
| Dashboard refresh and newer restart SOPs | 4 | Source fidelity, usability, reader answers, and citations. The dashboard also received the original full-answer and preservation checks. [Dashboard fixture](../finish-check/holdout.json) · [Restart fixtures](../procedure-restart/cases.json) |

Generation used fresh sessions in Codex CLI `0.172.0` with `gpt-6.2-sol` at low reasoning effort. Blind readers used `gpt-6.1-terra`, and model judges used `gpt-6.2-astra`. Artifact Tool and LibreOffice tested the spreadsheet scenarios on disposable copies. The published files keep the original values.

The original rubric and the independent SOP source-fidelity check measure different requirements. The SOP check can flag a new material instruction even if the older checklist passes. Readers and judges saw one task at a time without the skill identity. Benchmark fixtures are synthetic. Human reading time and slide performance remain unmeasured.

I corrected two label-matching errors before reporting the workbook results. The one-month checker now recognizes “Forecast ending cash” and “Projected ending cash.” The revision checker excludes a labeled trial gross-profit figure when testing the main forecast after changing its input. Both fixes apply to both conditions. The workbook files and the revision reader views were identical before and after the corrections.

## Reproduce

Use the [existing benchmark runtime and commands](../revision/README.md#reproduce). For the paired comparison, pass `--baseline-revision 73ea3f7 --revision 369a27c` to the generation runs. The [original full rerun](../full-rerun/) gives the forecast recalculation scenarios and the document method. The [first-action follow-up](../first-action/) and [SOP diagnostic report](../procedure-restart/) give the reader and scoring commands for those suites.
