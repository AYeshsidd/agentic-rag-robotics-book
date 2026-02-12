# Research: RAG Ingestion Pipeline

**Purpose**: To investigate best practices for the core technologies in the RAG ingestion pipeline and resolve any technical uncertainties before implementation.

---

### Decision 1: Web Content Extraction

-   **Technology**: `requests` for HTTP requests and `BeautifulSoup4` for HTML parsing.
-   **Decision**: Use `requests.get()` to fetch the raw HTML from a given URL. Use `BeautifulSoup` to parse the HTML document. Identify the main content area of the Docusaurus pages (typically within an `<article>` tag or a `div` with a specific class like `theme-doc-markdown`) to isolate the book text from headers, footers, and navigation sidebars.
-   **Rationale**: This combination is the standard and most robust approach for web scraping in Python. It is well-documented, flexible, and efficient for extracting text and structure from HTML.
-   **Alternatives Considered**:
    -   **Scrapy**: A more powerful, asynchronous scraping framework. It is overkill for this project's needs, which involve fetching from a simple list of URLs rather than complex, multi-level crawling.
    -   **LXML**: A faster parser, but `BeautifulSoup` provides a more convenient and Pythonic API for navigating the HTML tree, which is sufficient for this project's performance needs.

### Decision 2: Text Chunking Strategy

-   **Technology**: `langchain.text_splitter.RecursiveCharacterTextSplitter`.
-   **Decision**: Use `RecursiveCharacterTextSplitter` to chunk the cleaned text. This splitter attempts to split text based on a prioritized list of separators (e.g., `

`, `
`, ` `), which helps keep related paragraphs and sentences together. The `chunk_size` and `chunk_overlap` will be configurable as required by the spec.
-   **Rationale**: Naively splitting by a fixed character count can break sentences and separate related ideas. `RecursiveCharacterTextSplitter` is a standard, effective method for semantic chunking that is simple to implement and widely used in RAG pipelines.
-   **Alternatives Considered**:
    -   **Manual Splitting**: Writing a custom function to split text. This is error-prone and would reinvent a solved problem.
    -   **NLTK/spaCy**: Using sentence tokenizers from NLP libraries. This is a valid approach but adds heavier dependencies. LangChain's splitter is lightweight and designed specifically for this pre-embedding task.

### Decision 3: Embedding Generation

-   **Technology**: `cohere` Python client.
-   **Decision**: Use the `cohere.Client` to connect to the Cohere API. The `client.embed()` method will be used to generate embeddings. The pipeline should batch the text chunks before sending them to the API, as the `embed` endpoint is optimized for handling multiple inputs in a single call. A batch size of around 96 is a good starting point, as it's the maximum allowed by the Cohere API.
-   **Rationale**: Using the official Python client is the most reliable way to interact with the Cohere API. Batching is critical for performance and to avoid hitting rate limits unnecessarily.
-   **Alternatives Considered**:
    -   **Direct HTTP Requests**: Making `curl` or `requests` calls to the API endpoint. This adds unnecessary boilerplate for authentication and request/response handling, which the official client abstracts away.

### Decision 4: Vector Storage

-   **Technology**: `qdrant-client` Python package.
-   **Decision**: Use the `QdrantClient` to interact with the Qdrant Cloud instance.
    1.  The pipeline will first connect to the client using the URL and API key from the environment variables.
    2.  It will create a collection if it doesn't already exist, configuring it with the correct vector size for the chosen Cohere model.
    3.  It will use the `client.upsert()` method to add or update points in batches. Each point will consist of a unique ID (e.g., a UUID), the embedding vector, and the payload (the metadata from the `ContentChunk` entity).
-   **Rationale**: The official client provides a high-level, convenient API for all necessary Qdrant operations and is optimized for performance, especially for batch upserts.
-   **Alternatives Considered**:
    -   **Direct REST API calls**: Similar to the Cohere case, this would add unnecessary complexity compared to using the official, well-supported client library.

### Decision 5: Project & Dependency Management

-   **Technology**: `uv`.
-   **Decision**: The project will be initialized and managed using `uv`. A `pyproject.toml` file will be created to define project metadata and dependencies.
    -   `uv venv` will be used to create a virtual environment.
    -   `uv pip install -r requirements.txt` (or `uv pip install <package>`) will manage dependencies.
    -   A `requirements.txt` file will be generated from `pyproject.toml` for portability.
-   **Rationale**: `uv` is a modern, extremely fast Python packaging tool that simplifies dependency management and virtual environment creation. It's a good choice for a new project aiming for a fast and clean development workflow.
-   **Alternatives Considered**:
    -   **`pip` + `venv`**: The standard library approach. It works perfectly well but is significantly slower than `uv`.
    -   **Poetry/PDM**: More comprehensive project management tools. They are excellent but might be slightly more complex than what is needed for this simple script-based project. `uv` strikes a good balance of simplicity and speed.
