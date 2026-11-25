# Skill triggering evaluation

Measures whether an agent discovers and loads [`skills/good-enough/SKILL.md`](../../skills/good-enough/SKILL.md) when a user's request matches the skill's description, and skips it on unrelated or micro-edit requests.

## Cases

[`cases.json`](cases.json) contains 24 prompts:

- **12 positive cases** (`should_trigger: true`): creating or materially revising decision briefs, impact analyses, SOPs, financial models, trackers, and slide decks.
- **12 negative distractors** (`should_trigger: false`): typo fixes, one-sentence summaries, coding/SQL/regex/git tasks, translations, casual Slack replies, and factual Q&A.

## Method

For each prompt, [`run.py`](run.py) creates an isolated temporary workspace with `.agents/skills/good-enough/SKILL.md` installed from the chosen revision (or `WORKTREE` to test uncommitted edits to the YAML `description`). It runs `codex exec --json` with `good-enough` enabled and inspects the JSONL event stream to check whether `good-enough/SKILL.md` was loaded.

Metrics reported in `scores.json`:

- **Precision, Recall, F1, Accuracy**
- **Confusion matrix** (`tp`, `fp`, `tn`, `fn`) plus explicit `false_positives` and `false_negatives` lists
- **`pass_all_k_rate`** (`pass^k`) when `--repeats > 1`

## Run

Validate the case file without calling Codex:

```sh
python3 evals/triggering/run.py --dry-run
```

Run the suite against `HEAD` (or `--revision WORKTREE` while iterating on the skill description):

```sh
python3 evals/triggering/run.py --revision HEAD --repeats 3 --out /tmp/good-enough-triggering
```
