# Agent Skills

Portable agent skills for PR review and focused utilities, packaged for both Codex and Claude Code. Both hosts get the same seven skills. Each workflow lives in a standard `SKILL.md`; host-specific metadata stays outside the instructions.

Browse the [skills website](https://mttmcknn.github.io/skills/).

## Install in Codex

Add the repository as a marketplace, then choose either or both bundles:

```bash
codex plugin marketplace add mttmcknn/skills
codex plugin add review@mttmcknn
codex plugin add utilities@mttmcknn
```

Start a new task after installation to pick up the skills. In Codex, select a skill or mention it by name, for example:

```text
Use $address-review to address the comments on PR 42.
Use $checkpoint to save a handoff for this task.
Use $resume to continue from the latest checkpoint in this project.
```

The plugins contain instructions and resources. PR workflows use an available GitHub connector or the authenticated `gh` CLI; installing the skills does not configure credentials or grant repository access.

## Install in Claude Code

Add the same repository as a Claude Code marketplace, then choose either or both bundles:

```text
/plugin marketplace add https://github.com/mttmcknn/skills
/plugin install review@mttmcknn
/plugin install utilities@mttmcknn
```

Use Claude Code's skill picker to invoke any of the seven skills, including checkpoint/resume. Both bundles have their own `.claude-plugin/plugin.json` alongside the Codex manifest. Claude discovers the shared `skills/` folders directly; it does not require Codex to be installed. See [Claude Code's plugin structure](https://code.claude.com/docs/en/plugins-reference#skills).

The Claude manifests are generated to keep bundle names, versions, and descriptions in sync. They are committed and shipped with every release. Automatic updates depend on the client's marketplace settings.

## Bundles

| Bundle | Skills |
| --- | --- |
| `review` | `address-review`, `review-cycle`, `validate-merge-prs` |
| `utilities` | `code-as-image`, `interrogation`, `checkpoint`, `resume` |

Checkpoint/resume use project-local `.agents/checkpoints/` by default and accept an explicitly supplied path. They work across agent hosts and do not depend on a clear-chat command or the original conversation.

## Other agents

For any host that supports the [Agent Skills format](https://agentskills.io/specification), install or link individual folders from `plugins/<bundle>/skills/` into its skill discovery directory. Copy the whole skill folder so relative references remain available. For Codex local development, `.agents/skills/` is the repository discovery directory. Avoid loading both a plugin and a linked copy of the same skill.

## Repository layout

```text
.agents/plugins/marketplace.json     # Primary Codex catalog
plugins/<bundle>/
  .codex-plugin/plugin.json          # Native plugin metadata
  skills/<name>/
    SKILL.md                        # Portable workflow
    agents/openai.yaml              # Codex display metadata
    references/                     # Optional task-specific detail
  .claude-plugin/plugin.json         # Claude Code metadata (generated)
.claude-plugin/marketplace.json       # Claude Code catalog (generated)
```

The [website source](https://github.com/mttmcknn/skills/tree/gh-pages-src) is maintained on `gh-pages-src`. GitHub Actions combines it with the native catalog and skills from `main`, then publishes to `gh-pages`. Public skill-page URLs stay stable when repository folders move.

## Migration

If installed under the former marketplace name, remove those old entries before adding `mttmcknn` to avoid duplicate skills. Local symlinks to the former top-level `review/skills/` or `utilities/skills/` paths need updating to `plugins/<bundle>/skills/`.

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
```

See [the audit](maintenance/skill-audit.md) for scope decisions. The structure follows [OpenAI's skill guidance](https://learn.chatgpt.com/docs/build-skills) and [native marketplace format](https://learn.chatgpt.com/docs/enterprise/plugin-management).
