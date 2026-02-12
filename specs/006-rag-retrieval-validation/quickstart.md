# Quickstart: RAG Retrieval Pipeline Validation

**Purpose**: To provide developers with simple, step-by-step instructions to set up and run the RAG retrieval validation script.

---

### Prerequisites

1.  **Completed Ingestion**: You must have already successfully run the RAG Ingestion Pipeline (`backend/main.py`) to populate your Qdrant Cloud collection with data.
2.  **Python Environment**: The same Python environment used for the ingestion pipeline (with `uv`, `python-dotenv`, `cohere`, and `qdrant-client` installed) should be used.
3.  **`.env` File**: The `backend/.env` file must be correctly configured with your `COHERE_API_KEY`, `QDRANT_URL`, `QDRANT_API_KEY`, and the correct `QDRANT_COLLECTION_NAME`.

---

### 1. Set Up the Environment

If you have not already done so, set up the Python environment from the `backend` directory:

```bash
# Navigate to the backend directory
cd backend

# Activate the virtual environment if it's not already active
# For macOS and Linux:
source .venv/bin/activate
# For Windows:
.venv\Scripts\activate
```

---

### 2. Run the Validation Script

The script is designed to be run from the command line with a query provided as an argument.

**Basic Usage**:

To run a similarity search, execute the script with your query in quotes:

```bash
uv run python validate_retrieval.py "What is a ROS 2 Node?"
```

**Example with Options**:

You can also specify the number of results to retrieve (defaults to 3):

```bash
uv run python validate_retrieval.py "Describe the publisher-subscriber pattern" --limit 5
```

---

### 3. Interpret the Output

The script will print the results to the console. For each retrieved document, you will see:

-   **Score**: A similarity score (higher is more relevant).
-   **Payload**: The full metadata of the chunk, including:
    -   `source_url`
    -   `section_identifier`
    -   `chunk_index`
    -   `text_content`

**Example Output**:

```
--- Result 1 ---
Score: 0.89
Payload:
{
  "source_url": "https://.../docs/ros2-nervous-system/chapter1",
  "section_identifier": "main",
  "chunk_index": 2,
  "text_content": "Definition: A Node is an executable process that performs computations. Each node is responsible for a single, modular purpose..."
}

--- Result 2 ---
...
```

If no relevant documents are found, the script will print a "No relevant documents found." message.
