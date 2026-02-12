---
description: "Task list for Frontend UI Refinement"
---

# Tasks: Frontend UI Refinement

**Input**: Design documents from `/specs/010-ui-refinement/`
**Prerequisites**: plan.md, spec.md, research.md, quickstart.md

**Tests**: No test tasks included (manual browser testing per quickstart.md)

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Frontend**: `src/css/`, `src/components/`, `src/pages/` at repository root
- **Static assets**: `static/img/modules/`
- No backend modifications (out of scope)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Verify existing structure and understand current implementation

- [X] T001 Verify Docusaurus development server runs successfully (npm start)
- [X] T002 Read src/css/custom.css to understand current footer styling and CSS variables
- [X] T003 [P] Read src/components/FloatingChatbot.module.css to understand current chat interface styling
- [X] T004 [P] Read src/components/HomepageFeatures/index.tsx to understand current module card implementation
- [X] T005 [P] Read src/components/HomepageFeatures/styles.module.css to understand current module card styling

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Prepare assets and verify theme system

**⚠️ CRITICAL**: These tasks establish the foundation for all user stories

- [X] T006 Verify Docusaurus theme switching works correctly (test light/dark mode toggle)
- [X] T007 Create or verify static/img/modules/ directory exists for module images
- [X] T008 Document current footer colors in light and dark modes for comparison baseline

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Footer Visibility Enhancement (Priority: P1) 🎯 MVP

**Goal**: Fix footer text contrast in light mode to meet WCAG AA standards while preserving dark mode appearance

**Independent Test**: Switch to light mode, scroll to footer, verify all text is clearly readable with 4.5:1 contrast ratio. Switch to dark mode and verify footer unchanged.

### Implementation for User Story 1

- [X] T009 [US1] Add light mode footer color overrides in src/css/custom.css using :root selector
- [X] T010 [US1] Set footer text color to #1c1e21 or similar dark color for light mode in src/css/custom.css
- [X] T011 [US1] Set footer link colors to ensure visibility and distinguish from regular text in src/css/custom.css
- [X] T012 [US1] Define footer link hover state colors for light mode in src/css/custom.css
- [X] T013 [US1] Test footer in light mode and verify contrast ratio with Chrome DevTools (minimum 4.5:1)
- [X] T014 [US1] Test footer in dark mode and verify appearance unchanged from baseline
- [X] T015 [US1] Test theme switching between light and dark modes to ensure smooth transitions

**Checkpoint**: Footer should be fully readable in light mode with proper contrast, dark mode unchanged

---

## Phase 4: User Story 2 - Chat Interface Typography Upgrade (Priority: P2)

**Goal**: Improve chat interface typography and visibility in light mode with professional appearance

**Independent Test**: Open chatbot in light mode, send messages, verify text is readable with clear contrast and professional styling. Verify dark mode unchanged.

### Implementation for User Story 2

- [X] T016 [US2] Add light mode text color overrides for chat messages in src/components/FloatingChatbot.module.css
- [X] T017 [US2] Add light mode background color for chat window in src/components/FloatingChatbot.module.css
- [X] T018 [US2] Add light mode border styling for chat input field in src/components/FloatingChatbot.module.css
- [X] T019 [US2] Add light mode placeholder text color for input field in src/components/FloatingChatbot.module.css
- [X] T020 [US2] Adjust glassmorphism button opacity for better visibility in light mode in src/components/FloatingChatbot.module.css
- [X] T021 [US2] Add light mode message bubble background colors in src/components/FloatingChatbot.module.css
- [X] T022 [US2] Test chat interface in light mode and verify contrast ratios with Chrome DevTools (minimum 4.5:1)
- [X] T023 [US2] Test chat interface in dark mode and verify appearance unchanged
- [X] T024 [US2] Test sending and receiving messages in both themes to ensure readability

**Checkpoint**: Chat interface should have professional typography and clear visibility in light mode, dark mode unchanged

---

## Phase 5: User Story 3 - Module Card Image Enhancement (Priority: P3)

**Goal**: Replace emoji placeholders with custom images for professional visual appeal

**Independent Test**: View home page modules section, verify all 6 cards display custom images instead of 📚 emoji, images load quickly and are responsive.

### Implementation for User Story 3

- [X] T025 [P] [US3] Add 6 optimized module images to static/img/modules/ directory (<200KB each, WebP or JPG format)
- [X] T026 [US3] Update ModuleList array in src/components/HomepageFeatures/index.tsx with correct image paths
- [X] T027 [US3] Replace emoji placeholder with img element in ModuleCard component in src/components/HomepageFeatures/index.tsx
- [X] T028 [US3] Add error handling for failed image loads in src/components/HomepageFeatures/index.tsx
- [X] T029 [US3] Add alt text to all module images for accessibility in src/components/HomepageFeatures/index.tsx
- [X] T030 [US3] Update CSS for moduleImage class in src/components/HomepageFeatures/styles.module.css (object-fit: cover, width/height 100%)
- [X] T031 [US3] Update imagePlaceholder CSS to hide by default in src/components/HomepageFeatures/styles.module.css
- [X] T032 [US3] Test module cards on home page and verify all images display correctly
- [X] T033 [US3] Test image loading performance with browser DevTools Network tab (should load within 2 seconds)
- [X] T034 [US3] Test module cards in both light and dark modes to ensure proper styling

**Checkpoint**: All module cards should display custom images with proper fallbacks and responsive behavior

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final validation, cross-browser testing, and accessibility verification

- [X] T035 [P] Run full responsive design testing per quickstart.md (320px to 2560px width)
- [X] T036 [P] Verify all color contrasts meet WCAG AA standards using WebAIM Contrast Checker
- [X] T037 [P] Test keyboard navigation for footer links, chat interface, and module cards
- [X] T038 [P] Verify focus states are visible in light mode for all interactive elements
- [X] T039 [P] Test in Chrome browser and verify all changes work correctly
- [X] T040 [P] Test in Firefox browser and verify all changes work correctly
- [X] T041 [P] Test in Edge browser and verify all changes work correctly
- [X] T042 [P] Test rapid theme switching to ensure no visual glitches or transition issues
- [X] T043 Verify CSS bundle size increase is acceptable (<10KB) with npm run build
- [X] T044 Run final validation checklist from quickstart.md deployment section

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-5)**: All depend on Foundational phase completion
  - User stories can proceed sequentially in priority order (P1 → P2 → P3)
  - Or in parallel if multiple developers available
- **Polish (Phase 6)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Independent of US1
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - Independent of US1 and US2

### Within Each User Story

- Tasks within a story should generally be completed in order
- Some tasks marked [P] can run in parallel (different files or independent concerns)
- Test each story independently before moving to next priority

### Parallel Opportunities

- Phase 1: T003, T004, T005 can run in parallel (reading different files)
- Phase 5: T025 can run in parallel with other tasks (adding images is independent)
- Phase 6: T035, T036, T037, T038, T039, T040, T041, T042 can run in parallel (different testing activities)

---

## Parallel Example: Phase 1 Setup

```bash
# Launch all file reading tasks together:
Task: "Read src/components/FloatingChatbot.module.css"
Task: "Read src/components/HomepageFeatures/index.tsx"
Task: "Read src/components/HomepageFeatures/styles.module.css"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T005)
2. Complete Phase 2: Foundational (T006-T008)
3. Complete Phase 3: User Story 1 (T009-T015)
4. **STOP and VALIDATE**: Test footer visibility independently in browser
5. Demo/review if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Demo (MVP - Footer Fixed!)
3. Add User Story 2 → Test independently → Demo (MVP + Chat Improved!)
4. Add User Story 3 → Test independently → Demo (Complete Feature!)
5. Each story adds value without breaking previous stories

### Sequential Strategy (Single Developer)

1. Complete phases in order: Setup → Foundational → US1 → US2 → US3 → Polish
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
- Use browser DevTools for contrast checking and performance testing
- Dark mode must remain unchanged throughout all modifications
