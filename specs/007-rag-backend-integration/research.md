# Research: Frontend–Backend Integration for RAG Chatbot

**Feature**: 007-rag-backend-integration
**Date**: 2026-02-07
**Status**: Complete

## Overview

This document captures research findings for implementing a FastAPI backend that exposes the existing RAG agent functionality and integrates with the Docusaurus frontend.

## Research Areas

### 1. FastAPI Integration with Existing Python Modules

**Decision**: Use dependency injection pattern to instantiate RAGAgent once at startup

**Rationale**:
- FastAPI's dependency injection system allows sharing a single RAGAgent instance across requests
- Avoids repeated initialization overhead (Qdrant/OpenAI/Cohere client setup)
- Maintains conversation context across requests if needed
- Follows FastAPI best practices for stateful services

**Alternatives considered**:
- Creating new agent instance per request: Rejected due to initialization overhead and loss of conversation context
- Global singleton: Rejected in favor of FastAPI's built-in dependency injection which is more testable

**Implementation approach**:
```python
from fastapi import FastAPI, Depends
from agent import RAGAgent

app = FastAPI()
agent_instance = None

def get_agent():
    global agent_instance
    if agent_instance is None:
        agent_instance = RAGAgent()
    return agent_instance

@app.post("/api/query")
async def query(request: QueryRequest, agent: RAGAgent = Depends(get_agent)):
    return agent.query_with_context(request.query, request.limit)
```

### 2. CORS Configuration for Local Development

**Decision**: Enable CORS with specific localhost origins for development

**Rationale**:
- Docusaurus typically runs on http://localhost:3000
- FastAPI backend will run on http://localhost:8000
- Need explicit CORS configuration to allow cross-origin requests
- Should be restrictive even in development (only allow specific origins)

**Alternatives considered**:
- Allow all origins (*): Rejected as bad security practice even for local dev
- Proxy through Docusaurus: Rejected as adds complexity and doesn't match spec requirements

**Implementation approach**:
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)
```

### 3. Error Handling Patterns for API Wrappers

**Decision**: Implement structured error responses with appropriate HTTP status codes

**Rationale**:
- Frontend needs to distinguish between different error types
- HTTP status codes provide semantic meaning (400 for bad request, 500 for server error, 503 for service unavailable)
- Structured error responses allow frontend to display meaningful messages
- Aligns with REST API best practices

**Alternatives considered**:
- Always return 200 with error in body: Rejected as violates HTTP semantics
- Generic error messages: Rejected as reduces debuggability

**Implementation approach**:
```python
from fastapi import HTTPException
from pydantic import BaseModel

class ErrorResponse(BaseModel):
    error: str
    detail: str

@app.post("/api/query")
async def query(request: QueryRequest, agent: RAGAgent = Depends(get_agent)):
    try:
        result = agent.query_with_context(request.query, request.limit)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
```

### 4. Request/Response Models with Pydantic

**Decision**: Use Pydantic models for request validation and response serialization

**Rationale**:
- FastAPI integrates seamlessly with Pydantic
- Automatic validation of incoming requests
- Automatic OpenAPI/Swagger documentation generation
- Type safety and IDE support
- Matches the API contract defined in spec (FR-006)

**Alternatives considered**:
- Plain dictionaries: Rejected due to lack of validation and type safety
- Manual validation: Rejected as Pydantic provides this automatically

**Implementation approach**:
```python
from pydantic import BaseModel, Field
from typing import List, Optional

class QueryRequest(BaseModel):
    query: str = Field(..., min_length=1, description="User query")
    limit: Optional[int] = Field(3, ge=1, le=10, description="Max chunks to retrieve")

class SourceReference(BaseModel):
    url: str
    score: float

class QueryResponse(BaseModel):
    answer: str
    confidence: float
    sources: List[SourceReference]
```

### 5. Frontend Integration with Docusaurus

**Decision**: Create a React component using fetch API for backend communication

**Rationale**:
- Docusaurus is built on React, so React components integrate naturally
- Fetch API is standard and requires no additional dependencies
- Can be embedded in any Docusaurus page or as a standalone page
- Supports async/await for clean error handling

**Alternatives considered**:
- Axios library: Rejected as fetch API is sufficient and avoids extra dependency
- WebSocket connection: Rejected as not required for request/response pattern

**Implementation approach**:
```typescript
const ChatInterface: React.FC = () => {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    setLoading(true);
    try {
      const res = await fetch('http://localhost:8000/api/query', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query, limit: 3 })
      });
      const data = await res.json();
      setResponse(data);
    } catch (error) {
      console.error('Query failed:', error);
    } finally {
      setLoading(false);
    }
  };

  return (/* UI components */);
};
```

### 6. Testing Strategy

**Decision**: Implement three layers of testing: unit, integration, and contract tests

**Rationale**:
- Unit tests verify API endpoint logic in isolation
- Integration tests verify full flow including agent.py interaction
- Contract tests ensure API matches the defined schema
- Follows constitution requirement for integration testing

**Testing approach**:
- Unit tests: Mock RAGAgent, test request validation and error handling
- Integration tests: Use TestClient with real agent instance (mocked Qdrant/OpenAI)
- Contract tests: Validate request/response schemas match OpenAPI spec

**Implementation approach**:
```python
from fastapi.testclient import TestClient
import pytest

def test_query_endpoint_success(client: TestClient, mock_agent):
    response = client.post("/api/query", json={"query": "test"})
    assert response.status_code == 200
    assert "answer" in response.json()
    assert "confidence" in response.json()
    assert "sources" in response.json()

def test_query_endpoint_validation(client: TestClient):
    response = client.post("/api/query", json={"query": ""})
    assert response.status_code == 422  # Validation error
```

## Summary

All research areas have been resolved with clear decisions and implementation approaches. The plan uses FastAPI best practices, maintains separation of concerns, and follows the project constitution principles. No blocking issues or unresolved questions remain.