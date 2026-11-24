# Good Enough

**Ponytail for knowledge worker**

Good Enough is an agent skill for making documents, spreadsheets, financial models, and presentations that are complete, correct, and easy to use. When you revise an existing artifact, give the agent one task the reader must complete. The skill helps the agent clear that path and check that essential content survives.

[See the cash forecast benchmark](#cash-forecast-benchmark) for an example with downloadable workbooks.

| If you need a… | Good Enough helps the agent… |
| --- | --- |
| Decision brief | State the decision, the recommendation when supported, and the trade-offs that affect the choice. |
| Impact analysis | Show what changes in each affected case, who is affected, and what still needs a decision. |
| Standard operating procedure (SOP) | Write steps a new operator can follow, with common exceptions and a clear check for completion. |
| Tracker | Use a clear table and readable formulas. Add a dashboard when it serves a distinct task. |
| Financial model | Label the assumptions and show how they drive the results a human needs to understand. |
| Slide deck | Give each slide one main takeaway and keep the evidence that supports it. |

## Install

### Ask your agent to install

Copy this prompt into your agent's chat.

```text
Install the good-enough skill from https://github.com/bagusfarisa/good-enough.
The skill folder is skills/good-enough on main.

Identify the agent harness you're running in. Use its documented skill installer
or skills directory and perform the installation yourself. Use the current project
if there is one, or install it for my user account otherwise. If Good Enough is
already installed from this repository, update that installation.

Verify the installation and tell me how to invoke the skill. If I need to reload
or start a new session, tell me.
```

### Installer commands

From your project, run the [Skills CLI](https://github.com/vercel-labs/skills) (Node.js 22.20+) and select your agents when prompted. Add `-g` to install for your user account.

```sh
npx skills add bagusfarisa/good-enough --skill good-enough
```

In [Codex](https://learn.chatgpt.com/docs/build-skills#install-curated-skills-for-local-use), you can also paste this into a chat:

```text
$skill-installer https://github.com/bagusfarisa/good-enough/tree/main/skills/good-enough
```

In [Pi](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/packages.md), you can install directly from Git. Add `--local` for the current project.

```sh
pi install git:github.com/bagusfarisa/good-enough
```

### Install manually

Copy the [`good-enough` folder](skills/good-enough) into one of the locations below. For example, a project install in Claude Code should end up at `.claude/skills/good-enough/SKILL.md`.

| Agent | Project directory | Personal directory |
| --- | --- | --- |
| [Claude Code](https://code.claude.com/docs/en/skills#choose-where-skills-load) | `.claude/skills/` | `~/.claude/skills/` |
| [Antigravity](https://antigravity.google/docs/skills) | `.agents/skills/` | `~/.gemini/config/skills/` |
| [Pi](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/skills.md#add-it-to-pi) | `.agents/skills/` | `~/.agents/skills/` |
| [OpenCode](https://opencode.ai/docs/skills/#discovery) | `.opencode/skills/` | `~/.config/opencode/skills/` |
| [Codex](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills) | `.agents/skills/` | `~/.agents/skills/` |
| [Cursor](https://cursor.com/docs/skills#skill-directories) | `.cursor/skills/` | `~/.cursor/skills/` |
| [GitHub Copilot](https://docs.github.com/en/copilot/concepts/customizations/agent-skills#finding-and-storing-skills) | `.github/skills/` | `~/.copilot/skills/` |
| [Gemini CLI](https://geminicli.com/docs/cli/skills/) | `.gemini/skills/` | `~/.gemini/skills/` |

For any other agent that supports the [Agent Skills format](https://agentskills.io/specification), use its documented skills directory and the same [`SKILL.md`](skills/good-enough/SKILL.md).

## Update

Changes to [`skills/good-enough/SKILL.md`](skills/good-enough/SKILL.md) are published on `main`. Refresh your local installation after a change lands.

- **Skills CLI.** Run `npx skills update good-enough --project` from the project, or `npx skills update good-enough --global` for a personal install. If you install for multiple agents, choose the symlink option so they share one local copy. [Skills CLI reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#skills-update)
- **Pi Git package.** Run `pi update git:github.com/bagusfarisa/good-enough`, then `/reload` in your Pi session. For a project install, run the update from that project. [Pi package commands](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/cli.md#update-pi-or-packages)
- **Manual or Codex `$skill-installer` install.** Download the latest `SKILL.md` from `main` and replace the file in your existing `good-enough` folder. Open a new agent session if it still shows the previous version.

## Use it

Ask your agent to use the `good-enough` skill. Codex also accepts `$good-enough`, Claude Code and Antigravity offer `/good-enough`, and Pi offers `/skill:good-enough`.

```text
Use the good-enough skill to revise this launch brief. The Support lead needs
to tell a customer what happens to a request that was already open at launch.
Keep the pending decisions and exceptions accurate.
```

The skill guides how the agent structures and reviews the work. The file formats it can produce depend on its available tools.

## Existing artifact revision benchmark

In 36 revisions of six synthetic artifacts, Good Enough passed both the full reader task and preservation checks in 12 of 12 runs. The plain prompt passed 11 of 12, and the one-line concision prompt passed 8 of 12. The concision prompt supported more answers from the opening view. [Sources, outputs, scores, and reproduction steps](evals/revision/)

A follow-up compared two skill versions and scored the first action separately from the complete answer. [Opening-view check](evals/first-action/)

Two fresh rounds tested whether an explicit exception and restart check helps readers complete the task while preserving the source. The test also included a new SOP with overlapping exceptions. [Procedure recovery and preservation check](evals/finish-check/)

A follow-up separated SOP source fidelity, usability, reader answers, and citations. It used the published revisions to check the evaluator, then compared two skill versions on three new procedures. [SOP restart and source fidelity](evals/procedure-restart/)

## Cash forecast benchmark

Try the same task in both workbooks. Change **Payroll** from **$6,000** to **$7,000** and verify that **Ending cash** changes from **$7,000** to **$6,000**.

| Baseline | With Good Enough |
| --- | --- |
| ![Baseline workbook with ending cash below the inputs and intermediate totals](evals/inverted-pyramid/cash-forecast/01-baseline.png) | ![Good Enough workbook with ending cash in row 2 above the editable assumptions](evals/inverted-pyramid/cash-forecast/01-good-enough.png) |
| [Open the baseline workbook](evals/inverted-pyramid/cash-forecast/workbooks/01-baseline.xlsx) | [Open the Good Enough workbook](evals/inverted-pyramid/cash-forecast/workbooks/01-good-enough.xlsx) |

| Result across three pairs | Baseline | With Good Enough |
| --- | ---: | ---: |
| Scripted payroll task completed | 3/3 | 3/3 |
| Workbooks passing all correctness checks | 3/3 | 3/3 |
| Workbook failures | 0 | 0 |
| Median row of ending cash | 12 | 2 |
| Median filled rows on the opening sheet | 11 | 9 |

Good Enough put ending cash in row 2 in every run. The baseline workbooks included intermediate cash totals. Good Enough calculated ending cash directly from the four editable inputs. This pilot measured workbook behavior and layout. Reader completion time remains unmeasured.

Tested with Codex CLI **0.172.0**, model **`gpt-6.2-sol`** at low reasoning effort, and skill commit [`1b391a7`](https://github.com/bagusfarisa/good-enough/blob/1b391a77d96cbe3fb06af028fde121e49e6edaec/skills/good-enough/SKILL.md). [Method](evals/inverted-pyramid/) · [All six workbooks](evals/inverted-pyramid/cash-forecast/workbooks/) · [Raw scores](evals/inverted-pyramid/cash-forecast/scores.json) · [Original pilot and inputs](evals/cash-forecast/)

In the three-month follow-up, both skill revisions passed every calculation and reader check. The revised skill showed a labeled March payments subtotal in all three workbooks, compared with one of three for the previous revision. [Financial traceability test](evals/financial-traceability/)

## Automated document evaluation

In the inverted-pyramid rerun, both conditions passed all nine documents and supported all 27 reader answers. A blinded judge preferred Good Enough in six pairs and the baseline in three. The impact analyses surfaced the customer’s next step earlier. Overall evidence placement was tied. [Full rerun results and instructions](evals/inverted-pyramid/) · [Original evaluation](evals/automated/)

A follow-up compared two skill revisions on a decision brief with separate owners and deadlines. Both revisions put the required details in the first 100 words in all three runs. [Two-dependency brief results](evals/action-grouping/)

The full rerun covered six fixtures and 36 generated artifacts. It found earlier placement for some key details and equal full-artifact correctness. [Full rerun and proposed direction](evals/full-rerun/)

## Inspiration

Inspired by Dietrich Gebert’s [Ponytail](https://github.com/DietrichGebert/ponytail), which applies the same preference for simple, complete work to coding.
