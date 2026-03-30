# social.plus Colour System

Source of truth: Figma file node `131:3733`
https://www.figma.com/design/nDIDa7goXwKlqGWdKKlbIX/2026-Website-Visuals?node-id=131-3733

---

## Primary Brand Colour

| Preview | Name | HEX | RGB | Webflow variable |
|---------|------|-----|-----|------------------|
| ![](https://placehold.co/40x40/3b41ec/3b41ec) | **social.plus Blue (Ultramarine)** | `#3B41EC` | rgb(59, 65, 236) | `var(--social--main-blue)` |

Ultramarine is the hero colour. Use it for primary CTAs, key highlights, and primary
interactive elements. It appears prominently on the dark brand background. It is the
most recognisable social.plus colour.

### Interactive states (buttons, links)

| Preview | State | HEX | Webflow variable |
|---------|-------|-----|------------------|
| ![](https://placehold.co/40x40/3b41ec/3b41ec) | Default | `#3B41EC` | `var(--social--main-blue)` |
| ![](https://placehold.co/40x40/272b9d/272b9d) | Hover | `#272B9D` | `var(--social--button-hover)` |
| ![](https://placehold.co/40x40/27265e/27265e) | Pressed | `#27265E` | `var(--social--button-pressed)` |

---

## Supporting Colours

Used for visual variety, tags, status indicators, feature category highlights, and
illustrations. Never use accents as primary call-to-action colours — that role belongs
to social.plus Blue. Never use more than 2–3 of these together in a single
composition — let them breathe.

| Preview | Name | HEX | RGB | Webflow variable |
|---------|------|-----|-----|------------------|
| ![](https://placehold.co/40x40/3769ec/3769ec) | Blue | `#3769EC` | rgb(55, 105, 236) | — |
| ![](https://placehold.co/40x40/45a5ed/45a5ed) | Sky Blue | `#45A5ED` | rgb(69, 165, 237) | — |
| ![](https://placehold.co/40x40/f7c506/f7c506) | Yellow | `#F7C506` | rgb(247, 197, 6) | `var(--secondary--yellow)` |
| ![](https://placehold.co/40x40/f66005/f66005) | Orange | `#F66005` | rgb(246, 96, 5) | `var(--secondary--orange)` |
| ![](https://placehold.co/40x40/f568f0/f568f0) | Electric Pink | `#F568F0` | rgb(245, 104, 240) | `var(--secondary--pink)` |
| ![](https://placehold.co/40x40/27265e/27265e) | Dark Navy | `#27265E` | rgb(39, 38, 94) | — |
| ![](https://placehold.co/40x40/9f72ff/9f72ff) | Purple | `#9F72FF` | rgb(159, 114, 255) | `var(--secondary--purple)` |

---

## Neutral / Base Colours

### Dark palette

| Preview | Name | HEX | RGB | Webflow variable |
|---------|------|-----|-----|------------------|
| ![](https://placehold.co/40x40/111111/111111) | **Brand Black** | `#111111` | rgb(17, 17, 17) | `var(--social--dark)` |
| ![](https://placehold.co/40x40/1a1a1a/1a1a1a) | Dark Gray Background | `#1A1A1A` | rgb(26, 26, 26) | `var(--social--dark-gray-background)` |
| ![](https://placehold.co/40x40/222222/222222) | Grey | `#222222` | rgb(34, 34, 34) | `var(--social--grey)` |
| ![](https://placehold.co/40x40/272727/272727) | Dark Grey | `#272727` | rgb(39, 39, 39) | — |
| ![](https://placehold.co/40x40/444444/444444) | Light Grey | `#444444` | rgb(68, 68, 68) | `var(--social--light-grey)` |
| ![](https://placehold.co/40x40/100f26/100f26) | Deep Dark Navy | `#100F26` | rgb(16, 15, 38) | — |

### Light palette

| Preview | Name | HEX | RGB | Webflow variable |
|---------|------|-----|-----|------------------|
| ![](https://placehold.co/40x40/ffffff/ffffff) | **Brand White** | `#FFFFFF` | rgb(255, 255, 255) | `var(--main--white)` |
| ![](https://placehold.co/40x40/f5f5f5/f5f5f5) | Whitesmoke | `#F5F5F5` | rgb(245, 245, 245) | `var(--main--whitesmoke)` |
| ![](https://placehold.co/40x40/f9f9f9/f9f9f9) | Grey Background | `#F9F9F9` | rgb(249, 249, 249) | `var(--social--grey-background)` |

Brand Black (`#111`) is the default background. White is for primary text on dark
backgrounds. The dark palette defines elevation surfaces for cards, modals, and
layered UI.

---

## State / Utility Colours

| Preview | Name | HEX | Use | Webflow variable |
|---------|------|-----|-----|------------------|
| ![](https://placehold.co/40x40/ff305a/ff305a) | Red | `#FF305A` | Error states, alerts, destructive actions | `var(--secondary--red)` |
| ![](https://placehold.co/40x40/ff5252/ff5252) | Dark Orange | `#FF5252` | Warnings, secondary destructive states | — |
| ![](https://placehold.co/40x40/1dc497/1dc497) | Green | `#1DC497` | Success states, positive indicators, growth metrics | `var(--secondary--green)` |

These are functional colours. Do not use them for decorative purposes.

---

## Special

| Preview | Name | HEX / Value | Webflow variable |
|---------|------|-------------|------------------|
| ![](https://placehold.co/40x40/2a31e9/2a31e9) | Blue Transparent | `rgba(42, 49, 233, 0.1)` | `var(--social--blue-transparent)` |
| ![](https://placehold.co/40x40/181818/181818) | Menu Background | `#181818` | `var(--secondary--menu-bg)` |
| — | Transparent | — | `var(--main--transparant)` |

---

## Text Colours

### On light backgrounds

| Preview | Level | HEX | Webflow variable |
|---------|-------|-----|------------------|
| ![](https://placehold.co/40x40/111111/111111) | Headings | `#111111` | `var(--text--text-color-dark)` |
| ![](https://placehold.co/40x40/414347/414347) | Body text | `#414347` | `var(--text--text-color-grey-dark)` |
| ![](https://placehold.co/40x40/717275/717275) | Secondary text | `#717275` | `var(--text--text-color-grey-medium)` |
| ![](https://placehold.co/40x40/b3b3b3/b3b3b3) | Muted text | `#B3B3B3` | `var(--text--text-color-grey-light)` |

### On dark backgrounds

Use `#FFFFFF` (white) for headings and primary text. Use `#D0D0D1` for secondary text.
Use `#A0A1A3` for muted/tertiary text. Use `#717275` for disabled text.

---

## Borders and Dividers

### On light backgrounds

| Preview | Name | HEX | Webflow variable |
|---------|------|-----|------------------|
| ![](https://placehold.co/40x40/e7e7e7/e7e7e7) | Light Grey | `#E7E7E7` | `var(--border--border-light-grey)` |
| ![](https://placehold.co/40x40/d0d0d1/d0d0d1) | Med Grey | `#D0D0D1` | `var(--border--border-med-grey)` |
| ![](https://placehold.co/40x40/666666/666666) | Dark Grey | `#666666` | `var(--border--border-dark-grey)` |

### On dark backgrounds

| Preview | Name | HEX | Webflow variable |
|---------|------|-----|------------------|
| ![](https://placehold.co/40x40/232324/232324) | Dark | `#232324` | `var(--border--border-dark)` |
| ![](https://placehold.co/40x40/39393a/39393a) | Hover | `#39393A` | `var(--border--border-hover)` |

Use `rgba(255,255,255,0.12)` for subtle dividers on the dark background. Do not use
solid white — it is too harsh.

---

## Brand Gradients

### Brand Blue Gradient

Direction: 135° (top-left to bottom-right)
`#45A5ED` (Sky Blue) → `#3769EC` (Blue) → `#3B41EC` (Ultramarine)

```css
background: linear-gradient(
  135deg,
  var(--gradient--light-blue),
  var(--gradient--medium-blue),
  var(--gradient--dark-blue)
);
```

| Step | HEX | Webflow variable |
|------|-----|------------------|
| Start (light) | `#45A5ED` | `var(--gradient--light-blue)` |
| Middle | `#3769EC` | `var(--gradient--medium-blue)` |
| End (brand blue) | `#3B41EC` | `var(--gradient--dark-blue)` |

### Brand Pink Gradient

Direction: left → right
`#F568F0` (Electric Pink) → `#F66005` (Orange, ~51%) → `#F7C506` (Yellow)

```css
background: linear-gradient(to right, #F568F0, #F66005 51.5%, #F7C506);
```

Use these gradients for hero sections, feature cards, and key visual moments.
Never tile or repeat them — they should feel intentional and impactful.

---

## Flat Gradient Pairs (for components and cards)

Two-stop gradients for smaller UI elements:

| From | To | Feel |
|------|----|------|
| Ultramarine `#3B41EC` | Blue `#3769EC` | Cool authority |
| Blue `#3769EC` | Sky Blue `#45A5ED` | Airy, digital |
| Red `#FF305A` | Electric Pink `#F568F0` | Urgent energy |
| Electric Pink `#F568F0` | Orange `#F66005` | Warm vibrancy |
| Orange `#F66005` | Yellow `#F7C506` | Optimism |
| Black `#111111` | Dark Grey `#272727` | Depth |
| Dark Navy `#27265E` | Deep Dark Navy `#100F26` | Prestige |

---

## Colour Usage Principles

**Dark-first:** The brand lives on dark backgrounds. `#111` is the default canvas.
Text is white or light grey on this background.

**Ultramarine leads:** When you need one brand colour to anchor a design, reach for
Ultramarine. It is the most recognisable social.plus colour.

**social.plus Blue is the only CTA colour.** Accents are for decoration and status,
never for primary buttons or calls to action.

**Buttons always need three states.** Default, hover, and pressed. Never ship a button
with only one colour state.

**Gradients for moments:** Use the Brand Blue and Brand Pink gradients for hero sections
and key visual backgrounds. Never apply gradients to text — this includes CSS
`background-clip: text` effects. Text should always be a solid colour (white, black,
or a single brand colour).

**Cards and content boxes are greyscale by default:** When displaying a group of cards,
tiles, or content boxes, use consistent neutral background colours from the greyscale
palette (`#1e1e1e` or `#272727`) with a subtle border (`rgba(255,255,255,0.12)`). Do not
use different brand colours or gradients across cards in the same set — reserve colour
and gradients for intentional singular highlights (e.g. a featured card, a hero CTA
block).

**Respect the text hierarchy.** Headings are darkest, body text is medium, supporting
text is lighter. Don't skip levels.

**Accessibility:** When placing text on coloured backgrounds, ensure sufficient contrast.
White text works on Ultramarine, Blue, Dark Navy, and Black. Dark text should be used
on Yellow and Sky Blue. Electric Pink requires care — test before use.

**Only use colours from this palette.** If a colour isn't listed here, don't use it. If
a design requires a new colour, flag it to the marketing team first.

---

## For Developers: Webflow CSS Variables

All colours above are available as Webflow CSS variables. When writing CSS for the
social.plus website, always use the variable syntax instead of hardcoding hex values.

**Pattern:** `var(--{category}--{variable-name})`

| Colour | CSS Variable |
|--------|-------------|
| social.plus Blue | `var(--social--main-blue)` |
| Button Hover | `var(--social--button-hover)` |
| Button Pressed | `var(--social--button-pressed)` |
| Dark | `var(--social--dark)` |
| Grey | `var(--social--grey)` |
| Light Grey | `var(--social--light-grey)` |
| Grey Background | `var(--social--grey-background)` |
| Dark Gray Background | `var(--social--dark-gray-background)` |
| Blue Transparent | `var(--social--blue-transparent)` |
| White | `var(--main--white)` |
| Whitesmoke | `var(--main--whitesmoke)` |
| Transparent | `var(--main--transparant)` |
| Border Med Grey | `var(--border--border-med-grey)` |
| Border Light Grey | `var(--border--border-light-grey)` |
| Border Dark Grey | `var(--border--border-dark-grey)` |
| Border Dark | `var(--border--border-dark)` |
| Border Hover | `var(--border--border-hover)` |
| Green | `var(--secondary--green)` |
| Yellow | `var(--secondary--yellow)` |
| Red | `var(--secondary--red)` |
| Orange | `var(--secondary--orange)` |
| Purple | `var(--secondary--purple)` |
| Pink | `var(--secondary--pink)` |
| Menu BG | `var(--secondary--menu-bg)` |
| Text Grey Light | `var(--text--text-color-grey-light)` |
| Text Grey Medium | `var(--text--text-color-grey-medium)` |
| Text Grey Dark | `var(--text--text-color-grey-dark)` |
| Text Dark | `var(--text--text-color-dark)` |
| Gradient Light Blue | `var(--gradient--light-blue)` |
| Gradient Medium Blue | `var(--gradient--medium-blue)` |
| Gradient Dark Blue | `var(--gradient--dark-blue)` |
