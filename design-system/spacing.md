# social.plus Spacing System

All spacing in social.plus outputs uses this scale. Do not use arbitrary values —
always pick the closest token from the scale below.

---

## The Scale

| Token | Value | Typical use |
|-------|-------|-------------|
| `space-1` | 4px | Tight gaps — icon-to-label, badge padding |
| `space-2` | 8px | Small gaps between related items |
| `space-3` | 12px | Compact component padding |
| `space-4` | 16px | Default inner padding — inputs, small cards |
| `space-5` | 24px | Standard gap between components |
| `space-6` | 32px | Comfortable gap between larger elements |
| `space-7` | 40px | Card padding, mid-level section spacing |
| `space-8` | 48px | Section breathing room within a page |
| `space-9` | 64px | Large section breaks |
| `space-10` | 80px | Major layout separation |
| `space-11` | 96px | Hero sections, top-level page padding |
| `space-12` | 128px | Maximum section separation |

---

## Principles

**8pt grid with 4pt small steps.** Values below 16px use 4pt increments (4, 8, 12, 16)
for fine-grained control in tight UI. From 16px upwards the scale uses 8pt steps, then
grows in larger increments for layout-level spacing.

**Use the closest token — don't invent values.** If something needs more space than
space-6 (32px) but less than space-7 (40px), use space-7 and adjust surrounding
elements before reaching for an arbitrary value.

**Component spacing vs layout spacing.** As a rough guide:
- space-1 to space-4 (4–16px): inside components — padding, icon gaps, label spacing
- space-5 to space-7 (24–40px): between components — card gaps, list item spacing, form fields
- space-8 to space-9 (48–64px): section-level — breathing room between content blocks
- space-10 to space-12 (80–128px): page-level — hero padding, major section separation

---

## CSS Custom Properties

```css
:root {
  --space-1:  4px;
  --space-2:  8px;
  --space-3:  12px;
  --space-4:  16px;
  --space-5:  24px;
  --space-6:  32px;
  --space-7:  40px;
  --space-8:  48px;
  --space-9:  64px;
  --space-10: 80px;
  --space-11: 96px;
  --space-12: 128px;
}
```
