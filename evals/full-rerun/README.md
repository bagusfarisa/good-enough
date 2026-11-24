# Full Good Enough evaluation rerun

This rerun evaluates [skill revision `f2b31db`](https://github.com/bagusfarisa/good-enough/blob/f2b31db16147a1f1953c2b948b0724040afcf63a/skills/good-enough/SKILL.md) on all six existing synthetic fixtures. Each fixture ran three times per condition, for **18 pairs** and **36 artifacts**. Generation used fresh sessions in Codex CLI `0.172.0` with `gpt-6.2-sol` at low reasoning effort.

## Results

All 36 complete artifacts passed their correctness checks. The comparison condition is specified for each suite below.

| Suite and measure | Comparison | Current skill |
| --- | ---: | ---: |
| Plain-prompt documents · Full rubric pass | 9/9 | 9/9 |
| Plain-prompt documents · Supported reader answers | 27/27 | 27/27 |
| Plain-prompt documents · Median position of supporting evidence (word number) | 108 | 88 |
| Plain-prompt documents · Median document words | 159 | 168 |
| Plain-prompt documents · Blinded judge preferences | 5 | 3 |
| One-month forecast · Correct in both engines | 3/3 | 3/3 |
| One-month forecast · Median row of ending cash | 10 | 2 |
| Two-dependency brief · Full rubric pass | 3/3 | 3/3 |
| Two-dependency brief · All five checks passed in first 100 words | 2/3 | 3/3 |
| Three-month forecast · Correct in both engines | 3/3 | 3/3 |
| Three-month forecast · Visible March payments subtotal | 2/3 | 3/3 |
| Three-month forecast · Supported reader answers | 9/9 | 9/9 |

The original document suite had one tie in the blinded comparison. The strongest gains were in placement. The median evidence word for the Legal review owner and timing went from **156 to 51**. For the impact analysis, it went from **223 to 90** for open decisions and owners, and from **61 to 48** for the customer’s next step. The judge favored the plain-prompt version in all three impact-analysis pairs. Its reasons included grouping work by team and explaining what the launch-day scope decision meant for already-open requests. [Documents, rubric scores, and reader results](documents/)

The one-month forecasts placed the result earlier while preserving recalculation. The three-month forecast consistently showed the payments subtotal with the current skill. Both versions supported all reader answers. The two-dependency comparison missed one dependency in one opening excerpt, and every full brief passed. [One-month workbooks and scores](cash-forecast/) · [Two-dependency briefs and scores](action-grouping/) · [Three-month workbooks, visible values, and scores](financial-traceability/)

## Method

| Suite | Comparison condition | Checks |
| --- | --- | --- |
| Decision brief, impact analysis, and SOP | Plain task prompt | Original five-point rubric and the blind reader questions. [Fixtures](../automated/cases.json) · [Original rubric and method](../automated/) |
| One-month cash forecast | Plain task prompt | Workbook correctness, recalculation after editing payroll, and result placement. [Original fixture and method](../cash-forecast/) |
| Two-dependency decision brief | Skill revision `1b391a7` | Full-brief rubric and the same rubric applied to the opening 100 words. [Original fixture and method](../action-grouping/) |
| Three-month cash forecast | Skill revision `4fd6856` | Receipt-shift recalculation, visible calculation steps, and reader answers supported by cell values. [Original fixture and method](../financial-traceability/) |

The blinded document judge used `gpt-6.2-astra`. The blind reader used `gpt-6.1-terra` and saw the document or visible spreadsheet cells for one artifact at a time. Artifact Tool and LibreOffice independently recalculated disposable copies of every forecast. The workbooks in this report retain the generated inputs. Evidence word positions measure where supporting text appears. Human reading effort and slide deck performance remain unmeasured.

Two generated baseline documents ended with an unrelated session-status footer. The same filter was applied to both conditions before regrading, and the affected documents were reread. The one-month workbook grader matched labels to adjacent values so a side-by-side assumptions and forecast layout received the same calculation checks as a stacked layout.

## Proposed direction

**Prioritize revising existing artifacts for a specific reader task.** Plain prompts already produced accurate documents and one-month forecasts. A revision task gives the skill a clearer job. Start with an overbuilt brief, SOP, or workbook and make the next decision, action, or calculation trace easier to find while preserving the underlying requirements, data, and logic.

- **Give each reader a clear path.** In an impact analysis with several teams, use the team or decision owner as the entry point when that is how readers find their work. Keep an unresolved decision beside the consequence and the person who owns it.
- **Make the finish check specific.** Ask a question a reader actually needs to answer, such as what Support should tell a customer whose request was already open at launch. For a workbook, ask the reviewer to explain a result and predict the effect of one edit. For a revision, verify that material facts, exceptions, and calculations survive.
- **Test against a short instruction.** Compare Good Enough with a plain task prompt and with a one-line request to make the artifact concise and actionable. Use several distinct drafts with real ambiguity or duplicated material. Score successful reader actions and retained requirements before comparing length.
