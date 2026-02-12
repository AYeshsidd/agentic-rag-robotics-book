# Research: Home Page / Landing Page UI & UX Enhancement

**Feature**: 009-home-page-enhancement
**Date**: 2026-02-12
**Status**: Complete

## Overview

This document captures research findings and technical decisions for revamping the Docusaurus home page with professional AI/humanoid robotics aesthetics.

## Research Areas

### 1. Docusaurus Home Page Structure

**Decision**: Modify existing src/pages/index.tsx and create HomepageFeatures component

**Rationale**:
- Docusaurus uses React-based page components in src/pages/
- index.tsx is the home page entry point
- Component-based architecture allows modular development
- Existing Docusaurus projects often have HomepageFeatures for content sections

**Current Structure Analysis**:
- Home page likely has hero/banner section
- May have existing feature cards or content sections
- Footer is part of Docusaurus theme
- Custom CSS in src/css/custom.css for global overrides

**Implementation Approach**:
- Read current index.tsx to understand existing structure
- Enhance hero section with better typography and animations
- Create/modify HomepageFeatures for module cards
- Use CSS Modules for component-specific styling
- Use custom.css for global theme overrides

**Alternatives Considered**:
- Creating entirely new page: Rejected - would break existing navigation
- Using MDX instead of TSX: Rejected - less control over interactive elements
- Third-party component library: Rejected - adds unnecessary dependencies

---

### 2. Hero Section Design Patterns

**Decision**: Use gradient backgrounds, large typography, and glassmorphism buttons

**Rationale**:
- Gradient backgrounds create visual depth and AI/tech aesthetic
- Large, bold typography establishes clear hierarchy
- Glassmorphism (backdrop-filter) aligns with modern AI/robotics design trends
- Smooth animations create professional, polished feel

**Design Pattern**:
```tsx
<header className={styles.heroBanner}>
  <div className={styles.heroContent}>
    <h1 className={styles.heroTitle}>
      {/* Large, bold title with gradient text */}
    </h1>
    <p className={styles.heroSubtitle}>
      {/* Clear, concise subtitle */}
    </p>
    <div className={styles.heroButtons}>
      {/* Glassmorphism CTA buttons */}
    </div>
  </div>
</header>
```

**CSS Techniques**:
- Linear gradients for backgrounds
- Text gradients with background-clip
- Backdrop-filter for glassmorphism
- CSS animations with @keyframes
- Cubic-bezier easing for smooth motion

**Alternatives Considered**:
- Flat design: Rejected - less visually striking
- Video backgrounds: Rejected - performance concerns
- 3D graphics: Rejected - complexity and load time

---

### 3. Module Cards Implementation

**Decision**: Grid layout with card components containing image, title, description

**Rationale**:
- Cards are familiar UI pattern for content organization
- Grid layout provides clean, organized presentation
- Images on top create visual interest
- Hover effects provide interactivity feedback

**Component Structure**:
```tsx
const ModuleCard = ({ title, description, image, link }) => (
  <div className={styles.moduleCard}>
    <img src={image} alt={title} className={styles.moduleImage} />
    <h3 className={styles.moduleTitle}>{title}</h3>
    <p className={styles.moduleDescription}>{description}</p>
  </div>
);
```

**Layout Pattern**:
- CSS Grid for responsive layout
- 3 columns on desktop, 2 on tablet, 1 on mobile
- Gap between cards for breathing room
- Hover effects: scale, shadow, or glow

**Module Information Source**:
- Hardcoded in component (simplest approach)
- Could be extracted from Docusaurus sidebar config
- Images stored in static/img/modules/

**Alternatives Considered**:
- List layout: Rejected - less visually appealing
- Carousel/slider: Rejected - hides content, requires interaction
- Masonry layout: Rejected - unnecessary complexity

---

### 4. Animation Strategy

**Decision**: CSS animations with Intersection Observer for scroll-triggered effects

**Rationale**:
- CSS animations are performant (GPU-accelerated)
- Intersection Observer provides scroll-based triggering
- No JavaScript animation libraries needed
- Respects prefers-reduced-motion

**Animation Patterns**:

