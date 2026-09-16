"""Exercise installable package boundaries without changing agent configuration."""
import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_script(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'scripts' / f'{name}.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


validator = load_script('validate_skills')
compat = load_script('sync_claude_compat')


class PackagingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='skills-package-test-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for path in ('plugins', '.agents/plugins', '.claude-plugin'):
            shutil.copytree(ROOT / path, self.root / path)

    def test_native_catalog_loads_without_claude_metadata(self):
        shutil.rmtree(self.root / '.claude-plugin')
        for path in (self.root / 'plugins').glob('*/.claude-plugin'):
            shutil.rmtree(path)
        count, errors = validator.validate(self.root)
        self.assertEqual(count, 7)
        self.assertEqual(errors, [])

    def test_missing_reference_fails(self):
        path = self.root / 'plugins/review/skills/address-review/references/github-api-patterns.md'
        path.unlink()
        self.assertTrue(any('missing or external local resource' in e for e in validator.validate(self.root)[1]))

    def test_duplicate_skill_name_fails_across_bundles(self):
        shutil.copytree(self.root / 'plugins/utilities/skills/checkpoint',
                        self.root / 'plugins/review/skills/checkpoint')
        self.assertTrue(any('duplicate skill name' in e for e in validator.validate(self.root)[1]))

    def test_plugin_source_cannot_escape_repository(self):
        path = self.root / '.agents/plugins/marketplace.json'
        data = json.loads(path.read_text())
        data['plugins'][0]['source']['path'] = '../external-plugin'
        path.write_text(json.dumps(data))
        self.assertTrue(any('escapes repository' in e for e in validator.validate(self.root)[1]))
        with self.assertRaisesRegex(ValueError, 'escapes'):
            compat.outputs(self.root)

    def test_invalid_frontmatter_fails(self):
        path = self.root / 'plugins/utilities/skills/checkpoint/SKILL.md'
        path.write_text('---\nname: [\n---\nA task handoff.\n')
        self.assertTrue(any('invalid YAML' in e for e in validator.validate(self.root)[1]))

    def test_stale_skill_prompt_fails(self):
        path = self.root / 'plugins/utilities/skills/checkpoint/agents/openai.yaml'
        path.write_text(path.read_text().replace('$checkpoint', '$nonexistent-skill'))
        self.assertTrue(any('default prompt must invoke' in e for e in validator.validate(self.root)[1]))

    def test_compatibility_generation_tracks_native_release(self):
        self.assertEqual(compat.sync(self.root, check=True), [])
        path = self.root / 'plugins/review/.codex-plugin/plugin.json'
        data = json.loads(path.read_text())
        data['version'] = '0.4.1'
        path.write_text(json.dumps(data))
        destination = self.root / 'plugins/review/.claude-plugin/plugin.json'
        previous = destination.read_text()
        self.assertTrue(compat.sync(self.root, check=True))
        self.assertEqual(destination.read_text(), previous, 'Check mode must not mutate files')
        compat.sync(self.root)
        self.assertEqual(json.loads(destination.read_text())['version'], '0.4.1')
        self.assertEqual(compat.sync(self.root, check=True), [])
        self.assertEqual(compat.sync(self.root), [], 'Repeated generation must be idempotent')


if __name__ == '__main__':
    unittest.main()
