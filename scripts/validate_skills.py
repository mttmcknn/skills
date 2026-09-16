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
    marketplace = json.loads((root / '.agents/plugins/marketplace.json').read_text())
    plugins = marketplace['plugins']
    plugin_names = set()
    total = 0
    for plugin in plugins:
        name = plugin['name']
        if name in plugin_names:
            errors.append(f'Duplicate plugin: {name}')
        plugin_names.add(name)
        descriptor = plugin['source']
        if not isinstance(descriptor, dict) or descriptor.get('source') != 'local':
            errors.append(f'{name}: expected a repository-local plugin source')
            continue
        source = (root / descriptor['path']).resolve()
        if not source.is_relative_to(root.resolve()):
            errors.append(f'{name}: plugin source escapes repository')
            continue
        if source.name != name:
            errors.append(f'{name}: plugin directory name mismatch')
        policy = plugin.get('policy', {})
        if policy.get('installation') not in {'AVAILABLE', 'INSTALLED_BY_DEFAULT', 'NOT_AVAILABLE'} or policy.get('authentication') not in {'ON_INSTALL', 'ON_USE'}:
            errors.append(f'{name}: invalid marketplace policy')
        if not plugin.get('category'):
            errors.append(f'{name}: missing marketplace category')
        manifest = source / '.codex-plugin/plugin.json'
        if not manifest.is_file():
            errors.append(f'{name}: missing plugin manifest')
            continue
        data = json.loads(manifest.read_text())
        if data.get('name') != name:
            errors.append(f'{name}: plugin manifest name mismatch')
        if not re.fullmatch(r'\d+\.\d+\.\d+', data.get('version', '')):
            errors.append(f'{name}: missing/invalid version')
        if data.get('skills') != './skills/':
            errors.append(f'{name}: expected skills path ./skills/')
        interface = data.get('interface', {})
        for field in ('displayName', 'shortDescription', 'longDescription', 'developerName', 'category'):
            if not isinstance(interface.get(field), str) or not interface[field].strip():
                errors.append(f'{name}: missing interface.{field}')
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
            ui_path = skill.parent / 'agents/openai.yaml'
            if not ui_path.is_file():
                errors.append(f'{skill}: missing Codex UI metadata')
            else:
                try:
                    ui = yaml.safe_load(ui_path.read_text()).get('interface', {})
                    short = ui.get('short_description', '')
                    if not ui.get('display_name') or not 25 <= len(short) <= 64:
                        errors.append(f'{ui_path}: invalid UI name/description')
                    if '$' + skill_name not in ui.get('default_prompt', ''):
                        errors.append(f'{ui_path}: default prompt must invoke this skill')
                except (yaml.YAMLError, AttributeError, TypeError):
                    errors.append(f'{ui_path}: invalid UI metadata')
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
    print(f'Validated {count} skills: manifests, names, frontmatter, Codex UI metadata, and local resource links.')
