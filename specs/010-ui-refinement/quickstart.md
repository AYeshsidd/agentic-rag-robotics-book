# Quickstart Guide: Frontend UI Refinement

**Feature**: 010-ui-refinement
**Date**: 2026-02-12
**Purpose**: Development workflow and testing guide for UI refinement implementation

## Prerequisites

- Node.js 18+ and npm installed
- Repository cloned and dependencies installed (`npm install`)
- Branch `010-ui-refinement` checked out
- Docusaurus development server knowledge

## Development Setup

### 1. Start Development Server

```bash
cd /path/to/physical_book2
npm start
```

This starts the Docusaurus dev server at http://localhost:3000 with hot reload enabled.

### 2. File Locations

**Files to Modify**:
- `src/css/custom.css` - Footer light mode colors
- `src/components/FloatingChatbot.module.css` - Chat interface typography
- `src/components/HomepageFeatures/index.tsx` - Module card image integration
- `src/components/HomepageFeatures/styles.module.css` - Module card styling

**Files to Add**:
- `static/img/modules/*.jpg` or `*.webp` - Custom module images (6 images)

### 3. Development Workflow

**For Footer Visibility (P1)**:
1. Open `src/css/custom.css`
2. Locate footer-related CSS variables or `.footer` class
3. Add light mode color overrides in `:root` selector
4. Test in browser with light mode enabled
5. Verify contrast with Chrome DevTools (4.5:1 minimum)
6. Ensure dark mode unchanged by switching themes

**For Chat Interface Typography (P2)**:
1. Open `src/components/FloatingChatbot.module.css`
2. Add light mode specific styles for text, backgrounds, borders
3. Test by opening chatbot in light mode
4. Send test messages and verify readability
5. Check contrast ratios for all text elements
6. Verify dark mode unchanged

**For Module Card Images (P3)**:
1. Add 6 optimized images to `static/img/modules/`
2. Open `src/components/HomepageFeatures/index.tsx`
3. Update image paths in ModuleList array
4. Replace emoji placeholder with img element
5. Add error handling for failed image loads
6. Test on home page with both themes

## Testing Checklist

### Visual Testing

**Footer (Light Mode)**:
- [ ] Footer text is clearly readable (not gray/faded)
- [ ] Footer links are visible and distinguishable
- [ ] Hover states work and are visible
- [ ] Copyright text is readable
- [ ] Dark mode footer unchanged

**Chat Interface (Light Mode)**:
- [ ] Chat window background is appropriate
- [ ] Message text has good contrast
- [ ] Input field border is visible
- [ ] Placeholder text is readable
- [ ] Buttons are visible and clickable
- [ ] Glassmorphism effects maintained
- [ ] Dark mode chat unchanged

**Module Cards**:
- [ ] All 6 cards display custom images (not emojis)
- [ ] Images load within 2 seconds
- [ ] Hover effects work with images
- [ ] Cards are responsive on mobile
- [ ] Fallback works if image fails
- [ ] Alt text present for accessibility

### Contrast Testing

**Using Chrome DevTools**:
1. Right-click on text element → Inspect
2. In Styles panel, click color value
3. Color picker shows contrast ratio
4. Verify 4.5:1 or higher for normal text
5. Verify 3:1 or higher for large text

**Using WebAIM Contrast Checker**:
1. Go to https://webaim.org/resources/contrastchecker/
2. Input foreground color (text)
3. Input background color
4. Check WCAG AA compliance (4.5:1)

**Elements to Test**:
- Footer text on footer background
- Footer links on footer background
- Chat message text on message background
- Chat input text on input background
- Module card text on card background

### Responsive Testing

**Breakpoints to Test**:
- Mobile: 320px, 375px, 414px
- Tablet: 768px, 834px, 1024px
- Desktop: 1280px, 1440px, 1920px

**Test in Chrome DevTools**:
1. Open DevTools (F12)
2. Click device toolbar icon (Ctrl+Shift+M)
3. Select device or enter custom dimensions
4. Verify layout, text size, image sizing

**What to Check**:
- Footer text wraps properly on narrow screens
- Chat interface remains usable on mobile
- Module cards stack correctly (3 → 2 → 1 columns)
- Images scale appropriately
- No horizontal scrolling

### Theme Switching Testing

**Test Procedure**:
1. Start in light mode
2. Verify all changes look correct
3. Switch to dark mode (theme toggle in navbar)
4. Verify dark mode unchanged from before
5. Switch back to light mode
6. Verify changes still correct
7. Repeat 3-4 times to test stability

