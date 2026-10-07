# Ownership, composition, and portability

Apply these rules to every skill proposal, including changes to this skill.

## Establish ownership before choosing a target

The editable destinations are `mttmcknn/skills` for portable skills and the user's explicitly designated private skill repository for company-specific skills. Keep the private repository path and identity in local configuration alongside the reflection reports. No other source is editable by default. Verify the repository identity and canonical path using Git metadata, installation provenance, or a source manifest; a folder under a personal home directory does not establish ownership. If a local external-skill manifest exists, consult it as provenance, then resolve the relevant installed copy and source. Record the revision or content hash in the private review.

Treat skills not owned by either approved destination as external, including upstream checkouts, installed copies, package caches, vendored copies, and skills in other personally owned repositories. Copying or vendoring an external skill into either allowed repository does not transfer its ownership. If provenance is unknown, keep the finding private until it is established; do not edit the installation to bypass that check.

Canonical edits belong in the destination selected by content and verified ownership. Confirm the configured private repository's identity before editing it, and verify its private visibility before publishing internal content; a local directory name alone is not proof. Local drafting does not authorize publication. Synchronizing an authorized local installation of an owned skill is deployment of that source, not a separate authoring path. Reconcile existing differences before synchronization; preserve unrelated work. This does not authorize committing, pushing, or publishing.

## Build on an external component

When an external skill needs additional behavior, create or update a narrowly triggered companion skill in the appropriate owned repository. A generic extension belongs in the portable collection; an internal integration belongs in the designated private collection. Give it a distinct name; do not shadow the upstream name or silently replace its installation.

The companion must name the upstream skill and its source, state when to load it, and describe only the additional decisions or checks. Read the upstream instructions and relevant references before adding behavior. Keep upstream procedures in their original source rather than duplicating them in the companion. State any deliberate behavioral difference explicitly within the companion's narrow scope. A portable companion may reference only public components; references to internal components belong in the private collection.

Use available host skill discovery to resolve the dependency instead of hardcoding a machine path. Record the tested upstream revision in the private evaluation. If the component is absent or incompatible, report that dependency and continue independent work; do not fabricate its behavior, silently install another version, or vendor a replacement. A normal upstream update or contribution is separate work, not an automatic reflection action.

For example, an owned Kotlin review companion can load a public Kotlin API skill, apply its existing guidance, and add a narrowly scoped general review check. It must not patch that upstream skill. An employer-specific companion belongs in the private collection instead.

## Audit the complete proposed package

Before presenting a proposal, inspect every changed and newly included file: skill instructions, references, UI metadata, scripts, examples, fixtures, assets, generated manifests, and publication text. Repeat the audit after revisions and before installation or publication.

Check both literal content and meaning, then verify the destination. Portable packages must exclude employer-specific names and products, private review bots or coding services, internal commands and operational procedures, repository/PR/session identifiers, internal URLs, local work paths, credentials, source excerpts, and examples that reveal private contracts or incidents. A generic title, renamed identifier, or removal of the company name alone does not make proprietary material portable.

Extract only a general, independently understandable decision or procedure. Use synthetic public examples. If the useful lesson depends on an internal system or private contract, route a reusable skill or companion to the designated private collection; otherwise retain a private finding or separately scoped internal action. Audit private proposals too: permit only the internal context needed for the workflow, exclude secrets, personal/customer data and raw transcripts, and ensure no private dependency or generated file spills into the portable package. Keep raw evidence, source configuration, local denylist/search terms, and detailed audit notes outside the repository.

Use targeted searches for known private names, domains, paths, and identifiers, then read the complete resulting diff and package for semantic leaks. A clean keyword scan is supporting evidence, not a sufficient audit. Record ownership, upstream dependencies, files reviewed, scan/manual-review results, and remaining limits in the private report. An unresolved leak or unknown ownership keeps the proposal from being apply-ready; other supported work can continue.
