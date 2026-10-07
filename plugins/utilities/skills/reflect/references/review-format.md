# Weekly review and decision queue

Keep one compact `review.md` per interval and a separate private supporting record such as `details.md`. Reuse finding IDs across weeks when following up. Store proposed text under `proposals/` only when it is substantial enough to benefit from a separate file; otherwise an exact replacement block or diff in the supporting record is sufficient. No custom database or dashboard is required.

## Default output

Use this format in the chat response and `review.md`:

| Recommended change | Why it matters | What it fixes |
| --- | --- | --- |
| R01 — Specific action and affected skill | Practical cost or consequence | The concrete gap or behavior the change addresses |

Show only the highest-value three recommendations, or fewer when justified. Keep each cell to one short sentence. Do not add status, confidence, destination, or evidence columns. A material blocker or uncertainty belongs briefly in the affected row; do not imply a proposal is applied or an expected benefit is demonstrated.

Follow the table with one details link and, only if needed, one short decision prompt using finding IDs. Do not add a prose recap, coverage counts, methodology, experiment results, or no-change findings. If there are no recommendations, use one sentence saying so and the details link. Expand a finding only when requested.

## Supporting record

Save the following for traceability without rendering it in the default output:

1. **Interval and coverage.** Explicit start/end, timezone, generation date, and a per-source coverage table. Include configured delegated-session sources and automated PR feedback even when unavailable. Distinguish discovered, actually reviewed, and inaccessible conversations and PRs; link the source inventory if it is long.
2. **Decision queue.** Record finding ID, destination/action, confidence, status, and draft link for all findings. Retain remaining findings and prior decisions without presenting them as new.
3. **Evidence and proposals.** One section per finding using the fields below. Include meaningful contradictions and the reason a weaker signal did not become a proposal.
4. **What this week changes.** Show relevant skill/version, applicable opportunities, confirmed uses, verified misses, demonstrated successful behavior, and unknown cases. Connect material outcomes to the task/PR/reviewed SHA and classify guidance, discovery, execution, or unrelated causes. Fold useful adjustments to prior changes into the current queue. Keep previously implemented changes in place when there is no reason to revise them; a quiet week is not evidence of success.
5. **Next decision or completion.** Link applied changes and validation, or ask which concrete finding IDs to apply, revise, defer, or reject.

## Finding fields

These fields belong in the supporting record, not the recommendation table.

| Field | Required content |
| --- | --- |
| ID and status | Stable local ID; `proposed`, `approved`, `implemented`, `deferred`, `rejected`, or `superseded`. Record the user's actual decision, not an assumed approval. |
| Problem and scope | What happened, its observed cost or consequence, and the task/repository/agent scope where the lesson applies. |
| Evidence | Source + exact returned chat title if available + conversation/session ID + timestamp + message ID or file line. Short redacted user excerpt or paraphrase, assistant behavior, and observed outcome. Link returned source URLs or local files. |
| Strength | Independent incident count, direct correction versus suggestion/inferred gap, confidence with reason, attribution/date limits, and counterevidence. |
| Existing guidance | Relevant current skill/instruction path and section; explain absent guidance, unclear discovery, conflicting rules, or an execution failure. Mark historical skill availability unknown when it cannot be established. |
| Application and outcome | When PR/CI feedback is involved: skill-use evidence and historical version if recoverable; PR URL, comment/check ID, reviewed commit and live head, code verification, outcome, and what can or cannot be attributed to the skill. |
| Ownership and portability | Destination class (portable or private), verified repository/path/revision and whether owned, external, or unknown; external dependency and companion routing if needed; full-package company-content audit result and any remaining concerns. Unknown ownership prevents a direct edit. |
| Proposed change | Canonical path in the verified owned destination, exact before/after text or a full new skill draft, the future decision it changes, and why this is the smallest useful fix. A non-skill fix or no change is allowed. |
| Check | A realistic motivating scenario and expected behavior, plus a counterexample where the new rule should not apply. For a comparative experiment, record baseline/candidate versions, fixed criteria, cases, model/settings, results, and measured cost when available. Include structure/link/helper checks appropriate to the actual change. |
| Weekly evidence | Relevant new outcomes, recurrences, regressions, or opportunities and the resulting adjustment, if any. If there were no applicable tasks, say so briefly. This is evidence history, not a pending status or another approval step. |

Audit the complete proposed package before marking it ready to apply and repeat after edits or generation. No company-specific names, internal review or coding tools, workflows, URLs, identifiers, paths, private code, or identifying examples belong in portable skills or public fixtures. Route necessary company-specific guidance to the designated private collection and audit it for secrets, personal/customer data, raw evidence, and accidental public distribution. Renaming the company while retaining its private workflow is not sufficient. Record the audit privately, without putting a private denylist in the package.

Do not repeat sensitive transcripts in draft skills. Put generalizable guidance in the draft and keep minimal redacted evidence in the private review. A user approval to apply a finding is distinct from approval to publish it or modify memory.

## Decision examples

- `Apply R03 and R07.` Apply those concrete proposals, validate, and record the result.
- `Walk me through these.` Present one proposal with evidence and the exact change, then retain the decision and move to the next.
- `Defer R04 until we see another example.` Keep its evidence and revisit only when that condition is met.
- `Reject R05; that was specific to the migration.` Preserve the scope correction and avoid re-proposing the same global rule next week.

Mark an applied change implemented and let the next weekly run build on it naturally. Keep experiment results distinct from observations in real tasks, without requiring a separate effectiveness sign-off. Batch any decisions that still need user input; use existing authorization for work already approved.
