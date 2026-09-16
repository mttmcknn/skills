---
name: review-cycle
description: "Review and fix a pull request iteratively when the user requests a review-and-fix cycle. Recheck changed behavior and stop when no actionable issues remain; a review-only request must stay read-only."
---

# Pull Request Review and Fix Cycle

Resolve the target PR, base/head commit, repository conventions, and requested scope. Preserve unrelated local work; use an isolated checkout when changing branches would disturb it.

1. Read the diff plus surrounding code needed to judge behavior. Prioritize concrete correctness, security, reliability, and performance regressions. Cite the triggering condition and affected location; omit speculative improvements and style churn.
2. For a complex diff, independent reviewers may help when delegation is available and authorized. Assign distinct concerns and bounded artifacts tied to the same commit. Use available model defaults; small changes need no review team. Do not let parallel agents switch branches in a shared worktree.
3. Merge duplicates and validate findings against current code. Implement justified fixes only when requested; a request to review alone authorizes findings, not edits or pushes.
4. Run affected tests and repository-required checks. Review the local final diff so unpushed fixes are visible; reviewers must not accidentally reread a stale remote PR.
5. Repeat for remaining findings or risks introduced by new edits. Stop when no actionable findings remain, when an external blocker prevents progress, or after five fix rounds. Do not create fresh style work to prolong the loop.
6. If publishing is authorized, commit only task changes and push to the intended PR branch after validation. Re-read the remote head and relevant checks; do not imply local success means CI passed.

Report fixes/findings, exact validation, remaining blockers, and whether changes were published. Say no actionable findings were found under the performed review, rather than promising the PR is defect-free. Merging is a separate operation.
