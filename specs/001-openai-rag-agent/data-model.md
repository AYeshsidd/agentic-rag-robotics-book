# Data Model: OpenAI RAG Agent

## Entities

### Query
- **Description**: Represents a user's natural language request for information from the book knowledge base
- **Fields**:
  - query_text (string): The raw text of the user's query
  - timestamp (datetime): When the query was submitted
  - query_id (string): Unique identifier for the query
- **Validation**: Must be non-empty string less than 1000 characters
- **State Transitions**: Submitted → Processing → Responded

### RetrievedChunk
- **Description**: A segment of book content retrieved from Qdrant based on semantic similarity to the user's query
- **Fields**:
  - chunk_id (string): Unique identifier for the chunk
  - content (string): The actual text content of the chunk
  - source_url (string): URL where the content originated
  - similarity_score (float): How closely the chunk matches the query (0.0-1.0)
  - metadata (dict): Additional information about the chunk
- **Validation**: Content must be non-empty, similarity score must be between 0.0 and 1.0
- **Relationships**: Linked to Query via query_id

### AgentResponse
- **Description**: The generated answer produced by the OpenAI agent based on the retrieved content chunks
- **Fields**:
  - response_id (string): Unique identifier for the response
  - query_id (string): Links to the original query
  - content (string): The agent's response text
  - source_chunks (list): IDs of chunks used to generate the response
  - confidence_level (float): Agent's confidence in the response accuracy
  - timestamp (datetime): When the response was generated
- **Validation**: Content must be non-empty, confidence level must be between 0.0 and 1.0
- **Relationships**: Links to Query and multiple RetrievedChunks

### BookKnowledgeBase
- **Description**: The collection of book content stored in Qdrant as vector embeddings for retrieval
- **Fields**:
  - collection_name (string): Name of the Qdrant collection
  - total_chunks (int): Number of content chunks in the knowledge base
  - last_updated (datetime): When the knowledge base was last updated
  - embedding_model (string): Model used to generate the embeddings
- **Validation**: Collection must exist in Qdrant, embedding model must be valid
- **State Transitions**: Empty → Populating → Active → Updating

## Relationships

- One Query can result in multiple RetrievedChunks (1:M)
- One Query generates one AgentResponse (1:1)
- One AgentResponse can reference multiple RetrievedChunks (1:M)
- One BookKnowledgeBase contains many RetrievedChunks (1:M)

## State Transitions

### Query Lifecycle
1. **Submitted**: User enters query
2. **Processing**: Agent retrieves relevant chunks from Qdrant
3. **Responded**: Agent generates response based on retrieved chunks

### Knowledge Base Lifecycle
1. **Empty**: No content indexed
2. **Populating**: Content is being indexed into Qdrant
3. **Active**: Ready to serve queries
4. **Updating**: New content is being added or existing content updated