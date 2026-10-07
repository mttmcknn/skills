# External skills

Skills I use, with versions recorded on 2026-10-07.

| Repository | Recorded version | Used in |
| --- | --- | --- |
| [github/gh-stack](https://github.com/github/gh-stack) | 0.0.8 | Codex and Claude Code |
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | 2.6 | Codex |
| [chrisbanes/skills](https://github.com/chrisbanes/skills) | 2026.10.3 (package version) | Codex and Claude Code |

## Install

These commands install current upstream versions of the selected skills globally.
The versions above are a record, not install pins.

```sh
npx skills add github/gh-stack --skill gh-stack --global --agent codex claude-code

npx skills add cathrynlavery/diagram-design --skill diagram-design --global --agent codex

npx skills add chrisbanes/skills --global --agent codex claude-code \
  --skill compose-animations \
    compose-component-design \
    compose-focus-navigation \
    compose-performance \
    compose-state-and-effects \
    compose-ui-testing-patterns \
    gradle-run \
    grounded-writing \
    kotlin-api-design \
    kotlin-concurrency-and-flow \
    kotlin-control-flow \
    using-chrisbanes-skills
```
