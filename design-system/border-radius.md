# social.plus Border Radius System

All corner rounding in social.plus outputs uses this scale. Do not use arbitrary values —
always pick the closest token from the scale below.

---

## The Scale

| Token | Value | Typical use |
|-------|-------|-------------|
| `radius-1` | 4px | Subtle rounding — tags, badges, tooltips |
| `radius-2` | 8px | Buttons, inputs, small components |
| `radius-3` | 12px | Cards, dropdowns, popovers |
| `radius-4` | 16px | Large cards, modals, panels |
| `radius-5` | 24px | Feature sections, hero containers |
| `radius-6` | 32px | Large decorative containers |
| `radius-full` | 9999px | Pills, avatars, toggle switches, circular buttons |

---

## Principles

**Geometric, not bubbly.** The border radius scale reflects Figtree's geometric character —
structured and confident at small sizes, with softness introduced only at larger components.
Avoid reaching for large radii on small elements; it conflicts with the brand's premium,
bold feel.

**Consistency within a component set.** All cards in a group, all buttons of the same
type, all inputs in a form — use the same radius token. Never mix radius values within
a repeated set of elements.

**`radius-full` is intentional.** Use it deliberately for pill-shaped tags, avatar
circles, and toggles. Do not use it on large containers or cards — it reads as playful
rather than premium.

---

## CSS Custom Properties

```css
:root {
  --radius-1:    4px;
  --radius-2:    8px;
  --radius-3:    12px;
  --radius-4:    16px;
  --radius-5:    24px;
  --radius-6:    32px;
  --radius-full: 9999px;
}
```

---

## Common component defaults

| Component | Default token |
|-----------|--------------|
| Button (default) | `radius-2` (8px) |
| Input field | `radius-2` (8px) |
| Badge / tag | `radius-1` (4px) or `radius-full` for pill style |
| Card | `radius-3` (12px) or `radius-4` (16px) |
| Modal / drawer | `radius-4` (16px) |
| Avatar | `radius-full` |
| Tooltip | `radius-1` (4px) |
| Hero / feature block | `radius-5` (24px) |