**What to Verify**:
- Footer colors change appropriately
- Chat interface adapts correctly
- Module cards maintain styling
- No flashing or transition issues
- Smooth theme transitions

### Browser Compatibility Testing

**Browsers to Test**:
- Chrome (latest)
- Firefox (latest)
- Safari (latest, if on Mac)
- Edge (latest)

**What to Check**:
- CSS custom properties work
- Glassmorphism effects render (or fallback works)
- Images load correctly
- Hover effects work
- Theme switching works

### Accessibility Testing

**Keyboard Navigation**:
- [ ] Tab through footer links
- [ ] Tab through chat interface
- [ ] Tab through module cards
- [ ] Focus states visible
- [ ] Enter key activates links/buttons

**Screen Reader Testing** (Optional):
- Use NVDA (Windows) or VoiceOver (Mac)
- Navigate footer and verify content read
- Navigate chat interface
- Navigate module cards
- Verify alt text on images

**axe DevTools Extension**:
1. Install axe DevTools browser extension
2. Open extension on page
3. Click "Scan ALL of my page"
4. Review and fix any issues
5. Focus on contrast and accessibility violations

## Common Issues and Solutions

### Issue: Footer text still hard to read in light mode

**Solution**:
- Check if `:root` selector is being overridden
- Verify CSS specificity (may need `!important` temporarily)
- Use darker color: `#1c1e21` instead of gray
- Test contrast ratio with DevTools

### Issue: Chat interface text invisible in light mode

**Solution**:
- Ensure `color` property set explicitly for light mode
- Check if parent element has conflicting styles
- Verify CSS module class names are correct
- Use `var(--ifm-font-color-base)` for theme-aware color

### Issue: Module images not loading

**Solution**:
- Verify image paths start with `/img/modules/`
- Check file names match exactly (case-sensitive)
- Ensure images are in `static/img/modules/` directory
- Check browser console for 404 errors
- Verify image file sizes (<200KB)

### Issue: Dark mode affected by changes

**Solution**:
- Ensure changes only in `:root` selector, not `[data-theme='dark']`
- Test dark mode after every change
- Use CSS variables that respect theme
- Don't use hardcoded colors that override theme

### Issue: Glassmorphism not working in some browsers

**Solution**:
- Check if `backdrop-filter` supported
- Add fallback: `@supports not (backdrop-filter: blur(12px)) { ... }`
- Use solid background as fallback
- Test in target browsers

## Performance Verification

### Image Optimization

**Check Image Sizes**:
```bash
ls -lh static/img/modules/
```

All images should be <200KB. If larger:
- Use image optimization tools (ImageOptim, Squoosh)
- Convert to WebP format
- Reduce dimensions if too large

### CSS Bundle Size

**Before Changes**:
```bash
npm run build
# Note the CSS bundle size in build output
```

**After Changes**:
```bash
npm run build
# Compare CSS bundle size
# Should increase by <10KB
```

### Page Load Testing

**Using Chrome DevTools**:
1. Open DevTools → Network tab
2. Disable cache
3. Reload page
4. Check "Finish" time
5. Should be <100ms increase from baseline

## Deployment Checklist

Before merging to main:

- [ ] All visual tests pass
- [ ] All contrast tests pass (4.5:1 minimum)
- [ ] Responsive design works on all breakpoints
- [ ] Theme switching works smoothly
- [ ] Browser compatibility verified
- [ ] Accessibility tests pass
- [ ] Images optimized (<200KB each)
- [ ] CSS bundle size acceptable
- [ ] Dark mode unchanged
- [ ] No console errors
- [ ] Code reviewed
- [ ] Manual testing on staging environment

## Quick Reference

**Start Dev Server**: `npm start`
**Build for Production**: `npm run build`
**Serve Production Build**: `npm run serve`

**Key Files**:
- Footer: `src/css/custom.css`
- Chat: `src/components/FloatingChatbot.module.css`
- Modules: `src/components/HomepageFeatures/`

**Testing Tools**:
- Chrome DevTools (F12)
- WebAIM Contrast Checker: https://webaim.org/resources/contrastchecker/
- axe DevTools Extension

**Target Metrics**:
- Contrast: 4.5:1 minimum (WCAG AA)
- Image size: <200KB each
- CSS increase: <10KB
- Page load increase: <100ms
