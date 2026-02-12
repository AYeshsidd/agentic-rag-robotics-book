# Research: Frontend UI Refinement

**Feature**: 010-ui-refinement
**Date**: 2026-02-12
**Purpose**: Document technical decisions, patterns, and best practices for UI refinement

## Research Areas

### 1. Footer Styling in Light Mode

**Decision**: Use CSS custom properties with light mode overrides

**Rationale**:
- Docusaurus uses CSS variables (--ifm-*) for theming
- Light mode can be targeted with `:root` selector
- Dark mode uses `[data-theme='dark']` attribute selector
- Allows theme-specific color overrides without duplicating styles

**Implementation Pattern**:
```css
/* Light mode (default) */
:root {
  --ifm-footer-color: #1c1e21;  /* Dark text for light background */
  --ifm-footer-link-color: #1c1e21;
  --ifm-footer-link-hover-color: var(--ifm-color-primary);
}

/* Dark mode (preserve existing) */
[data-theme='dark'] {
  /* Keep existing dark mode colors unchanged */
}
```

**WCAG AA Contrast Requirements**:
- Minimum contrast ratio: 4.5:1 for normal text
- Minimum contrast ratio: 3:1 for large text (18pt+ or 14pt+ bold)
- Test with tools: Chrome DevTools, WebAIM Contrast Checker
- Footer text should be #1c1e21 (near black) on light background for ~16:1 ratio

**Alternatives Considered**:
- Inline styles: Rejected - not maintainable, doesn't support theming
- Separate light/dark CSS files: Rejected - increases bundle size, harder to maintain
- JavaScript theme detection: Rejected - CSS-only solution is simpler and faster

---

### 2. Chat Interface Typography Improvements

**Decision**: Update FloatingChatbot.module.css with light mode specific styles

**Rationale**:
- Chat interface currently uses CSS modules for scoped styling
- Need to add light mode overrides for text colors, backgrounds, borders
- Maintain existing glassmorphism effects while improving visibility
- Professional fonts already in use (system font stack)

**Light Mode Color Palette**:
```css
/* Chat container */
background: var(--ifm-background-color);  /* White in light mode */
border: 1px solid var(--ifm-color-emphasis-300);  /* Light gray border */

/* Chat messages */
color: var(--ifm-font-color-base);  /* Dark text */
background: rgba(0, 0, 0, 0.03);  /* Very light gray for message bubbles */

/* Input field */
border: 1px solid var(--ifm-color-emphasis-300);
color: var(--ifm-font-color-base);
background: var(--ifm-background-color);

/* Buttons */
/* Keep existing glassmorphism but adjust opacity for visibility */
background: linear-gradient(135deg, rgba(var(--ifm-color-primary-rgb), 0.15), rgba(var(--ifm-color-primary-rgb), 0.1));
```

**Typography Best Practices**:
- Font size: 14-16px for body text (already implemented)
- Line height: 1.5-1.7 for readability (already implemented)
- Font weight: 400 for body, 500-600 for emphasis
- Letter spacing: 0.01em for improved readability

**Alternatives Considered**:
- Custom font import: Rejected - adds load time, system fonts are professional
- Complete redesign: Rejected - only need light mode fixes, preserve existing design
- Separate light/dark components: Rejected - CSS theming is cleaner

---

### 3. Module Card Image Integration

**Decision**: Replace emoji placeholders with actual image elements using img tags

**Rationale**:
- Current implementation uses emoji (📚) as placeholder in imagePlaceholder div
- Need to replace with actual <img> elements for custom images
- Images should be in static/img/modules/ directory
- Fallback to gradient background if image fails to load

**Image Implementation Pattern**:
```jsx
// In HomepageFeatures/index.tsx
<div className={styles.imageContainer}>
  {image ? (
    <img
      src={image}
      alt={`${title} module`}
      className={styles.moduleImage}
      onError={(e) => {
        e.target.style.display = 'none';
        e.target.nextSibling.style.display = 'flex';
      }}
    />
  ) : null}
  <div className={styles.imagePlaceholder}>
    <span className={styles.placeholderIcon}>📚</span>
  </div>
</div>
```

