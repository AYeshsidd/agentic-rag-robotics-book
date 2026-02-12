# Data Model: Frontend–Backend Integration for RAG Chatbot

**Feature**: 007-rag-backend-integration
**Date**: 2026-02-07
**Status**: Complete

## Overview

This document defines the data entities and their relationships for the FastAPI backend that exposes RAG agent functionality.

## Entities

### QueryRequest

**Purpose**: Represents a user query submitted to the API

**Fields**:
- `query` (string, required): The natural language question from the user
  - Validation: Must be non-empty (min_length=1)
  - Example: "What is ROS2?"
- `limit` (integer, optional): Maximum number of source chunks to retrieve
  - Validation: Must be between 1 and 10 (inclusive)
  - Default: 3
  - Example: 5

**Relationships**: None (input entity)

**State Transitions**: N/A (stateless request)

**Validation Rules**:
- Query string cannot be empty or whitespace-only
- Limit must be a positive integer between 1 and 10
- Request body must be valid JSON

**Example**:
```json
{
  "query": "Explain ROS2 nodes",
  "limit": 3
}
```

---

### QueryResponse

**Purpose**: Represents the structured response from the RAG agent

**Fields**:
- `answer` (string, required): The generated response text from the agent
  - Example: "ROS2 nodes are the fundamental building blocks..."
- `confidence` (float, required): Confidence score for the response
  - Validation: Must be between 0.0 and 1.0
  - Example: 0.85
- `sources` (array of SourceReference, required): List of source documents that contributed to the answer
  - Validation: Can be empty array if no sources found
  - Example: [{"url": "...", "score": 0.92}, ...]
- `conversation_context` (string, optional): Previous conversation context if available
  - Only included when using query_with_context method
  - Example: "Previous conversation context:\nQ1: What is ROS2?\n..."

**Relationships**:
- Contains multiple SourceReference entities

**State Transitions**: N/A (stateless response)

**Validation Rules**:
- Confidence must be a valid float between 0.0 and 1.0
- Sources array must contain valid SourceReference objects
- Answer string can be empty if no information found (with appropriate message)

**Example**:
```json
{
  "answer": "ROS2 nodes are the fundamental building blocks of a ROS2 system...",
  "confidence": 0.85,
  "sources": [
    {
      "url": "https://example.com/book/chapter1",
      "score": 0.92
    },
    {
      "url": "https://example.com/book/chapter2",
      "score": 0.78
    }
  ]
}
```

---

### SourceReference

**Purpose**: Represents a single source document/chunk that contributed to the response

**Fields**:
- `url` (string, required): URL or identifier of the source document
  - Example: "https://example.com/book/ros2-basics"
- `score` (float, required): Similarity/relevance score for this source
  - Validation: Must be between 0.0 and 1.0
  - Example: 0.92
- `chunk_id` (string, optional): Internal identifier for the chunk
  - Used for debugging and tracing
  - Example: "chunk_12345"
- `content_preview` (string, optional): Short preview of the source content
  - Truncated to ~200 characters
  - Example: "ROS2 is the next generation of the Robot Operating System..."

**Relationships**:
- Child of QueryResponse (many-to-one)

**State Transitions**: N/A (immutable reference)

**Validation Rules**:
- URL must be a valid string (not necessarily a valid HTTP URL, could be internal identifier)
- Score must be between 0.0 and 1.0
- Content preview should be truncated if longer than 200 characters

**Example**:
```json
{
  "url": "https://example.com/book/ros2-basics",
  "score": 0.92,
  "chunk_id": "chunk_12345",
  "content_preview": "ROS2 is the next generation of the Robot Operating System..."
}
```

---

### ErrorResponse

**Purpose**: Represents error information returned when requests fail

**Fields**:
- `error` (string, required): Error type or category
  - Example: "ValidationError", "ServiceUnavailable"
- `detail` (string, required): Human-readable error message
  - Example: "Query string cannot be empty"
- `status_code` (integer, required): HTTP status code
  - Example: 400, 500, 503

**Relationships**: None (error entity)

**State Transitions**: N/A (error response)

**Validation Rules**:
- Error and detail must be non-empty strings
- Status code must be a valid HTTP error code (4xx or 5xx)

**Example**:
```json
{
  "error": "ValidationError",
  "detail": "Query string cannot be empty",
  "status_code": 400
}
```

## Entity Relationships

```
QueryRequest (1) ──submits──> API Endpoint
                                    │
                                    ▼
                            RAGAgent.query_with_context()
                                    │
                                    ▼
QueryResponse (1) ──contains──> SourceReference (0..*)
```

## Data Flow

1. Client submits QueryRequest to POST /api/query
2. FastAPI validates request using Pydantic model
3. API calls RAGAgent.query_with_context(query, limit)
4. Agent returns dictionary with answer, confidence, sources
5. API transforms agent response to QueryResponse model
6. FastAPI serializes QueryResponse to JSON
7. Client receives JSON response

## Validation Summary

| Entity | Field | Validation Rule |
|--------|-------|----------------|
| QueryRequest | query | Non-empty string, min_length=1 |
| QueryRequest | limit | Integer, 1 ≤ limit ≤ 10, default=3 |
| QueryResponse | confidence | Float, 0.0 ≤ confidence ≤ 1.0 |
| QueryResponse | sources | Array of SourceReference |
| SourceReference | score | Float, 0.0 ≤ score ≤ 1.0 |
| SourceReference | url | Non-empty string |
| ErrorResponse | status_code | Valid HTTP error code (4xx, 5xx) |