# Automated evaluation

The suite evaluates Good Enough on three synthetic document tasks. Each case has a frozen prompt, source notes, and five pass/fail checks. It runs each task three times with and without the skill in fresh sessions, then compares the outputs against the same rubric. [Anthropic's evaluation and iteration guidance](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices#evaluation-and-iteration)

## Results

Each condition passed **9/9 documents** and **45/45 checks**. The model judge preferred Good Enough in five pairs, the baseline in two, and called two ties.

| Case | Baseline preferred | Good Enough preferred | Ties | Baseline median words | Good Enough median words |
| --- | ---: | ---: | ---: | ---: | ---: |
| Decision brief | 1 | 2 | 0 | 156 | 166 |
| Impact analysis | 1 | 2 | 0 | 269 | 240 |
| SOP | 0 | 1 | 2 | 155 | 151 |
| Overall | 2 | 5 | 2 | 160 | 166 |

The judge preferred Good Enough when decision briefs put the approval condition and owner beside the request, or when impact analyses put operational actions beside the cases that trigger them. The baseline won one decision brief by making the action explicit for each Legal outcome. It won one impact analysis by making the open decisions and their owners easier to locate. The median word count varied by case. [Raw scores and judge evidence](results/scores.json) · [All 18 documents](results/artifacts/)

## Method

- **Cases.** The [case file](cases.json) covers a decision brief, an impact analysis, and an SOP. Both conditions receive the same task, source notes, model, and tool restrictions. The Good Enough condition also receives the exact `SKILL.md` text from [commit `01eb485`](https://github.com/bagusfarisa/good-enough/blob/01eb48510be3bbbcffc88263268865b5448098eb/skills/good-enough/SKILL.md). The generator cannot see the checks.
- **Grading.** Each run passes when it passes all five checks. A separate judge grades outputs labeled A and B, with the conditions alternating positions. It records a preference or tie and quotes evidence for passing content checks. The runner verifies each quote against the artifact and counts words separately.
- **Scope.** Codex CLI 0.172.0 ran `gpt-6.2-sol` for generation and `gpt-6.2-astra` for judging, both at low reasoning effort. The suite measures output behavior when the skill is explicitly supplied. Skill discovery and human task performance remain unmeasured. The [cash forecast pilot](../cash-forecast/) used the same skill revision and measured workbook correctness independently with calculation engines.

## Rerun

From a clone of this repository, use an authenticated Codex CLI and Python 3.

```sh
python3 evals/automated/run.py --revision 01eb485 --out /tmp/good-enough-evaluation
```

The [runner](run.py) writes the generated Markdown, model usage, and grading results to the output directory. Use a fresh output directory for a different skill revision.
