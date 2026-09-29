---
name: adopt-stack
description: Adopt every open pull request in a stack from any supplied PR URL by resolving dependencies, applying the adopt-pr workflow bottom to top, and preserving stack relationships. Use when asked to adopt, finish, or prepare a whole PR stack.
---

# Adopt a stack

Use any PR URL in the stack to find the complete stack, then take each open PR from handoff to ready for review. Read and follow [adopt-pr](../adopt-pr/SKILL.md) for each PR; this skill adds stack discovery, ordering, and cross-PR consistency. If `adopt-pr` is unavailable, report that it must be installed alongside this skill.

## Scope

A request to adopt a stack authorizes the `adopt-pr` actions for every open PR in the resolved stack. Honor narrower instructions such as review-only, local-only, or no-push.

Adopt the whole connected stack, not only the PRs above the supplied URL. Stop at the trunk or last merged ancestor. Do not reopen, merge, close, split, re-parent, or change draft status unless explicitly requested.

If the dependencies form more than one child path, or the stack cannot be identified confidently, report the candidate structure and ask one focused question before editing.

## 1. Resolve the stack

Start with the exact supplied PR URL and repository. Prefer native stack metadata or the repository's supported stack tool. If none is available, follow PR base/head relationships to open parents and children.

Record every PR's URL, state, draft status, base, head, and head commit. Confirm that each base matches the previous PR's head. Report closed or merged entries and keep them unchanged.

## 2. Recover context

Read each open PR's description, discussion, review findings, CI results, and parent diff. Search for handoff notes by stack, PR URLs, branches, or titles. Identify shared decisions and dependencies before changing the lowest affected PR.

## 3. Adopt bottom to top

Prepare one checkout or isolated worktree for the stack. Avoid overlapping writers.

For each open PR, apply the `adopt-pr` review, fix, validation, publication, and handoff rules against its actual parent. Put each fix in the lowest PR that owns it. Before moving upward, bring descendants up to date using the repository's stack convention. Resolve conflicts against the intended final stack state.

Do not force-push or rewrite history without authorization. If restacking requires it, ask once before the first rewrite and protect every authorized push with an exact expected-head lease.

## 4. Validate and publish

Validate each PR at its final head, then validate the top of the stack when the combined behavior matters. Refresh descriptions and evidence for each PR's own diff. Preserve stack links and required metadata.

After the last push, reread every PR's base, head, description, and checks. Treat results from an earlier head as stale.

Return a bottom-to-top table with each PR's link, changes, validation, CI state, and blockers. Report pending checks as pending. Do not start a monitor unless requested.
