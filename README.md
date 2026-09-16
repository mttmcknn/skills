# AI Skills

The `mttmcknn` plugin marketplace — Matt McKenna's personal agent skills for PR review and focused utilities.

Browse the [skills website](https://mttmcknn.github.io/skills/). Its Jekyll source lives on [`gh-pages-src`](https://github.com/mttmcknn/skills/tree/gh-pages-src); GitHub Actions combines that source with the skills on `main` and publishes to `gh-pages`.

## Plugins

| Plugin | Skills |
| --- | --- |
| `review@mttmcknn` | `address-review`, `review-cycle`, `validate-merge-prs` |
| `utilities@mttmcknn` | `code-as-image`, `interrogation` |

Utilities also includes `/checkpoint` and `/resume` commands for Claude Code.

## Install

In Claude Code:

```text
/plugin marketplace add https://github.com/mttmcknn/skills
/plugin install review@mttmcknn
/plugin install utilities@mttmcknn
```

For an existing installation under the former marketplace name, uninstall those old plugin entries and remove the old marketplace using `/plugin`, then add/install the names above. Avoid keeping both copies active. Automatic updates depend on the client's marketplace settings; check `/plugin` for update controls.

For local skill development, link only the skills you need into the host's discovery directory. Codex discovers repository skills in `.agents/skills/`; Claude Code uses `.claude/skills/`. Avoid loading the same skill both through a plugin and a local symlink. Commands under `utilities/commands/` are Claude Code commands, not standalone Codex skills.

## Android skills

Android workflows now belong entirely to Google's [Android skills](https://github.com/android/skills), maintained through the upstream Android CLI/plugin. The local Android plugin and its 15 skills have been removed to avoid competing guidance for project creation, UI interaction, testing, debugging, and profiling.

For existing installs, uninstall this marketplace's Android plugin and remove local symlinks pointing to its former skill folders. Keep separately installed upstream Android skills. The review and utilities plugins remain available here.

## Maintenance

- Skills live at `<plugin>/skills/<name>/SKILL.md`; plugin manifests live at `<plugin>/.claude-plugin/plugin.json`.
- Keep each description specific enough to distinguish it from upstream skills and its neighbors. Keep the entrypoint short, and link conditional details from `references/`; templates belong in `assets/`.
- Validate frontmatter, names, resource links, and marketplace paths with `python3 scripts/validate_skills.py` (requires PyYAML from `requirements-dev.txt`). Check representative routing cases in [the audit](maintenance/skill-audit.md) when changing scope.
- Bump the affected plugin version and publish the reviewed changes. For new plugins, also add a relative-source entry to `.claude-plugin/marketplace.json`.

The writing guidance follows [OpenAI's skill documentation](https://learn.chatgpt.com/docs/build-skills): precise discovery, progressive disclosure, and workflows scoped to the requested task.
