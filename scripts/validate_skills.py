#!/usr/bin/env python3
"""Validate the skills actually distributed by this marketplace (requires PyYAML)."""
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml


def validate(root):
    errors, names = [], {}
    marketplace = json.loads((root / '.claude-plugin/marketplace.json').read_text())
    plugins = marketplace['plugins']
    plugin_names = set()
    total = 0
    for plugin in plugins:
        name = plugin['name']
        if name in plugin_names:
            errors.append(f'Duplicate plugin: {name}')
        plugin_names.add(name)
        source = (root / plugin['source']).resolve()
        if not source.is_relative_to(root.resolve()):
            errors.append(f'{name}: plugin source escapes repository')
            continue
        manifest = source / '.claude-plugin/plugin.json'
        if not manifest.is_file():
            errors.append(f'{name}: missing plugin manifest')
            continue
        data = json.loads(manifest.read_text())
        if data.get('name') != name:
            errors.append(f'{name}: plugin manifest name mismatch')
        if not re.fullmatch(r'\d+\.\d+\.\d+', data.get('version', '')):
            errors.append(f'{name}: missing/invalid version')
        skills = sorted((source / 'skills').glob('*/SKILL.md'))
        if not skills:
            errors.append(f'{name}: no skills found')
        for skill in skills:
            total += 1
            text = skill.read_text()
            match = re.match(r'\A---\n(.*?)\n---(?:\n|$)', text, re.S)
            if not match:
                errors.append(f'{skill}: missing YAML frontmatter')
                continue
            try:
                meta = yaml.safe_load(match[1])
            except yaml.YAMLError as exc:
                errors.append(f'{skill}: invalid YAML: {exc}')
                continue
            if not isinstance(meta, dict):
                errors.append(f'{skill}: frontmatter must be a mapping')
                continue
            skill_name = meta.get('name', '')
            if not isinstance(skill_name, str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', skill_name) or len(skill_name) > 64:
                errors.append(f'{skill}: invalid skill name')
                continue
            if skill_name != skill.parent.name:
                errors.append(f'{skill}: name differs from directory')
            if skill_name in names:
                errors.append(f'{skill}: duplicate skill name ({names[skill_name]})')
            names[skill_name] = skill
            description = meta.get('description')
            if not isinstance(description, str) or not description.strip() or len(description) > 1024:
                errors.append(f'{skill}: missing/invalid description')
            if not text[match.end():].strip():
                errors.append(f'{skill}: empty skill body')
            for doc in skill.parent.rglob('*.md'):
                # This repo uses inline Markdown links; ignore fenced code examples.
                body = re.sub(r'(?ms)^```.*?^```[^\n]*$', '', doc.read_text())
                for target in re.findall(r'\[[^\]]*\]\(([^)\s]+)\)', body):
                    parsed = urlsplit(target)
                    if parsed.scheme or parsed.netloc or not parsed.path:
                        continue
                    resource = (doc.parent / unquote(parsed.path)).resolve()
                    if not resource.is_relative_to(source) or not resource.exists():
                        errors.append(f'{doc}: missing or external local resource {target}')
    return total, errors


if __name__ == '__main__':
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    try:
        count, errors = validate(root)
    except (OSError, KeyError, ValueError) as exc:
        sys.exit(f'Validation failed: {exc}')
    if errors:
        sys.exit('\n'.join(errors))
    print(f'Validated {count} skills: manifests, names, frontmatter, and local resource links.')
