# Implementation Plan: Frontend UI Refinement

**Branch**: `010-ui-refinement` | **Date**: 2026-02-12 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/010-ui-refinement/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Refine the frontend UI to improve light mode visibility and professional appearance. This includes fixing footer text contrast in light mode, upgrading chat interface typography for better readability, and replacing module card emojis with custom images. All changes are CSS/JSX only with no backend, API, or RAG modifications. Dark mode appearance remains unchanged.

## Technical Context

**Language/Version**: TypeScript/JavaScript (React 18+, ES2020+)
**Primary Dependencies**: Docusaurus 2.x, React, CSS Modules (existing)
**Storage**: N/A (UI-only feature, no data persistence)
**Testing**: Manual browser testing (visual inspection, contrast checking)
**Target Platform**: Modern web browsers (Chrome, Firefox, Safari, Edge - last 2 versions)
**Project Type**: Web (frontend only)
**Performance Goals**: <100ms CSS load increase, images <200KB each, maintain 60fps animations
**Constraints**: Frontend-only changes, no backend/API/RAG modifications, dark mode unchanged, WCAG AA contrast (4.5:1)
**Scale/Scope**: 3 components (footer, chat interface, module cards), ~200-400 lines of CSS/JSX changes

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

**Status**: No project constitution found (constitution.md is template only)

**Assessment**: N/A - Proceeding without constitution gates. This is a straightforward UI refinement with clear boundaries (frontend-only, no architectural changes).

## Project Structure

### Documentation (this feature)

```text
specs/010-ui-refinement/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command) - N/A for UI-only
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command) - N/A for UI-only
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
src/
├── pages/
│   └── index.js                     # Home page - NO CHANGES (already has module cards)
├── components/
│   ├── HomepageFeatures/            # Module cards - MODIFY (replace emoji with images)
│   │   ├── index.tsx
│   │   └── styles.module.css
│   ├── FloatingChatbot.tsx          # Chat interface - MODIFY (typography, light mode)
│   └── FloatingChatbot.module.css   # Chat styles - MODIFY
└── css/
    └── custom.css                   # Global styles - MODIFY (footer light mode)

static/
└── img/
    └── modules/                     # Module images - ADD (custom images for cards)

backend/                             # NO MODIFICATIONS (out of scope)
```

**Structure Decision**: This is a web application with existing Docusaurus structure. Changes are focused on CSS styling for light mode (footer, chat interface) and replacing module card emoji placeholders with actual images. No new components needed - only modifications to existing files.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

N/A - No constitution violations as no constitution exists.
