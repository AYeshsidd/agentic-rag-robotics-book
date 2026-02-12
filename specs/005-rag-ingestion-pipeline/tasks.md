# Tasks: RAG Knowledge Ingestion Pipeline

**Input**: Design documents from `specs/005-rag-ingestion-pipeline/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md

**Tests**: Unit tests are included for User Story 2 to ensure data processing logic is correct, as outlined in the implementation plan.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2)
- Include exact file paths in descriptions

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure for the Python backend.

- [X] T001 Create the project directory `backend/` at the repository root.
- [X] T002 [P] Inside `backend/`, create an empty `main.py` file.
- [X] T003 [P] Inside `backend/`, create an empty directory named `tests/`.
- [X] T004 [P] Create the `backend/.env.example` file with placeholders for `COHERE_API_KEY`, `QDRANT_URL`, `QDRANT_API_KEY`, `QDRANT_COLLECTION_NAME`, and `SOURCE_URLS`.
- [X] T005 Initialize a `uv` project inside the `backend/` directory, creating a `pyproject.toml` file.
- [X] T006 Add the following dependencies to `backend/pyproject.toml`: `python-dotenv`, `requests`, `beautifulsoup4`, `cohere`, `qdrant-client`, `langchain`, and `pytest`.

**Checkpoint**: The basic Python project structure is now in place.

---

## Phase 2: User Story 1 - Configure and Run Ingestion Pipeline (Priority: P1) 🎯 MVP

**Goal**: Implement the complete end-to-end ingestion pipeline script, making it fully functional.

**Independent Test**: With a valid `.env` file in the `backend/` directory, run `python backend/main.py`. The script should execute without errors, and the processed vectors should appear in the specified Qdrant collection.

### Implementation for User Story 1

- [X] T007 [US1] Define the `ContentChunk` data class at the top of `backend/main.py` according to `data-model.md`.
- [X] T008 [US1] Implement environment variable loading at the start of `backend/main.py` using `dotenv`.
- [X] T009 [US1] Create a function `fetch_html(url: str) -> str` in `backend/main.py` to get raw HTML content using the `requests` library.
- [X] T010 [US1] Create a function `extract_text_from_html(html: str) -> str` in `backend/main.py` to parse and clean the HTML using `BeautifulSoup`.
- [X] T011 [US1] Create a function `chunk_text(text: str) -> list[str]` in `backend/main.py` using `langchain.text_splitter.RecursiveCharacterTextSplitter`.
- [X] T012 [US1] Implement client factory functions `get_cohere_client()` and `get_qdrant_client()` in `backend/main.py` that initialize and return the respective clients.
- [X] T013 [US1] Create a function `generate_embeddings(chunks: list[ContentChunk], cohere_client) -> list[dict]` in `backend/main.py` to generate embeddings in batches.
- [X] T014 [US1] Create a function `upsert_vectors_to_qdrant(records: list[dict], qdrant_client)` in `backend/main.py` to load the final records into Qdrant.
- [X] T015 [US1] Implement the main execution block (`if __name__ == "__main__":`) in `backend/main.py` to orchestrate the full pipeline: load env, fetch urls, process each url, and upsert the data.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently. The pipeline can be run from the command line.

---

## Phase 3: User Story 2 - Verify Content Processing (Priority: P2)

**Goal**: Add unit tests for the data processing functions to ensure their correctness and reliability.

**Independent Test**: From the `backend/` directory, run `uv run pytest`. All tests should pass.

### Implementation for User Story 2

- [X] T016 [P] [US2] Create the test file `backend/tests/test_extraction.py`.
- [X] T017 [US2] In `backend/tests/test_extraction.py`, write a unit test with a sample HTML string to verify that `extract_text_from_html` correctly extracts only the main article content.
- [X] T018 [P] [US2] Create the test file `backend/tests/test_chunking.py`.
- [X] T019 [US2] In `backend/tests/test_chunking.py`, write a unit test with a long string of text to verify that `chunk_text` correctly splits it into chunks of the expected size and overlap.

**Checkpoint**: At this point, the core data processing logic is verified by automated tests.

---

## Phase 4: Polish & Cross-Cutting Concerns

**Purpose**: Finalize the script with logging, documentation, and improved robustness.

- [X] T020 Add structured logging (e.g., using Python's `logging` module) throughout `backend/main.py` to report progress and errors.
- [X] T021 [P] Add comprehensive docstrings and type hints to all functions in `backend/main.py`.
- [X] T022 Manually execute the steps in `specs/005-rag-ingestion-pipeline/quickstart.md` to ensure it is accurate and complete.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: Must be completed first.
- **User Story 1 (Phase 2)**: Depends on Setup completion. This phase delivers the core MVP.
- **User Story 2 (Phase 3)**: Depends on the function definitions from User Story 1. It can be worked on after the relevant functions in `main.py` are defined.
- **Polish (Phase 4)**: Depends on the completion of User Story 1.

### Parallel Opportunities

- Within Phase 1, tasks T002, T003, and T004 can be done in parallel.
- Once the function signatures are defined in `main.py` (T009-T014), the corresponding tests in Phase 3 (T017, T019) can be written in parallel with the implementation of the function bodies.

---

## Implementation Strategy

### MVP First (User Story 1)

1.  Complete all tasks in **Phase 1: Setup**.
2.  Complete all tasks in **Phase 2: User Story 1**.
3.  **STOP and VALIDATE**: The core pipeline is now functional and delivers the primary value.

### Incremental Delivery

1.  After the MVP is validated, proceed to **Phase 3: User Story 2** to build confidence in the data processing logic with automated tests.
2.  Finally, complete **Phase 4: Polish** to make the script more robust and maintainable.
