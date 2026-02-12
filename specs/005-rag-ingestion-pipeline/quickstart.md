# Quickstart: RAG Ingestion Pipeline

**Purpose**: To provide developers with simple, step-by-step instructions to set up and run the RAG ingestion pipeline locally.

---

### Prerequisites

1.  **Python 3.11+**: Ensure you have a compatible Python version installed.
2.  **`uv`**: This project uses `uv` for package management. Install it if you haven't already:
    ```bash
    # For macOS and Linux
    curl -LsSf https://astral.sh/uv/install.sh | sh

    # For Windows
    powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```
3.  **API Keys**:
    -   **Cohere**: You need an API key from your [Cohere Dashboard](https://dashboard.cohere.com/).
    -   **Qdrant Cloud**: You need a free-tier [Qdrant Cloud](https://cloud.qdrant.io/) instance. From your cluster dashboard, you will need the **Cluster URL** and an **API Key**.

---

### 1. Set Up the Environment

1.  **Navigate to the backend directory**:
    ```bash
    cd backend
    ```

2.  **Create a virtual environment**:
    ```bash
    uv venv
    ```
    This will create a `.venv` directory. Your shell should be automatically activated. If not, activate it manually:
    ```bash
    # For macOS and Linux
    source .venv/bin/activate

    # For Windows
    .venv\Scripts\activate
    ```

3.  **Install dependencies**:
    ```bash
    uv pip install -r requirements.txt
    ```
    *(Note: The `requirements.txt` file will be created during the implementation phase).*

---

### 2. Configure Environment Variables

1.  **Create a `.env` file** in the `backend/` directory by copying the example file:
    ```bash
    cp .env.example .env
    ```

2.  **Edit the `.env` file** and add your credentials:
    ```dotenv
    # .env

    # Cohere API Key
    COHERE_API_KEY="your_cohere_api_key"

    # Qdrant Cloud credentials
    QDRANT_URL="https://your-qdrant-cluster-url.aws.cloud.qdrant.io:6333"
    QDRANT_API_KEY="your_qdrant_api_key"

    # Name of the collection to create in Qdrant
    QDRANT_COLLECTION_NAME="physical_ai_book"

    # List of comma-separated Docusaurus URLs to ingest
    SOURCE_URLS="https://url-to-book1.com/docs/intro,https://url-to-book2.com/docs/chapter1"
    ```

---

### 3. Run the Pipeline

Once the environment is configured and dependencies are installed, run the main script:

```bash
python main.py
```

The script will log its progress to the console, showing which URLs are being fetched, processed, and uploaded to Qdrant. Upon completion, you can verify the results in your Qdrant Cloud dashboard.
