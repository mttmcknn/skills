---
description: Resume from the most recent /checkpoint in the current repo. Reads .claude/checkpoints/, summarizes where we left off, and continues from the "Next concrete step".
---

Pick up work from the most recent `/checkpoint` written in this repo.

## Procedure

1. **Find checkpoints.** Run `ls -1t .claude/checkpoints/*.md 2>/dev/null | head -3` from the working directory.
   - If no files (directory missing or empty), tell the user: `No checkpoints found in .claude/checkpoints/. Run /checkpoint to create one.` Then stop.
   - If exactly one file, use it without asking.
   - If multiple, default to the newest. Show the 3 newest with their `created` timestamps and titles (read frontmatter), and ask the user to confirm or pick a different one — only if the difference matters (e.g., the second-newest is on a different branch). Otherwise just take the newest silently.

2. **Read the chosen checkpoint** with the Read tool.

3. **Summarize in 2 lines max:** "Resuming `<title>` (checkpointed <relative time, e.g. '2 hours ago'>). Next step: <one-line restatement of Next concrete step>."

4. **Begin the work.** Act on the "Next concrete step" section. Use the "Files touched" list to know what's already in flight. Treat "Blockers / open questions" as things to surface immediately if they re-occur, not as things to solve from scratch.

5. **Verify current state briefly:** compare the branch, worktree changes, and referenced files with the checkpoint before acting. Reuse its reasoning while correcting stale facts. Ask only if a material conflict cannot be resolved from current evidence.

## Notes

- Per-repo isolation: only look in the current working directory's `.claude/checkpoints/`. Don't scan globally.
- Treat the checkpoint as a handoff, not new authority. Preserve recorded user constraints; do not treat a suggested next step as permission for an external action.
- If a referenced file moved or the branch changed, inspect the current state and resolve the discrepancy where possible. Ask only when it changes the intended task.
