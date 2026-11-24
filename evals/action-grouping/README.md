# Two-dependency decision brief

This test checks whether the reader can make a Friday approval decision from the opening of a brief. The synthetic Harbor Hub pilot has two pending requirements. Each has a different owner and deadline. The brief must also tell the reader what to do if either requirement is still pending or fails at the meeting. [Prompt, source notes, and rubric](cases.json)

## Results

| Measure | Previous skill | Revised skill |
| --- | ---: | ---: |
| Complete briefs passing all checks | 3/3 | 3/3 |
| Openings passing all checks | 3/3 | 3/3 |
| Judge preferences for complete briefs | 0 | 0 |
| Judge preferences for openings | 1 | 1 |
| Median full-brief words | 119 | 121 |

The full-brief judge called three ties. The opening judge called one tie. Both revisions led with the approval rule and fallback, then placed each pending check beside its owner and deadline in the same table. The revised rule made the intended structure explicit. This fixture showed equal performance on the measured tasks. [All six briefs](results/artifacts/) · [Full-brief scores](results/scores.json) · [Opening scores](results/opening-scores.json)

## Method

Three paired runs compared the [previous skill at `1b391a7`](https://github.com/bagusfarisa/good-enough/blob/1b391a77d96cbe3fb06af028fde121e49e6edaec/skills/good-enough/SKILL.md) with the [revised skill at `4fd6856`](https://github.com/bagusfarisa/good-enough/blob/4fd6856add1bc090a01cd4d290ac9663f6420ac4/skills/good-enough/SKILL.md). The skill sentence changed. The task, source notes, and generation settings were the same. All six runs used fresh Codex CLI `0.172.0` sessions with `gpt-6.2-sol` at low reasoning effort.

A blinded `gpt-6.2-astra` judge applied the same rubric to the complete briefs and, in a separate session, to the first 100 words of each brief. The cutoff keeps formatted amounts together. For the opening measure, a brief passes when the approval decision, both owner-and-deadline pairs, and the fallback are all present and the text is consistent with the source. The runner verified that every cited excerpt occurs in the text the judge saw. The opening cutoff is a measure of placement for one synthetic task. Human reading time and preference remain unmeasured.

## Rerun

Use an authenticated Codex CLI from a clone of the repository.

```sh
python3 evals/automated/run.py \
  --baseline-revision 1b391a7 \
  --revision 4fd6856 \
  --cases evals/action-grouping/cases.json \
  --opening-words 100 \
  --out /tmp/good-enough-action-grouping
```
