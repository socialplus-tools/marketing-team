---
name: case-study
description: >
  Write customer stories for social.plus following the exact Webflow CMS structure.
  Use this skill for: customer stories, case studies, customer success stories,
  customer spotlights, testimonial write-ups, or any content that tells the story
  of how a customer uses social.plus. Also trigger when the user wants to create
  or update a customer story CMS item in Webflow, or when they provide customer
  data, interview notes, or sales call notes and want them turned into a publishable
  customer story. Trigger on phrases like "case study", "customer story", "success
  story", "customer spotlight", "write about how [customer] uses", "write a CS for",
  or "new customer story."
  Do NOT trigger for general blog posts without a customer focus (use blog-seo-content).
---

# social.plus Customer Stories

This skill produces customer stories that match the exact structure of the social.plus website. The output maps directly to the Webflow CMS collection fields so content can be pasted into the CMS without reformatting.

## What to do

1. Fetch the main brain for cross-domain routing, precedence rules, and the compliance check:
```
https://github.com/socialplus-tools/marketing-team/blob/main/brain.md
```

2. Fetch the messaging router:
```
https://github.com/socialplus-tools/marketing-team/blob/main/messaging/brain.md
```

3. Follow the messaging router's **"Long-form content"** routing. This loads:
   - `terminology.md` + `tone.md` (always)
   - `narrative.md` (messaging hierarchy and narrative structure)
   - `value-story.md` (value creation model — maps directly to customer story outcomes)
   - `positioning.md` (product pillars for framing the solution)

4. Also follow **"Short-form content"** routing for:
   - `boilerplates.md` (company descriptions for reference)

## Webflow CMS field mapping

Every customer story is a CMS item in the `💼 Customer Stories` collection. When writing a customer story, produce content for each of these fields. Present each field clearly labeled so the user can paste directly into Webflow.

### Required fields

**Name Company** (`name`, PlainText)
The customer's company name. This is the CMS item name.

**Slug** (`slug`, PlainText)
URL-safe slug. Lowercase, hyphens, no spaces. Example: `smart-fit`, `the-ring-magazine`.

### Hero section

**Hero Title** (`title`, PlainText)
Pattern: "How [Company] [past-tense verb] [outcome] with social.plus"
Examples from the live site:
- "How Smart Fit built a digital fitness community with social.plus"
- "How Talkspace is strengthening teen mental health support with social.plus"
- "How Snai elevated user engagement by integrating social.plus"
- "How Winner redefined interactive betting experiences using social.plus"

Keep it under 80 characters when possible. The customer's outcome leads — not social.plus's product.

**Hero Introduction Paragraph** (`hero-introduction-paragraph`, PlainText)
One to two sentences that expand on the hero title. Sets the scene for the full story.
Examples:
- "Embedding social features into the Smart Fit app to boost engagement, motivation, and member connection."
- "Winner transformed its platform by integrating powerful social features that fostered connection and engagement among users."

### Metrics (up to 3 boxes)

**Metric Box 1–3** (`numbers-box-1`, `numbers-box-2`, `numbers-box-3`, RichText)
Each metric box uses custom HTML tags for styling. Format:
```html
<p><big-nr>[VALUE]<big-nr><br><cs-number-text>[DESCRIPTION]<cs-number-text></p>
```
Examples:
- `<p><big-nr>60%<big-nr><br><cs-number-text>community growth rate MoM<cs-number-text></p>`
- `<p><big-nr>1.5M<big-nr><br><cs-number-text>Patients<cs-number-text></p>`
- `<p><big-nr>18%<big-nr><br><cs-number-text>Increase in betting rate of casual users<cs-number-text></p>`

Metrics can be: company facts (founded year, employees, revenue), platform stats (users, downloads, locations), or social.plus outcomes (engagement growth, retention lift, integration timeline). Aim for at least 2 boxes. If the user doesn't provide specific numbers, ask — don't invent them.

**Thumbnail Metric** (`thumbnail-cs-overview-page-large-metric`, PlainText)
The most impressive single number, displayed on the customer stories overview page. Short format: `60%`, `1M`, `200k`, `4 weeks`. Pick the metric that stops someone scrolling.

**Thumbnail Metric Description** (`thumbnail-cs-overview-page-metric-description`, PlainText)
One-line description of the thumbnail metric. Lowercase. Examples: `community growth rate MoM`, `app downloads`, `patients`.

### Customer quote (optional)

**Top Quote** (`top-quote`, PlainText)
A direct quote from the customer. Include quotation marks. Only use if the user provides a real quote — never fabricate.

**Top Quote | Name** (`top-quote-name`, PlainText)
Full name of the person quoted.

**Top Quote | Job Title** (`top-quote-job-title`, PlainText)
Job title. Examples: "CEO", "Online Casino Executive", "Head of Product".

### Main body

**Customer Story** (`section-2-text`, RichText)
This is the full story. It uses rich text with custom HTML tags for section dividers. The structure follows a consistent pattern across all stories on the site:

#### Section structure

1. **Opening paragraphs** (2-3 paragraphs)
   Company background and context. Who they are, what they do, why they matter. Written as narrative prose.

2. **The Challenge** section
   ```html
   <p><sprscript-green>The Challenge<sprscript-green></p>
   ```
   Followed by an H2 or H3 subheading that frames the specific problem.
   Then 2-3 paragraphs describing the challenge in detail. Frame using the core problems from `value-story.md` where they map naturally.

