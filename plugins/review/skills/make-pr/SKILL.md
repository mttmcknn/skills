---
name: make-pr
description: Create or update a pull request following the current repository's conventions. Use when asked to make or open a PR, prepare a PR draft, or improve its description.
---

# Make a PR

## 1. Read the repository's guidance

Read the current repository's PR skill, if one exists. Look in local skill directories and locations named by `AGENTS.md`. Follow its title conventions, PR template, and required checks. Apply the preferences below within that format.

## 2. Prepare the change

Review the diff against the intended base and check for an existing PR. Run the required checks, preserve unrelated changes, and commit and push the intended work as needed. Honor requests for local drafts or no-push work. For stacked PRs, describe only the actual parent diff, preserve stack metadata, and include at most one short dependency link when it helps reviewers locate context.

## 3. Write for the reviewer

Lead with the problem and resulting behavior. Explain only the mechanism needed to understand the change. Describe the final implementation, rewrite the description to that final state rather than appending its history, and state what remains unverified.

Default to one short summary paragraph, no more than three grouped validation bullets, and the current media required below. Keep most descriptions under 200 prose words; use fewer when the change is simple. Exclude required metadata and media from that count. Do not pad to reach a length target. Include a consequential tradeoff or limitation when a sound review needs it, even when that exceeds the target; do not omit key information solely to meet a word count. Keep each detail in one place: use the summary for behavior and necessary mechanism, validation bullets for grouped checks, and media captions for the displayed state and tested build. Avoid repeating details across them or listing individual assertions. Reread the completed description for rapid skimability and remove redundant or incidental detail.

Add a concise call tree, code-shape diff, or diagram when it helps explain the change.

## 4. Include useful evidence

Keep PR media reflective of the current PR code. Default to one final-state artifact in the description, not comments: a screenshot for static changes, a short video for interaction, motion, or streaming, or a diagram for non-UI work. Use additional captures only when needed to show distinct required states; every capture must represent the same final implementation. Do not accumulate before/after comparisons, intermediate iterations, or superseded reference images.

Capture after the final relevant code change, identify the tested commit or build in the caption, and verify the evidence against the current PR head before publishing. When later edits affect the appearance or behavior shown, replace the media and its caption. Labeling an outdated capture with an older commit does not make it valid final-state evidence.

Always organize every screenshot and image in a compact Markdown table, whether it shows a single final state, distinct required screens, or an explanatory diagram. This applies even when there is only one image and no comparison. Use short, descriptive headers appropriate to the content; describe the final states shown. Place multiple required images side by side when useful, and use additional rows instead of an overly wide table. Keep captions brief and avoid repeating the same image outside the table.

Use HTML `<img>` tags inside table cells to control display size. For portrait phone screenshots, default to `width="280"` (280 CSS pixels), with descriptive `alt` text and no `height` attribute so proportions are preserved. A table alone does not constrain image height. Use an explicit width rather than a minimum width; choose a larger width for landscape screenshots or diagrams when needed for legibility. Keep the original uploaded resolution.

```markdown
| Search screen | Settings screen |
| --- | --- |
| <img src="SEARCH_IMAGE_URL" alt="Search screen" width="280"> | <img src="SETTINGS_IMAGE_URL" alt="Settings screen" width="280"> |
```

For a single image:

```markdown
| Final state |
| --- |
| <img src="IMAGE_URL" alt="Final state" width="280"> |
```

Inspect the media before uploading. Label previews, fixtures, and explanatory diagrams accurately; they do not prove live integration. Reuse evidence only after verifying that it still represents the current PR head. Remove obsolete embeds, links, captions, and duplicate attachments from the description when replacing evidence. If current capture or upload is blocked, remove misleading stale media and report the missing evidence; do not substitute an outdated capture.

## 5. Publish and verify

Write the description to a body file. Use `gh pr create` or `gh pr edit` with `--body-file`. Check CLI help for attachment support; when `--attach` is available, use it to upload media:

```sh
gh pr edit PR_NUMBER --repo OWNER/REPO --body-file ./pr-body.md --attach './after.png#Final state'
```

Use the uploaded image URLs as `src` values in the final table, replacing the example placeholders above. If the upload tool rewrites only Markdown image references, upload using temporary Markdown references to the local files, then replace those references with sized `<img>` tags using the returned URLs. Do not assume local paths inside HTML tags will be uploaded or rewritten. Repeat `--attach` for additional files; omit `#alt text` for videos. Preserve an existing uploaded URL only for evidence verified as current. Replace the media section as a whole when refreshing it, and remove any duplicate previews appended by the upload tool.

If the command fails, inspect the PR before retrying: attachment uploads can partially fail after the PR is created. Retry only missing attachments. If attachment support is unavailable, use an available upload tool or report the limitation; do not publish local file paths as working media links. Do not use `gh pr create --dry-run` for a local-only draft; it can push changes.

Verify that the published description contains only the intended final-state media, that every capture reflects the current PR code, and that the media render correctly with compact image widths and preserved proportions. If rendering cannot be checked, say so. Return the PR link and any material validation limits.
