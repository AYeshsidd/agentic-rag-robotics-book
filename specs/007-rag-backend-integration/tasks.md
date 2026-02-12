# Implementation Tasks: Frontend–Backend Integration for RAG Chatbot

**Feature**: Frontend–Backend Integration for RAG Chatbot
**Branch**: `007-rag-backend-integration` | **Date**: 2026-02-07
**Spec**: [spec link](spec.md) | **Plan**: [plan link](plan.md)

## Implementation Strategy

Build the integration incrementally starting with the backend API (User Story 2), then adding frontend integration (User Story 1), and finally enhanced display features (User Story 3). Each user story will be independently testable and deliver value.

**MVP Scope**: User Story 2 (Backend API) + User Story 1 (Frontend Integration) - Core functionality to expose the RAG agent via API and enable frontend queries.

## Dependencies

User stories have the following dependencies:

**Story Order**: US2 → US1 → US3

- **US2 (Backend API)**: No dependencies on other stories - can start after Foundational phase
- **US1 (Frontend Integration)**: Depends on US2 completion (needs working API)
- **US3 (Enhanced Display)**: Depends on US1 completion (needs basic display working)

## Parallel Execution Examples

- T001-T003 (Setup) can run in parallel
- T010-T013 (Foundational models) can run in parallel
- T020-T021 (US2 endpoint implementation) can be developed in parallel with different endpoints
- T030-T032 (US1 frontend components) can be developed in parallel with backend work

---

## Phase 1: Setup

Initialize project dependencies and structure.

- [x] T001 [P] Install FastAPI and Uvicorn dependencies in backend/requirements.txt
- [x] T002 [P] Create backend/tests/ directory structure with test_api.py and test_integration.py
- [x] T003 [P] Verify existing backend/agent.py is accessible and functional

## Phase 2: Foundational

Implement core data models and FastAPI application structure that all user stories depend on.

- [x] T010 [P] Create QueryRequest Pydantic model in backend/api.py with query and limit fields
- [x] T011 [P] Create QueryResponse Pydantic model in backend/api.py with answer, confidence, and sources fields
- [x] T012 [P] Create SourceReference Pydantic model in backend/api.py with url and score fields
- [x] T013 [P] Create ErrorResponse Pydantic model in backend/api.py with error, detail, and status_code fields
- [x] T014 Initialize FastAPI application in backend/api.py with title and description
- [x] T015 Configure CORS middleware in backend/api.py to allow localhost:3000 and localhost:8000
- [x] T016 Implement get_agent() dependency injection function in backend/api.py to provide singleton RAGAgent instance

## Phase 3: [US2] Backend API Implementation (Priority: P2)

Implement the FastAPI backend that exposes RAG agent functionality through REST endpoints.

**Goal**: Enable developers to query the RAG agent through a reliable API endpoint with proper error handling and response formatting.

**Independent Test Criteria**: Make direct API calls to the FastAPI endpoint with sample queries and verify that properly formatted responses with answers and sources are returned.

- [x] T020 [US2] Implement POST /api/query endpoint in backend/api.py that accepts QueryRequest and returns QueryResponse
- [x] T021 [US2] Implement query endpoint logic to call agent.query_with_context() with request parameters in backend/api.py
- [x] T022 [US2] Add error handling for ValueError (400), generic exceptions (500), and service unavailable (503) in backend/api.py
- [x] T023 [US2] Implement GET /health endpoint in backend/api.py that returns service health status
- [x] T024 [US2] Add request validation error handling (422) for malformed requests in backend/api.py
- [x] T025 [US2] Transform agent response dictionary to QueryResponse model in backend/api.py
- [x] T026 [P] [US2] Create unit tests for /api/query endpoint in backend/tests/test_api.py
- [x] T027 [P] [US2] Create unit tests for request validation in backend/tests/test_api.py
- [x] T028 [P] [US2] Create unit tests for error handling in backend/tests/test_api.py
- [x] T029 [US2] Create integration test for full query flow in backend/tests/test_integration.py
- [x] T030 [US2] Test API with curl commands and verify responses match OpenAPI spec

## Phase 4: [US1] Frontend Integration (Priority: P1)

Implement the React chat interface that connects to the backend API and displays responses.

**Goal**: Enable users to submit natural language queries through the frontend and receive relevant, sourced answers.

**Independent Test Criteria**: Submit a natural language query through the frontend and verify that a relevant, sourced answer is returned within 10 seconds.

- [x] T040 [US1] Create ChatInterface.tsx component in docs/src/components/ with basic structure
- [x] T041 [US1] Implement query input field and submit button in ChatInterface.tsx
- [x] T042 [US1] Implement handleSubmit function with fetch API call to http://localhost:8000/api/query in ChatInterface.tsx
- [x] T043 [US1] Add loading state management (loading, setLoading) in ChatInterface.tsx
- [x] T044 [US1] Add response state management (response, setResponse) in ChatInterface.tsx
- [x] T045 [US1] Implement response display section showing answer text in ChatInterface.tsx
- [x] T046 [US1] Add error handling for network failures and display error messages in ChatInterface.tsx
- [x] T047 [US1] Add error handling for API error responses (400, 500, 503) in ChatInterface.tsx
- [x] T048 [US1] Create a page or integrate ChatInterface component into existing Docusaurus page
- [x] T049 [US1] Test end-to-end flow: submit query → receive response → display answer
- [x] T050 [US1] Verify "No relevant information found" message displays when no sources available

