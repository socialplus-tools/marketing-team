# social.plus Email Templates

Read this file before creating any email — marketing campaigns, newsletters, or
transactional messages — for social.plus.

Also read: `colors.md`, `typography.md`, `tone.md`

---

## Email Design Principles

**Dark-first, but email is the exception.** Most email clients do not reliably support
dark mode CSS. For broad compatibility, social.plus marketing emails use a **dark background**
by default (consistent with brand identity), but include light-mode fallbacks.

The simplest approach: use `#111111` as the email background with white text, which
renders consistently across all major clients.

---

## HTML Email Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Email Subject]</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      background-color: #111111;
      font-family: 'Figtree', 'Inter', Arial, sans-serif;
      color: #ffffff;
    }
    .email-wrapper {
      max-width: 600px;
      margin: 0 auto;
      background-color: #111111;
    }
    .email-header {
      padding: 32px 40px 24px;
      border-bottom: 1px solid rgba(255,255,255,0.15);
    }
    .email-body {
      padding: 40px;
    }
    .email-footer {
      padding: 24px 40px;
      border-top: 1px solid rgba(255,255,255,0.15);
      font-size: 12px;
      color: #a0a1a3;
    }
    h1 {
      font-size: 32px;
      font-weight: 700;
      line-height: 1.4;
      margin: 0 0 16px;
      color: #ffffff;
    }
    h2 {
      font-size: 24px;
      font-weight: 700;
      line-height: 1.4;
      margin: 0 0 12px;
      color: #ffffff;
    }
    p {
      font-size: 16px;
      line-height: 1.6;
      margin: 0 0 16px;
      color: #d0d0d1;
    }
    .cta-button {
      display: inline-block;
      background-color: #3B41EC;
      color: #ffffff !important;
      font-family: 'Figtree', 'Inter', Arial, sans-serif;
      font-size: 16px;
      font-weight: 700;
      text-decoration: none;
      padding: 14px 28px;
      border-radius: 8px;
      margin: 16px 0;
    }
    .cta-button:hover {
      background-color: #3769EC;
    }
    .gradient-bar {
      height: 4px;
      background: linear-gradient(to right, #3769EC, #3B41EC 50.5%, #45A5ED);
    }
    .highlight {
      color: #3B41EC;
    }
  </style>
</head>
<body>
  <div class="email-wrapper">
    <!-- Gradient accent bar at top -->
    <div class="gradient-bar"></div>

    <!-- Header with logo -->
    <div class="email-header">
      <!-- Logo: use white SVG/PNG version of social.plus full name logo -->
      <img src="[LOGO_URL]" alt="social.plus" height="28" />
    </div>

    <!-- Main body -->
    <div class="email-body">
      <h1>[Headline]</h1>
      <p>[Body copy — direct, warm, specific]</p>
      <a href="[CTA_URL]" class="cta-button">[CTA Text]</a>
    </div>

    <!-- Footer -->
    <div class="email-footer">
      <p>© 2026 social.plus. All rights reserved.</p>
      <p>
        <a href="#" style="color: #a0a1a3;">Unsubscribe</a> ·
        <a href="#" style="color: #a0a1a3;">Privacy Policy</a> ·
        <a href="#" style="color: #a0a1a3;">Terms</a>
      </p>
    </div>
  </div>
</body>
</html>
```

---

## Email Content Guidelines

### Subject lines
- 40–50 characters is ideal for mobile preview
- Lead with the value or hook — front-load the most important word
- Avoid spam trigger words: "FREE", "Act now", all-caps, multiple exclamation marks
- Emojis can increase open rates when used tastefully (one max per subject line)

**Examples of strong subject lines:**
- "Your community just got a lot smarter"
- "New: Webhooks for every event"
- "[First name], here's what's new in March"
- "We built this based on your feedback"

### Preview text (preheader)
- 80–100 characters
- Complements the subject, doesn't repeat it
- Should make the reader curious enough to open

### Email body structure

1. **Hook** (1–2 sentences): Why are you emailing right now? Make it worth their time.
2. **Value** (2–4 sentences or a short list): What's the substance? Be specific.
3. **CTA** (one primary action): One clear next step. Do not give multiple equal CTAs.
4. **Secondary info** (optional): Additional context, links, or social proof.

### CTA best practices
- One primary CTA per email
- Use action verbs: "Start building", "See the demo", "Read the guide", "Join now"
- Button colour: Ultramarine `#3B41EC`
- Keep button text under 5 words

---

## Email Types

### Newsletter
- Clear sections with sub-headings
- Mix of: product news, community spotlight, useful resources
- Consistent rhythm — readers should know what to expect each edition

### Transactional (password reset, receipt, onboarding)
- Ultra-clear and efficient
- No marketing language
- The key information (link, code, confirmation) should be visually prominent
- Minimal design — just enough brand presence to be recognisable

### Campaign / promotional
- Strong headline that states the value proposition
- Urgency or exclusivity if genuine (not manufactured)
- One CTA, one goal
