# Maintaining this skill collection

- Explicit user instructions take precedence over these conventions.
- Keep skill workflows portable. Put Codex presentation metadata in `agents/openai.yaml`, not host-specific tool or model requirements in `SKILL.md`.
- Use Vercel's `skills` CLI as the primary installation path. Verify discovery and project installation for both Codex and Claude Code with `python3 scripts/check_skills_install.py`; it uses a temporary project, never global installation.
- Maintain existing Codex and Claude Code plugin packaging for every bundle, with the same skills available in each.
- `.agents/plugins/marketplace.json` and `plugins/*/.codex-plugin/plugin.json` define bundle metadata for validation and the website. Generate Claude compatibility metadata with `python3 scripts/sync_claude_compat.py`; do not duplicate skill bodies or recreate a commands-only implementation.
- Keep descriptions specific and short. Link conditional instructions from `references/`; keep output templates in `assets/` only when needed.
- Leave Android workflows to the upstream Android CLI skills unless the user explicitly requests a new, distinct local capability.
- Bump affected bundle versions when releasing changes. Validate with `python3 scripts/validate_skills.py`, `python3 scripts/sync_claude_compat.py --check`, and `python3 -m unittest discover -s tests -v` after installing `requirements-dev.txt`.
- Website source is on `gh-pages-src`; it reads the native marketplace and preserves `/bundle/skills/name/` URLs independently of repository layout. Validate site changes before publishing both branches.
