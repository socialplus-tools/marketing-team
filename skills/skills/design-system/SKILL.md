---
name: design-system
description: >
  Reference for the social.plus design system — colors, typography, spacing, buttons,
  inputs, layout, shadows, icons, imagery, accessibility, and logo usage.
  Use this skill for: writing CSS, styling components, building Webflow elements,
  creating HTML mockups, designing visual layouts, or any output where visual accuracy
  matters for social.plus. Also trigger when someone asks about brand colors, the
  color palette, button states, dark mode colors, design tokens, spacing, border
  radius, typography, or layout. Trigger even for quick questions like "what blue
  do we use" or "what's the hover color for buttons."
  Do NOT trigger for written content only (use brand-messaging skill) — this skill
  is for visual output and design token reference.
---

# social.plus Design System

This skill provides the full social.plus design system reference. The source of truth lives on GitHub and must be fetched fresh every time.

## What to do

1. Fetch the main brain for cross-domain routing, precedence rules, and the compliance check:
```
https://github.com/cruciate-hub/marketing-team/blob/main/brain.md
```

2. Fetch the design system router:
```
https://github.com/cruciate-hub/marketing-team/blob/main/design-system/brain.md
```

3. Follow the design system router's instructions — it tells you which additional files to fetch based on the user's task.

4. If the output includes any text content (headings, labels, CTAs, descriptions), also fetch:
```
https://github.com/cruciate-hub/marketing-team/blob/main/messaging/brain.md
```

5. Before delivering, run the compliance check from the main brain.

## Important: URL format

**Always use `github.com/.../blob/...` URLs when fetching files.** Never attempt `raw.githubusercontent.com` — it is blocked by network egress settings and will throw an error. This applies to brain.md and all files it routes to.
