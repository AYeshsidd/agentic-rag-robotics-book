# Quickstart: Chatbot UI Polish

**Feature**: 008-chatbot-ui-polish
**Date**: 2026-02-12

## Overview

This guide covers setup, development, and testing for the Chatbot UI Polish feature - a visual enhancement of the existing floating chatbot with professional, AI-humanoid robotics aesthetics.

## Prerequisites

- Node.js 16+ installed
- Existing Docusaurus project running
- FloatingChatbot component already implemented
- Backend RAG system running on port 8001 (for functional testing)

## Quick Start

### 1. Verify Current Setup

```bash
# Ensure you're on the feature branch
git branch --show-current
# Should show: 008-chatbot-ui-polish

# Check that frontend is running
npm start
# Should start Docusaurus on http://localhost:3000
```

### 2. Locate Files to Modify

```bash
# Component file
src/components/FloatingChatbot.tsx

# Styling file
src/components/FloatingChatbot.module.css
```

### 3. Development Workflow

**Start Development Server**:
```bash
npm start
```

**Open Browser**:
- Navigate to http://localhost:3000
- Open any page (chatbot appears globally)
- Click the floating button (💬) to test

**Hot Reload**:
- Changes to .tsx and .css files auto-reload
- No server restart needed

### 4. Testing Checklist

**Visual Testing**:
```bash
# Test in browser
1. Open http://localhost:3000
2. Toggle light/dark mode (moon/sun icon in navbar)
3. Verify chatbot matches theme colors
4. Test on different pages
5. Resize browser window (test responsive design)
```

**Functional Testing**:
```bash
# Ensure backend is running
cd backend
uvicorn api:app --host 0.0.0.0 --port 8001 --reload

# Test chat functionality
1. Click floating button
2. Enter question: "What is ROS2?"
3. Verify response displays correctly
4. Check sources are clickable
5. Close chatbot with X button
```

**Animation Testing**:
```bash
# In browser DevTools
1. Open Performance tab
2. Click floating button (open chatbot)
3. Stop recording
4. Verify 60fps during animation
5. Check animation duration (should be 200-400ms)
```

**Responsive Testing**:
```bash
# In browser DevTools
1. Open Device Toolbar (Ctrl+Shift+M)
2. Test on:
   - iPhone SE (375px)
   - iPad (768px)
   - Desktop (1920px)
3. Verify chatbot is appropriately sized
4. Check touch targets are 44px minimum
```

## Key Implementation Areas

### 1. Theme Integration

**What to do**: Update CSS to use Docusaurus theme variables

**Files**: `FloatingChatbot.module.css`

**Key variables**:
```css
var(--ifm-color-primary)
var(--ifm-background-color)
var(--ifm-font-color-base)
var(--ifm-color-emphasis-300)
```

**Test**: Toggle light/dark mode, verify colors adapt

---

### 2. Glass Effect Buttons

**What to do**: Add glassmorphism styling to interactive buttons

**Files**: `FloatingChatbot.module.css`

**Pattern**:
```css
backdrop-filter: blur(10px) saturate(180%);
background: rgba(255, 255, 255, 0.1);
border: 1px solid rgba(255, 255, 255, 0.2);
```

**Test**: Verify glass effect on buttons, check fallback in older browsers

---

### 3. Smooth Animations

**What to do**: Add CSS animations for open/close transitions

**Files**: `FloatingChatbot.module.css`

**Pattern**:
```css
@keyframes slideUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
```

**Test**: Click open/close rapidly, verify smooth transitions

---

### 4. Reduced Window Size

**What to do**: Adjust chatWindow dimensions

**Files**: `FloatingChatbot.module.css`

**Current**: 400px × 600px
**Target**: 340px × 510px (15% reduction)

**Test**: Measure with DevTools, verify readability

---

### 5. Robotic Icon

**What to do**: Update floating button icon

**Files**: `FloatingChatbot.tsx`

**Current**: 💬
**Target**: 🤖

