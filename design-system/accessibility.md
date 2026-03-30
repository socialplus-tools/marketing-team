# social.plus Accessibility Standards

social.plus targets **WCAG 2.1 AA** compliance across all products and marketing surfaces. Accessibility is not a post-launch concern — it is built into every component decision.

---

## Colour Contrast

| Context | Minimum ratio | Target ratio |
|---------|---------------|--------------|
| Body text on dark background | 4.5:1 | 7:1 |
| Large text (18px+ bold or 24px+ regular) | 3:1 | 4.5:1 |
| UI components and graphical elements | 3:1 | 4.5:1 |
| Placeholder text | 3:1 | — |

### Verified brand colour pairings

| Foreground | Background | Ratio | Pass |
|-----------|------------|-------|------|
| `#FFFFFF` | `#111111` | 19.5:1 | ✅ AAA |
| `#C0C0C2` (text-subtle) | `#111111` | 7.1:1 | ✅ AAA |
| `#808080` (text-muted) | `#111111` | 3.95:1 | ✅ AA |
| `#FFFFFF` | `#3B41EC` (Ultramarine) | 4.8:1 | ✅ AA |
| `#FFFFFF` | `#1e1e1e` (surface-1) | 15.3:1 | ✅ AAA |
| `#8890f8` (badge text) | `#111111` | 4.6:1 | ✅ AA |

**Do not use** muted text colours (`#808080` or lower) for any text that conveys critical information — reserve them for purely decorative labels and secondary metadata.

---

## Focus States

Every interactive element must have a visible focus indicator. Never use `outline: none` without providing a custom alternative.

**Standard focus ring:**
```css
:focus-visible {
  outline: 2px solid #3B41EC;
  outline-offset: 3px;
}
```

- Use `:focus-visible` (not `:focus`) to avoid showing focus rings on mouse click while preserving them for keyboard navigation
- Focus ring colour is always Ultramarine `#3B41EC` — never hidden, never a pure greyscale ring on dark backgrounds
- Minimum focus indicator area: 3px perimeter around the component

---

## Keyboard Navigation

All interactive elements must be reachable and operable via keyboard alone.

- **Tab order** must follow the visual reading order (left to right, top to bottom)
- **Focusable elements:** links, buttons, inputs, selects, checkboxes, radios, toggles — all must receive focus
- **Custom components** (dropdowns, modals, toggles) must implement the appropriate ARIA pattern and keyboard behaviour:

| Component | Keyboard behaviour |
|-----------|-------------------|
| Button | `Enter` or `Space` to activate |
| Link | `Enter` to follow |
| Select / dropdown | `Enter` to open, arrow keys to navigate, `Enter` to select, `Escape` to close |
| Modal / dialog | `Escape` to close, focus trapped inside while open |
| Toggle | `Space` to toggle |
| Checkbox | `Space` to check/uncheck |
| Radio group | Arrow keys to move between options |

---

## ARIA

Use ARIA attributes to communicate roles, states, and properties that are not implicit in the HTML.

### Required patterns

| Pattern | ARIA requirement |
|---------|-----------------|
| Icon-only button | `aria-label="[action]"` |
| Loading state | `aria-busy="true"` on the container |
| Error message | `aria-live="polite"` on the error region; `aria-describedby` linking input to error |
| Modal | `role="dialog"`, `aria-modal="true"`, `aria-labelledby` pointing to the title |
| Toggle | `role="switch"`, `aria-checked="true/false"` |
| Navigation | `role="navigation"`, `aria-label` to distinguish multiple navs |
| Current page link | `aria-current="page"` |

### What to avoid

- Do not use `aria-label` to override visible text unless the visible text is genuinely insufficient
- Do not use `role="button"` on a `<div>` — use a real `<button>` element
- Do not use placeholder text as the only label for an input
- Do not rely on colour alone to communicate status (e.g. error states must also include an icon or text)

---

## Images and Icons

- All `<img>` elements must have an `alt` attribute
  - Decorative images: `alt=""`
  - Informative images: `alt="[concise description of what it conveys]"`
- SVG logos must have an `aria-label` on the `<svg>` element and `role="img"`
- Icon-only interactive elements must have `aria-label`
- Icons that are purely decorative alongside visible text: `aria-hidden="true"`

---

## Motion and Animation

- All animations must respect `prefers-reduced-motion`:
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```
- Never use flashing content that exceeds 3 flashes per second
- Hover/focus transitions (0.15–0.3s) are acceptable without reduction; longer animations should be opt-in or reduced

---

## Typography and Readability

- Minimum body text size: **14px**. Never use smaller type for anything that conveys information.
- Line height for body text: **1.6 minimum**
- Maximum line length: **75 characters** (use `container-narrow` for reading content)
- Do not use `letter-spacing` on body text in a way that impairs readability
- Never use all-caps for body text — only for labels and badges at small sizes

---

## Forms

- Every input must have a visible, programmatically associated `<label>` (not just a placeholder)
- Error messages must be surfaced in text, not colour alone
- Required fields must be marked in both the label (`*`) and the input (`required` attribute)
- Group related inputs with `<fieldset>` and `<legend>` (radio groups, checkbox groups)

---

## Checklist

Before shipping any component or page:

- [ ] All text meets minimum contrast ratio (4.5:1 for body, 3:1 for large text)
- [ ] All interactive elements are keyboard accessible
- [ ] Focus rings are visible on all focusable elements
- [ ] No information is conveyed by colour alone
- [ ] All images have appropriate `alt` text
- [ ] All icon-only buttons have `aria-label`
- [ ] Form inputs have associated labels
- [ ] Error states include text, not just colour
- [ ] Animations respect `prefers-reduced-motion`
- [ ] Tab order matches visual reading order
