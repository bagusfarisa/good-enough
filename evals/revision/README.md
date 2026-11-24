# Existing artifact revision benchmark

Can an AI agent revise a crowded artifact so its intended reader can complete a specific task? This benchmark tests whether the revision also keeps the material facts, exceptions, inputs, and formulas.

## Tasks

| Source | Intended reader | Task checked after revision |
| --- | --- | --- |
| [Returns rollout brief](fixtures/returns-launch.md) | Support lead | Explain what happens to an already-open request while Product decides scope. |
| [Dispatch decision brief](fixtures/dispatch-brief.md) | COO | Identify what can be approved now, both launch gates, and the fallback. |
| [Price import SOP](fixtures/price-import.md) | Catalog operator | Recover from a duplicate SKU at Preview and resume at the correct step. |
| [Laptop return SOP](fixtures/device-return.md) | Service desk operator | Follow the documented swelling exception, including the hold and whom to call. |
| [Cash forecast](fixtures/cash-review.xlsx) | FP&A reviewer | Explain April ending cash and predict the effect of changing collections. |
| [Gross profit model](fixtures/margin-review.xlsx) | Finance reviewer | Explain June gross profit and predict the effect of changing unit cost. |

## Results

| Measure | Plain prompt | One-line concision prompt | Good Enough |
| --- | ---: | ---: | ---: |
| Answered from the opening view with evidence | 0/12 | 4/12 | 2/12 |
| Answered from the full artifact with evidence | 11/12 | 10/12 | 12/12 |
| Passed all preservation checks | 12/12 | 10/12 | 12/12 |
| Passed both the full reader and preservation checks | 11/12 | 8/12 | 12/12 |
| Median document length | 316 words | 238 words | 307 words |

The reader could answer from five of the six full source artifacts and from none of their opening views. The revision conditions each include eight documents and four workbooks.

The one-line prompt put enough evidence in the opening for more reader answers. It also lost material context in two documents. One rollout brief omitted why already-open requests could expire immediately and force customers to start again if Product included them. [Source brief](fixtures/returns-launch.md) · [One-line revision](artifacts/returns-launch-1-concise.md) · [Document scores](md-scores.json)

All 12 workbooks preserved their input and calculation schedules and passed both engine checks. Both Good Enough cash forecasts showed the opening cash, collections, and payments subtotal on the opening sheet. The reader needed the build tab to recover the individual payment amounts. [Cash workbook example](artifacts/cash-review-1-good-enough.xlsx) · [Workbook reader scores](xlsx-scores.json) · [Calculation checks and visible cells](workbook-checks.json)

Good Enough's strongest result was preserving the source while supporting the full reader task. Plain revision prompts came close. This experiment measures the whole current skill. The incremental effect of the new revision instructions remains unmeasured. [All 36 revisions](artifacts/)

## Method

All inputs are synthetic. Every task ran twice under each of three conditions in fresh Codex CLI `0.172.0` sessions. Generation used `gpt-6.2-sol` at low reasoning effort. The reader was `gpt-6.1-terra` and the judge was `gpt-6.2-astra`.

1. Use the revision prompt alone.
2. Add one sentence to the prompt, “Make it concise and actionable.”
3. Apply [Good Enough at skill revision `9e0f917`](https://github.com/bagusfarisa/good-enough/blob/9e0f917481060f457c49c4693e534bedfaa767a8/skills/good-enough/SKILL.md).

A blind model reader answered each fixture's question from the revision alone. Separate sessions read the opening 120 words or the workbook's opening sheet at A1:H18, and then the full artifact. For workbooks, readers saw values and labels from visible cells. They received the source artifacts through the same reader checks as a reference point. The generator received the revision task and source. The reader questions, expected answers, and checks stayed in the grader.

A separate blind judge graded each answer against the expected answer and the reader's verbatim evidence. The script checked that the quotes appeared in the artifact. The judge also checked five material facts or exception groups per full document and cited the lines that support each passing check. Workbook checks compared the original input and calculation schedules in place. Artifact Tool and LibreOffice verified two input-change scenarios on disposable copies. The published revisions keep their original input values.

The workbook checker uses the adjacent label when identifying an opening result to recalculate. This keeps a separate what-if result out of the base forecast check, even if both amounts happen to be equal.

The opening view measures evidence placement under a fixed cutoff. The full view measures whether the model reader can answer with evidence. Human completion time and slide deck performance remain unmeasured.

## Reproduce

Use an authenticated Codex CLI. Workbook generation uses Node.js, `@oai/artifact-tool`, and its API quick start. Workbook checking also requires Python with `openpyxl` and LibreOffice on PATH.

```sh
python3 evals/revision/run.py --out /tmp/good-enough-revision \
  --revision 9e0f917 --api /path/to/API_QUICK_START.md \
  --node-modules /path/to/node_modules
python3 evals/revision/check_workbooks.py --out /tmp/good-enough-revision \
  --node-modules /path/to/node_modules
python3 evals/revision/score.py --out /tmp/good-enough-revision --format md
python3 evals/revision/score.py --out /tmp/good-enough-revision --format xlsx
```

The [fixture manifest](cases.json) records the task prompts, reader questions, expected answers, and preservation checks. [Source workbook generator](make_workbooks.mjs)
