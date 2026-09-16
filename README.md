# Agent Skills

Portable agent skills for PR review and focused utilities. Install them in Codex, Claude Code, or another supported agent with [Vercel's skills CLI](https://github.com/vercel-labs/skills). Each workflow lives in a standard `SKILL.md`; host-specific metadata stays outside the instructions.

Browse the [skills website](https://mttmcknn.github.io/skills/).

## Install

With Node.js 22.20+ and Git available, run this from the project where you want to use the skills:

```bash
npx skills add mttmcknn/skills
```

Choose your skills and agents when prompted. To explicitly install all seven for both Codex and Claude Code:

```bash
npx skills add mttmcknn/skills --skill '*' --agent codex claude-code
```

Use `--agent codex` or `--agent claude-code` to target one host. Add `--global` for installation across projects, or `--yes` for a non-interactive install. Other agents are selectable through the same CLI.

Preview the catalog or install just one skill:

```bash
npx skills add mttmcknn/skills --list
npx skills add mttmcknn/skills --skill address-review --agent codex claude-code
```

Start a new agent session after installation, then select a skill or invoke it using your host's syntax. For example, Codex accepts `$address-review` and Claude Code accepts `/address-review` for an individually installed skill.

The CLI installs the complete skill folders and their references. PR workflows use an available GitHub connector or authenticated `gh` CLI; installing skills does not configure credentials or grant repository access.

## Manage installed skills

Run these from the project where you installed the skills:

```bash
npx skills list
npx skills update --project
npx skills remove address-review --agent codex claude-code
```

For global installs, use `npx skills list --global`, `npx skills update --global`, or add `--global` to the remove command. Project installs create a `skills-lock.json` file to track their sources.

## Bundles

| Bundle | Skills |
| --- | --- |
| `review` | `address-review`, `review-cycle`, `validate-merge-prs` |
| `utilities` | `code-as-image`, `interrogation`, `checkpoint`, `resume` |

Checkpoint/resume use project-local `.agents/checkpoints/` by default and accept an explicitly supplied path. They work across agent hosts and do not depend on a clear-chat command or the original conversation.

## Existing plugin installations

Both Codex and Claude Code plugin manifests remain available for existing installations. The skills CLI is the recommended installation path for this collection and installs skills directly into your chosen agents' discovery directories.

When switching from a plugin install, remove that host's `review` and `utilities` plugin installations before installing the same skills through this CLI. This avoids loading duplicate copies. The generated Claude manifests keep both bundles' names, versions, and descriptions in sync with the Codex manifests.

## Repository layout

```text
.agents/plugins/marketplace.json     # Bundle catalog / Codex compatibility
plugins/<bundle>/
  .codex-plugin/plugin.json          # Codex plugin metadata
  skills/<name>/
    SKILL.md                        # Portable workflow
    agents/openai.yaml              # Codex display metadata
    references/                     # Optional task-specific detail
  .claude-plugin/plugin.json         # Claude Code metadata (generated)
.claude-plugin/marketplace.json       # Claude Code catalog (generated)
```

The [website source](https://github.com/mttmcknn/skills/tree/gh-pages-src) is maintained on `gh-pages-src`. GitHub Actions combines it with the native catalog and skills from `main`, then publishes to `gh-pages`. Public skill-page URLs stay stable when repository folders move.

## Migration

Remove old plugin installations under the former marketplace name before switching to the skills CLI. Local symlinks to the former top-level `review/skills/` or `utilities/skills/` paths need updating to `plugins/<bundle>/skills/`.

The former checkpoint/resume commands are now portable skills. Existing handoffs can be resumed by passing their exact path; no files are moved automatically.

The Android plugin and its 15 skills have been removed. Use Google's [Android skills](https://github.com/android/skills) through the upstream CLI/plugin. Uninstall this marketplace's old Android plugin and remove its local symlinks while keeping separately installed upstream skills.

## Authoring and validation

1. Add or edit `plugins/<bundle>/skills/<name>/SKILL.md`. Keep the trigger narrow, instructions host-neutral, and optional detail in linked references.
2. Add matching `agents/openai.yaml` display metadata. Do not hardcode a model, tool provider, or mandatory delegation into a portable workflow.
3. Update the bundle's native manifest/version, then run `python3 scripts/sync_claude_compat.py`. Edit generated compatibility metadata only through that script.
4. Validate before publishing:

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate_skills.py
python3 scripts/sync_claude_compat.py --check
python3 -m unittest discover -s tests -v
python3 scripts/check_skills_install.py
```

The installation check uses a pinned skills CLI version to install the current checkout into a temporary project, verifies both agents' files/resources, and removes the fixture afterward. It requires Node.js and npm, and leaves your actual agent installations alone.

See [the audit](maintenance/skill-audit.md) for scope decisions. The workflows follow the [Agent Skills format](https://agentskills.io/specification) and [OpenAI's skill guidance](https://learn.chatgpt.com/docs/build-skills).
