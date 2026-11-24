# Inverted-pyramid evaluation

This rerun tests the rule that readers should see the result, decision, or first action they need and any condition that changes it before the supporting detail. The tested skill is [commit `1b391a7`](https://github.com/bagusfarisa/good-enough/blob/1b391a77d96cbe3fb06af028fde121e49e6edaec/skills/good-enough/SKILL.md).

## Documents

| Measure | Baseline | Good Enough |
| --- | ---: | ---: |
| Documents passing the rubric | 9/9 | 9/9 |
| Rubric checks passed | 45/45 | 45/45 |
| Blinded judge preferences | 3 | 6 |
| Reader answers supported by the document | 27/27 | 27/27 |
| Median word count | 159 | 156 |
| Median word where supporting evidence ends | 94 | 94 |

| Reader question | Baseline median evidence word | Good Enough median evidence word |
| --- | ---: | ---: |
| Decision brief · Legal review owner and expected timing | 144 | 147 |
| Impact analysis · Expiry timing | 38 | 29 |
| Impact analysis · Customer's next step | 81 | 47 |
| Impact analysis · Open decisions and owners | 239 | 240 |
| SOP · Verification before recording the batch ID | 159 | 152 |

The clearest placement gain was the impact analysis. The revised skill brought the expiry rule and the customer's next step into the opening. Decision-brief timing showed little movement in this rerun. [All 18 documents](documents/artifacts/) · [Rubric scores and judge reasoning](documents/scores.json) · [Reader answers and evidence](documents/intelligibility.json)

## Cash forecast

Both conditions completed the payroll edit and passed all correctness checks in **3 of 3** runs. Changing payroll from **$6,000** to **$7,000** brought ending cash from **$7,000** to **$6,000** in both calculation engines.

| Measure | Baseline | Good Enough |
| --- | ---: | ---: |
| Median row of ending cash | 12 | 2 |
| Median filled rows on the opening sheet | 11 | 9 |
| Workbooks showing an intermediate cash total | 3/3 | 0/3 |
| Workbook failures | 0 | 0 |

The result appeared in row 2 in all three skill runs. The baseline sheets also displayed intermediate cash totals a reviewer could use to trace the calculation. Both conditions had two nonzero tool command exits and recovered in the affected runs. [All six workbooks](cash-forecast/workbooks/) · [Raw workbook scores](cash-forecast/scores.json) · [Original benchmark](../cash-forecast/)

## Method

The four synthetic fixtures were a decision brief, an impact analysis, an SOP, and a cash forecast. Each ran three times in each condition in fresh Codex CLI `0.172.0` sessions with `gpt-6.2-sol` at low reasoning effort. The baseline received the same task and inputs as the skill condition. Both conditions were regenerated for this rerun. [Document fixtures](../automated/cases.json) · [Cash forecast prompt and inputs](../cash-forecast/)

The three document tasks used the [original automated rubric](../automated/). Two baseline responses appended a trailing session-status footnote about saving a vault note. The same filter was applied to both conditions to remove those messages before grading. A blinded `gpt-6.2-astra` judge applied five criteria to each document and recorded pairwise preferences. In a separate test, a blinded `gpt-6.1-terra` reader answered three stakeholder questions from each document alone. The reader test verifies quoted evidence and records the word position at the end of the supporting excerpts. That position measures placement in the text. Human reading time remains unmeasured. [Grading runner](../automated/run.py) · [Reader test](../automated/reader.py)

Cash forecasts used the [original workbook checks](../cash-forecast/#checks). The payroll edit was tested in Artifact Tool and LibreOffice on disposable copies. All workbook links point to original generated outputs.

## Rerun the document suite

From a clone with an authenticated Codex CLI, run both commands in a fresh output directory.

```sh
python3 evals/automated/run.py --revision 1b391a7 --out /tmp/good-enough-inverted-pyramid
python3 evals/automated/reader.py --results /tmp/good-enough-inverted-pyramid
```
