---
name: checkpoint
description: Save a compact project handoff when the user asks to pause, checkpoint, or preserve task context for a later session. Records the goal, decisions, changes, validation, blockers, and next step without requiring a particular agent host.
---

# Save a Task Checkpoint

Capture enough context for another session or agent to continue without repeating the investigation. Use the current conversation and repository evidence; do not invent missing history.

1. Use the user's destination when supplied. Otherwise write under `.agents/checkpoints/` in the current project, named `<UTC YYYYMMDDTHHMMSSZ>-<short-slug>.md`. Avoid overwriting an existing checkpoint; add a suffix on collision. If no project or writable workspace is available, provide the handoff in chat and say it was not saved to disk.
2. Record the project path, branch and head commit when applicable, goal, relevant decisions, changed files, checks actually run and their results, unresolved blockers, and the next concrete action. Distinguish committed/pushed changes from local work. Keep only context that will affect continuation.
3. Record user constraints and any pending approval accurately. A checkpoint does not authorize new external actions. Exclude credentials and sensitive payloads; use paths or summaries instead.
4. Include a self-contained continuation prompt with the checkpoint's absolute path and a reminder to verify the current project state before acting.
5. Read back the saved file to verify its path and completeness. Return a clickable path and a short next-step summary. Do not require a host-specific clear command, new task, or model. If the request was to pause, stop after saving.

Use a short document with headings such as Goal, Decisions, Current state, Validation, Blockers, and Next step. Omit empty sections. A small amount of progress needs a small checkpoint, not another confirmation prompt.
