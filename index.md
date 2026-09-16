---
layout: page
title: Install
icon: fas fa-download
order: 0
permalink: /
---

The `mttmcknn` Claude Code plugin marketplace — Matt McKenna's personal skill bundles for pull request review workflows and focused utilities.

## Plugins

- **[review](./categories/review/)** — Pull request review workflows: addressing human and bot feedback, iterative review cycles, and batch PR validation.
- **[utilities](./categories/utilities/)** — Code snippet images, focused clarification, and checkpoint/resume commands.

## Install

In Claude Code:

```bash
/plugin marketplace add https://github.com/mttmcknn/skills
/plugin install review@mttmcknn
/plugin install utilities@mttmcknn
```

Update settings are controlled by your client. If migrating from the former marketplace name, remove the old plugin/marketplace entries before installing these names to avoid duplicate skills.

Android workflows now live entirely in [Google’s Android skills](https://github.com/android/skills). The local Android plugin has been retired; uninstall the old plugin and keep your upstream CLI skills.

## Source

Repo: <https://github.com/mttmcknn/skills>
