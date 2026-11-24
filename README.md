# Good Enough

**Ponytail for knowledge worker**

Good Enough is an agent skill for making documents, spreadsheets, financial models, and presentations that are complete, correct, and easy to use. Every section, tab, slide, and visual should help the reader do something.

| If you need a… | Good Enough helps the agent… |
| --- | --- |
| Decision brief | Lead with the decision and put the evidence where the reader needs it. |
| Tracker | Use a clear table and readable formulas. Add a dashboard when it serves a distinct task. |
| Financial model | Label the assumptions and show how they drive the results a human needs to understand. |
| Slide deck | Give each slide one main takeaway and keep the evidence that supports it. |

## Try it in Codex

Paste this into Codex to install the skill. [Codex skill documentation](https://learn.chatgpt.com/docs/build-skills#install-curated-skills-for-local-use)

```text
$skill-installer https://github.com/bagusfarisa/good-enough/tree/main/skills/good-enough
```

Use `$good-enough` in a task. For example:

```text
Use $good-enough to build a 12-month cash forecast. Make it easy for a reviewer to trace the ending cash balance back to the assumptions.
```

The full instructions are in [SKILL.md](skills/good-enough/SKILL.md).

## Inspiration

Inspired by Dietrich Gebert’s [Ponytail](https://github.com/DietrichGebert/ponytail), which applies the same preference for simple, complete work to coding.
