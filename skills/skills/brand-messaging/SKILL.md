---
name: brand-messaging
description: >
  Enforces social.plus brand messaging consistency across all written content.
  Use this skill for: marketing copy, blog posts, landing page text, press releases,
  pitch materials, website copy, product descriptions,
  investor communications, taglines, subject lines, or any text representing the
  social.plus brand. Also trigger when reviewing or auditing existing copy against
  brand guidelines, or when someone asks about brand voice, tone, approved terminology,
  messaging frameworks, value propositions, competitive positioning, or boilerplates.
  Do NOT trigger for HTML email generation (use newsletters skill) or social media
  posts (use social-media skill) — those have dedicated skills with format-specific
  instructions.
---

# social.plus Brand Messaging

This skill ensures all social.plus content aligns with official brand messaging. The source of truth lives on GitHub and must be fetched fresh every time.

## What to do

1. Fetch the main brain for cross-domain routing, precedence rules, and the compliance check:
```
https://github.com/cruciate-hub/marketing-team/blob/main/brain.md
```

2. Fetch the messaging router:
```
https://github.com/cruciate-hub/marketing-team/blob/main/messaging/brain.md
```

3. Follow the messaging router's instructions — it tells you which additional files to fetch based on the user's task.

4. If the output includes any visual styling (HTML, CSS, colors, layout), also fetch:
```
https://github.com/cruciate-hub/marketing-team/blob/main/design-system/brain.md
```

5. Before delivering, run the compliance check from the main brain.

## Important: URL format

**Always use `github.com/.../blob/...` URLs when fetching files.** Never attempt `raw.githubusercontent.com` — it is blocked by network egress settings and will throw an error. This applies to brain.md and all files it routes to.