**Hero Fade-In**:
```css
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.heroBanner {
  animation: fadeInUp 0.8s cubic-bezier(0.4, 0, 0.2, 1);
}
```

**Staggered Card Animation**:
```tsx
// Use Intersection Observer in component
useEffect(() => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, index) => {
      if (entry.isIntersecting) {
        entry.target.style.animationDelay = `${index * 0.1}s`;
        entry.target.classList.add('animate-in');
      }
    });
  });
  // Observe card elements
}, []);
```

**Performance Considerations**:
- Use transform and opacity (GPU-accelerated)
- Avoid animating layout properties (width, height, top, left)
- Add will-change sparingly
- Respect prefers-reduced-motion

**Alternatives Considered**:
- Framer Motion: Rejected - adds 50KB+ to bundle
- GSAP: Rejected - overkill for simple animations
- React Spring: Rejected - unnecessary complexity

---

### 5. Glassmorphism Button Styling

**Decision**: Backdrop-filter with semi-transparent backgrounds and borders

**Rationale**:
- Creates modern, premium aesthetic
- Aligns with AI/robotics theme
- Good browser support (95%+ modern browsers)
- Graceful degradation for older browsers

**CSS Pattern**:
```css
.glassButton {
  background: linear-gradient(
    135deg,
    rgba(var(--ifm-color-primary-rgb), 0.9),
    rgba(var(--ifm-color-primary-rgb), 0.7)
  );
  backdrop-filter: blur(12px) saturate(180%);
  -webkit-backdrop-filter: blur(12px) saturate(180%);
  border: 1px solid rgba(255, 255, 255, 0.2);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.glassButton:hover {
  transform: translateY(-2px) scale(1.02);
  box-shadow: 0 6px 24px rgba(var(--ifm-color-primary-rgb), 0.3);
}

/* Fallback for unsupported browsers */
@supports not (backdrop-filter: blur(12px)) {
  .glassButton {
    background: var(--ifm-color-primary);
  }
}
```

**Alternatives Considered**:
- Solid buttons: Fallback only
- Neumorphism: Rejected - doesn't fit AI theme
- Flat material design: Rejected - less premium feel

---

### 6. Light/Dark Mode Color Strategy

**Decision**: Use Docusaurus CSS variables with enhanced contrast and AI-themed accents

**Rationale**:
- Docusaurus provides built-in theme switching
- CSS variables automatically adapt to theme
- Can enhance with custom color definitions
- Ensures consistency across the site

**Color Approach**:
```css
/* In custom.css */
:root {
  /* Light mode enhancements */
  --hero-gradient-start: #667eea;
  --hero-gradient-end: #764ba2;
  --card-bg: rgba(255, 255, 255, 0.9);
  --card-border: rgba(0, 0, 0, 0.1);
}

[data-theme='dark'] {
  /* Dark mode enhancements */
  --hero-gradient-start: #4c6ef5;
  --hero-gradient-end: #7950f2;
  --card-bg: rgba(30, 30, 30, 0.9);
  --card-border: rgba(255, 255, 255, 0.1);
}
```

**Testing Strategy**:
- Test all components in both themes
- Verify contrast ratios meet WCAG AA
- Check glassmorphism visibility in both modes
- Test on actual devices, not just DevTools

**Alternatives Considered**:
- Separate stylesheets: Rejected - harder to maintain
- JavaScript theme detection: Rejected - CSS variables are simpler
- Single theme only: Rejected - spec requires both modes

---

### 7. Footer Enhancement

**Decision**: Modify Docusaurus theme footer with custom styling

**Rationale**:
- Docusaurus footer is part of theme system
- Can be customized via docusaurus.config.js
- Can add custom CSS for styling improvements
- Maintains Docusaurus functionality

**Approach**:
- Update footer config in docusaurus.config.js
- Add custom CSS in custom.css for styling
- Improve layout with flexbox/grid
- Add glassmorphism effects if appropriate
- Ensure responsive design

**Alternatives Considered**:
- Swizzling footer component: Rejected - more complex, harder to maintain
- Third-party footer: Rejected - breaks Docusaurus integration

---

### 8. Chatbot Size Reduction

