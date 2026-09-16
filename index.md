---
layout: page
title: Install
icon: fas fa-download
order: 0
permalink: /
---

Portable agent skills for PR review and focused utilities, with Codex as the primary integration. The same `SKILL.md` workflows work in other compatible agents.

## Install in Codex

```bash
codex plugin marketplace add mttmcknn/skills
codex plugin add review@mttmcknn
codex plugin add utilities@mttmcknn
```

Start a new task after installation, then select a skill or mention it by name:

```text
Use $address-review to address the comments on PR 42.
Use $checkpoint to save a handoff for this task.
Use $resume to continue from the latest checkpoint in this project.
```

## Bundles

- **[review](./categories/review/)** — Review feedback, iterative review and fixes, and dependency-aware PR validation.
- **[utilities](./categories/utilities/)** — Code snippet images, focused clarification, and portable checkpoint/resume handoffs.

## Other agents

Install individual skill folders from `plugins/<bundle>/skills/` into your agent’s supported discovery directory. Keep each folder’s references with it. The workflows do not require a particular model or host-specific tools.

Claude Code compatibility uses the same instructions:

```text
/plugin marketplace add https://github.com/mttmcknn/skills
/plugin install review@mttmcknn
/plugin install utilities@mttmcknn
```

Avoid loading both a plugin and a local copy of the same skill. Update settings belong to your client. PR workflows require an available GitHub connector or authenticated `gh` CLI.

## Existing installations

The marketplace name is `mttmcknn`. Remove entries under the former name before reinstalling. Local symlinks should point to `plugins/<bundle>/skills/`.

Checkpoint/resume are now portable skills using `.agents/checkpoints/`. Pass an old handoff’s exact path to resume it; no files are moved automatically.

Android workflows now live entirely in [Google’s Android skills](https://github.com/android/skills). The local Android plugin is retired; uninstall it while keeping your upstream skills.

## Source

[Repository and authoring guide](https://github.com/mttmcknn/skills)
