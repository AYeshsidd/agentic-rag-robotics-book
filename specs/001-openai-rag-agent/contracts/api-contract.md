# API Contract: RAG Agent Service

## Endpoints

### POST /query
Submit a natural language query to the RAG agent

**Request**:
```json
{
  "query": "Explain ROS2",
  "max_chunks": 3,
  "temperature": 0.3
}
```

**Response**:
```json
{
  "response_id": "uuid-string",
  "query": "Explain ROS2",
  "answer": "Detailed explanation of ROS2...",
  "retrieved_chunks": [
    {
      "chunk_id": "uuid",
      "content": "Content of the retrieved chunk...",
      "source_url": "https://source-url",
      "similarity_score": 0.85
    }
  ],
  "confidence": 0.92,
  "timestamp": "2026-02-06T02:22:00Z"
}
```

**Errors**:
- 400: Invalid query format
- 408: Query timeout
- 500: Internal server error

### GET /health
Check the health status of the RAG agent service

**Response**:
```json
{
  "status": "healthy",
  "qdrant_connected": true,
  "openai_connected": true,
  "timestamp": "2026-02-06T02:22:00Z"
}
```

## Data Types

### QueryRequest
- query (string, required): Natural language query text
- max_chunks (integer, optional): Maximum number of chunks to retrieve (default: 3)
- temperature (number, optional): Generation temperature (0.0-1.0, default: 0.3)

### QueryResponse
- response_id (string): Unique identifier for the response
- query (string): Original query text
- answer (string): Generated response based on retrieved content
- retrieved_chunks (array[Chunk]): List of retrieved content chunks
- confidence (number): Confidence score for the response (0.0-1.0)
- timestamp (string): ISO 8601 timestamp

### Chunk
- chunk_id (string): Unique identifier for the chunk
- content (string): Content text
- source_url (string): Source of the content
- similarity_score (number): Similarity score (0.0-1.0)