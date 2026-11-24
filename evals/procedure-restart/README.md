# SOP restart and source fidelity

The earlier finish-check experiment found a restart step that the source left unspecified. The preservation checklist missed the addition. It also counted incomplete reader answers and incomplete citations together. This experiment separates those outcomes before testing a narrower SOP instruction.

## Targeted results

| Check on six fresh revisions per condition | Published skill | Candidate |
| --- | ---: | ---: |
| Source fidelity | 4/6 | 6/6 |
| Artifact usability | 6/6 | 6/6 |
| Fidelity and usability on the same revision | 4/6 | 6/6 |
| Reader answer completeness | 6/6 | 5/6 |
| Reader citation completeness | 6/6 | 6/6 |

Both combined gains came from the translation SOP. Both baseline drafts added a requirement to test whether registration links work. The source requires checking that the links match the workbook. The candidate drafts also made the route for an unspecified restart explicit by naming the Schedule procedure owner. Usability passed in both conditions. [Translation source](fixtures/schedule-translation.md) · [All targeted scores](targeted/scores.json)

Both conditions passed fidelity and usability on both runs of the handout and library SOPs. One library reader with the candidate named Member Services as the decision maker but omitted the clerk's step of asking that team about reinstatement. [All 12 generated SOPs](targeted/artifacts/)

The targeted run improved on one of three fixtures. The rerun criteria required gains on at least two, so the published skill uses the existing wording.

## Calibration on published revisions

| Check | Passed |
| --- | ---: |
| Source fidelity | 6/20 |
| Artifact usability for the tested question | 20/20 |
| Reader answer completeness | 16/20 |
| Reader citation completeness | 15/20 |

- The laptop-return revision invented a return to inspection after Facilities clearance. The source-fidelity check caught the addition and the usability check passed the handling steps asked for in the scenario. [Round 2 diagnostics](calibration/round-2.json)
- The price-import SOP supported the complete restart, including reopening Preview. The reader quoted that step and omitted it from its answer. The revised evaluator passed the artifact and citation checks and failed the answer check. [Round 2 diagnostics](calibration/round-2.json)
- A dashboard reader gave both recovery paths and named the owner of the unresolved overlap. It missed the **11:30 UTC** cutoff in its quotes, so the answer passed and the citations failed. [Dashboard diagnostics](calibration/holdout.json)

The low source-fidelity count includes added requirements outside the reader scenarios. For example, some price-import revisions made waiting for Catalog Operations mandatory after a failed batch. The source requires the wait after an Applied price mismatch and gives a separate rule for Failed batches. [Round 1 diagnostics](calibration/round-1.json) · [Round 2 diagnostics](calibration/round-2.json)

## Checks

- **Source fidelity.** A blind judge compares the revised SOP with the original. It checks for missing, changed, and unsupported new instructions, including restart steps, exception priorities, and approval authority.
- **Artifact usability.** A separate blind judge tries the scenario with the revised SOP and the expected task requirements. It follows precise references to their target steps and checks what to do if a restart or overlap remains unresolved. It receives neither the source nor the recorded reader answer.
- **Reader performance.** A third blind judgment scores the recorded reader answer and its citations separately. The answer can be incomplete even if a quote contains the missing action. The citations can be incomplete even if the answer is correct.

The calibration covers 20 published SOP revisions from the [finish-check experiment](../finish-check/). It reuses the recorded reader answers so differences reflect the evaluator. It includes both original-suite rounds and the dashboard holdout.

The targeted run uses [three new SOPs](fixtures/) covering a specified restart with a specified exception priority, an unresolved overlap, and an unspecified restart after a single hold. Both conditions revise each SOP twice in fresh sessions. [Questions and source requirements](cases.json) · [Published skill](https://github.com/bagusfarisa/good-enough/blob/17a3c58/skills/good-enough/SKILL.md) · [Candidate skill](https://github.com/bagusfarisa/good-enough/blob/369a27c30fdd9182deaf41da621da3dcc018ff16/skills/good-enough/SKILL.md)

The full-suite rerun requires a gain in the number of revisions passing both fidelity and usability on at least two of the three fixtures, with no fixture regressing and no loss of source fidelity overall. The published wording remains the default during the experiment.

Generation uses Codex CLI, `gpt-6.2-sol` at low reasoning effort, and the same revision prompt in both conditions. The reader uses `gpt-6.1-terra`. Separate `gpt-6.2-astra` sessions judge the three checks. These are synthetic fixtures and AI readers.

## Reproduce

From the repository root with an authenticated Codex CLI, run the following.

```sh
for round in round-1 round-2; do
  archive="evals/finish-check/$round"
  python3 evals/revision/procedure.py --input "$archive" \
    --archived-readers "$archive/md-scores.json" \
    --cases evals/revision/cases.json --case price-import --case device-return \
    --out "/tmp/good-enough-procedure/calibration/$round.json"
done

archive=evals/finish-check/holdout
python3 evals/revision/procedure.py --input "$archive" \
  --archived-readers "$archive/md-scores.json" \
  --cases evals/finish-check/holdout.json \
  --out /tmp/good-enough-procedure/calibration/holdout.json

target=/tmp/good-enough-procedure/targeted
python3 evals/revision/run.py --out "$target" --format md \
  --baseline-revision 17a3c58 --revision 369a27c \
  --cases evals/procedure-restart/cases.json
python3 evals/revision/procedure.py --input "$target" --out "$target/scores.json" \
  --cases evals/procedure-restart/cases.json
```