**Decision**: Reduce FloatingChatbot dimensions by additional 15-20%

**Rationale**:
- Already reduced in previous feature (008)
- Further reduction requested for home page context
- Should not compromise usability
- Maintains all functionality

**Size Adjustments**:
- Current: 340px × 510px
- Target: ~290px × 430px (15% reduction)
- Mobile: Maintain responsive percentages
- Button: Keep at 56-60px (already optimized)

**Implementation**:
- Modify FloatingChatbot.module.css
- Adjust font sizes if needed for readability
- Test on various screen sizes
- Ensure touch targets remain 44px+

---

### 9. Chatbot Hint/Greeting

**Decision**: Add subtle hint text near hero section or as floating tooltip

**Rationale**:
- Increases chatbot discoverability
- Provides context for new visitors
- Should be non-intrusive
- Can be dismissed or fade after time

**Placement Options**:
1. Below hero CTA buttons (recommended)
2. Floating tooltip near chatbot button
3. In hero subtitle text

**Implementation**:
```tsx
<div className={styles.chatbotHint}>
  <span className={styles.hintIcon}>💬</span>
  <p>Click the AI assistant (🤖) to get instant explanations from the book</p>
</div>
```

**Styling**:
- Subtle, not competing with main content
- Uses theme colors
- Optional fade-in animation
- Responsive on mobile

---

### 10. Responsive Design Strategy

**Decision**: Mobile-first approach with breakpoints at 768px and 1024px

**Rationale**:
- Mobile-first ensures core experience works everywhere
- Standard breakpoints align with common devices
- Docusaurus already uses these breakpoints
- Progressive enhancement for larger screens

**Breakpoints**:
- Mobile: < 768px (1 column, stacked layout)
- Tablet: 768px - 1024px (2 columns, adjusted spacing)
- Desktop: > 1024px (3 columns, full layout)

**Testing Devices**:
- Mobile: iPhone SE (375px), iPhone 12 (390px)
- Tablet: iPad (768px), iPad Pro (1024px)
- Desktop: 1920px, 2560px

---

## Technology Stack Summary

**Core Technologies**:
- React 18+ (existing)
- TypeScript (existing)
- Docusaurus 2.x (existing)
- CSS Modules (existing)

**New Techniques**:
- CSS gradients for hero backgrounds
- Backdrop-filter for glassmorphism
- CSS animations with @keyframes
- Intersection Observer for scroll animations
- CSS Grid for module card layout

**No New Dependencies Required**: All enhancements use native CSS, React, and Docusaurus features.

---

## Performance Considerations

**Optimization Strategies**:
1. Use CSS transforms (GPU-accelerated) for animations
2. Optimize images for web (< 200KB each, WebP format)
3. Lazy load module card images
4. Use will-change only during active animations
5. Implement @supports for graceful degradation
6. Respect prefers-reduced-motion

**Expected Impact**:
- Page load increase: < 200ms (within performance goal)
- Animation performance: 60fps on modern devices
- Image loading: Progressive with lazy loading
- CSS bundle increase: ~3-5KB

---

## Accessibility Considerations

**WCAG AA Compliance**:
- Maintain 4.5:1 contrast ratio for text
- Ensure focus states are visible
- Support keyboard navigation
- Respect prefers-reduced-motion
- Add appropriate alt text for images
- Ensure touch targets are 44px minimum

**Implementation**:
```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## Implementation Risks & Mitigations

**Risk 1**: Backdrop-filter not supported in older browsers
- **Mitigation**: @supports fallback to solid backgrounds

**Risk 2**: Animations cause performance issues on low-end devices
- **Mitigation**: Use GPU-accelerated properties, respect prefers-reduced-motion

**Risk 3**: Module images not available or slow to load
- **Mitigation**: Lazy loading, placeholder images, optimized formats

**Risk 4**: Chatbot size reduction makes mobile interaction difficult
- **Mitigation**: Test thoroughly on mobile, maintain responsive sizing

**Risk 5**: Light/dark mode colors don't provide sufficient contrast
- **Mitigation**: Test both themes, use contrast checker tools

---

## Open Questions

None - all technical decisions are resolved and documented above.
