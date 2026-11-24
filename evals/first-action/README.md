# Opening-view check

This evaluation tests a narrow change to Good Enough. When the reader needs to act on the first pass, the candidate asks the agent to try that action from the opening view. It asks the agent to keep required details beside the action and point to the exact location of supporting detail.

## Results

| Check | Baseline | Candidate |
| --- | ---: | ---: |
| First action from the opening | 7/12 | 7/12 |
| Complete answer from the opening | 4/12 | 5/12 |
| Complete answer from the full artifact | 11/12 | 11/12 |
| Preservation checks | 11/12 | 11/12 |
| Complete full answer and preservation | 11/12 | 10/12 |

The candidate tied on the metric it targeted. In one laptop-return SOP, the opening told the reader how to handle the battery, which the matched baseline opening cut off. In one gross-profit workbook, the candidate labeled the actual cost input as a source and directed the reader to edit a separate scenario cell. The reader found the scenario control and could not identify where to edit the actual forecast. [Document scores](md-scores.json) · [Workbook scores](xlsx-scores.json)

The candidate gained complete opening answers on one returns brief and one gross-profit workbook. It lost one on the dispatch brief, where the excerpt ended before the second gate. All eight workbooks retained their inputs and formulas and passed both calculation engines. One document in each condition failed preservation. [All 24 revisions](artifacts/) · [Workbook checks and visible cells](workbook-checks.json)

The default skill uses the baseline wording. The opening-view check remains available in the candidate commit for comparison.

## Method

We generated two fresh revisions per condition for each of the six [existing revision fixtures](../revision/README.md#tasks). Both conditions used the same task, source artifact, model, and tool access. The only change was the skill text. [Baseline skill](https://github.com/bagusfarisa/good-enough/blob/9e0f917481060f457c49c4693e534bedfaa767a8/skills/good-enough/SKILL.md) · [Candidate skill](https://github.com/bagusfarisa/good-enough/blob/a84608fd7e6a9b83ba6bd5b5524b652f08ead2ec/skills/good-enough/SKILL.md)

- **First action from the opening.** Can the reader identify what to do immediately and find the details needed for that step? This uses a [separate question with a narrower answer](questions.json).
- **Complete answer from the opening.** Can a separate reader answer the original, more detailed question from that same view?
- **Complete answer from the full artifact.** Can a reader answer the detailed question using the whole document or all visible workbook sheets?
- **Preservation.** Do the document's material facts and exceptions survive? Do the workbook's inputs and formulas survive, and do both test edits recalculate as expected?

The opening view is the first 120 words of a document or the visible cells in `A1:H18` on a workbook's opening sheet. The reader got only the question and the relevant view. A separate blind judge required correct answers with verifiable evidence. Artifact Tool and LibreOffice applied the workbook edits to disposable copies.

Generation used Codex CLI `0.172.0` and `gpt-6.2-sol` at low reasoning effort. The blind reader used `gpt-6.1-terra`, and the judge used `gpt-6.2-astra`. These six synthetic fixtures were used to identify the problem. Human reading time, ease of following references, and performance on fresh fixtures remain unmeasured.

## Reproduce

Use the [revision evaluation dependencies](../revision/README.md#reproduce). Run the following from the repository root.

```sh
python3 evals/revision/run.py --out /tmp/good-enough-first-action \
  --baseline-revision 9e0f917 --revision a84608f \
  --api /path/to/API_QUICK_START.md --node-modules /path/to/node_modules
python3 evals/revision/check_workbooks.py --out /tmp/good-enough-first-action \
  --node-modules /path/to/node_modules
python3 evals/revision/score.py --out /tmp/good-enough-first-action \
  --first-actions evals/first-action/questions.json --format md
python3 evals/revision/score.py --out /tmp/good-enough-first-action \
  --first-actions evals/first-action/questions.json --format xlsx
```