**Test**: Verify icon displays correctly across browsers

---

## Common Issues & Solutions

### Issue 1: Theme colors not applying

**Symptom**: Chatbot doesn't match light/dark theme

**Solution**:
```css
/* Ensure you're using CSS variables, not hardcoded colors */
background: var(--ifm-background-color); /* ✅ Correct */
background: #ffffff; /* ❌ Wrong */
```

---

### Issue 2: Animations are janky

**Symptom**: Animations stutter or drop frames

**Solution**:
```css
/* Use GPU-accelerated properties */
transform: translateY(20px); /* ✅ Correct */
top: 20px; /* ❌ Wrong - causes reflow */

/* Add will-change during animation */
.chatWindow {
  will-change: transform, opacity;
}
```

---

### Issue 3: Glass effect not visible

**Symptom**: Buttons look solid, not translucent

**Solution**:
```css
/* Check browser support */
@supports (backdrop-filter: blur(10px)) {
  /* Glass effect here */
}

/* Ensure there's content behind to blur */
/* Glass effect only works over other elements */
```

---

### Issue 4: Mobile chatbot too small

**Symptom**: Chatbot is tiny on mobile devices

**Solution**:
```css
/* Use responsive sizing */
@media (max-width: 768px) {
  .chatWindow {
    width: 95vw;
    height: 80vh;
  }
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
4. Open/close chatbot 3 times
5. Stop recording
6. Verify:
   - FPS stays at 60
   - No long tasks (>50ms)
   - Animation completes in 200-400ms
```

### Check CSS Load Impact

```bash
# In Chrome DevTools Network tab
1. Hard refresh (Ctrl+Shift+R)
2. Find FloatingChatbot.module.css
3. Verify size increase is <3KB
4. Check load time is <50ms
```

---

## Accessibility Testing

### Keyboard Navigation

```bash
1. Tab through page elements
2. Verify floating button is focusable
3. Press Enter to open chatbot
4. Tab through chatbot elements
5. Press Escape to close (if implemented)
```

### Screen Reader Testing

```bash
# With NVDA or JAWS
1. Navigate to floating button
2. Verify aria-label is announced
3. Open chatbot
4. Verify content is readable
5. Close chatbot
```

### Reduced Motion

```bash
# In browser settings
1. Enable "Reduce motion" preference
2. Open chatbot
3. Verify animations are minimal/instant
```

---

## Deployment Checklist

Before merging to main:

- [ ] Visual testing in light mode ✓
- [ ] Visual testing in dark mode ✓
- [ ] Functional testing (send/receive messages) ✓
- [ ] Animation performance (60fps) ✓
- [ ] Responsive design (mobile, tablet, desktop) ✓
- [ ] Browser compatibility (Chrome, Firefox, Safari, Edge) ✓
- [ ] Accessibility (keyboard, screen reader, reduced motion) ✓
- [ ] No backend/API changes (verify git diff) ✓
- [ ] CSS file size increase <3KB ✓
- [ ] Load time impact <50ms ✓

---

## Rollback Plan

If issues are discovered after deployment:

```bash
# Revert to previous version
git revert <commit-hash>

# Or checkout previous component files
git checkout HEAD~1 -- src/components/FloatingChatbot.tsx
git checkout HEAD~1 -- src/components/FloatingChatbot.module.css
```

---

## Support & Resources

**Documentation**:
- [Docusaurus Theming](https://docusaurus.io/docs/styling-layout)
- [CSS Backdrop Filter](https://developer.mozilla.org/en-US/docs/Web/CSS/backdrop-filter)
- [CSS Animations](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Animations)

**Related Files**:
- Spec: `specs/008-chatbot-ui-polish/spec.md`
- Research: `specs/008-chatbot-ui-polish/research.md`
- Plan: `specs/008-chatbot-ui-polish/plan.md`

**Testing**:
- Backend must be running on port 8001 for functional tests
- Frontend runs on port 3000
- Use browser DevTools for performance and responsive testing
