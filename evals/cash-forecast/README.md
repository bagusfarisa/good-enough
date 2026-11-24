# Cash forecast benchmark

This pilot tests a December 2026 cash forecast for an operations lead. The source data is synthetic. The published workbooks are the agent outputs, saved with their original $6,000 payroll assumption.

## Runs

- Harness and model used for all six runs were Codex CLI `0.172.0` and `gpt-6.2-sol` at low reasoning effort.
- Three pairs ran in fresh, isolated working directories with the same [task](prompt.txt), [input CSV](cash-inputs.csv), and [runtime instructions](runtime.txt). Each could read the same Artifact Tool API guide and use the same installed Node.js and Artifact Tool bundle.
- The two conditions used the same harness settings. Personal configuration, local rules, and memories were disabled. Automatic loading by name was disabled for `good-enough` and `artifact-ponytail` in both conditions. The treatment added the [explicit skill instruction](with-skill.txt) and a local copy of [Good Enough at `01eb485`](https://github.com/bagusfarisa/good-enough/blob/01eb48510be3bbbcffc88263268865b5448098eb/skills/good-enough/SKILL.md). All three treatment command logs showed a successful read of the skill file.
- The README shows pair 1. The [raw scores](scores.json) link to all six workbooks and include elapsed CLI time, token use, and tool exit counts as run metadata.

## Checks

The expected starting result is **$10,000 + $5,000 − $6,000 − $2,000 = $7,000**. Raising payroll to **$7,000** lowers ending cash to **$6,000**.

- A workbook passes correctness when it contains the four labeled numeric inputs, shows December 2026 and USD, saves a formula-driven $7,000 ending cash balance, recalculates to $6,000 after the payroll change, and has no stored formula errors. The scenario was tested on disposable copies with Artifact Tool and LibreOffice.
- A scripted task completes when the labeled payroll input can be changed and the ending cash formula produces the expected before and after values. Separate layout observations record whether payroll and ending cash are on the opening worksheet and how many rows there contain a value or formula. These are workbook observations. Reader timing and preference remain unmeasured.

Both conditions completed the scripted task and passed correctness in **3 of 3 runs**. The baseline had **2 nonzero tool command exits** and Good Enough had **1**. Those runs recovered and produced passing workbooks. Median filled rows were **11** for baseline and **9** with Good Enough. Each baseline output included at least one intermediate cash total. Each Good Enough output computed ending cash directly from the inputs.
