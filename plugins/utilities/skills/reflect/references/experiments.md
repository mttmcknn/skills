# Compare a skill change during the weekly review

Use a small controlled comparison when a consequential behavioral change would benefit from evidence beyond reading the proposed text. Keep it within the current reflection. The purpose is a better decision this week; later weeks naturally add more evidence.

## Set up a bounded comparison

Write one hypothesis: the behavior this edit should improve and the failure it should avoid. Snapshot the current owned skill and candidate, changing one meaningful behavior at a time. For an external component, compare the unchanged upstream skill alone with the same upstream revision plus the owned companion; never create a patched upstream variant. Record the upstream source and revision. Use temporary copies and isolated task snapshots so testing does not alter live skills, user work, PRs, or external systems.

Choose the smallest set of cases that can distinguish the versions: the motivating scenario, a separate related scenario not used to write the candidate, and a counterexample where the new rule should not apply. Reconstruct the information available before the original failure. Exclude later corrections, later review findings, fixes, and expected answers from the test agent's input. Keep the expected outcomes with the evaluator. Retain only redacted cases suitable for local reuse.

Freeze the cases and evaluation criteria before running the comparison. The agent editing the candidate must not change those criteria to improve its result. Prefer executable checks and observable behaviors; use a fixed rubric and an independent evaluator for judgment calls when available and authorized. A self-rating alone is not strong evidence.

Run baseline and candidate in fresh contexts with the same model, reasoning settings, tools, task snapshot, and resource limit. Use an authorized evaluation facility or bounded subagents when available. Test natural skill selection if the hypothesis concerns discovery; explicitly supplying the skill tests its guidance instead. Record which is being measured.

Set a small attempt and resource budget before starting, proportional to the decision and existing authorization. Begin with one baseline and one candidate. Repeat close or inconsistent results only when justified within that budget. Log inconclusive results and continue the weekly review when execution, access, or budget prevents a useful comparison; never present a walkthrough as an executed test.

## Use the result in this week's decision

Record the hypothesis, skill versions, case references, fixed criteria, model/settings, outputs, comparison, and actual time/token usage when available. Assess the intended improvement alongside regressions, unnecessary actions, complexity, and cost. A verified correctness or authority regression cannot be offset by a nicer explanation or lower token count. Review feedback supplies candidate cases and independently checked findings, not a raw comment-count score.

Recommend the candidate when it improves the intended behavior without material regressions. Prefer the simpler version when results are equivalent. Keep the baseline when the candidate is worse; mark the comparison inconclusive when evidence cannot distinguish them. These are experiment results that inform the normal apply/revise/defer/reject decision, not extra lifecycle stages.

Apply supported changes within the user's existing authorization. Put any remaining concrete decisions in the weekly review as one batch. Retain the experiment record so later runs can learn from unsuccessful variants and compare further improvements. If a previously unseen case is subsequently used to tune an edit, it is no longer an independent validation case; use another related case for the next comparison.

Once applied, the change is implemented. Continue improving the skill in later weekly runs using whatever relevant evidence arrives, without holding it in an awaiting-evidence queue. Do not claim broad real-world effectiveness from a small offline comparison.
