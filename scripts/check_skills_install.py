#!/usr/bin/env python3
"""Exercise Vercel skills discovery and installation in a temporary project."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
CLI_VERSION = '1.5.26'
AGENTS = {'Codex': '.agents/skills', 'Claude Code': '.claude/skills'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', default=str(ROOT), help='Checkout path or published owner/repo')
    parser.add_argument('--npm-cache', type=Path, help='Optional npm cache directory')
    args = parser.parse_args()
    expected = {path.parent.name: path.parent for path in ROOT.glob('plugins/*/skills/*/SKILL.md')}
    assert expected, 'No source skills found'
    command = ['npx', '--yes']
    if args.npm_cache:
        command += ['--cache', str(args.npm_cache.resolve())]
    command += [f'skills@{CLI_VERSION}']
    environment = dict(os.environ, DISABLE_TELEMETRY='1')

    with tempfile.TemporaryDirectory(prefix='skills-install-check-') as directory:
        project = Path(directory).resolve()

        def run(*arguments):
            result = subprocess.run(command + list(arguments), cwd=project, env=environment,
                                    text=True, capture_output=True, timeout=120)
            if result.returncode:
                raise RuntimeError(f'skills command failed:\n{result.stdout}\n{result.stderr}')
            return result.stdout

        listing = run('add', args.source, '--list')
        for name in expected:
            assert name in listing, f'Discovery missed {name}'
        assert not (project / '.agents/skills').exists(), '--list must not install skills'

        installed = json.loads(run('add', args.source, '--skill', '*', '--agent',
                                   'codex', 'claude-code', '--yes', '--json'))
        assert len(installed) == len(expected), 'Unexpected number of installed skills'
        assert {item['name'] for item in installed} == expected.keys(), 'Installed skill set differs'
        for item in installed:
            assert item['status'] == 'installed', item
            assert item['scope'] == 'project', item
            assert set(item['agents']) == AGENTS.keys(), item

        visible = json.loads(run('list', '--agent', 'codex', 'claude-code', '--json'))
        assert {item['name'] for item in visible} == expected.keys(), 'Installed skills are not listed'
        for item in visible:
            assert item['scope'] == 'project', item
            assert Path(item['path']).resolve().is_relative_to(project), item

        # `list` labels only locally detected agent apps. CI has neither app;
        # verify both target directories directly instead of asserting those labels.
        for name, source in expected.items():
            for agent, destination in AGENTS.items():
                installed_path = project / destination / name
                assert installed_path.resolve().is_relative_to(project), 'Skill escaped test project'
                for resource in source.rglob('*'):
                    if resource.is_file():
                        target = installed_path / resource.relative_to(source)
                        assert target.read_bytes() == resource.read_bytes(), f'{agent}: resource differs: {target}'

        print(f'skills@{CLI_VERSION}: discovered and installed all {len(expected)} skills for '
              'Codex and Claude Code; verified complete resources and installed-skill listing.')


if __name__ == '__main__':
    main()
