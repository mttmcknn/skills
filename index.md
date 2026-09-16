---
layout: page
title: Install
icon: fas fa-download
order: 0
permalink: /
---

Portable agent skills for PR review and focused utilities. Install the same seven skills in Codex, Claude Code, or another supported agent with [Vercel's skills CLI](https://github.com/vercel-labs/skills).

## Install

With Node.js 22.20+ and Git available, run this from your project:

```bash
npx skills add mttmcknn/skills
```

Choose skills and agents when prompted. To install all seven for both Codex and Claude Code:

```bash
npx skills add mttmcknn/skills --skill '*' --agent codex claude-code
```

Use `--agent codex` or `--agent claude-code` for one host. Add `--global` to make the skills available across projects, or `--yes` for a non-interactive install.

Preview the catalog or choose one skill:

```bash
npx skills add mttmcknn/skills --list
npx skills add mttmcknn/skills --skill address-review --agent codex claude-code
```

Start a new agent session after installation, then select a skill or invoke it with your host's syntax.

## Bundles

- **[review](./categories/review/)** — Review feedback, iterative review and fixes, and dependency-aware PR validation.
- **[utilities](./categories/utilities/)** — Code snippet images, focused clarification, and portable checkpoint/resume handoffs.

## Manage installed skills

```bash
npx skills list
npx skills update --project
npx skills remove address-review --agent codex claude-code
```

Run these from the project where you installed the skills. For global installs, use `--global` with list, update, or remove. PR workflows require an available GitHub connector or authenticated `gh` CLI.

## Existing installations

Both Codex and Claude Code plugin manifests remain available. When switching to the skills CLI, remove your old `review` and `utilities` plugin installations first so your agent loads only one copy of each skill. This also applies to installs under the former marketplace name.

Checkpoint/resume are now portable skills using `.agents/checkpoints/`. Pass an old handoff’s exact path to resume it; no files are moved automatically.

Android workflows now live entirely in [Google’s Android skills](https://github.com/android/skills). The local Android plugin is retired; uninstall it while keeping your upstream skills.

## Source

[Repository and authoring guide](https://github.com/mttmcknn/skills)
