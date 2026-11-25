# Good Enough

**Ponytail for knowledge worker**

[Use it](#use-it) · [Install](#install) · [Update](#update) · [Inspiration](#inspiration)

Good Enough is an agent skill for making documents, spreadsheets, financial models, and presentations that are complete, correct, and easy to use. When you revise an existing artifact, give the agent one task the reader must complete. The skill helps the agent clear that path and check that essential content survives.

| If you need a… | Good Enough helps the agent… |
| --- | --- |
| Decision brief | State the decision, the recommendation when supported, and the trade-offs that affect the choice. |
| Impact analysis | Show what changes in each affected case, who is affected, and what still needs a decision. |
| Standard operating procedure (SOP) | Write steps a new operator can follow, with common exceptions and a clear check for completion. |
| Tracker | Use a clear table and readable formulas. Add a dashboard when it serves a distinct task. |
| Financial model | Label the assumptions and show how they drive the results a human needs to understand. |
| Slide deck | Give each slide one main takeaway and keep the evidence that supports it. |

## Use it

Ask your agent to use the `good-enough` skill, or invoke it directly:

- **Claude Code / Antigravity:** `/good-enough`
- **Codex:** `$good-enough`
- **Pi:** `/skill:good-enough`

```text
Use the good-enough skill to revise this Q3 budget proposal. Our department
head needs to decide whether to approve the request in a quick review.
```

The skill guides how the agent structures and reviews the work. The file formats it can produce depend on its available tools.

## Install

Choose the option that fits your setup: [ask your agent](#ask-your-agent-to-install), use a [CLI installer](#installer-commands), or [install manually](#install-manually).

### Ask your agent to install

Paste this prompt into your agent's chat:

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

- **[Skills CLI](https://github.com/vercel-labs/skills)** (Node.js 22.20+) — run from your project, or add `-g` for your user account:
  ```sh
  npx skills add bagusfarisa/good-enough --skill good-enough
  ```
- **[Codex](https://learn.chatgpt.com/docs/build-skills#install-curated-skills-for-local-use)** — paste into a chat:
  ```text
  $skill-installer https://github.com/bagusfarisa/good-enough/tree/main/skills/good-enough
  ```
- **[Pi](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/packages.md)** — install from Git (add `--local` for the current project):
  ```sh
  pi install git:github.com/bagusfarisa/good-enough
  ```

### Install manually

Copy the [`good-enough` folder](skills/good-enough) into your agent's project or personal skills directory (for example, `.claude/skills/good-enough/SKILL.md` for a Claude Code project install).

<details>
<summary>Show directory paths by agent</summary>

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

</details>

## Update

Changes to [`skills/good-enough/SKILL.md`](skills/good-enough/SKILL.md) are published on `main`. Update using the method you installed with:

- **Skills CLI:** Run `npx skills update good-enough --project` (or `--global` for a personal install). If you install for multiple agents, choose the symlink option so they share one local copy. ([Reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#skills-update))
- **Pi Git package:** Run `pi update git:github.com/bagusfarisa/good-enough` (from the project directory for a project install), then `/reload` in your Pi session. ([Reference](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/cli.md#update-pi-or-packages))
- **Manual or Codex `$skill-installer`:** Download the latest `SKILL.md` from `main`, replace the file in your `good-enough` folder, and start a new session if the previous version still appears.

## Inspiration

Inspired by Dietrich Gebert’s [Ponytail](https://github.com/DietrichGebert/ponytail), which applies the same preference for simple, complete work to coding.