## Phase 5: [US3] Enhanced Display with Source Attribution (Priority: P3)

Add confidence indicators and source citations to enhance user trust and transparency.

**Goal**: Show confidence scores and source citations with each response so users can assess reliability and relevance.

**Independent Test Criteria**: Verify that response payloads include confidence scores and source references that are properly displayed in the frontend UI.

- [x] T060 [P] [US3] Add confidence score display in ChatInterface.tsx showing percentage or decimal value
- [x] T061 [P] [US3] Add sources list display in ChatInterface.tsx showing all source references
- [x] T062 [US3] Format each source reference with URL and similarity score in ChatInterface.tsx
- [x] T063 [US3] Make source URLs clickable links in ChatInterface.tsx
- [x] T064 [US3] Add visual styling for confidence levels (high/medium/low) in ChatInterface.tsx
- [x] T065 [US3] Test display with multiple sources and verify all are shown correctly
- [x] T066 [US3] Test display with zero sources and verify appropriate message is shown

## Phase 6: Polish & Cross-Cutting Concerns

Final improvements and quality enhancements across the system.

- [x] T070 [P] Add comprehensive logging for all API requests and responses in backend/api.py
- [x] T071 [P] Add API documentation comments and docstrings in backend/api.py
- [x] T072 [P] Update backend/README.md with API usage examples and setup instructions
- [x] T073 [P] Add TypeScript types for API request/response in ChatInterface.tsx
- [x] T074 Test API with various query types (short, long, special characters)
- [x] T075 Test error scenarios (Qdrant down, OpenAI rate limit, empty query)
- [x] T076 Verify response times are under 10 seconds for 95% of queries
- [x] T077 Run quickstart.md validation to ensure all setup steps work
- [x] T078 [P] Add input validation and sanitization in ChatInterface.tsx
- [x] T079 Final end-to-end testing with multiple query scenarios

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Story 2 (Phase 3)**: Depends on Foundational phase completion
- **User Story 1 (Phase 4)**: Depends on User Story 2 completion (needs working API)
- **User Story 3 (Phase 5)**: Depends on User Story 1 completion (needs basic display)
- **Polish (Phase 6)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 2 (Backend API)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 1 (Frontend Integration)**: DEPENDS on User Story 2 completion - Cannot start until API is working
- **User Story 3 (Enhanced Display)**: DEPENDS on User Story 1 completion - Builds on basic display

### Within Each User Story

- Models before endpoint implementation
- Endpoint implementation before tests
- Unit tests before integration tests
- Backend complete before frontend integration
- Basic display before enhanced display

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (T010-T013)
- Within US2: Unit tests (T026-T028) can run in parallel
- Within US3: Display components (T060-T061) can run in parallel
- Different developers can work on US2 and prepare US1 structure simultaneously

---

## Parallel Example: User Story 2 (Backend API)

```bash
# Launch all Pydantic models together:
Task: "Create QueryRequest Pydantic model in backend/api.py"
Task: "Create QueryResponse Pydantic model in backend/api.py"
Task: "Create SourceReference Pydantic model in backend/api.py"
Task: "Create ErrorResponse Pydantic model in backend/api.py"

# Launch all unit tests together after endpoint implementation:
Task: "Create unit tests for /api/query endpoint in backend/tests/test_api.py"
Task: "Create unit tests for request validation in backend/tests/test_api.py"
Task: "Create unit tests for error handling in backend/tests/test_api.py"
```

---

## Implementation Strategy

### MVP First (US2 + US1)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 2 (Backend API)
4. **STOP and VALIDATE**: Test API independently with curl/Postman
5. Complete Phase 4: User Story 1 (Frontend Integration)
6. **STOP and VALIDATE**: Test end-to-end flow
7. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 2 → Test API independently → API ready for integration
3. Add User Story 1 → Test end-to-end → Deploy/Demo (MVP!)
4. Add User Story 3 → Test enhanced display → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Developer A: User Story 2 (Backend API)
3. Once US2 is done:
   - Developer B: User Story 1 (Frontend Integration)
   - Developer A: Prepare User Story 3 components
4. Once US1 is done:
   - Developer B: User Story 3 (Enhanced Display)

---

## Notes

- [P] tasks = different files, no dependencies, can run in parallel
- [Story] label maps task to specific user story for traceability
- US1 depends on US2 even though US1 has higher priority (P1 vs P2)
- Each user story should be independently testable after completion
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Backend API must be running for frontend integration testing
- Use http://localhost:8000 for backend, http://localhost:3000 for frontend