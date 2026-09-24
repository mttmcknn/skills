---
name: make-pr
description: Create or update a pull request following the current repository's conventions. Use when asked to make or open a PR, prepare a PR draft, or improve its description.
---

# Make a PR

## 1. Read the repository's guidance

Read the current repository's PR skill, if one exists. Look in local skill directories and locations named by `AGENTS.md`. Follow its title conventions, PR template, and required checks. Apply the preferences below within that format.

## 2. Prepare the change

Review the diff against the intended base and check for an existing PR. Run the required checks, preserve unrelated changes, and commit and push the intended work as needed. Honor requests for local drafts or no-push work. For stacked PRs, use the actual parent diff and preserve stack metadata.

## 3. Write for the reviewer

Lead with the problem and resulting behavior. Explain only the mechanism needed to understand the change. Keep paragraphs short, describe the final implementation, and state what was tested and what remains unverified.

Add a concise call tree, code-shape diff, or diagram when it helps explain the change.

## 4. Include useful evidence

Include relevant media in the PR description, not comments. Prefer one final-state screenshot for static changes or a short video for interaction, motion, or streaming. Add before/after comparisons only when they help. For non-UI work, a rendered explanatory diagram can serve as the image.

Always organize every screenshot and image in a compact Markdown table, whether it shows a single final state, different screens, unrelated examples, an explanatory diagram, or a before/after comparison. This applies even when there is only one image and no comparison. Use short, descriptive headers appropriate to the content; do not require Before / After labels. Place images side by side when useful, and use additional rows instead of an overly wide table. Keep captions brief and avoid repeating the same image outside the table.

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

Inspect the media before uploading. Label previews, fixtures, and explanatory diagrams accurately; they do not prove live integration. Reuse current evidence and remove redundant attachments. If capture or upload is blocked, state the limitation and include the best available evidence.

## 5. Publish and verify

Write the description to a body file. Use `gh pr create` or `gh pr edit` with `--body-file`. Check CLI help for attachment support; when `--attach` is available, use it to upload media:

```sh
gh pr edit PR_NUMBER --repo OWNER/REPO --body-file ./pr-body.md --attach './after.png#Final state'
```

Use the uploaded image URLs as `src` values in the final table, replacing the example placeholders above. If the upload tool rewrites only Markdown image references, upload using temporary Markdown references to the local files, then replace those references with sized `<img>` tags using the returned URLs. Do not assume local paths inside HTML tags will be uploaded or rewritten. Repeat `--attach` for additional files; omit `#alt text` for videos. Preserve existing uploaded URLs when editing and remove any duplicate previews appended by the upload tool.

If the command fails, inspect the PR before retrying: attachment uploads can partially fail after the PR is created. Retry only missing attachments. If attachment support is unavailable, use an available upload tool or report the limitation; do not publish local file paths as working media links. Do not use `gh pr create --dry-run` for a local-only draft; it can push changes.

Verify the published description and media render correctly, including compact image widths and preserved proportions. If rendering cannot be checked, say so. Return the PR link and any material validation limits.
