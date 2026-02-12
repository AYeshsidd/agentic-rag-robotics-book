# Quickstart: Home Page / Landing Page UI & UX Enhancement

**Feature**: 009-home-page-enhancement
**Date**: 2026-02-12

## Overview

This guide covers setup, development, and testing for the Home Page Enhancement feature - a comprehensive UI/UX revamp with professional AI/humanoid robotics aesthetics.

## Prerequisites

- Node.js 16+ installed
- Existing Docusaurus project running
- Frontend server accessible
- Basic understanding of React and CSS

## Quick Start

### 1. Verify Current Setup

```bash
# Ensure you're on the feature branch
git branch --show-current
# Should show: 009-home-page-enhancement

# Start Docusaurus development server
npm start
# Should start on http://localhost:3000
```

### 2. Locate Files to Modify

```bash
# Home page
src/pages/index.tsx

# Module cards component (may need to create)
src/components/HomepageFeatures/index.tsx
src/components/HomepageFeatures/styles.module.css

# Chatbot component
src/components/FloatingChatbot.tsx
src/components/FloatingChatbot.module.css

# Global styles
src/css/custom.css

# Module images (to be added)
static/img/modules/
```

### 3. Development Workflow

**Start Development Server**:
```bash
npm start
```

**Open Browser**:
- Navigate to http://localhost:3000
- View home page changes in real-time
- Toggle light/dark mode to test both themes

**Hot Reload**:
- Changes to .tsx and .css files auto-reload
- No server restart needed

### 4. Testing Checklist

**Visual Testing**:
```bash
# Test in browser
1. Open http://localhost:3000
2. Verify hero section with new design
3. Scroll to see module cards
4. Check footer improvements
5. Toggle light/dark mode
6. Resize browser window (test responsive)
```

**Animation Testing**:
```bash
# In browser DevTools
1. Open Performance tab
2. Reload page
3. Verify hero fade-in animation
4. Scroll to module cards
5. Verify staggered card animations
6. Check 60fps performance
```

**Responsive Testing**:
```bash
# In browser DevTools
1. Open Device Toolbar (Ctrl+Shift+M)
2. Test on:
   - iPhone SE (375px)
   - iPad (768px)
   - Desktop (1920px)
3. Verify layout adapts correctly
4. Check touch targets are 44px minimum
```

## Key Implementation Areas

### 1. Hero Section Redesign

**What to do**: Update hero section in src/pages/index.tsx

**Key changes**:
- Improve typography (larger, bolder headings)
- Add gradient background
- Implement glassmorphism buttons
- Add fade-in animation

**Test**: Load home page, verify hero looks professional and animates smoothly

---

### 2. Module Cards Creation

**What to do**: Create/modify HomepageFeatures component

**Key changes**:
- Create card component with image, title, description
- Implement CSS Grid layout (3 columns desktop, 2 tablet, 1 mobile)
- Add hover effects (scale, shadow)
- Add scroll-triggered animations

**Test**: Scroll to module section, verify cards display and animate

---

### 3. Glassmorphism Buttons

**What to do**: Add glassmorphism styling to all buttons

**Pattern**:
```css
backdrop-filter: blur(12px) saturate(180%);
background: linear-gradient(135deg, rgba(...), rgba(...));
border: 1px solid rgba(255, 255, 255, 0.2);
```

**Test**: Hover over buttons, verify glass effect and smooth transitions

---

### 4. Footer Enhancement

**What to do**: Update footer styling in custom.css

**Key changes**:
- Improve layout and spacing
- Add better typography
- Ensure responsive design

**Test**: Scroll to footer, verify improved appearance

---

### 5. Chatbot Size Reduction

**What to do**: Adjust FloatingChatbot dimensions

**Current**: 340px × 510px
**Target**: ~290px × 430px (15% reduction)

**Test**: Open chatbot, verify smaller size but still usable

---

### 6. Chatbot Hint Text

**What to do**: Add hint text about chatbot on home page

**Placement**: Below hero CTA buttons or near chatbot

**Text**: "Click the AI assistant (🤖) to get instant explanations from the book"

**Test**: Verify hint is visible and non-intrusive

---

## Common Issues & Solutions

### Issue 1: Animations are janky

**Symptom**: Animations stutter or drop frames

**Solution**:
```css
/* Use GPU-accelerated properties */
transform: translateY(20px); /* ✅ Correct */
top: 20px; /* ❌ Wrong - causes reflow */

/* Add will-change during animation */
.animating {
  will-change: transform, opacity;
}
```

