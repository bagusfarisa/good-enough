# Create from scratch evaluation

This pilot tested a short addition to Good Enough. It asks the agent to choose one concrete reader task, build the smallest artifact that supports it, state any material assumption or unresolved decision, and try the task before adding more.

## Results

| Check across three runs per format | Plain prompt | Previous skill | Creation rule |
| --- | ---: | ---: | ---: |
| Source fidelity | 9/9 | 9/9 | 9/9 |
| Artifact usable for the task | 9/9 | 9/9 | 9/9 |
| Complete reader answers | 6/9 | 6/9 | 9/9 |
| Complete reader citations | 4/9 | 3/9 | 4/9 |
| Sections, tabs, or slides flagged as avoidable | 5 | 4 | 0 |

- **Decision memo.** Complete answers rose from 2/3 to 3/3. One previous-skill draft had a section the judge could merge. The candidate had zero flagged sections and kept the unassigned retention-plan owner and clearance date visible. [Memo artifacts](artifacts/) · [Memo scores](decision-memo-scores.json)
- **Cash forecast.** Complete answers rose from 1/3 to 3/3. All nine workbooks used one visible tab. Both spreadsheet engines verified that increasing confirmed July receipts by $2,500 moved closing cash from $6,000 to $8,500 and the reserve gap from $1,000 below to $1,500 above. [Workbooks](artifacts/) · [Forecast scores](cash-forecast-scores.json) · [Calculation checks](cash-file-checks.json)
- **Approval deck.** All three candidate decks used two slides. Every deck in both comparison conditions used three. All nine decks passed the reader-answer, package, geometry, rendering, and editable-text checks after the reader question was aligned with the rubric. The candidate kept the trial counts, lack of a control group, and Maple’s unresolved clearance date. [Editable decks](artifacts/) · [Deck scores](approval-deck-scores.json) · [File checks](deck-file-checks.json)

The candidate met the release criteria. It passed every source and file check, kept artifact usability at 3/3 in every format, and reduced flagged structure in two formats. The memo structure gain was one flagged section. The deck gain repeated across all three runs. [Criteria written before generation](protocol.md)

## Catalog SOP regression check

Both skill versions passed the original five-point rubric in all three fresh catalog SOP runs. The candidate drafts retained the source's duplicate-SKU and price-mismatch paths. None introduced the unassigned process-owner handoff found in the earlier restart-rule experiment. [Original SOP rubric](../automated/cases.json) · [Six guardrail drafts and scores](catalog-guardrail/)

## Method

The pilot used one synthetic brief per format and three fresh runs per condition. Both skill conditions used the same task, brief, tool access, and output format as the plain-prompt condition. Generation used Codex CLI 0.172.0 and `gpt-6.2-sol` at low reasoning effort. Readers used `gpt-6.1-terra`, and judges used `gpt-6.2-astra`. Readers saw the artifact without the source. Source fidelity, artifact usability, and reader performance were scored separately. [Generation briefs and rubrics](fixtures.json) · [Previous skill](https://github.com/bagusfarisa/good-enough/blob/9b82636/skills/good-enough/SKILL.md)

I corrected the evaluation in all conditions before making the release decision. The workbook fidelity grader received formulas and independent recalculation evidence. The deck reader question explicitly requested raw counts and the fallback already expected by the rubric. The quote checker treats matching outer quotation marks as formatting and verifies the text inside them. Deck rendering used the bundled runtime. The generated artifacts were unchanged throughout these checks. [Aligned deck reader question](reader-questions.json)

The pilot measures AI reader behavior on three synthetic briefs. Human reading time and performance on other creation tasks remain unmeasured.
