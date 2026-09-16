---
name: validate-merge-prs
description: "Validate a requested set of pull requests and determine dependency-aware merge order; execute merges only within the user-authorized scope. Use for a PR queue or stacked PRs, not a single code review."
---

# Validate and Merge a PR Queue

## Inspect the requested queue

Resolve the repository and user-specified PRs or filter. For a request covering all open PRs, list all authors, not just `@me`. Fetch drafts, base/head repositories and refs, head OIDs, reviews, required checks, merge state, and dependency metadata.

Build prerequisite → dependent edges from actual stacked-branch topology and explicit dependencies. `A depends on B` means B → A; `A blocks B` means A → B. File overlap is a coordination signal, not a dependency. Flag cycles, unavailable prerequisites, and ambiguous relationships.

## Validate

Review relevant changes and repository requirements. Use `review-cycle` only if fixes are requested; queue validation alone must not rewrite or push PRs. Parallel local validation requires a separate worktree per PR. Remote read-only checks can run concurrently without branch checkout.

Classify readiness against the current head OID and current base: required checks complete and successful, required approvals satisfied, non-draft, no unresolved merge conflict, no known actionable blocker, and prerequisites ready/merged. Pending, unknown, or unavailable evidence is not a pass. Check repository rules and merge-queue requirements rather than inferring them from a single approval or empty check list.

Topologically order eligible PRs, keeping blocked dependencies out. Use overlap and age only as tie-breakers. Choose the user-requested merge method or repository convention among allowed methods; a lack of merge commits cannot distinguish squash from rebase.

## Execute within authorization

Present the concrete order, method, and blockers. If the user already authorized merging the eligible set, proceed without asking again. If they requested validation or a plan only, finish that work and request approval for the concrete merges before performing them.

Immediately before each merge, refresh the head OID, base, checks, reviews, and mergeability. Merge the reviewed head using a commit match guard (for example `gh pr merge NUMBER --squash --match-head-commit SHA`) or the equivalent connector guard. Respect the merge queue and branch protection; do not use an admin bypass. Confirm merge completion rather than treating an auto-merge request as already merged.

After a prerequisite merges, inspect each dependent PR again. Retargeting changes a base reference; it does not rebase commits. Squash/rebase merges can leave parent commits in descendants. Inspect the new diff, update/rebase only within authorization, and wait for validation against the resulting head/base. Do not assume retargeting automatically ran CI. Keep branches needed by downstream PRs; delete branches only when requested or established policy requires it.

Stop an affected dependency chain on failure and continue independent authorized merges. Report merged, queued, blocked, and skipped PRs with links and reasons.
