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
| [address-review](plugins/review/skills/address-review/SKILL.md) | Address pull request review comments. |
| [review-cycle](plugins/review/skills/review-cycle/SKILL.md) | Review and fix a pull request. |
| [validate-merge-prs](plugins/review/skills/validate-merge-prs/SKILL.md) | Validate a PR queue and merge order. |
| [code-as-image](plugins/utilities/skills/code-as-image/SKILL.md) | Render code snippets as images. |
| [interrogation](plugins/utilities/skills/interrogation/SKILL.md) | Clarify an idea through a focused interview. |
| [checkpoint](plugins/utilities/skills/checkpoint/SKILL.md) | Save a task handoff. |
| [resume](plugins/utilities/skills/resume/SKILL.md) | Continue from a saved handoff. |

[Website](https://mttmcknn.github.io/skills/) · [CLI options](https://github.com/vercel-labs/skills)
