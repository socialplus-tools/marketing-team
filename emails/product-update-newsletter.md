# social.plus Email HTML Templates — Reference

Complete HTML component library and MailerLite-specific conventions for social.plus marketing emails. Follow this exactly when generating email HTML.

## Table of Contents

1. [MailerLite Technical Requirements](#mailerlite-technical-requirements)
2. [Brand Colors for Email](#brand-colors-for-email)
3. [Module Color Accents](#module-color-accents)
4. [Typography](#typography)
5. [MailerLite Merge Tags](#mailerlite-merge-tags)
6. [Base Template Shell](#base-template-shell)
7. [Component: Preheader](#component-preheader)
8. [Component: Header](#component-header)
9. [Component: Intro Text](#component-intro-text)
10. [Component: Hero Image](#component-hero-image)
11. [Component: Body Intro](#component-body-intro)
12. [Component: Tier 1 Feature](#component-tier-1-feature)
13. [Component: Tier 2 Feature](#component-tier-2-feature)
14. [Component: Tier 3 Feature Row](#component-tier-3-feature-row)
15. [Component: Tier 4 List](#component-tier-4-list)
16. [Component: Divider](#component-divider)
17. [Component: CTA Button](#component-cta-button)
18. [Component: Closing Text](#component-closing-text)
19. [Component: Footer](#component-footer)
20. [Assembly Order: Monthly Product Update](#assembly-order-monthly-product-update)
21. [Assembly Order: Feature Launch Announcement](#assembly-order-feature-launch-announcement)
22. [Dark Mode Support](#dark-mode-support)
23. [Image Preparation](#image-preparation)
24. [Image Placeholder Convention](#image-placeholder-convention)
25. [Checklist Before Delivery](#checklist-before-delivery)

---

## MailerLite Technical Requirements

These come directly from MailerLite's documentation and are non-negotiable:

**CSS strategy:** Use an embedded `<style>` block in `<head>`. MailerLite's automatic CSS inliner converts embedded styles to inline, preserving only `@media` queries. Enable "Automatic CSS inline" in the Settings tab when editing.

**Responsive approach:** Use a single `@media all and (max-width:789px)` breakpoint (750px content width + scrollbar buffer). Define responsive utility classes (`.container`, `.row`, `.mobile-stack`, `.mobile-hide`) that override fixed widths on small screens.

**Layout:** Table-based only. Use `<table>`, `<tr>`, `<td>` with `role="presentation"` for accessibility. Never rely on `<div>` for structural layout.

**Outlook support:** Include conditional comments for `<!--[if mso]>` to force font-family and set PixelsPerInch to 96. Use VML `<v:roundrect>` fallback for rounded buttons.

**Device fixes:**
- iOS: `a[x-apple-data-detectors]` to prevent blue link styling
- Android: `div[style*="margin: 16px 0"]` center fix
- Meta tags: `format-detection` to prevent auto-linking phone numbers/dates

**Width:** 750px max content width. Collapses to 100% on mobile via media queries.

**Images:** Always set explicit `width` attribute, use `style="display:block;"`, include meaningful `alt` text.

**Footer requirements:** Must include visible `{$unsubscribe}` link (mandatory for MailerLite delivery). Should include `{$preferences}` link.

---

## Brand Colors for Email

Hardcoded hex values only — email clients do not support CSS custom properties.

| Role | Light Hex | Dark Hex | Usage |
|------|-----------|----------|-------|
| Brand Blue | `#3b41ec` | `#7b7fff` | CTA buttons, header button border, links |
| Blue Hover | `#272b9d` | — | Button hover (in `<style>` block only) |
| Page Background | `#f5f5f5` | `#1a1a1a` | `<body>` and outer wrapper |
| Content Background | `#ffffff` | `#2d2d2d` | Content area cells |
| Alt Section Background | `#f9f9f9` | `#2d2d2d` | Tier 3 feature section, divider areas |
| Footer Background | `#ffffff` | `#2d2d2d` | Footer (with top border) |
| Heading Text | `#111111` | `#f0f0f0` | Headings, footer brand name |
| Body Text | `#414347` | `#e0e0e0` | Paragraph text |
| Secondary Text | `#717275` | `#a0a0a3` | Module tags, preheader, captions, footer text |
| Muted Text | `#b3b3b3` | `#555555` | Footer separator pipe |
| White | `#ffffff` | — | Button text, social icon text (X) |
| Border | `#e7e7e7` | `#444444` | Divider lines, footer top border |
| Footer Link | `#3b41ec` | `#7b7fff` | Unsubscribe/preferences links |

---

## Module Color Accents

Each product module has a background/text color pair used for category badges in the email. Apply as a small inline badge next to feature headings when the module tag is present.

| Module | Background | Text/Accent |
|--------|-----------|-------------|
| Console | `#e8deff` | `#c5aaff` |
| UI Kit | `#fff4d9` | `#f7c506` |
| Chat | `#e8f9f5` | `#1dc497` |
| Video | `#fff4d9` | `#ffd500` |
| Analytics | `#8abfff` | `#222222` |
| Social | `#ffe9ed` | `#ff456b` |
| Flutter | `#fff1f0` | `#ff5a36` |
| React Native | `#d6ede2` | `#084c41` |

Badge HTML pattern (place after the heading text):
```html
<span style="display:inline-block; padding:2px 8px; border-radius:4px; background-color:MODULE_BG; color:MODULE_TEXT; font-size:12px; font-weight:600; line-height:18px; margin-left:8px; vertical-align:middle;">Module Name</span>
```

---

## Typography

```
font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
```

| Element | Size | Weight | Color | Line-height |
|---------|------|--------|-------|-------------|
| H1 (email title) | 28px | 700 | `#111111` | 36px |
| H2 (section heading) | 22px | 700 | `#111111` | 30px |
| H3 (feature name) | 18px | 700 | `#111111` | 26px |
| Module tag label | 13px | 600 | `#717275` | 18px |
| Body text | 16px | 400 | `#414347` | 26px |
| Small text | 14px | 400 | `#717275` | 22px |
| Button text | 16px | 600 | `#ffffff` | 20px |
| Outlined button | 14px | 600 | `#3b41ec` | 20px |
| Footer heading | 16px | 700 | `#111111` | 24px |
| Footer text | 14px | 400 | `#717275` | 22px |

---

## MailerLite Merge Tags

| Tag | Purpose | Required? |
|-----|---------|-----------|
| `{$unsubscribe}` | Unsubscribe URL | Yes (mandatory) |
| `{$preferences}` | Update preferences URL | Recommended |
| `{$url}` | View-in-browser URL | Recommended |
| `{$name}` | Subscriber's first name | Optional |
| `{$email}` | Subscriber's email | Optional |

---

## Base Template Shell

Every email starts with this HTML wrapper. Place all components inside `<body>`.

```html
<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=yes">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="format-detection" content="telephone=no, date=no, address=no, email=no, url=no">
  <meta name="x-apple-disable-message-reformatting">
  <meta name="color-scheme" content="light dark">
  <meta name="supported-color-schemes" content="light dark">
  <title>{{EMAIL_TITLE}}</title>

  <!--[if !mso]>-->
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <!--<![endif]-->

  <!--[if mso]>
  <style>
    * { font-family: sans-serif !important; }
  </style>
  <noscript>
    <xml>
      <o:OfficeDocumentSettings>
        <o:PixelsPerInch>96</o:PixelsPerInch>
      </o:OfficeDocumentSettings>
    </xml>
  </noscript>
  <![endif]-->

  <style type="text/css">
    /* RESET STYLES — MailerLite CSS inliner will convert these to inline */
    html, body {
      margin: 0 !important;
      padding: 0 !important;
      width: 100% !important;
      height: 100% !important;
    }
    body {
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      text-rendering: optimizeLegibility;
      background-color: #f5f5f5;
    }
    img {
      border: 0;
      outline: none;
      text-decoration: none;
      -ms-interpolation-mode: bicubic;
    }
    table, td, a {
      -webkit-text-size-adjust: 100%;
      -ms-text-size-adjust: 100%;
    }
    h1, h2, h3, h4, h5, p {
      margin: 0;
      word-break: break-word;
    }

    /* iOS BLUE LINKS */
    a[x-apple-data-detectors] {
      color: inherit !important;
      text-decoration: none !important;
      font-size: inherit !important;
      font-family: inherit !important;
      font-weight: inherit !important;
      line-height: inherit !important;
    }

    /* ANDROID CENTER FIX */
    div[style*="margin: 16px 0;"] {
      margin: 0 !important;
    }

    /* IMAGE BORDER RADIUS — Bam exports flat images, HTML applies radius */
    .img-rounded {
      border-radius: 16px;
    }

    /* BUTTON HOVER */
    .btn-primary:hover {
      background-color: #272b9d !important;
    }
    .btn-outline:hover {
      background-color: #3b41ec !important;
      color: #ffffff !important;
    }

    /* RESPONSIVE — preserved by MailerLite CSS inliner */
    @media all and (max-width: 789px) {
      .container {
        width: 100% !important;
        min-width: 100% !important;
        padding: 0 !important;
      }
      .row {
        padding-left: 20px !important;
        padding-right: 20px !important;
      }
      .mobile-stack {
        display: block !important;
        width: 100% !important;
        max-width: 100% !important;
      }
      .mobile-stack img {
        width: 100% !important;
        height: auto !important;
        margin-bottom: 16px !important;
      }
      .mobile-hide {
        display: none !important;
      }
      .mobile-center {
        text-align: center !important;
      }
      .mobile-full-width {
        width: 100% !important;
      }
      .mobile-padding {
        padding-left: 20px !important;
        padding-right: 20px !important;
      }
      /* Header button stacking */
      .header-cell {
        display: block !important;
        width: 100% !important;
        text-align: center !important;
      }
      .header-cell-btn {
        display: block !important;
        width: 100% !important;
        text-align: center !important;
        padding-top: 12px !important;
      }
      .btn-outline {
        font-size: 13px !important;
        padding: 8px 16px !important;
      }
      .mobile-mt-20 {
        margin-top: 20px !important;
      }
      .img-rounded {
        border-radius: 12px !important;
      }
    }
    /* Single breakpoint at 789px covers 750px content + scrollbar buffer */

    /* DARK MODE — Apple Mail, iOS Outlook, Outlook macOS */
    :root {
      color-scheme: light dark;
      supported-color-schemes: light dark;
    }
    @media (prefers-color-scheme: dark) {
      .body-bg { background-color: #1a1a1a !important; }
      .container-bg { background-color: #2d2d2d !important; }
      .text-dark { color: #f0f0f0 !important; }
      .text-body { color: #e0e0e0 !important; }
      .text-secondary { color: #a0a0a3 !important; }
      .link-muted { color: #a0a0a3 !important; }
      .link-brand { color: #7b7fff !important; }
      .footer-border { border-top-color: #444444 !important; }
      .footer-separator { color: #555555 !important; }
      .btn-outline { border-color: #7b7fff !important; color: #7b7fff !important; }
      .logo-light { display: none !important; }
      .logo-dark { display: block !important; }
      .preheader-ghost { color: #1a1a1a !important; }
    }

    /* DARK MODE — Outlook Android */
    [data-ogsc] .text-dark { color: #f0f0f0 !important; }
    [data-ogsc] .text-body { color: #e0e0e0 !important; }
    [data-ogsc] .text-secondary { color: #a0a0a3 !important; }
    [data-ogsc] .link-brand { color: #7b7fff !important; }
    [data-ogsc] .logo-light { display: none !important; }
    [data-ogsc] .logo-dark { display: block !important; }

    /* DARK MODE — Outlook.com */
    [data-ogsb] .body-bg { background-color: #1a1a1a !important; }
    [data-ogsb] .container-bg { background-color: #2d2d2d !important; }
    [data-ogsb] .logo-light { display: none !important; }
    [data-ogsb] .logo-dark { display: block !important; }
  </style>
</head>
<body class="body-bg" style="margin:0; padding:0; background-color:#f5f5f5; -webkit-text-size-adjust:none; -ms-text-size-adjust:none;">
  <!-- EMAIL CONTENT GOES HERE -->
</body>
</html>
```

---

## Component: Preheader

Hidden preview text + visible preheader bar with "View in browser" link.

```html
<!-- Hidden preheader text -->
<div class="preheader-ghost" style="display:none; max-height:0px; overflow:hidden; font-size:0px; line-height:0px; color:#f5f5f5;">
  {{PREHEADER_TEXT}} &#847; &#847; &#847; &#847; &#847; &#847; &#847; &#847; &#847; &#847; &#847; &#847; &#847; &#847; &#847; &#847; &#847; &#847; &#847; &#847;
</div>

<!-- Visible preheader bar -->
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" class="body-bg" style="background-color:#f5f5f5;">
  <tr>
    <td align="center" style="padding:10px 0;">
      <table role="presentation" class="container" width="750" cellpadding="0" cellspacing="0" border="0">
        <tr>
          <td class="row text-secondary" align="left" style="font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif; font-size:13px; color:#717275; line-height:20px; padding:0 40px;">
            {{PREHEADER_TEXT}}
          </td>
          <td class="row" align="right" style="font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif; font-size:13px; line-height:20px; padding:0 40px; white-space:nowrap;">
            <a href="{$url}" class="link-muted" style="color:#414347; text-decoration:underline;">View in browser</a>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
```

---

## Component: Header

Logo left, outlined CTA button right.

```html
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" class="body-bg" style="background-color:#f5f5f5;">
  <tr>
    <td align="center">
      <table role="presentation" class="container container-bg" width="750" cellpadding="0" cellspacing="0" border="0" style="background-color:#ffffff;">
        <tr>
          <td class="row" style="padding:24px 40px;">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
              <tr>
                <td class="header-cell" align="left" valign="middle">
                  <a href="https://social.plus" target="_blank">
                    <!--[if !mso]><!-- Dark mode: light logo (hidden by default, shown in dark) -->
                    <img class="logo-dark" src="{{LOGO_WHITE_URL}}" alt="social.plus" width="140" style="display:none; border:0;" />
                    <!-- Light mode: dark logo (shown by default, hidden in dark) -->
                    <!--<![endif]-->
                    <img class="logo-light" src="{{LOGO_URL}}" alt="social.plus" width="140" style="display:block; border:0;" />
                  </a>
                </td>
                <td class="header-cell-btn" align="right" valign="middle" style="white-space:nowrap;">
                  <a href="{{HEADER_CTA_URL}}" target="_blank" class="btn-outline" style="display:inline-block; padding:10px 10px; border:2px solid #3b41ec; border-radius:6px; font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif; font-size:14px; font-weight:600; color:#3b41ec; text-decoration:none; line-height:20px; white-space:nowrap;">{{HEADER_CTA_TEXT}}</a>
                </td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
```

Default values: `{{HEADER_CTA_TEXT}}` = "Explore All Updates", `{{HEADER_CTA_URL}}` = "https://social.plus/product-updates"

---

## Component: Intro Text

Opening paragraph before the hero image.

```html
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#f5f5f5;" class="body-bg">
  <tr>
    <td align="center">
      <table role="presentation" class="container container-bg" width="750" cellpadding="0" cellspacing="0" border="0" style="background-color:#ffffff;">
        <tr>
          <td class="row" style="padding:24px 40px 24px 40px;">
            <p class="text-body" style="font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif; font-size:16px; font-weight:400; color:#414347; line-height:26px;">{{INTRO_TEXT}}</p>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
```

---

## Component: Hero Image

Full-width monthly product update graphic. Links to the video or product update page.

```html
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#f5f5f5;" class="body-bg">
  <tr>
    <td align="center">
      <table role="presentation" class="container container-bg" width="750" cellpadding="0" cellspacing="0" border="0" style="background-color:#ffffff;">
        <tr>
          <td align="center">
            <a href="{{HERO_LINK}}" target="_blank">
              <img src="{{IMAGE_HERO}}" alt="{{HERO_ALT_TEXT}}" width="750" style="display:block; width:100%; max-width:750px; height:auto; border:0;" />
            </a>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
```

---

## Component: Body Intro

Secondary intro text below the hero — sets context for the features.

Same structure as Intro Text component but with different padding: `padding:24px 40px 8px 40px`.

---

## Component: Tier 1 Feature

Lead feature with full-width screenshot, heading, detailed description, and CTA button. Gets maximum visual weight.

```html
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#f5f5f5;" class="body-bg">
  <tr>
    <td align="center">
      <table role="presentation" class="container container-bg" width="750" cellpadding="0" cellspacing="0" border="0" style="background-color:#f9f9f9;">
        <!-- Full-width feature image -->
        <tr>
          <td align="center" style="padding:32px 0 0 0;">
            <img src="{{IMAGE_TIER1}}" alt="{{FEATURE_ALT}}" width="750" style="display:block; width:100%; max-width:750px; height:auto; border:0;" />
          </td>
        </tr>
        <!-- Feature text -->
        <tr>
          <td class="row" style="padding:24px 40px 8px 40px;">
            <h2 class="text-dark" style="font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif; font-size:22px; font-weight:700; color:#111111; line-height:30px;">{{FEATURE_HEADING}}</h2>
          </td>
        </tr>
        <tr>
          <td class="row" style="padding:0 40px 24px 40px;">
            <p class="text-body" style="font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif; font-size:16px; font-weight:400; color:#414347; line-height:26px;">{{FEATURE_DESCRIPTION}}</p>
          </td>
        </tr>
        <!-- CTA button (outlined) -->
        <tr>
          <td class="row" align="center" style="padding:0 40px 32px 40px;">
            <a href="{{FEATURE_CTA_URL}}" target="_blank" class="btn-outline" style="display:inline-block; padding:10px 24px; border:2px solid #3b41ec; border-radius:6px; font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif; font-size:14px; font-weight:600; color:#3b41ec; text-decoration:none; line-height:20px;">{{FEATURE_CTA_TEXT}}</a>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
```

---

## Component: Tier 2 Feature

Secondary feature. Same visual structure as Tier 1 but on white background to create visual hierarchy distinction.

Same HTML as Tier 1 but with `background-color:#ffffff` instead of `#f9f9f9`. Alternate between `#ffffff` and `#f9f9f9` if there are multiple Tier 2 features to create visual rhythm.

---

## Component: Tier 3 Feature Row

Zigzag layout — image on one side, text on the other. Alternate direction for each row. Maximum 280 characters for description.

**Module tag styling:** Use a separate `<p>` element for the module tag (as shown below), NOT an inline `<span>` inside the `<h3>`. If using an inline badge span, never add `margin-left` — it causes misalignment on mobile.

**Image Left, Text Right:**

```html
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#f5f5f5;" class="body-bg">
  <tr>
    <td align="center">
      <table role="presentation" class="container container-bg" width="750" cellpadding="0" cellspacing="0" border="0" style="background-color:#f9f9f9;">
        <tr>
          <td class="row" style="padding:32px 40px;">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
              <tr>
                <td class="mobile-stack" width="335" valign="top" style="padding-right:20px;">
                  <img class="img-rounded" src="{{IMAGE_TIER3}}" alt="{{FEATURE_ALT}}" width="315" style="display:block; width:315px; height:auto; border:0; border-radius:16px;" />
                </td>
                <td class="mobile-stack" width="335" valign="middle">
                  <h3 class="text-dark" style="font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif; font-size:18px; font-weight:700; color:#111111; line-height:26px; padding-bottom:4px;">{{FEATURE_HEADING}}</h3>
                  <p class="text-secondary" style="font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif; font-size:13px; font-weight:600; color:#717275; line-height:18px; padding-bottom:8px;">{{MODULE_TAG}}</p>
                  <p class="text-body" style="font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif; font-size:16px; font-weight:400; color:#414347; line-height:26px;">{{FEATURE_DESCRIPTION}}</p>
                </td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
```

**Text Left, Image Right:** Same structure but swap the two `<td>` elements. The image cell should have NO left/right padding (remove `padding-left`/`padding-right`). Set `valign="middle"` on the image cell to vertically center it alongside the text.

Alternate direction for each successive Tier 3 feature to create the zigzag pattern.

---

## Component: Tier 4 List

Simple bullet list of feature names with module tags. No images, minimal space.

```html
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#f5f5f5;" class="body-bg">
  <tr>
    <td align="center">
      <table role="presentation" class="container container-bg" width="750" cellpadding="0" cellspacing="0" border="0" style="background-color:#ffffff;">
        <tr>
          <td class="row" style="padding:24px 40px 8px 40px;">
            <p class="text-dark" style="font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif; font-size:16px; font-weight:600; color:#111111; line-height:26px; padding-bottom:12px;">We also added</p>
          </td>
        </tr>
        <tr>
          <td class="row" style="padding:0 40px 24px 40px;">
            <!-- Repeat this block for each Tier 4 item -->
            <p class="text-body" style="font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif; font-size:16px; font-weight:400; color:#414347; line-height:32px;">
              &#8226;&nbsp; <span class="text-secondary" style="font-size:13px; font-weight:600; color:#717275;">{{MODULE_TAG}}</span>&nbsp; {{FEATURE_TITLE}}
            </p>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
```

---

## Component: Divider

Thin line between sections.

```html
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#f5f5f5;" class="body-bg">
  <tr>
    <td align="center">
      <table role="presentation" class="container container-bg" width="750" cellpadding="0" cellspacing="0" border="0" style="background-color:#ffffff;">
        <tr>
          <td style="padding:0 40px;">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
              <tr>
                <td style="border-top:1px solid #e7e7e7; font-size:0; line-height:0; height:1px;">&nbsp;</td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
```

---

## Component: CTA Button

Primary filled button (brand blue). Used sparingly — typically one per email.

```html
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#f5f5f5;" class="body-bg">
  <tr>
    <td align="center">
      <table role="presentation" class="container container-bg" width="750" cellpadding="0" cellspacing="0" border="0" style="background-color:#ffffff;">
        <tr>
          <td align="center" style="padding:32px 40px;">
            <!--[if mso]>
            <v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="{{CTA_URL}}" style="height:48px;v-text-anchor:middle;width:220px;" arcsize="13%" fillcolor="#3b41ec">
              <w:anchorlock/>
              <center style="color:#ffffff;font-family:'Inter',Helvetica,Arial,sans-serif;font-size:16px;font-weight:600;">{{CTA_TEXT}}</center>
            </v:roundrect>
            <![endif]-->
            <!--[if !mso]><!-->
            <a href="{{CTA_URL}}" target="_blank" class="btn-primary" style="display:inline-block; padding:14px 32px; background-color:#3b41ec; border-radius:6px; font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif; font-size:16px; font-weight:600; color:#ffffff; text-decoration:none; line-height:20px; text-align:center;">{{CTA_TEXT}}</a>
            <!--<![endif]-->
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
```

---

## Component: Closing Text

Warm sign-off before the footer.

```html
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#f5f5f5;" class="body-bg">
  <tr>
    <td align="center">
      <table role="presentation" class="container container-bg" width="750" cellpadding="0" cellspacing="0" border="0" style="background-color:#ffffff;">
        <tr>
          <td class="row" style="padding:24px 40px 32px 40px;">
            <p class="text-body" style="font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif; font-size:16px; font-weight:600; color:#414347; line-height:26px; text-align:center;">{{CLOSING_TEXT}}</p>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
```

---

## Component: Footer

Light footer with logo, tagline, social icons, unsubscribe, and preferences links. Separated from content by a top border.

```html
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#f5f5f5;" class="body-bg">
  <tr>
    <td align="center">
      <table role="presentation" class="container container-bg footer-border" width="750" cellpadding="0" cellspacing="0" border="0" style="background-color:#ffffff; border-top:1px solid #e7e7e7;">
        <tr>
          <td class="row" style="padding:32px 40px;">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
              <tr>
                <td class="mobile-stack" width="50%" valign="top">
                  <p class="text-dark" style="font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif; font-size:16px; font-weight:700; color:#111111; line-height:24px; padding-bottom:8px;">social.plus</p>
                  <p class="text-secondary" style="font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif; font-size:14px; font-weight:400; color:#717275; line-height:22px; padding-bottom:16px;">The best version of every app is Social+</p>
                  <!-- Social icons (colored rounded squares with white logos via jsDelivr CDN) -->
                  <div style="padding-bottom:20px;">
                  <table role="presentation" cellpadding="0" cellspacing="0" border="0">
                    <tr>
                      <td style="padding-right:8px;">
                        <a href="https://www.linkedin.com/company/socialpluscorp/" target="_blank" style="display:inline-block; width:36px; height:36px; border-radius:6px; background-color:#0A66C2; text-align:center; line-height:36px; text-decoration:none;"><img src="https://cdn.jsdelivr.net/gh/gauravghongde/social-icons@master/PNG/White/LinkedIN_white.png" alt="LinkedIn" width="20" height="20" style="border:0; vertical-align:middle;" /></a>
                      </td>
                      <td style="padding-right:8px;">
                        <a href="https://www.instagram.com/wearesocial.plus" target="_blank" style="display:inline-block; width:36px; height:36px; border-radius:6px; background-color:#E4405F; text-align:center; line-height:36px; text-decoration:none;"><img src="https://cdn.jsdelivr.net/gh/gauravghongde/social-icons@master/PNG/White/Instagram_white.png" alt="Instagram" width="20" height="20" style="border:0; vertical-align:middle;" /></a>
                      </td>
                      <td style="padding-right:8px;">
                        <a href="https://x.com/socialpluscorp" target="_blank" style="display:inline-block; width:36px; height:36px; border-radius:6px; background-color:#000000; text-align:center; line-height:36px; font-family:'Inter',Helvetica,Arial,sans-serif; font-size:15px; font-weight:700; color:#ffffff; text-decoration:none;">X</a>
                      </td>
                      <td style="padding-right:8px;">
                        <a href="https://www.youtube.com/@wearesocialplus" target="_blank" style="display:inline-block; width:36px; height:36px; border-radius:6px; background-color:#FF0000; text-align:center; line-height:36px; text-decoration:none;"><img src="https://cdn.jsdelivr.net/gh/gauravghongde/social-icons@master/PNG/White/Youtube_white.png" alt="YouTube" width="20" height="20" style="border:0; vertical-align:middle;" /></a>
                      </td>
                      <td>
                        <a href="https://github.com/Amityco" target="_blank" style="display:inline-block; width:36px; height:36px; border-radius:6px; background-color:#333333; text-align:center; line-height:36px; text-decoration:none;"><img src="https://cdn.jsdelivr.net/gh/gauravghongde/social-icons@master/PNG/White/Github_white.png" alt="GitHub" width="20" height="20" style="border:0; vertical-align:middle;" /></a>
                      </td>
                    </tr>
                  </table>
                  </div>
                </td>
                <td class="mobile-stack" width="50%" valign="top" align="left" style="text-align:left;">
                  <p class="text-secondary" style="font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif; font-size:14px; font-weight:400; color:#717275; line-height:22px; padding-bottom:24px; text-align:left;">If you no longer wish to receive this newsletter, you can unsubscribe here:</p>
                  <p style="font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif; font-size:14px; line-height:22px; text-align:left;">
                    <a href="{$unsubscribe}" class="link-brand" style="color:#3b41ec; text-decoration:underline;">Unsubscribe</a>
                    <span class="footer-separator" style="color:#b3b3b3; padding:0 8px;">|</span>
                    <a href="{$preferences}" class="link-brand" style="color:#3b41ec; text-decoration:underline;">Update preferences</a>
                  </p>
                </td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
```

---

## Assembly Order: Monthly Product Update

Build the email by stacking components in this order:

1. **Base Template Shell** (wraps everything)
2. **Preheader** (hidden preview text + "View in browser")
3. **Header** (logo + "Explore All Updates" button)
4. **Intro Text** (opening remark from the doc)
5. **Hero Image** (monthly product update graphic)
6. **Body Intro** (contextual paragraph setting up the features)
7. **Tier 1 Feature(s)** — if present
8. **Tier 2 Feature(s)** — if present, separated by Dividers
9. **Tier 3 Feature Rows** — if present, alternating zigzag direction
10. **Tier 4 List** — if present
11. **Closing Text** (from the doc's closing remarks)
12. **Footer** (light, with social icons + unsubscribe)

Not every tier needs to be present. The skill should include only the tiers that appear in Bam's source doc.

---

## Assembly Order: Feature Launch Announcement

For single-feature launch emails (e.g., "Events is now live on social.plus"). Use when Bam's doc focuses on one major feature with sub-features rather than a monthly roundup.

1. **Base Template Shell** (wraps everything)
2. **Preheader** (hidden preview text + "View in browser")
3. **Header** (logo + CTA button — e.g., "Visit Website")
4. **Hero Image** (full-width feature launch graphic, 750×425)
5. **Feature Title** — centered H1 heading with the launch headline
6. **Feature Description** — 1-2 paragraphs explaining the feature
7. **Section Heading** — e.g., "What's included" (centered H2, `font-size:22px; font-weight:700`)
8. **Tier 3 Feature Rows** — zigzag layout for sub-features (alternating image/text direction)
9. **CTA Button** — primary filled button (e.g., "See full announcement")
10. **Hero Image** (optional — secondary graphic, video thumbnail, or recap image)
11. **Closing Text** (semi-bold, centered)
12. **Footer** (light, with social icons + unsubscribe)

Key differences from Monthly Product Update: no tiers 1/2/4, no Body Intro, the Hero acts as the launch visual, sub-features use Tier 3 zigzag layout, and there may be a secondary image/video embed after the CTA.

---

## Dark Mode Support

The templates include full dark mode support for email clients that honor `prefers-color-scheme`. MailerLite's CSS inliner preserves `@media` queries, so all dark mode styles survive delivery.

**How it works:**

Three layers of dark mode targeting:
1. `@media (prefers-color-scheme: dark)` — Apple Mail (iOS + macOS), Outlook macOS, iOS Outlook
2. `[data-ogsc]` attribute selectors — Outlook Android app (text color overrides)
3. `[data-ogsb]` attribute selectors — Outlook.com (background overrides)

Gmail ignores all three and applies its own forced color inversion. The `<meta name="color-scheme" content="light dark">` and `<meta name="supported-color-schemes" content="light dark">` meta tags signal dark mode awareness, which reduces Gmail's aggressive inversion artifacts.

**Dark mode CSS classes (add to HTML elements):**

| Class | Target | Light mode value | Dark mode value |
|-------|--------|-----------------|----------------|
| `body-bg` | Outer wrapper tables, `<body>` | `#f5f5f5` | `#1a1a1a` |
| `container-bg` | Content container tables | `#ffffff` / `#f9f9f9` | `#2d2d2d` |
| `text-dark` | Headings, footer brand name | `#111111` | `#f0f0f0` |
| `text-body` | Body paragraphs, closing text | `#414347` | `#e0e0e0` |
| `text-secondary` | Preheader, captions, footer text | `#717275` | `#a0a0a3` |
| `link-muted` | "View in browser" link | `#414347` | `#a0a0a3` |
| `link-brand` | Unsubscribe, preferences, learn more | `#3b41ec` | `#7b7fff` |
| `footer-border` | Footer container top border | `#e7e7e7` | `#444444` |
| `footer-separator` | Pipe between footer links | `#b3b3b3` | `#555555` |
| `preheader-ghost` | Hidden preheader text | `#f5f5f5` | `#1a1a1a` |
| `logo-light` | Default (dark) logo | `display:block` | `display:none` |
| `logo-dark` | White logo for dark backgrounds | `display:none` | `display:block` |

**Logo swap:**

Two logo images are embedded in the header — the dark logo (default, visible) and a white logo (hidden by default). In dark mode, CSS swaps visibility. The white logo is wrapped in `<!--[if !mso]>` conditional comments to prevent Outlook Desktop from showing both.

```html
<a href="https://social.plus" target="_blank">
  <!--[if !mso]><!-- -->
  <img class="logo-dark" src="{{LOGO_WHITE_URL}}" alt="social.plus" width="140" style="display:none; border:0;" />
  <!--<![endif]-->
  <img class="logo-light" src="{{LOGO_URL}}" alt="social.plus" width="140" style="display:block; border:0;" />
</a>
```

**Logo URLs:**
- Light mode (dark text): `https://storage.mlcdn.com/account_image/958330/0OpCmydxj01SEFXO54Jr1WOrPLK15IhrfL3CzQdj.png`
- Dark mode (white text): Bam must upload a white version to MailerLite and replace `REPLACE_WITH_WHITE_LOGO.png` with the actual URL

**What doesn't need overrides:**
- CTA primary button (`#3b41ec` bg + white text) — works on both light and dark
- Social icon colored squares (LinkedIn blue, Instagram pink, etc.) — high saturation survives inversion
- Feature screenshots — images render as-is in both modes
- Module badge colors — the colored backgrounds remain readable

**Gmail behavior:** Gmail ignores `prefers-color-scheme` entirely and applies its own auto-dark-mode. It inverts light backgrounds to dark and adjusts text colors. The meta tags help reduce the most aggressive inversions but you cannot fully control Gmail's rendering.

---

## Image Preparation

**Critical rule: Bam must export all images as flat rectangles — no border-radius, no borders, no shadows baked into the image file.** The HTML template applies `border-radius: 16px` on desktop and `12px` on mobile via the `.img-rounded` CSS class. If images have baked-in rounded corners or borders, they will double up with the CSS border-radius and create a visible artifact (white edge/gap).

**Checklist for Bam before uploading images to MailerLite:**

1. Export screenshots as flat PNG or JPEG — no rounded corners, no drop shadows, no border
2. Crop tightly to the content area — no extra whitespace or transparent padding
3. Test the image on both white (`#ffffff`) and light gray (`#f9f9f9`) backgrounds to ensure no visible edge artifacts
4. Use the correct dimensions: 750×425 for hero/Tier 1, 670×385 for Tier 2, 315×210 for Tier 3
5. File format: PNG for UI screenshots (sharp edges), JPEG for photos (smaller size)

**Border-radius is handled by CSS, not the image.** The `.img-rounded` class applies `border-radius:16px` on desktop, overridden to `12px` on mobile via the media query. Full-width images (hero, Tier 1) have no border-radius — they go edge-to-edge. Only Tier 2 and Tier 3 feature images get rounded corners.

---

## Image Placeholder Convention

Use visible `placehold.co` placeholder images so Bam can visually identify and swap each image in MailerLite's media manager after pasting the HTML. Each placeholder shows a labeled colored box at the correct dimensions.

**Format:** `https://placehold.co/{WIDTH}x{HEIGHT}/{BG_HEX}/{TEXT_HEX}?text={LABEL}`

**Standard placeholders:**

| Slot | Dimensions | Example URL |
|------|-----------|-------------|
| Hero image | 750×425 | `https://placehold.co/750x425/e8eaff/3b41ec?text=HERO+IMAGE` |
| Tier 1 feature | 750×425 | `https://placehold.co/750x425/e8eaff/3b41ec?text=FEATURE+NAME` |
| Tier 2 feature | 670×385 | `https://placehold.co/670x385/e8eaff/3b41ec?text=FEATURE+NAME` |
| Tier 3 feature | 315×210 | `https://placehold.co/315x210/e8eaff/3b41ec?text=FEATURE+NAME` |

**Rules:**
- Replace `FEATURE+NAME` with the actual feature name in URL-encoded format (spaces as `+`)
- Use brand light purple `e8eaff` background with brand blue `3b41ec` text for all placeholders
- Always include meaningful `alt` text on the `<img>` tag describing what screenshot to insert
- The logo URL is hardcoded (not a placeholder): `https://storage.mlcdn.com/account_image/958330/0OpCmydxj01SEFXO54Jr1WOrPLK15IhrfL3CzQdj.png`
- Social media icons use colored rounded squares with white PNG logos from jsDelivr CDN (`cdn.jsdelivr.net/gh/gauravghongde/social-icons@master/PNG/White/`). X uses text fallback since no updated icon exists. Each icon is 20×20px inside a 36×36px colored rounded square. The social icons container has 20px bottom padding for spacing.

**Swap workflow:** After pasting HTML into MailerLite's custom HTML editor, Bam uses MailerLite's media library to upload the real screenshots, then replaces each `placehold.co` URL with the MailerLite-hosted CDN URL.

---

## Checklist Before Delivery

Verify before giving the HTML to the user:

- [ ] All copy follows terminology.md rules
- [ ] Tone matches tone.md guidelines
- [ ] All colors are hardcoded hex from brand palette
- [ ] Table-based layout with `role="presentation"` throughout
- [ ] Embedded `<style>` block present (not all-inline)
- [ ] Single responsive breakpoint at 789px
- [ ] Outlook conditional comments in `<head>`
- [ ] iOS blue link fix and Android center fix present
- [ ] `{$unsubscribe}` in footer (mandatory)
- [ ] `{$url}` in preheader "View in browser" link
- [ ] `{$preferences}` in footer
- [ ] All images have alt text
- [ ] Image placeholders use `placehold.co` with labeled colored boxes at correct dimensions
- [ ] 750px max content width
- [ ] VML fallback on primary CTA button (if used)
- [ ] Module color badges applied where tags are present
- [ ] Tiers correctly mapped to layout components
- [ ] Preheader text matches email subject/purpose
- [ ] Feature images use `class="img-rounded"` with inline `border-radius:16px` fallback
- [ ] Images are flat exports (no baked-in border-radius, borders, or shadows)
- [ ] Closing text uses `font-weight:600` (semi-bold)
- [ ] Dark mode meta tags present (`color-scheme`, `supported-color-schemes`)
- [ ] Dark mode `@media (prefers-color-scheme: dark)` block with all class overrides
- [ ] `[data-ogsc]` and `[data-ogsb]` Outlook dark mode selectors present
- [ ] All wrapper tables have `class="body-bg"`
- [ ] All container tables have `container-bg` in class list
- [ ] Text elements have appropriate dark mode classes (`text-dark`, `text-body`, `text-secondary`)
- [ ] Brand links have `class="link-brand"`
- [ ] Logo swap: both `logo-light` and `logo-dark` images in header
- [ ] Footer table has `footer-border` class
- [ ] `body` tag has `class="body-bg"`
