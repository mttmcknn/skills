---
name: code-as-image
description: "Render a supplied code snippet as a syntax-highlighted image for sharing or presentation. Produce an actual image when requested; return a renderer link alone only when that is the requested output or rendering is unavailable."
---

# Render Code as an Image

1. Resolve the snippet from the user's code block or specified file. Read the clipboard only when requested. Preserve literal bytes and newlines; infer language from the fence or file extension.
2. Use the user's renderer/style if specified. Otherwise use an available local renderer for private code, or ray.so for code suitable for that web service. Do not send private repository content to a third-party renderer without authorization covering that transfer.
3. For ray.so, read [URL encoding](references/ray-url.md). Use defaults (candy, 64px padding, dark mode, background enabled) unless the user gives preferences. Inspect the live site's controls for supported themes/languages rather than relying on a copied catalog.
4. Open the renderer using available browser tools, wait for the actual code and fonts, and export PNG or capture the code frame. Confirm the current DOM from the browser; do not hardcode a provider-specific tool or stale selector. Use a task output directory unless the user specified another destination.
5. Inspect the resulting image for exact code, syntax highlighting, clipping, and legibility. File size alone cannot establish correctness. Fix the rendering if needed, then return the absolute image path and preview.

If only a link is possible, report that limitation and provide the usable renderer link without claiming a PNG was produced. Copy to clipboard only if requested. A URL fragment containing code is an encoding, not a confidentiality guarantee.