3. **Why social.plus** section
   ```html
   <p><sprscript-green>Why social.plus<sprscript-green></p>
   ```
   Followed by an H2 or H3 subheading about why they chose social.plus.
   Then 2-3 paragraphs explaining the selection rationale. Use product pillar language from `positioning.md` but keep the customer as the subject.

4. **Implementation** section (optional, include when the user provides technical details)
   ```html
   <p><sprscript-green>Implementation<sprscript-green></p>
   ```
   Followed by H2/H3 and paragraphs about how they built it — SDKs used, UIKits, customization, timeline.

5. **Results / Impact** section (optional, include when outcome data is available)
   ```html
   <p><sprscript-green>The Results<sprscript-green></p>
   ```
   Quantified outcomes. Map to the value creation model from `value-story.md`: functional → strategic → economic → compounding.

#### Body guidelines
- Target length: 4,000–7,000 characters (matching existing stories on the site).
- The customer is the hero. social.plus is the tool they chose. Write "they implemented" not "we provided."
- Use `<strong>` for emphasis within paragraphs where needed.
- Images can be referenced with `<figure>` tags but leave image URLs as placeholders for the user to upload.
- The `<sprscript-green>` tag renders as a styled green section divider on the website. Always use it for section headers. Always close it: `<sprscript-green>Text<sprscript-green>`.

### Sidebar

**Sidebar | About** (`sidebar-about`, PlainText)
2-3 sentences describing the customer's company. Factual, third person. Include: what they do, founding year or scale indicator, and headquarters/region.

**Sidebar | Location** (`sidebar-location`, PlainText)
Company headquarters. Format: "City, Country" or just "Country". Examples: "São Paulo, Brazil", "United States", "Limassol, Cyprus".

**Sidebar | Use Cases** (`new-use-cases`, MultiReference)
References to Use Case CMS items. Tell the user which use cases apply (e.g., "Activity Feed", "Group Chat", "Live Chat", "Livestream") so they can link them in Webflow.

**Sidebar | Implementation** (`implementation-web`, `implementation-mobile-app`, Switches)
Tell the user which to toggle: Web, App, or both.

**Sidebar | SDK and UIKit** (`sdk`, `uikit`, MultiReference)
Tell the user which SDKs and UIKits the customer uses, if known.

**Sidebar | UIKit Customization** (`uikit-customization`, Option)
Options: Low, Medium, High, Custom UI. Indicate which applies based on how heavily the customer customized the UI.

### Meta

**Meta Description** (`meta-description`, PlainText)
SEO meta description, under 155 characters. Pattern: "Discover how [Company] [outcome] with social.plus. [Key metric or detail]."

### Display controls (tell the user to set these)

- **Order and ID** — The user assigns this based on where they want the story in the list.
- **Industry** — Tell the user which industry reference(s) to link.
- **Show on homepage / /chat / /social / /video** — Recommend which product pages should feature this story based on what the customer uses.
- **Show on industry pages** — Recommend which industry page toggles to enable.
- **Demo Link** — If a demo exists, format: `https://www.social.plus/demo/[slug]`

## Output format

Present the output as a clearly labeled field-by-field mapping. The user copies each value into the corresponding Webflow CMS field. Example structure:

```
## [Company Name] — Customer Story

**Name Company:** [value]
**Slug:** [value]
**Hero Title:** [value]
**Hero Introduction Paragraph:** [value]
**Meta Description:** [value]

**Metric Box 1:**
[HTML]

**Metric Box 2:**
[HTML]

**Metric Box 3:**
[HTML]

**Thumbnail Metric:** [value]
**Thumbnail Metric Description:** [value]

**Top Quote:** [quote or "N/A — no quote provided"]
**Top Quote | Name:** [value]
**Top Quote | Job Title:** [value]

**Customer Story (body):**
[Full rich text HTML]

**Sidebar | About:** [value]
**Sidebar | Location:** [value]
**Sidebar | Use Cases:** [list]
**Sidebar | Implementation:** Web: [yes/no] | App: [yes/no]
**Sidebar | SDK:** [list or "Ask customer"]
**Sidebar | UIKit:** [list or "Ask customer"]
**Sidebar | UIKit Customization:** [Low/Medium/High/Custom UI]

**Display recommendations:**
- Industry: [recommendation]
- Show on homepage: [yes/no]
- Show on /social: [yes/no]
- Show on /chat: [yes/no]
- Show on /video: [yes/no]
- Industry pages: [list]
- Demo link: [URL or "N/A"]
```

## What NOT to do

- Never fabricate metrics, quotes, or customer statements. If the user doesn't provide numbers, ask — leave the field empty rather than inventing data.
- Never name a customer without explicit permission from the user.
- Never overstate social.plus's role. The customer built their experience; social.plus provided the infrastructure.
- Never use competitor names unless the user specifically requests a comparison angle.
- Never use the `<sprscript-green>` tags for anything other than section headers (The Challenge, Why social.plus, Implementation, The Results).

## Before delivering

Run the compliance check from `brain.md`. Customer stories are permanent, public-facing assets — a terminology violation or fabricated claim lives on the website indefinitely.

## Important: URL format

**Always use `github.com/.../blob/...` URLs when fetching files.** Never attempt `raw.githubusercontent.com` — it is blocked by network egress settings.
