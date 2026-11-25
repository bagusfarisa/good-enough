# Targeted-edit guardrail evaluation

Tests Rule 1 of [`skills/good-enough/SKILL.md`](../../skills/good-enough/SKILL.md):

> *For a targeted edit, reuse the existing structure and change only what was requested and what depends on it.*

This suite catches over-simplification regressions where the skill causes an agent to reorganize, trim, or rewrite untouched sections during a narrow edit.

## Cases

[`cases.json`](cases.json) reuses four Markdown fixtures from [`evals/revision/fixtures/`](../revision/fixtures/):

| Case | Fixture | Narrow edit requested |
| --- | --- | --- |
| `returns-expiry-window` | `returns-launch.md` | Change expiry window from 7 to 10 calendar days (+ dependent historic-queue reference) |
| `price-import-threshold` | `price-import.md` | Change Merchandising approval threshold from 10% to 15% (+ boundary rule) |
| `dispatch-atlas-cost` | `dispatch-brief.md` | Update Atlas pilot quote from `$4,800` to `$5,500` in both locations |
| `device-return-extension` | `device-return.md` | Change Facilities emergency extension from `221` to `418` |

## Grading (100% deterministic)

No LLM judge is required. Each edited artifact must pass four deterministic checks:

1. **`required_updates`**: Requested values and dependent references are present (with minimum occurrence counts where applicable).
2. **`no_stale_values`**: Replaced values do not remain anywhere in the document.
3. **`headings_preserved`**: Every original Markdown heading is preserved verbatim.
4. **`scope_discipline`**: Word-level diff ratio (`1 - SequenceMatcher.ratio()`) stays within `max_changed_ratio` (0.20–0.25).

## Run

Validate fixtures and scoring logic without calling Codex:

```sh
python3 evals/targeted-edit/run.py --dry-run
```

Run a paired baseline vs. `good-enough` evaluation:

```sh
python3 evals/targeted-edit/run.py --revision HEAD --repeats 3 --out /tmp/good-enough-targeted-edit
```
