# social.plus Shadow & Elevation System

On dark backgrounds, shadows are less visible than on light ones. The social.plus elevation
system therefore combines two signals: a **drop shadow** (deeper opacity as elevation rises)
and a **surface colour shift** (higher surfaces use a slightly lighter grey). Both signals
work together to communicate depth.

---

## Elevation Scale

| Token | Shadow | Surface colour | Typical use |
|-------|--------|----------------|-------------|
| `elevation-0` | none | `#111111` | Page background — base canvas |
| `elevation-1` | `0 1px 4px rgba(0,0,0,0.5)` | `#1e1e1e` | Cards, inputs, table rows |
| `elevation-2` | `0 4px 16px rgba(0,0,0,0.6)` | `#272727` | Dropdowns, popovers, tooltips |
| `elevation-3` | `0 8px 32px rgba(0,0,0,0.7)` | `#2e2e2e` | Modals, drawers, bottom sheets |
| `elevation-4` | `0 16px 48px rgba(0,0,0,0.8)` | `#2e2e2e` | Sticky nav (scrolled), floating bars |

---

## Brand Glow Variants

Glows are used sparingly on interactive or highlighted elements where brand energy needs
to surface — hover states, active selections, feature callouts. Each accent colour has
its own glow token.

| Token | Value | Colour |
|-------|-------|--------|
| `glow-ultramarine` | `0 4px 20px rgba(59, 65, 236, 0.45)` | Ultramarine `#3B41EC` |
| `glow-blue`        | `0 4px 20px rgba(55, 105, 236, 0.40)` | Blue `#3769EC` |
| `glow-sky`         | `0 4px 20px rgba(69, 165, 237, 0.40)` | Sky Blue `#45A5ED` |
| `glow-pink`        | `0 4px 20px rgba(245, 104, 240, 0.40)` | Electric Pink `#F568F0` |
| `glow-orange`      | `0 4px 20px rgba(246, 96, 5, 0.40)` | Orange `#F66005` |
| `glow-yellow`      | `0 4px 20px rgba(247, 197, 6, 0.35)` | Yellow `#F7C506` |
| `glow-navy`        | `0 4px 20px rgba(39, 38, 94, 0.60)` | Dark Navy `#27265E` |

### Glow usage rules

- **`glow-ultramarine`** — primary button hover, focus rings, active UI states
- **`glow-blue` / `glow-sky`** — gradient button hover (paired), card accent highlights
- **`glow-pink`** — campaign/marketing callouts, feature spotlights
- **`glow-orange`** — notification badges, alert states, energy moments
- **`glow-yellow`** — achievement states, success highlights, celebratory moments
- **`glow-navy`** — deep background panels, decorative layering only
- **Never stack two glows** on the same element
- **Never use glow as a default state** — always tied to hover, active, or deliberate accent

---

## CSS Custom Properties

```css
:root {
  /* Elevation shadows */
  --shadow-1: 0 1px 4px rgba(0,0,0,0.5);
  --shadow-2: 0 4px 16px rgba(0,0,0,0.6);
  --shadow-3: 0 8px 32px rgba(0,0,0,0.7);
  --shadow-4: 0 16px 48px rgba(0,0,0,0.8);

  /* Elevation surfaces */
  --surface-0: #111111;
  --surface-1: #1e1e1e;
  --surface-2: #272727;
  --surface-3: #2e2e2e;

  /* Brand glows */
  --glow-ultramarine: 0 4px 20px rgba(59, 65, 236, 0.45);
  --glow-blue:        0 4px 20px rgba(55, 105, 236, 0.40);
  --glow-sky:         0 4px 20px rgba(69, 165, 237, 0.40);
  --glow-pink:        0 4px 20px rgba(245, 104, 240, 0.40);
  --glow-orange:      0 4px 20px rgba(246, 96, 5, 0.40);
  --glow-yellow:      0 4px 20px rgba(247, 197, 6, 0.35);
  --glow-navy:        0 4px 20px rgba(39, 38, 94, 0.60);
}
```

---

## Principles

**Shadow alone is not enough on dark backgrounds.** Always pair elevation shadow with the
corresponding surface colour — `elevation-1` cards sit on `#1e1e1e`, not `#111`.

**Glows communicate brand energy, not depth.** Do not use glow tokens to imply elevation —
they exist purely for interactive feedback and accent moments.

**Subtlety over drama.** Yellow and navy glows use a slightly reduced opacity because their
luminance is higher (yellow) or their hue is less saturated (navy) — matching the visual
weight of the other glows without overpowering them.
