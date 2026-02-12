---
description: "Task list for Home Page / Landing Page UI & UX Enhancement"
---

# Tasks: Home Page / Landing Page UI & UX Enhancement

**Input**: Design documents from `/specs/009-home-page-enhancement/`
**Prerequisites**: plan.md, spec.md, research.md, quickstart.md

**Tests**: No test tasks included (manual browser testing per quickstart.md)

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4)
- Include exact file paths in descriptions

## Path Conventions

- **Frontend**: `src/pages/`, `src/components/`, `src/css/` at repository root
- **Static assets**: `static/img/modules/`
- No backend modifications (out of scope)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Verify existing structure and prepare for UI enhancements

- [X] T001 Verify Docusaurus development server runs successfully (npm start)
- [X] T002 Read current src/pages/index.tsx to understand existing home page structure
- [X] T003 [P] Check if src/components/HomepageFeatures/ exists, read if present
- [X] T004 [P] Read src/components/FloatingChatbot.tsx and FloatingChatbot.module.css to understand current chatbot implementation
- [X] T005 [P] Read src/css/custom.css to understand current global styles and theme variables

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Prepare module images and establish base styling patterns

**⚠️ CRITICAL**: These tasks establish the foundation for all user stories

- [X] T006 Create static/img/modules/ directory for module card images
- [X] T007 Add placeholder or actual module images to static/img/modules/ (5-10 images, optimized <200KB each)
- [X] T008 Define CSS custom properties for glassmorphism and AI-themed colors in src/css/custom.css for both light and dark modes

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Hero Section Transformation (Priority: P1) 🎯 MVP

**Goal**: Redesign hero section with professional AI-themed styling, improved typography, glassmorphism buttons, and smooth entrance animation

**Independent Test**: Load home page at http://localhost:3000, verify hero section displays with improved typography, AI-themed gradient background, glassmorphism buttons with hover effects, and smooth fade-in animation in both light and dark modes

### Implementation for User Story 1

- [X] T009 [US1] Update hero section layout and structure in src/pages/index.tsx with improved semantic HTML
- [X] T010 [US1] Implement hero section typography improvements in src/pages/index.tsx (larger headings, better hierarchy, gradient text effects)
- [X] T011 [US1] Add AI-themed gradient background to hero section in src/pages/index.tsx or create src/pages/index.module.css
- [X] T012 [US1] Implement glassmorphism styling for hero CTA buttons in src/pages/index.tsx or src/pages/index.module.css
- [X] T013 [US1] Add smooth entrance animation (fade-in) for hero section using CSS @keyframes in src/pages/index.tsx or src/pages/index.module.css
- [X] T014 [US1] Ensure hero section is responsive across mobile, tablet, and desktop in src/pages/index.tsx or src/pages/index.module.css
- [X] T015 [US1] Test hero section in both light and dark modes, adjust colors for proper contrast and visibility

**Checkpoint**: Hero section should be fully functional with professional AI-themed styling, animations, and responsive design

---

## Phase 4: User Story 2 - Module Cards Display (Priority: P2)

**Goal**: Create module cards section with images, titles, descriptions, hover effects, and responsive grid layout

**Independent Test**: Scroll below hero section, verify module cards display in grid layout (3 columns desktop, 2 tablet, 1 mobile) with images on top, titles, descriptions, hover effects, and proper styling in both themes

### Implementation for User Story 2

- [X] T016 [US2] Create or modify src/components/HomepageFeatures/index.tsx with module card component structure
- [X] T017 [US2] Create or modify src/components/HomepageFeatures/styles.module.css with CSS Grid layout for responsive module cards
- [X] T018 [US2] Add module data (names, descriptions, image paths) to src/components/HomepageFeatures/index.tsx
- [X] T019 [US2] Implement hover effects (scale, shadow, glow) for module cards in src/components/HomepageFeatures/styles.module.css
- [X] T020 [US2] Add scroll-triggered staggered entrance animations for module cards using Intersection Observer in src/components/HomepageFeatures/index.tsx
- [X] T021 [US2] Ensure module cards are responsive and stack properly on mobile/tablet in src/components/HomepageFeatures/styles.module.css
- [X] T022 [US2] Test module cards in both light and dark modes, adjust card backgrounds and borders for proper contrast

**Checkpoint**: Module cards section should display with images, descriptions, animations, and work independently of other features

---

## Phase 5: User Story 3 - Content Enhancement & Animations (Priority: P3)

**Goal**: Improve overall page content typography, spacing, readability, and add smooth animations; enhance footer styling

**Independent Test**: Load page and observe smooth animations throughout, verify improved text spacing and readability, scroll to footer and verify improved styling and layout

### Implementation for User Story 3

