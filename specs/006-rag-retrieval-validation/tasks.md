# Tasks: RAG Retrieval Pipeline Validation

**Input**: Design documents from `specs/006-rag-retrieval-validation/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md

**Tests**: This feature is a validation tool, so no separate test files will be created. The script itself serves as the test.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing.

## Format: `[ID] [P?] [Story] Description`

-   **[P]**: Can run in parallel (different files, no dependencies)
-   **[Story]**: Which user story this task belongs to (e.g., US1, US2)
-   Include exact file paths in descriptions

---

## Phase 1: Setup

**Purpose**: Prepare the project for the new validation script.

-   [X] T001 [P] Create the new validation script file `backend/validate_retrieval.py`.
-   [X] T002 [P] Add `typer` to the `dependencies` list in `backend/pyproject.toml`. 

---

## Phase 2: User Story 1 - Validate Ingestion via Retrieval (Priority: P1) 🎯 MVP

**Goal**: Implement the core logic for the validation script to connect to Qdrant, perform a similarity search with a user's query, and display the results.

**Independent Test**: Run `uv run python backend/validate_retrieval.py "your query"` from the command line. The script should connect to Qdrant, find relevant results, and print them to the console.

### Implementation for User Story 1

-   [X] T003 [US1] In `backend/validate_retrieval.py`, import necessary libraries: `os`, `logging`, `typer`, `cohere`, `qdrant_client`, and `dotenv`.
-   [X] T004 [US1] Set up basic logging and call `load_dotenv()` at the top of `backend/validate_retrieval.py`.
-   [X] T005 [US1] Implement the `get_cohere_client()` and `get_qdrant_client()` factory functions in `backend/validate_retrieval.py` (similar to `main.py`).
-   [X] T006 [US1] Define the main function `validate(query: str, limit: int = 3)` in `backend/validate_retrieval.py`, decorated with `@app.command()` from `typer`.
-   [X] T007 [US1] Inside  `validate`, initialize the Cohere and Qdrant clients.
-   [X] T008 [US1] Inside `validate`, generate an embedding for the user's `query` using the Cohere client.
-   [X] T009 [US1] Inside `validate`, perform a similarity search on the Qdrant collection using `qdrant_client.search()`, passing the query embedding and the `limit`.
-   [X] T010 [US1] Implement a check for the search results. If no results are returned, print a "No relevant documents found." message and exit.
-   [X] T011 [US1] Create the main execution block (`if __name__ == "__main__":`) in `backend/validate_retrieval.py` to run the `typer` app.

---

## Phase 3: User Story 2 - Verify Chunking and Metadata (Priority: P2)

**Goal**: Enhance the script to neatly display the full metadata for each retrieved chunk, allowing for manual verification.

**Independent Test**: Run the script with a query. The console output for each result should clearly show the similarity score and the full payload, including `source_url`, `section_identifier`, `chunk_index`, and `text_content`.

### Implementation for User Story 2

-   [X] T012 [US2] Inside the `validate` function in `backend/validate_retrieval.py`, loop through the search results.
-   [X] T013 [US2] For each result, print the similarity score (`result.score`).
-   [X] T014 [US2] For each result, print the full payload (`result.payload`) in a readable format (e.g., using `json.dumps` with indentation).

---

## Dependencies & Execution Order

### Phase Dependencies

-   **Setup (Phase 1)**: Must be completed first.
-   **User Story 1 (Phase 2)**: Depends on Setup completion. This phase delivers the core MVP.
-   **User Story 2 (Phase 3)**: Depends on User Story 1 completion.

### Parallel Opportunities

-   The two tasks in Phase 1 (T001, T002) can be executed in parallel.

## Implementation Strategy

### MVP First (User Story 1)

1.  Complete **Phase 1: Setup**.
2.  Complete all tasks in **Phase 2: User Story 1**.
3.  **STOP and VALIDATE**: The core validation script is now functional.

### Incremental Delivery

1.  After the MVP is validated, proceed to **Phase 3: User Story 2** to add detailed metadata display.
