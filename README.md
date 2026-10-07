# Skills

Agent skills for pull request reviews, code images, and task handoffs. Works with Codex, Claude Code, and other compatible agents.

## Install

```bash
npx skills add mttmcknn/skills
```

Choose your skills and agents. Add `--global` to install across projects.

## Skills

| Skill | Description |
| --- | --- |
| [adopt-pr](plugins/review/skills/adopt-pr/SKILL.md) | Take over a PR, validate it, and prepare it for review. |
| [adopt-stack](plugins/review/skills/adopt-stack/SKILL.md) | Take over every PR in a stack. |
| [address-review](plugins/review/skills/address-review/SKILL.md) | Address pull request review comments. |
| [review-cycle](plugins/review/skills/review-cycle/SKILL.md) | Review and fix a pull request. |
| [validate-merge-prs](plugins/review/skills/validate-merge-prs/SKILL.md) | Validate a PR queue and merge order. |
| [code-as-image](plugins/utilities/skills/code-as-image/SKILL.md) | Render code snippets as images. |
| [interrogation](plugins/utilities/skills/interrogation/SKILL.md) | Clarify an idea through a focused interview. |
| [checkpoint](plugins/utilities/skills/checkpoint/SKILL.md) | Save a task handoff. |
| [resume](plugins/utilities/skills/resume/SKILL.md) | Continue from a saved handoff. |
| [reflect](plugins/utilities/skills/reflect/SKILL.md) | Review development outcomes and improve owned skills. |

[Website](https://mttmcknn.github.io/skills/) · [CLI options](https://github.com/vercel-labs/skills)

## Versions

Versions use the update day's date in `YYYY-MM-DD` format (America/New_York),
for example `"2026-10-07"`. Each skill declares this quoted string in `SKILL.md`
under `metadata.version` and shares its bundle's version.

When updating a bundle, set its manifest and all its skill versions to that day's
date, then run `python3 scripts/sync_claude_compat.py`. Multiple updates on the same
day keep the same date; Git commits distinguish them. Validation rejects invalid
dates and mismatches across skill metadata and Codex/Claude packaging.