---

### Issue 2: Glassmorphism not visible

**Symptom**: Buttons look solid, not translucent

**Solution**:
```css
/* Check browser support */
@supports (backdrop-filter: blur(12px)) {
  /* Glass effect here */
}

/* Ensure there's content behind to blur */
/* Glass effect only works over other elements */
```

---

### Issue 3: Module cards not responsive

**Symptom**: Cards don't stack properly on mobile

**Solution**:
```css
/* Use CSS Grid with responsive columns */
.moduleGrid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

@media (max-width: 768px) {
  .moduleGrid {
    grid-template-columns: 1fr;
  }
}
```

---

### Issue 4: Light/dark mode colors don't work

**Symptom**: Colors don't adapt when switching themes

**Solution**:
```css
/* Use CSS variables that adapt to theme */
background: var(--ifm-background-color); /* ✅ Correct */
background: #ffffff; /* ❌ Wrong - hardcoded */

/* Define custom variables for both themes */
:root {
  --hero-gradient-start: #667eea;
}

[data-theme='dark'] {
  --hero-gradient-start: #4c6ef5;
}
```

---

## Performance Verification

### Check Animation Performance

```bash
# In Chrome DevTools
1. Open Performance tab
2. Enable "Screenshots" and "Web Vitals"
3. Click Record
4. Reload page and scroll through content
5. Stop recording
6. Verify:
   - FPS stays at 60
   - No long tasks (>50ms)
   - Animations complete in <500ms
```

### Check Page Load Impact

```bash
# In Chrome DevTools Network tab
1. Hard refresh (Ctrl+Shift+R)
2. Check total load time
3. Verify increase is <200ms from baseline
4. Check image sizes are <200KB each
```

---

## Accessibility Testing

### Keyboard Navigation

```bash
1. Tab through page elements
2. Verify all buttons are focusable
3. Verify focus states are visible
4. Test Enter key on buttons
5. Verify logical tab order
```

### Screen Reader Testing

```bash
# With NVDA or JAWS
1. Navigate through hero section
2. Verify headings are announced correctly
3. Navigate to module cards
4. Verify card content is readable
5. Check image alt text is present
```

### Reduced Motion

```bash
# In browser settings
1. Enable "Reduce motion" preference
2. Reload page
3. Verify animations are minimal/instant
4. Check page is still usable
```

---

## Deployment Checklist

Before merging to main:

- [ ] Hero section displays correctly in light mode ✓
- [ ] Hero section displays correctly in dark mode ✓
- [ ] Module cards display with images and descriptions ✓
- [ ] All buttons use glassmorphism styling ✓
- [ ] Animations are smooth (60fps) ✓
- [ ] Responsive design works (mobile, tablet, desktop) ✓
- [ ] Footer has improved styling ✓
- [ ] Chatbot hint text is visible ✓
- [ ] Chatbot size is reduced appropriately ✓
- [ ] Browser compatibility (Chrome, Firefox, Safari, Edge) ✓
- [ ] Accessibility (keyboard, screen reader, reduced motion) ✓
- [ ] No backend/API changes (verify git diff) ✓
- [ ] Page load increase <200ms ✓
- [ ] Color contrast meets WCAG AA ✓

---

## Rollback Plan

If issues are discovered after deployment:

```bash
# Revert to previous version
git revert <commit-hash>

# Or checkout previous files
git checkout HEAD~1 -- src/pages/index.tsx
git checkout HEAD~1 -- src/components/HomepageFeatures/
git checkout HEAD~1 -- src/css/custom.css
```

---

## Support & Resources

**Documentation**:
- [Docusaurus Pages](https://docusaurus.io/docs/creating-pages)
- [Docusaurus Styling](https://docusaurus.io/docs/styling-layout)
- [CSS Backdrop Filter](https://developer.mozilla.org/en-US/docs/Web/CSS/backdrop-filter)
- [CSS Animations](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Animations)
- [Intersection Observer](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API)

**Related Files**:
- Spec: `specs/009-home-page-enhancement/spec.md`
- Research: `specs/009-home-page-enhancement/research.md`
- Plan: `specs/009-home-page-enhancement/plan.md`

**Testing**:
- Frontend runs on port 3000
- Use browser DevTools for performance and responsive testing
- Test in both light and dark modes
- Verify on actual mobile devices when possible