**Image Specifications**:
- Format: WebP (best compression) with JPG fallback
- Dimensions: 800x600px (4:3 aspect ratio)
- File size: <200KB each (optimized)
- Alt text: Descriptive for accessibility
- Loading: Lazy loading with loading="lazy" attribute

**CSS for Images**:
```css
.moduleImage {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.imagePlaceholder {
  /* Show only if image fails to load */
  display: none;
}
```

**Alternatives Considered**:
- Background images: Rejected - img tags better for accessibility and SEO
- SVG icons: Rejected - custom images provide better visual appeal
- Icon libraries: Rejected - custom images more relevant to content

---

### 4. Docusaurus Theme Switching Patterns

**Decision**: Use CSS custom properties with data-theme attribute selector

**Rationale**:
- Docusaurus automatically adds `data-theme="light"` or `data-theme="dark"` to HTML element
- CSS can target these attributes for theme-specific styles
- No JavaScript needed for theme detection
- Automatic theme switching handled by Docusaurus

**Theme Detection Pattern**:
```css
/* Light mode (default) */
:root {
  --custom-var: light-value;
}

/* Dark mode */
[data-theme='dark'] {
  --custom-var: dark-value;
}

/* Component uses var(--custom-var) and gets correct value automatically */
```

**Best Practices**:
- Define all theme variables in custom.css
- Use semantic variable names (--footer-text-color, not --color-1)
- Test both themes after every change
- Ensure smooth transitions between themes

**Alternatives Considered**:
- JavaScript theme detection: Rejected - CSS-only is simpler and faster
- Separate theme files: Rejected - harder to maintain consistency
- Media query prefers-color-scheme: Rejected - Docusaurus handles this already

---

### 5. WCAG AA Contrast Testing

**Decision**: Use browser DevTools and automated contrast checkers

**Rationale**:
- Chrome DevTools has built-in contrast checker in Elements panel
- WebAIM Contrast Checker provides detailed analysis
- Automated testing catches issues early
- Manual testing confirms real-world usability

**Testing Tools**:
1. **Chrome DevTools**:
   - Inspect element → Styles panel → Color picker
   - Shows contrast ratio and WCAG compliance
   - Real-time feedback while adjusting colors

2. **WebAIM Contrast Checker**:
   - https://webaim.org/resources/contrastchecker/
   - Input foreground and background colors
   - Shows AA and AAA compliance levels

3. **axe DevTools Extension**:
   - Automated accessibility testing
   - Scans entire page for contrast issues
   - Provides specific recommendations

**Testing Workflow**:
1. Implement color changes
2. Run Chrome DevTools contrast check on each text element
3. Verify 4.5:1 minimum for normal text
4. Test with axe DevTools for comprehensive scan
5. Manual visual inspection in both themes

**Alternatives Considered**:
- Manual calculation: Rejected - error-prone and time-consuming
- Post-deployment testing only: Rejected - catch issues during development
- Single tool: Rejected - multiple tools provide better coverage

---

## Summary of Technical Decisions

| Area | Decision | Key Benefit |
|------|----------|-------------|
| Footer Styling | CSS custom properties with :root overrides | Theme-aware, maintainable |
| Chat Typography | Light mode color palette in CSS modules | Preserves dark mode, improves light mode |
| Module Images | Replace emoji with img tags | Better visuals, accessibility, SEO |
| Theme Switching | Use data-theme attribute selector | Automatic, no JavaScript needed |
| Contrast Testing | Chrome DevTools + WebAIM + axe | Comprehensive, real-time feedback |

## Dependencies

- No new dependencies required
- All changes use existing Docusaurus theme system
- CSS Modules already in use for component styling
- Image optimization can use existing build tools

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Images increase page load time | Optimize images to <200KB, use lazy loading |
| Light mode changes affect dark mode | Test both themes after every change |
| Contrast issues on different displays | Test on multiple devices and brightness levels |
| Module images not available | Implement fallback to gradient background |
| Browser compatibility issues | Test in Chrome, Firefox, Safari, Edge |

## Next Steps

Phase 1 will generate:
- data-model.md (N/A for UI-only feature)
- contracts/ (N/A for UI-only feature)
- quickstart.md (development and testing workflow)
