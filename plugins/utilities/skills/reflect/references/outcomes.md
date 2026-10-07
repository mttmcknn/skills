# Evaluate skills using development outcomes

Use downstream feedback to test whether skills helped the work. This is read-only evidence gathering and skill-improvement drafting; it does not authorize fixing PR code, replying to reviewers, requesting rechecks, resolving threads, or changing merge state.

## Discover related outcomes

Start with PR URLs, commits, CI runs, and delegated-session result links in the reviewed chats and earlier reflection reports. Follow those explicit links even when a PR has since merged or closed. Also discover the user's PRs with review activity during the interval in the relevant repositories/accounts, so feedback on an older chat is not missed. Scope additional discovery to the user's authored work and explicitly linked adopted/reviewed PRs; do not crawl unrelated colleagues' work.

Use available GitHub connectors or the installed `gh` CLI. Verify the exact host, repository, and authenticated identity without printing credentials; the user's work and personal identities can differ. Respect existing repository-specific authentication. Check current command help before using flags. For example:

```sh
gh search prs --author=@me --repo OWNER/REPO --updated '>=START_DATE' --sort updated --limit 100 --json number,url,repository,updatedAt
gh pr view PR_NUMBER --repo OWNER/REPO --json url,state,baseRefOid,headRefOid,comments,reviews,statusCheckRollup
gh api --paginate repos/OWNER/REPO/pulls/PR_NUMBER/comments
gh api --paginate repos/OWNER/REPO/issues/PR_NUMBER/comments
gh api --paginate repos/OWNER/REPO/pulls/PR_NUMBER/reviews
```

The date in the search is a broad candidate bound, not the event filter. Include a timezone margin when using day-only search qualifiers, then filter actual comment/review/check timestamps to the interval. Do not upper-bound `updated` at the interval end: a PR with in-window feedback may have been updated again since. Include merged/closed PRs. Record repository/account coverage and search/result caps; paginate or split a capped search by repository/date as supported, and label any remaining gap. Missing chat-to-PR attribution does not make the feedback disappear; retain it as an unattributed outcome.

## Read the evidence

Gather PR head/base, review summaries, issue comments, inline review comments, GraphQL `reviewThreads` with resolution/outdated state, relevant CI/check runs, and subsequent fixes. Paginate both the thread connection and nested comment connections; an initial page or `gh pr view --comments` alone is insufficient. Capture review/comment IDs, author identity, timestamps, reviewed/original commit when provided, paths/lines, source URLs, and edited comment state.

If a comment was edited after the interval, its current body may not be the text originally posted. Label the snapshot and edit time; do not attribute later text to the original week without historical evidence.

Identify configured automated reviewers from actual bot/app metadata and check names, not body text alone. An available review skill can supply read-only finding-verification guidance as a component; its fix, recheck, and monitoring modes do not apply to reflection. Keep organization-specific identities and skill routing in the private source configuration. Do not post even a recheck during reflection.

Compare the finding with the code at the reviewed commit, surrounding callers/contracts, and relevant validation. Trace fixing commits when available. Classify substantive items as **confirmed**, **mistaken**, **unverified**, **pre-existing/unrelated**, or **preference**. Calibrate confirmed findings by reachability and impact; a low-impact optional suggestion is not equivalent to a correctness failure. Retain uncertain feedback as a hypothesis without rewriting a skill around it.

Resolved or outdated threads can still show a historical miss; retain their reviewed SHA and fix evidence. They are not automatically current blockers. Conversely, resolution, a later code change, or an assistant's “fixed” claim does not alone prove the concern was addressed. Do not label feedback pre-existing merely because it touches old lines: verify whether the task introduced a new reachable path or regression.

An explicit automated approval is current only when tied to the live head, with no unresolved actionable finding and successful relevant checks for that head. If the reviewed SHA cannot be established, say unverified. This verdict is not a general merge-readiness claim and does not replace other required gates. CI failures count against a skill only when logs/code support that connection; distinguish product defects, flaky checks, infrastructure problems, and unavailable validation.

## Attribute the outcome to the skill

Construct the shortest supported chain:

`task request → skill/version and use evidence → implementation decision → reviewed commit → finding/check → verified fix or unresolved outcome`

Use chat/tool traces, delegated-session messages, skill read/invocation records, and skill-source history when available. Record the relevant historical text or revision/hash without copying whole skills into every finding. Current guidance may already contain a later fix; do not judge an earlier execution against text that did not yet exist. If historical text or provenance is missing, mark it unknown and narrow the conclusion.

| Observed chain | Interpretation |
| --- | --- |
| Relevant skill was followed, but a verified preventable miss remains | Candidate guidance gap; draft a targeted decision/check tied to this failure mode. |
| Skill was selected but a clear applicable instruction was skipped | Execution failure; investigate the concrete reason before adding more instructions. |
| An applicable available skill was demonstrably not selected | Candidate discovery problem; examine trigger/routing before creating another skill. |
| Guidance changed a decision and the resulting behavior is verified | Positive evidence for that scoped guidance; preserve what worked. |
| Use/version/causality is unknown, or feedback is mistaken/unrelated | Keep the outcome visible without assigning a skill failure or success. |

Count each root incident once across automated inline comments, summary comments, repeated review rounds, CI failures, originating chats, and delegated sessions. Separate new regressions from rediscovery of the same bug. A successful fix is evidence of recovery; it does not erase the initial miss. Preserve explicit user scope exceptions and avoid converting reviewer preferences into universal requirements.

## Report effectiveness honestly

For each relevant skill, report known applicable tasks, confirmed applications, verified misses, demonstrated successful behavior, and attribution gaps. Separate “not selected” from “unknown use,” and distinguish changes made from evidence about their effects. Record effects as part of the weekly evidence history, not a separate status that needs to be cleared. Multiple skills can contribute to one task; do not sum per-skill counts into unique task totals.

For before/after follow-up, compare reasonably similar tasks and state changed task mix, sample size, and missing data. No bot comments, a passing check, or fewer comments in a quieter week cannot alone show improvement. Prefer a few concrete traces over numerical ratings that imply unsupported precision. Feed only supported improvements into the normal apply/revise/defer/reject queue.
