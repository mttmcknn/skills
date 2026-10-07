# Repository notes

- Skills live in `plugins/<bundle>/skills/<name>/SKILL.md`. Keep instructions concise and portable; put conditional detail in `references/`.
- Keep work logs, audits, and planning documents out of the repository.
- Use Vercel's skills CLI for installation. Preserve Codex and Claude plugin support. Leave Android workflows upstream.
- Use the update day's date in `YYYY-MM-DD` format for versions (America/New_York). Every `SKILL.md` has a quoted `metadata.version` matching `.codex-plugin/plugin.json`. When updating a bundle, set the bundle and all its skill versions to that date, then run `python3 scripts/sync_claude_compat.py`. Multiple updates on the same day keep the same date; Git commits distinguish them.
- Website source is on `gh-pages-src`. Preserve existing skill URLs.

## Checks

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate_skills.py
python3 scripts/sync_claude_compat.py --check
python3 -m unittest discover -s tests -v
python3 scripts/check_skills_install.py
```
