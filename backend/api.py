"""
FastAPI Backend for RAG Chatbot

This module exposes the RAG agent functionality through REST endpoints,
enabling the Docusaurus frontend to submit queries and receive grounded answers.
"""

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional
import logging
from agent import RAGAgent

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Pydantic Models

class QueryRequest(BaseModel):
    """Request model for user queries."""
    query: str = Field(..., min_length=1, description="Natural language question from the user")
    limit: Optional[int] = Field(3, ge=1, le=10, description="Maximum number of source chunks to retrieve")

    class Config:
        json_schema_extra = {
            "example": {
                "query": "What is ROS2?",
                "limit": 3
            }
        }


class SourceReference(BaseModel):
    """Model for source document references."""
    url: str = Field(..., description="URL or identifier of the source document")
    score: float = Field(..., ge=0.0, le=1.0, description="Similarity/relevance score for this source")
    chunk_id: Optional[str] = Field(None, description="Internal identifier for the chunk")
    content_preview: Optional[str] = Field(None, description="Short preview of the source content")

    class Config:
        json_schema_extra = {
            "example": {
                "url": "https://example.com/book/ros2-basics",
                "score": 0.92,
                "chunk_id": "chunk_12345",
                "content_preview": "ROS2 is the next generation..."
            }
        }


class QueryResponse(BaseModel):
    """Response model for query results."""
    answer: str = Field(..., description="Generated response text from the RAG agent")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confidence score for the response")
    sources: List[SourceReference] = Field(..., description="List of source documents that contributed to the answer")
    conversation_context: Optional[str] = Field(None, description="Previous conversation context (optional)")

    class Config:
        json_schema_extra = {
            "example": {
                "answer": "ROS2 is the next generation of the Robot Operating System...",
                "confidence": 0.85,
                "sources": [
                    {
                        "url": "https://example.com/book/chapter1",
                        "score": 0.92
                    }
                ]
            }
        }


class ErrorResponse(BaseModel):
    """Model for error responses."""
    error: str = Field(..., description="Error type or category")
    detail: str = Field(..., description="Human-readable error message")
    status_code: int = Field(..., description="HTTP status code")

    class Config:
        json_schema_extra = {
            "example": {
                "error": "ValidationError",
                "detail": "Query string cannot be empty",
                "status_code": 400
            }
        }


# FastAPI Application

app = FastAPI(
    title="RAG Chatbot API",
    description="FastAPI backend that exposes RAG agent functionality for querying book content",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)

# Dependency Injection for RAGAgent
agent_instance = None

def get_agent() -> RAGAgent:
    """
    Dependency injection function to provide singleton RAGAgent instance.

    Returns:
        RAGAgent: Singleton instance of the RAG agent
    """
    global agent_instance
    if agent_instance is None:
        logger.info("Initializing RAGAgent instance")
        agent_instance = RAGAgent()
    return agent_instance


# API Endpoints

@app.post("/api/query", response_model=QueryResponse)
async def query_endpoint(request: QueryRequest, agent: RAGAgent = Depends(get_agent)):
    """
    Submit a query to the RAG agent and receive a grounded answer with source references.

    This endpoint processes natural language queries by:
    1. Embedding the query using Cohere or OpenAI
    2. Retrieving relevant chunks from Qdrant vector database
    3. Generating a grounded response using OpenAI
    4. Validating the response against retrieved context

    Args:
        request: QueryRequest containing the user's query and optional limit
        agent: RAGAgent instance (injected via dependency)

    Returns:
        QueryResponse: Answer with confidence score and source references

    Raises:
        HTTPException: 400 for validation errors, 500 for server errors, 503 for service unavailable

    Example:
        Request:
            POST /api/query
            {
                "query": "What is ROS2?",
                "limit": 3
            }

        Response:
            {
                "answer": "ROS2 is the next generation...",
                "confidence": 0.85,
                "sources": [...]
            }
    """
    request_id = id(request)
    logger.info(f"[{request_id}] Received query request")
    logger.debug(f"[{request_id}] Query: {request.query[:100]}... | Limit: {request.limit}")

    try:
        logger.info(f"[{request_id}] Processing query: {request.query[:50]}...")

        # Call the agent with the query
        result = agent.query_with_context(request.query, request.limit)
        logger.debug(f"[{request_id}] Agent returned {len(result.get('retrieved_chunks', []))} chunks")

        # Transform agent response to QueryResponse model
        sources = []
        for chunk in result.get('retrieved_chunks', []):
            sources.append(SourceReference(
                url=chunk.get('source_url', 'Unknown'),
                score=chunk.get('similarity_score', 0.0),
                chunk_id=chunk.get('chunk_id'),
                content_preview=chunk.get('content')
            ))

        response = QueryResponse(
            answer=result.get('answer', ''),
            confidence=result.get('confidence', 0.0),
            sources=sources,
            conversation_context=result.get('conversation_context')
        )

        logger.info(f"[{request_id}] Query processed successfully. Confidence: {response.confidence:.2f}, Sources: {len(sources)}")
        return response

    except ValueError as e:
        logger.error(f"[{request_id}] Validation error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except ConnectionError as e:
        logger.error(f"[{request_id}] Service unavailable: {str(e)}")
        raise HTTPException(status_code=503, detail="Vector database or AI service temporarily unavailable")
    except Exception as e:
        logger.error(f"[{request_id}] Internal server error: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@app.get("/health")
async def health_check():
    """
    Health check endpoint to verify service status.

    Returns:
        dict: Service health status and timestamp
    """
    from datetime import datetime

    try:
        # Try to get the agent to verify it can be initialized
        agent = get_agent()

        return {
            "status": "healthy",
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        return {
            "status": "unhealthy",
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }

