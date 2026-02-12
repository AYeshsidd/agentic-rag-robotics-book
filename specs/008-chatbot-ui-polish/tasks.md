# Tasks: Chatbot UI Polish

**Input**: Design documents from `/specs/008-chatbot-ui-polish/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md

**Tests**: No test tasks included (not requested in specification)

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Frontend**: `src/components/` at repository root
- All changes isolated to FloatingChatbot component files

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Verify current implementation and prepare for enhancements

- [x] T001 Verify FloatingChatbot component is working in src/components/FloatingChatbot.tsx
- [x] T002 Verify current styling in src/components/FloatingChatbot.module.css
- [x] T003 Test chatbot functionality (open/close, send message) on http://localhost:3000

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 Document current dimensions (400x600) and colors for comparison baseline
- [x] T005 Verify Docusaurus theme variables are available in browser DevTools

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Visual Theme Integration (Priority: P1) 🎯 MVP

**Goal**: Chatbot seamlessly matches Docusaurus book theme in both light and dark modes

**Independent Test**: Open chatbot on any page, toggle light/dark mode (moon/sun icon), verify colors/fonts/spacing match book theme

### Implementation for User Story 1

- [x] T006 [US1] Replace hardcoded primary colors with var(--ifm-color-primary) in src/components/FloatingChatbot.module.css
- [x] T007 [US1] Replace hardcoded background colors with var(--ifm-background-color) in src/components/FloatingChatbot.module.css
- [x] T008 [US1] Replace hardcoded text colors with var(--ifm-font-color-base) in src/components/FloatingChatbot.module.css
- [x] T009 [US1] Replace border/emphasis colors with var(--ifm-color-emphasis-*) in src/components/FloatingChatbot.module.css
- [x] T010 [US1] Update font-family to use var(--ifm-font-family-base) in src/components/FloatingChatbot.module.css
- [x] T011 [US1] Test chatbot in light mode - verify colors match book theme
- [x] T012 [US1] Test chatbot in dark mode - verify colors match book theme
- [x] T013 [US1] Verify color contrast meets WCAG AA standards in both modes

**Checkpoint**: At this point, User Story 1 should be fully functional - chatbot matches theme in both light and dark modes

---

## Phase 4: User Story 2 - Enhanced Interaction Design (Priority: P2)

**Goal**: Smooth, polished interactions with glass effects, animations, and robotic icon

**Independent Test**: Click floating button to open/close, hover over buttons, verify smooth animations and glass effects

### Implementation for User Story 2

- [x] T014 [P] [US2] Add glass effect to floating button using backdrop-filter in src/components/FloatingChatbot.module.css
- [x] T015 [P] [US2] Add glass effect to submit/clear buttons using backdrop-filter in src/components/FloatingChatbot.module.css
- [x] T016 [US2] Add @supports fallback for browsers without backdrop-filter support in src/components/FloatingChatbot.module.css
- [x] T017 [US2] Create @keyframes slideUp animation for chat window open in src/components/FloatingChatbot.module.css
- [x] T018 [US2] Add closing animation (reverse slideUp or fadeOut) in src/components/FloatingChatbot.module.css
- [x] T019 [US2] Add cubic-bezier easing to all transitions in src/components/FloatingChatbot.module.css
- [x] T020 [US2] Add hover effects to floating button (scale transform) in src/components/FloatingChatbot.module.css
- [x] T021 [US2] Add hover effects to submit/clear buttons (translateY, shadow) in src/components/FloatingChatbot.module.css
- [x] T022 [US2] Add hover effects to close button in src/components/FloatingChatbot.module.css
- [x] T023 [US2] Change floating button icon from 💬 to 🤖 in src/components/FloatingChatbot.tsx
- [x] T024 [US2] Add will-change property for animated elements in src/components/FloatingChatbot.module.css
- [x] T025 [US2] Test open animation completes in 200-400ms using browser DevTools Performance tab
- [x] T026 [US2] Test close animation completes in 200-400ms using browser DevTools Performance tab
- [x] T027 [US2] Test hover effects respond within 100ms
- [x] T028 [US2] Verify animations maintain 60fps (no frame drops)

**Checkpoint**: At this point, User Stories 1 AND 2 should both work - theme integration + smooth interactions

---

## Phase 5: User Story 3 - Optimized Layout and Responsiveness (Priority: P3)

**Goal**: Appropriately sized chatbot that works well on all devices without being intrusive

**Independent Test**: Open chatbot on desktop (1920px), tablet (768px), and mobile (375px), verify appropriate sizing and touch-friendly elements

### Implementation for User Story 3

- [x] T029 [US3] Reduce chatWindow width from 400px to 340px in src/components/FloatingChatbot.module.css
- [x] T030 [US3] Reduce chatWindow height from 600px to 510px in src/components/FloatingChatbot.module.css
- [x] T031 [US3] Update max-width to calc(100vw - 48px) for smaller screens in src/components/FloatingChatbot.module.css
- [x] T032 [US3] Update max-height to calc(100vh - 100px) for smaller screens in src/components/FloatingChatbot.module.css
- [x] T033 [US3] Add responsive breakpoint for tablets (768px) with 90vw width, 70vh height in src/components/FloatingChatbot.module.css
- [x] T034 [US3] Add responsive breakpoint for mobile (<768px) with 95vw width, 80vh height in src/components/FloatingChatbot.module.css
- [x] T035 [US3] Reduce floating button size on mobile (56px instead of 60px) in src/components/FloatingChatbot.module.css
- [x] T036 [US3] Verify touch targets are minimum 44px on mobile devices
- [x] T037 [US3] Test on desktop (1920px width) - verify chatbot is less intrusive than before
- [x] T038 [US3] Test on tablet (768px width) - verify appropriate sizing and touch-friendly
- [x] T039 [US3] Test on mobile (375px width) - verify appropriate sizing and touch-friendly
- [x] T040 [US3] Test on very small screens (320px width) - verify chatbot doesn't break layout
- [x] T041 [US3] Test with browser zoom at 150% and 200% - verify usability

**Checkpoint**: All user stories should now be independently functional - theme integration + interactions + responsive layout

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories and final validation

- [x] T042 [P] Add @media (prefers-reduced-motion) support to disable/minimize animations in src/components/FloatingChatbot.module.css
- [x] T043 [P] Verify keyboard navigation still works (Tab to button, Enter to open)
- [x] T044 [P] Test rapid open/close clicks - verify no animation conflicts
- [x] T045 [P] Test theme switching while chatbot is open - verify smooth transition
- [x] T046 [P] Verify screen reader compatibility (aria-labels still work)
- [x] T047 Test in Chrome (latest version) - verify all features work
- [x] T048 Test in Firefox (latest version) - verify all features work
- [x] T049 Test in Safari (latest version) - verify all features work
- [x] T050 Test in Edge (latest version) - verify all features work
- [x] T051 Verify CSS file size increase is less than 3KB
- [x] T052 Verify page load time impact is less than 50ms
- [x] T053 Verify all existing chat functionality works (send/receive messages, display sources)
- [x] T054 Run through quickstart.md validation checklist
- [x] T055 Visual comparison: Take screenshots before/after to document improvements

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-5)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Phase 6)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Independent of US1 (different CSS properties)
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - Independent of US1/US2 (different CSS properties)

### Within Each User Story

- **US1**: All color replacement tasks can run in parallel (different CSS properties)
- **US2**: Glass effects (T014-T016) can run in parallel, animations (T017-T019) can run in parallel, hover effects (T020-T022) can run in parallel
- **US3**: Dimension changes (T029-T032) can run together, responsive breakpoints (T033-T035) can run in parallel

### Parallel Opportunities

- **Phase 1**: T001, T002, T003 can run in parallel (verification tasks)
- **Phase 2**: T004, T005 can run in parallel (documentation tasks)
- **Phase 3 (US1)**: T006-T010 can all run in parallel (different CSS properties in same file)
- **Phase 4 (US2)**: T014-T016 (glass effects), T017-T019 (animations), T020-T022 (hover effects) can each group run in parallel
- **Phase 5 (US3)**: T029-T032 (dimensions), T033-T035 (responsive) can run in parallel
- **Phase 6**: T042-T046 can all run in parallel (different concerns)
- **All three user stories (Phase 3-5) can be worked on in parallel by different developers** since they modify different CSS properties

---

## Parallel Example: User Story 1

```bash
# Launch all color replacement tasks together (all modify different CSS properties):
Task: "Replace hardcoded primary colors with var(--ifm-color-primary)"
Task: "Replace hardcoded background colors with var(--ifm-background-color)"
Task: "Replace hardcoded text colors with var(--ifm-font-color-base)"
Task: "Replace border/emphasis colors with var(--ifm-color-emphasis-*)"
Task: "Update font-family to use var(--ifm-font-family-base)"
```

## Parallel Example: User Story 2

```bash
# Launch glass effect tasks together:
Task: "Add glass effect to floating button using backdrop-filter"
Task: "Add glass effect to submit/clear buttons using backdrop-filter"
Task: "Add @supports fallback for browsers without backdrop-filter support"

# Then launch animation tasks together:
Task: "Create @keyframes slideUp animation for chat window open"
Task: "Add closing animation (reverse slideUp or fadeOut)"
Task: "Add cubic-bezier easing to all transitions"
```

## Parallel Example: All User Stories

```bash
# After Foundational phase completes, launch all three user stories in parallel:
Developer A: Phase 3 (US1 - Visual Theme Integration)
Developer B: Phase 4 (US2 - Enhanced Interaction Design)
Developer C: Phase 5 (US3 - Optimized Layout and Responsiveness)

# Each developer works independently on different CSS properties
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T003)
2. Complete Phase 2: Foundational (T004-T005)
3. Complete Phase 3: User Story 1 (T006-T013)
4. **STOP and VALIDATE**: Test theme integration in both light and dark modes
5. Deploy/demo if ready - chatbot now matches book theme!

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 (T006-T013) → Test independently → Deploy/Demo (MVP - theme integration!)
3. Add User Story 2 (T014-T028) → Test independently → Deploy/Demo (+ smooth interactions!)
4. Add User Story 3 (T029-T041) → Test independently → Deploy/Demo (+ responsive layout!)
5. Add Polish (T042-T055) → Final validation → Deploy/Demo (complete!)

Each story adds value without breaking previous stories.

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together (T001-T005)
2. Once Foundational is done:
   - Developer A: User Story 1 (T006-T013) - Theme integration
   - Developer B: User Story 2 (T014-T028) - Interactions & animations
   - Developer C: User Story 3 (T029-T041) - Layout & responsiveness
3. Stories complete independently, then merge
4. Team completes Polish together (T042-T055)

---

## Task Summary

**Total Tasks**: 55

**By Phase**:
- Phase 1 (Setup): 3 tasks
- Phase 2 (Foundational): 2 tasks
- Phase 3 (US1 - Theme Integration): 8 tasks
- Phase 4 (US2 - Interaction Design): 15 tasks
- Phase 5 (US3 - Layout & Responsiveness): 13 tasks
- Phase 6 (Polish): 14 tasks

**By User Story**:
- User Story 1 (P1): 8 tasks
- User Story 2 (P2): 15 tasks
- User Story 3 (P3): 13 tasks
- Infrastructure/Polish: 19 tasks

**Parallel Opportunities**: 25 tasks marked [P] can run in parallel

**MVP Scope**: Phase 1 + Phase 2 + Phase 3 (13 tasks total) delivers theme integration

---

## Notes

- [P] tasks = different CSS properties or independent concerns, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- All changes are in CSS/component files - no backend modifications
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Test in both light and dark modes after each user story
- Verify existing chat functionality remains intact throughout