- [X] T023 [P] [US3] Improve global typography and spacing in src/css/custom.css (headings, paragraphs, line-height, letter-spacing)
- [X] T024 [P] [US3] Add CSS animation utilities in src/css/custom.css for fade-in, slide-up effects with prefers-reduced-motion support
- [X] T025 [US3] Enhance footer styling and layout in src/css/custom.css (better spacing, typography, responsive design)
- [X] T026 [US3] Apply glassmorphism styling to any remaining buttons on the page in src/css/custom.css
- [X] T027 [US3] Test all animations for 60fps performance using browser DevTools Performance tab
- [X] T028 [US3] Verify prefers-reduced-motion preference is respected (animations disabled/minimal when enabled)

**Checkpoint**: Page content should have improved readability, smooth animations throughout, and enhanced footer styling

---

## Phase 6: User Story 4 - Chatbot Integration & Polish (Priority: P4)

**Goal**: Add chatbot hint text on home page, reduce chatbot interface size, fix fonts/colors for light/dark modes, apply glassmorphism to chatbot buttons

**Independent Test**: View home page and see chatbot hint text, open chatbot and verify reduced size (~290x430px), check fonts and colors are clear in both light and dark modes, verify glassmorphism buttons

### Implementation for User Story 4

- [X] T029 [US4] Add chatbot hint/greeting text to home page in src/pages/index.tsx (e.g., below hero CTA buttons or as floating tooltip)
- [X] T030 [US4] Reduce chatbot interface dimensions in src/components/FloatingChatbot.module.css (from 340x510px to ~290x430px, 15% reduction)
- [X] T031 [US4] Fix chatbot fonts and colors for light mode in src/components/FloatingChatbot.module.css (ensure clear visibility and contrast)
- [X] T032 [US4] Fix chatbot fonts and colors for dark mode in src/components/FloatingChatbot.module.css (ensure clear visibility and contrast)
- [X] T033 [US4] Apply glassmorphism styling to chatbot buttons in src/components/FloatingChatbot.module.css (consistent with page buttons)
- [X] T034 [US4] Test chatbot on mobile devices to ensure reduced size is still usable and touch targets are 44px minimum

**Checkpoint**: Chatbot should have hint text on page, reduced size, improved styling in both themes, and glassmorphism buttons

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Final validation, optimization, and cross-browser testing

- [X] T035 [P] Run full responsive design testing per quickstart.md (320px to 2560px width)
- [X] T036 [P] Verify color contrast meets WCAG AA standards in both light and dark modes using contrast checker tools
- [X] T037 [P] Test keyboard navigation and focus states for all interactive elements
- [X] T038 [P] Verify all images have appropriate alt text for accessibility
- [X] T039 [P] Test page load performance and verify increase is <200ms from baseline
- [X] T040 [P] Test in multiple browsers (Chrome, Firefox, Safari, Edge) and verify glassmorphism fallbacks work
- [X] T041 Optimize any large images or CSS if performance goals not met
- [X] T042 Run final validation checklist from quickstart.md deployment section

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-6)**: All depend on Foundational phase completion
  - User stories can proceed sequentially in priority order (P1 → P2 → P3 → P4)
  - Or in parallel if multiple developers available
- **Polish (Phase 7)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Independent of US1 but may reference hero section styling patterns
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - Independent but enhances US1 and US2
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - Independent of other stories

### Within Each User Story

- Tasks within a story should generally be completed in order
- Some tasks marked [P] can run in parallel (different files)
- Test each story independently before moving to next priority

### Parallel Opportunities

- Phase 1: T003, T004, T005 can run in parallel (reading different files)
- Phase 2: T007 and T008 can run in parallel (images vs CSS)
- Phase 5: T023, T024, T025, T026 can run in parallel (different concerns in CSS)
- Phase 7: T035, T036, T037, T038, T039, T040 can run in parallel (different testing activities)

---

## Parallel Example: Phase 1 Setup

```bash
# Launch all file reading tasks together:
Task: "Check if src/components/HomepageFeatures/ exists, read if present"
Task: "Read src/components/FloatingChatbot.tsx and FloatingChatbot.module.css"
Task: "Read src/css/custom.css to understand current global styles"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T005)
2. Complete Phase 2: Foundational (T006-T008)
3. Complete Phase 3: User Story 1 (T009-T015)
4. **STOP and VALIDATE**: Test hero section independently in browser
5. Demo/review if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Demo (MVP - Hero Section!)
3. Add User Story 2 → Test independently → Demo (MVP + Module Cards!)
4. Add User Story 3 → Test independently → Demo (MVP + Content Polish!)
5. Add User Story 4 → Test independently → Demo (Complete Feature!)
6. Each story adds value without breaking previous stories

### Sequential Strategy (Single Developer)

1. Complete phases in order: Setup → Foundational → US1 → US2 → US3 → US4 → Polish
2. Test each user story independently before moving to next
3. Commit after completing each user story phase

---

## Notes

- [P] tasks = different files or independent concerns, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Manual testing via browser per quickstart.md (no automated tests)
- Commit after each user story phase completion
- Stop at any checkpoint to validate story independently
- All changes are frontend-only - no backend/API/RAG modifications
- Use browser DevTools for performance, responsive, and accessibility testing
