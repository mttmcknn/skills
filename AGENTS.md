# Repository notes

- Skills live in `plugins/<bundle>/skills/<name>/SKILL.md`. Keep instructions concise and portable; put conditional detail in `references/`.
- Keep work logs, audits, and planning documents out of the repository.
- Use Vercel's skills CLI for installation. Preserve Codex and Claude plugin support. Leave Android workflows upstream.
- Bump bundle versions for skill releases. Edit `.codex-plugin/plugin.json`, then run `python3 scripts/sync_claude_compat.py`.
- Website source is on `gh-pages-src`. Preserve existing skill URLs.

## Checks

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate_skills.py
python3 scripts/sync_claude_compat.py --check
python3 -m unittest discover -s tests -v
python3 scripts/check_skills_install.py
```
