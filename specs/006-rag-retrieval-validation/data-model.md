# Data Model: RAG Retrieval Pipeline Validation

**Purpose**: To define the data structures for the validation script's inputs and outputs.

---

### Entity: `Query`

-   **Description**: Represents the user's input to the validation script. This is the text that will be used to search for similar content in the vector database.
-   **Attributes**:
    -   `query_text` (string, required): The natural language query provided by the user via the command line.

---

### Entity: `SearchResult`

-   **Description**: Represents a single result returned from the Qdrant vector database search. It contains the retrieved data point and its similarity score.
-   **Attributes**:
    -   `id` (string/UUID, required): The unique identifier of the vector point in the Qdrant collection.
    -   `score` (float, required): The similarity score between the query vector and the result vector. A higher score indicates greater similarity.
    -   `payload` (object, required): The metadata associated with the vector. This will match the structure of the `ContentChunk` from the ingestion pipeline, containing:
        -   `source_url` (string)
        -   `section_identifier` (string)
        -   `chunk_index` (integer)
        -   `text_content` (string)

---

## Data Flow Diagram

```
[User Input (Query Text)]
        |
        v
[Validation Script CLI]
        |
        v
[Cohere Client] -> Generates a query vector
        |
        v
[Qdrant Client] -> Performs similarity search with the query vector
        |
        v
[Qdrant Database] -> Returns a list of [SearchResult] objects
        |
        v
[Validation Script Display] -> Formats and prints the SearchResult text and metadata
```
