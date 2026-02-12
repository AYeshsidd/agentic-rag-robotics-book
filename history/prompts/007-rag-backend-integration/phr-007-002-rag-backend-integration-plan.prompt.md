---
id: phr-007-002
title: rag-backend-integration-plan
stage: plan
date: 2026-02-07T23:00:00Z
surface: cli
model: claude-sonnet-4-5
feature: 007-rag-backend-integration
branch: 007-rag-backend-integration
user: developer
command: /sp.plan
labels: [planning, fastapi, backend-integration, api-design]
links:
  spec: specs/007-rag-backend-integration/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - path: specs/007-rag-backend-integration/plan.md
    action: created
    lines: 83
  - path: specs/007-rag-backend-integration/research.md
    action: created
    lines: 180
  - path: specs/007-rag-backend-integration/data-model.md
    action: created
    lines: 200
  - path: specs/007-rag-backend-integration/contracts/openapi.yaml
    action: created
    lines: 280
  - path: specs/007-rag-backend-integration/quickstart.md
    action: created
    lines: 280
  - path: CLAUDE.md
    action: updated
    lines: 32
tests: []
---

## Prompt

User requested implementation planning for: "Frontend–Backend Integration — Spec 4"

Key requirements:
- Set up FastAPI backend to expose RAG agent functionality
- Create a POST endpoint (e.g., /chat) to receive user queries
- Integrate existing agent.py logic to process incoming queries
- Return responses with source references in JSON format
- Handle errors and fallback responses gracefully
- Connect Docusaurus frontend to the backend API using fetch
- Enable users to submit questions from the book interface
- Display agent answers and source links in the UI
- Maintain conversation context for follow-up queries
- Test end-to-end flow locally (frontend → backend → Qdrant)
- Ensure deterministic and grounded responses
- Validate retrieval and response display correctness

## Response snapshot

Created comprehensive implementation plan with:

**Phase 0: Research**
- FastAPI integration patterns with existing Python modules
- CORS configuration for local development
- Error handling patterns for API wrappers
- Request/response models with Pydantic
- Frontend integration with Docusaurus
- Testing strategy (unit, integration, contract tests)

**Phase 1: Design & Contracts**
- Data model with 4 entities: QueryRequest, QueryResponse, SourceReference, ErrorResponse
- OpenAPI 3.0 specification with complete API contracts
- Quickstart guide with setup instructions and examples
- Agent context updated in CLAUDE.md

**Technical Decisions**:
- Use FastAPI dependency injection for RAGAgent singleton
- Enable CORS for localhost:3000 (Docusaurus) and localhost:8000 (FastAPI)
- Implement structured error responses with HTTP status codes
- Use Pydantic models for validation and serialization
- React component with fetch API for backend communication
- Three-layer testing: unit, integration, contract

**Constitution Check**: All principles satisfied
- Library-First: api.py wraps existing agent.py
- CLI Interface: Preserves existing CLI, adds HTTP interface
- Test-First: Unit tests before implementation
- Integration Testing: Full flow verification
- Observability: Leverages FastAPI and agent.py logging

## Outcome

- ✅ Impact: Complete implementation plan ready for task generation
- 🧪 Tests: Testing strategy defined (unit, integration, contract)
- 📁 Files: 5 files created (plan.md, research.md, data-model.md, openapi.yaml, quickstart.md), 1 updated (CLAUDE.md)
- 🔁 Next prompts: /sp.tasks to generate task breakdown, /sp.implement to execute implementation
- 🧠 Reflection: Plan successfully balances technical requirements with constitution principles. FastAPI integration maintains separation of concerns while reusing existing agent.py functionality.

## Evaluation notes (flywheel)

- Failure modes observed: None - planning completed successfully
- Graders run and results (PASS/FAIL): Constitution Check PASS, all design artifacts complete
- Prompt variant (if applicable): Standard /sp.plan workflow
- Next experiment (smallest change to try): Proceed to task generation with /sp.tasks