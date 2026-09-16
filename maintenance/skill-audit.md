# Skill audit — 2026-09-16

Reviewed all 20 original skills against the installed Android CLI catalog, Google's current Android skills, OpenAI's skill-writing guidance, and their actual instructions/resources. The final scope follows the decision to remove overlapping Android workflows and start from a smaller collection.

## Android ownership

Removed the entire Android plugin and its 15 skills, including its template assets. Google's upstream skills own project creation, SDK/device operations, journeys, UI interaction, test setup, edge-to-edge support, and performance profiling. Existing local installs/symlinks should be removed separately; this repository update does not uninstall an independently installed upstream skill.

| Removed skill | Reason |
| --- | --- |
| `android-cli` | Direct duplicate of upstream CLI orchestration and journey instructions |
| `new-android-app` | Overlaps upstream project creation and testing; imposed a personal stack on generic app requests |
| `verify-android-layout` | Repeated upstream layout/interaction guidance; claimed all UI checks |
| `verify-android-screen` | Repeated upstream capture/visual interaction; mandatory model-specific delegation |
| `android-probe-logging` | Android debugging workflow retained upstream/in project context instead of a parallel local bundle |
| `android-reproduce-as-test` | Overlap with upstream testing work; universal test-first and full-suite requirements |
| `android-strictmode-probe` | Overlapping performance/debugging workflow with repeated setup and cleanup instructions |
| `android-snapshot-diff` | Repeated UI/memory inspection; baseline sequencing and leak-inference errors |
| `android-regression-diff-scan` | Removed with Android bundle for a clean slate; had unsupported claims about diff scanning replacing bisect |
| `android-crash-repro-loop` | Overlapping debugging workflow; broad log matches and guessed device-setting resets |
| `android-trace-sections` | Marker instrumentation is part of upstream profiling workflows |
| `android-runtime-flag-probe` | Overlapping framework/rendering diagnostics; guessed resets and unsupported flag claims |
| `android-coroutine-trace` | Prescribed JVM DebugProbes on unsupported Android runtime |
| `android-perfetto-capture` | Direct overlap with upstream `android-profiler` recording |
| `android-perfetto-analyze` | Direct overlap with upstream `android-profiler` analysis and SQL |

## Remaining skills

| Skill | Change |
| --- | --- |
| `address-review` | Removed mandatory triage approval for already-requested fixes; read complete thread context; preserved authorization for external replies; corrected stale-line handling and pagination |
| `review-cycle` | Narrowed review-only versus review-and-fix behavior; optional proportional delegation; local final-diff review; bounded rounds; no mandatory model choice |
| `validate-merge-prs` | Respects requested authors/PR scope; isolated checkouts; correct dependency direction; current-head merge guard; distinguishes retargeting from rebasing and queued from merged |
| `code-as-image` | Image output is the deliverable; portable tools; no unsolicited clipboard changes; conditional URL-encoding reference; visual verification instead of file-size claims |
| `interrogation` | User-requested interview only; available input tools; no ritual final confirmation; stops when the required information is known |

Checkpoint/resume commands now link to the saved artifact instead of duplicating it in chat, preserve authorization limits, and verify current repository state before following old instructions.

## Routing and boundary checks

These are manual review scenarios, not a measured model-routing benchmark.

| Request | Expected behavior |
| --- | --- |
| “Create a blank Android app”, “tap Login”, “record a Perfetto trace”, “fix IME overlap” | No skill from this marketplace; use upstream Android capabilities |
| “Review PR 42” | Findings only; no fixes, pushes, or merge |
| “Review and fix PR 42” | `review-cycle`; justified fixes and focused validation; no mandatory review team |
| “Address Alice's comments on PR 42” | `address-review`; contextual triage and fixes; respect reply authorization |
| “Validate all open PRs” | `validate-merge-prs`; all authors, no silent `@me` filter or merges |
| “Merge these approved PRs when checks pass” | Validate current heads and dependencies, then execute within existing authorization |
| “Turn this snippet into a PNG” | `code-as-image`; produce and inspect a real image or report a rendering limitation |
| “Interview me about this idea” | `interrogation`; bounded questions, then act when clear |
| “Fix this typo” | No automatic interview, review cycle, or Android debugging workflow |

## Sources and verification scope

- [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills): concise discovery and progressive disclosure. The locally installed OpenAI skill-creator guidance also informed scope preservation and proportional workflows.
- [Google's Android skills](https://github.com/android/skills): catalog checked through `android skills list` and cached skill sources, including `android-profiler`, `testing-setup`, and `android-cli`.
- [Kotlin coroutine debug limitations](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-debug/): confirms Android runtime does not support DebugProbes instrumentation.
- [Claude Code marketplace management](https://code.claude.com/docs/en/discover-plugins): update behavior depends on marketplace settings, not a universal startup guarantee.

Validation covers packaged skill metadata/resources, the website generator, GitHub identity references, and representative scope decisions. It is not an Android app/device test or an empirical latency/quality benchmark. Removed skills are preserved in Git history, not in a second active skill directory.

## Portable / Codex-first follow-up

Moved bundles to `plugins/`, added the native `.agents/plugins/marketplace.json` catalog and `.codex-plugin/plugin.json` manifests, and supplied Codex display names/default prompts separately in each skill’s `agents/openai.yaml`. The website and validation read the native catalog. Claude metadata is generated from it and has no separate workflow bodies.

Converted checkpoint/resume commands into two standard skills, bringing the remaining collection to seven skills. Handoffs default to `.agents/checkpoints/`, accept explicit legacy paths, and require no host-specific file tool, clear-chat command, or conversation state. Installation documentation prioritizes Codex and includes individual skill-folder use in other compatible hosts.

Packaging validation checks both native metadata and compatibility synchronization. Fixture tests exercise missing resources, duplicate names, bad metadata, escaped plugin paths, and synchronization behavior. These checks do not measure live model routing or claim every agent host was exercised.

## Support for both hosts

Codex and Claude Code both remain supported. Each bundle ships both manifests and one shared `skills/` directory; the old top-level Claude manifests moved with their bundles into `plugins/`. The README and website now give each host its own installation section. Generating Claude metadata keeps releases synchronized and does not make Codex a runtime dependency.

A packaging regression test checks that the Claude catalog exposes all seven skills at matching versions after removing all Codex metadata from a fixture. Release checks also validate the marketplace and both bundles with `claude plugin validate --strict`. Claude's [plugin reference](https://code.claude.com/docs/en/plugins-reference#skills) documents discovery of the shared `skills/` layout.
