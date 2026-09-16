---
layout: page
title: Install
icon: fas fa-download
order: 0
permalink: /
---

Agent skills for pull request reviews, code images, and task handoffs. Works with Codex, Claude Code, and other compatible agents.

```bash
npx skills add mttmcknn/skills
```

Choose your skills and agents. Add `--global` to install across projects.

## Skills

| Skill | Description |
| --- | --- |
| [address-review]({{ '/review/skills/address-review/' | relative_url }}) | Address pull request review comments. |
| [review-cycle]({{ '/review/skills/review-cycle/' | relative_url }}) | Review and fix a pull request. |
| [validate-merge-prs]({{ '/review/skills/validate-merge-prs/' | relative_url }}) | Validate a PR queue and merge order. |
| [code-as-image]({{ '/utilities/skills/code-as-image/' | relative_url }}) | Render code snippets as images. |
| [interrogation]({{ '/utilities/skills/interrogation/' | relative_url }}) | Clarify an idea through a focused interview. |
| [checkpoint]({{ '/utilities/skills/checkpoint/' | relative_url }}) | Save a task handoff. |
| [resume]({{ '/utilities/skills/resume/' | relative_url }}) | Continue from a saved handoff. |

[GitHub](https://github.com/mttmcknn/skills) · [CLI options](https://github.com/vercel-labs/skills)
