# Procedure recovery and preservation check

This test compares the published Good Enough skill with a candidate that asks the agent to walk through the task using the revised artifact. The candidate also asks for the next action and exact restart step for material exceptions. If the source leaves an overlap unresolved, the candidate asks the agent to flag it for the owner.

## Results

| Full reader answer and preservation on the same revision | Published skill | Candidate |
| --- | ---: | ---: |
| Existing suite, round 1 | 11/12 | 12/12 |
| Existing suite, round 2 | 12/12 | 10/12 |
| New SOP with overlapping exceptions | 0/2 | 1/2 |

Both versions passed preservation on all 24 of their existing-suite revisions. All 16 workbooks retained their original inputs and formulas and passed both calculation engines. [Round 1 workbook checks](round-1/workbook-checks.json) · [Round 2 workbook checks](round-2/workbook-checks.json)

- **Round 1.** A baseline price-import reader named the restart step number and left out the fresh upload and Preview rerun. The artifact contained both actions. [Round 1 document scores](round-1/md-scores.json)
- **Round 2.** A candidate price-import reader quoted the upload and Preview instructions and left Preview out of its answer. A candidate laptop-return reader cited all required handling actions. It also named the inspection step without quoting the line that identifies it, so it failed the evidence check. [Round 2 document scores](round-2/md-scores.json)
- **Manual source review.** The candidate laptop SOP also added a return to inspection after Facilities clearance. The source says when the hold ends and leaves the restart step unspecified. This fell outside the existing preservation rubric. The published scores use the original rubric. [Candidate laptop SOP](round-2/artifacts/device-return-1-good-enough.md) · [Source SOP](../revision/fixtures/device-return.md)

The candidate missed the promotion target. The published skill uses the baseline wording. [All round 1 revisions](round-1/artifacts/) · [All round 2 revisions](round-2/artifacts/) · [Round 1 workbook reader scores](round-1/xlsx-scores.json) · [Round 2 workbook reader scores](round-2/xlsx-scores.json)

## Held-out SOP

The baseline scored **0/2** on the combined check, and the candidate scored **1/2**. In one run per condition, the document contained the **11:30 UTC** cutoff, but the reader quoted only the late-file response. The judge required evidence that the noon arrival in the question triggered that response. Both documents passed preservation. The other baseline revision omitted that Sales Operations owns adjustment approvals. The other candidate passed both checks. [New SOP scores and evidence](holdout/md-scores.json)

## Method

Each round uses all six [revision fixtures](../revision/README.md#tasks). Each fixture ran twice per condition in fresh Codex sessions, for 12 revisions per condition per round. The same [reader questions and preservation criteria](../revision/cases.json) were used in both rounds. [Published baseline](https://github.com/bagusfarisa/good-enough/blob/367af6a/skills/good-enough/SKILL.md) · [Candidate](https://github.com/bagusfarisa/good-enough/blob/ed9c6adb728424817c9429e55ccfa91abdce55c6/skills/good-enough/SKILL.md)

A [new SOP](fixtures/dashboard-refresh.md) adds two exception paths, each with an owner. Its source leaves their overlap unresolved. The candidate was committed before this fixture was written. Both versions revised it twice. [Held-out question and rubric](holdout.json)

The reader received the full revised artifact and the question. A blind judge checked whether the answer included every required part and cited evidence from the artifact. The judge checked document preservation separately. Workbook preservation compared input values and formula schedules, then recalculated two test edits in Artifact Tool and LibreOffice. The combined check requires both a correct reader answer and preservation on the same revision.

The promotion target was 12/12 on the combined check in both rounds and 2/2 on the held-out SOP. The experiment uses synthetic sources and AI readers. Human task completion remains unmeasured.

Generation used Codex CLI `0.172.0` and `gpt-6.2-sol` at low reasoning effort. The reader used `gpt-6.1-terra`, and the judge used `gpt-6.2-astra`.

## Reproduce

Use the [revision evaluation dependencies](../revision/README.md#reproduce). Generate the original suite twice in separate output directories. Run the following from the repository root.

```sh
for round in round-1 round-2; do
  results="/tmp/good-enough-finish/$round"
  python3 evals/revision/run.py --out "$results" \
    --baseline-revision 367af6a --revision ed9c6ad \
    --api /path/to/API_QUICK_START.md --node-modules /path/to/node_modules
  python3 evals/revision/check_workbooks.py --out "$results" \
    --node-modules /path/to/node_modules
  python3 evals/revision/score.py --out "$results" --format md --full-only
  python3 evals/revision/score.py --out "$results" --format xlsx --full-only
done

held_out="/tmp/good-enough-finish/holdout"
python3 evals/revision/run.py --out "$held_out" --format md \
  --baseline-revision 367af6a --revision ed9c6ad \
  --cases evals/finish-check/holdout.json
python3 evals/revision/score.py --out "$held_out" --format md --full-only \
  --cases evals/finish-check/holdout.json
```
