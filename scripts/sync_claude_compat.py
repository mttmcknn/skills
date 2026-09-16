#!/usr/bin/env python3
"""Generate optional Claude packaging from the native Codex catalog/manifests."""
import argparse
import json
from pathlib import Path


def outputs(root):
    root = root.resolve()
    catalog = json.loads((root / '.agents/plugins/marketplace.json').read_text())
    entries, files = [], {}
    for entry in catalog['plugins']:
        descriptor = entry['source']
        if descriptor.get('source') != 'local':
            raise ValueError('Compatibility generation requires repository-local plugins')
        source = (root / descriptor['path']).resolve()
        if not source.is_relative_to(root.resolve()):
            raise ValueError('Plugin source escapes the repository')
        plugin = json.loads((source / '.codex-plugin/plugin.json').read_text())
        shared = {key: plugin[key] for key in
                  ('name', 'version', 'description', 'author', 'homepage', 'repository')}
        files[source / '.claude-plugin/plugin.json'] = shared
        entries.append({
            'name': plugin['name'], 'source': descriptor['path'],
            'description': plugin['description'], 'author': plugin['author'],
            'homepage': plugin['homepage'],
        })
    files[root / '.claude-plugin/marketplace.json'] = {
        '$schema': 'https://anthropic.com/claude-code/marketplace.schema.json',
        'name': catalog['name'],
        'description': 'Optional Claude Code packaging for the same portable agent skills.',
        'owner': {'name': 'Matt McKenna'}, 'plugins': entries,
    }
    return files


def sync(root, check=False):
    root = root.resolve()
    stale = []
    for path, payload in outputs(root).items():
        content = json.dumps(payload, indent=2) + '\n'
        if not path.exists() or path.read_text() != content:
            stale.append(path.relative_to(root))
            if not check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content)
    return stale


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail instead of writing stale compatibility metadata')
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    changed = sync(args.root.resolve(), args.check)
    if args.check and changed:
        parser.exit(1, 'Stale compatibility metadata: ' + ', '.join(map(str, changed)) + '\nRun python3 scripts/sync_claude_compat.py\n')
    print('Compatibility metadata is current.' if args.check else f'Updated {len(changed)} compatibility manifests.')
