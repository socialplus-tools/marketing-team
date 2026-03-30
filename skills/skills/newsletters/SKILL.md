---
name: newsletters
description: >
  Generate MailerLite-compatible responsive HTML marketing emails for social.plus.
  Use this skill for: email campaigns, newsletters, product update emails, feature
  announcement emails, monthly release emails, or any HTML email content for social.plus.
  Trigger on phrases like "create an email", "write a newsletter", "email HTML",
  "MailerLite email", "campaign email", "product update email", "monthly update email",
  "feature announcement email", "email template", "newsletter HTML", or when the user
  wants to generate HTML that will be pasted into MailerLite. Also trigger when the user
  pastes content from a product update document and wants it turned into an email, or
  shares a Google Doc link containing release notes.
  This skill owns all HTML email output. Do NOT use brand-messaging for emails —
  this skill handles both copy and HTML generation with email-specific rules.
---

# social.plus Newsletter HTML Generator

Generate MailerLite-compatible responsive HTML emails from Bam's docs. Supports two email types: **Monthly Product Updates** (multi-feature roundup with tiered layout) and **Feature Launch Announcements** (single-feature spotlight with sub-features in zigzag layout). The output is complete HTML that gets pasted directly into MailerLite's custom HTML editor.

## Step 0: Fetch the main brain

Fetch the main brain for cross-domain routing, precedence rules, and the compliance check you must run before delivering:

```
https://github.com/socialplus-tools/marketing-team/blob/main/brain.md
```

## Step 1: Fetch brand guidelines

Fetch the messaging router to get terminology and tone:

```
https://github.com/socialplus-tools/marketing-team/blob/main/messaging/brain.md
```

Follow its "Any content task" routing to fetch `terminology.md` and `tone.md`. For email subject lines and body copy, also check if "Short-form content" routing applies.

Fetch the color system directly (emails need hex values, not CSS variables):

```
https://github.com/socialplus-tools/marketing-team/blob/main/design-system/colors.md
```

## Step 2: Fetch the email template references

```
https://github.com/socialplus-tools/marketing-team/blob/main/emails/product-update-newsletter.md
https://github.com/socialplus-tools/marketing-team/blob/main/emails/emails.md
```

`product-update-newsletter.md` contains the HTML component library, MailerLite merge tags, responsive patterns, tier-to-layout mapping, and the complete base template. Follow it exactly when generating HTML.

`emails.md` contains email content strategy — subject line rules, body structure, CTA best practices, and email type guidelines. Apply these when writing the email copy.

## Step 3: Determine email type

Look at Bam's source document to identify which type of email to generate:

- **Monthly Product Update** — Multiple features across tiers, subject line pattern "What's New in [month year]", has Newsletter section with tiered features. Use the "Assembly Order: Monthly Product Update" from reference.md.
- **Feature Launch Announcement** — Single major feature with sub-features, subject line focuses on one launch (e.g., "Events is now live"), no tier structure. Use the "Assembly Order: Feature Launch Announcement" from reference.md.

## Step 4: Parse the input

Bam's source document is a Google Doc (or pasted text from one).

### For Monthly Product Updates:

The Newsletter section uses a **tiered feature system**:

- **Tier 1** — Lead feature. Has: title, full description, image placeholder, "Learn more" CTA link.
- **Tier 2** — Secondary features. Has: title, product module tag, full description, image placeholder, "Learn more" CTA link.
- **Tier 3** — Smaller features. Has: title, product module tag, image placeholder, short description (max 280 chars), documentation link.
- **Tier 4** — Brief mentions. Has: product module tag, title only. No images, no descriptions.

The doc also contains Website, Video, and Product Activation sections — **ignore everything outside the Newsletter section.**

If the user shares a Google Doc link, use the google_drive_fetch tool to read it. If they paste text, parse it directly.

Extract from the Newsletter section:
1. The subject line (from the heading pattern "What's New in [month year]: [highlights]")
2. The opening remark paragraph
3. Each tiered feature with its title, description, module tag, image reference, and link
4. The closing remark

### For Feature Launch Announcements:

Extract:
1. The subject line (feature launch headline)
2. The hero image description
3. The feature title and description
4. Sub-features (each with: title, short description, image reference)
5. CTA link (full announcement page)
6. The closing remark

## Step 5: Generate the HTML

Follow all patterns from the email template reference file. Use the correct assembly order for the email type.

Key requirements:

- Use embedded `<style>` block for CSS — MailerLite's automatic CSS inliner converts it to inline styles, preserving only `@media` queries for responsive behavior
- Single responsive breakpoint: `@media all and (max-width:789px)` (750px content + scrollbar buffer)
- Outlook conditional comments for font-family and PixelsPerInch
- iOS blue link fix (`a[x-apple-data-detectors]`) and Android center fix
- `role="presentation"` on all layout tables
- 750px max content width
- Inter font with system fallbacks
- Brand colors as hardcoded hex values (not CSS custom properties — email clients don't support them)
- Per-module color accents for category badges
- MailerLite merge tags: `{$unsubscribe}`, `{$url}`, `{$preferences}`
- Visible `placehold.co` placeholder images with labeled colored boxes at correct dimensions (see reference file for format)
- Map tiers to the correct layout components from the reference file
- Feature images use `.img-rounded` CSS class (`border-radius:16px` desktop, `12px` mobile) — never bake border-radius into images
- Closing text uses `font-weight:600` (semi-bold)
- Dark mode support: include `<meta name="color-scheme" content="light dark">` and `<meta name="supported-color-schemes" content="light dark">` meta tags, `:root { color-scheme: light dark; }`, `@media (prefers-color-scheme: dark)` block with all override classes, plus `[data-ogsc]` and `[data-ogsb]` Outlook selectors
- Dark mode CSS classes on all HTML elements: `body-bg` on wrapper tables and body, `container-bg` on content tables, `text-dark`/`text-body`/`text-secondary` on text, `link-brand` on links, `footer-border` on footer table, `preheader-ghost` on hidden preheader
- Logo swap: include both `logo-light` (default dark logo) and `logo-dark` (white logo, hidden by default) images in header, wrapped in MSO conditional comments

## Step 6: Run compliance check and deliver

Run the compliance check from `brain.md` before delivering. Pay special attention to terminology in email subject lines and CTAs — these are high-visibility.

Output the complete HTML in a single code block. If the email is long, also save it as an `.html` file so the user can preview it in a browser before pasting into MailerLite.

Remind the user to:
1. Paste the HTML into MailerLite's custom HTML editor
2. Upload screenshots to MailerLite's media library, then replace each `placehold.co` URL with the MailerLite CDN URL — the colored placeholder boxes show exactly which image goes where
3. **Export all images as flat rectangles** — no border-radius, no borders, no shadows baked in. The HTML applies border-radius via CSS.
4. **Upload a white version of the social.plus logo** to MailerLite and replace `REPLACE_WITH_WHITE_LOGO.png` in the header with the actual MailerLite CDN URL (needed for dark mode logo swap)
5. Preview in MailerLite using Preview and Test before sending — check both light and dark mode rendering
6. Enable "Automatic CSS inline" in MailerLite's Settings tab

## Important: URL format

**Always use `github.com/.../blob/...` URLs when fetching files.** The `raw.githubusercontent.com` domain is blocked by network egress settings.
