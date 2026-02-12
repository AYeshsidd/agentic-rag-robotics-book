# OpenAI RAG Agent for Book Knowledge Base

This agent uses OpenAI's API to process user queries, retrieve relevant content from Qdrant vector database, and generate responses based on retrieved context.

## Features

- **Natural Language Queries**: Accept natural language questions about book content
- **Vector Search**: Uses Qdrant for semantic similarity search in book content
- **Grounded Responses**: Generates responses strictly based on retrieved context to prevent hallucination
- **Conversation Context**: Maintains conversation history for follow-up queries
- **Confidence Scoring**: Provides confidence scores based on context relevance
- **Error Handling**: Comprehensive error handling and retry logic
- **Performance Monitoring**: Tracks response times and performance metrics

## Architecture

- **API Layer**: FastAPI backend exposing REST endpoints for frontend integration
- **Frontend**: Command-line interface supporting interactive and batch queries
- **Core Logic**: RAGAgent class orchestrating query processing flow
- **Embeddings**: Cohere or OpenAI for converting queries to embeddings
- **Vector Store**: Qdrant for similarity search in book content
- **Generation**: OpenAI for generating contextually-aware responses
- **Validation**: Response validation to ensure grounding in retrieved context

## API Usage

### Starting the FastAPI Server

```bash
cd backend
uvicorn api:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

### API Endpoints

#### POST /api/query

Submit a query to the RAG agent and receive a grounded answer with source references.

**Request:**
```json
{
  "query": "What is ROS2?",
  "limit": 3
}
```

**Response:**
```json
{
  "answer": "ROS2 is the next generation of the Robot Operating System...",
  "confidence": 0.85,
  "sources": [
    {
      "url": "https://example.com/book/chapter1",
      "score": 0.92,
      "chunk_id": "chunk_12345",
      "content_preview": "ROS2 is..."
    }
  ]
}
```

**Example with curl:**
```bash
curl -X POST http://localhost:8000/api/query \
  -H "Content-Type: application/json" \
  -d '{"query": "Explain ROS2 nodes", "limit": 3}'
```

#### GET /health

Check the health status of the API service.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2026-02-07T10:30:00Z"
}
```

### API Documentation

Once the server is running, you can access:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## CLI Usage

### Interactive Mode
```bash
python agent.py
```

### Single Query
```bash
python agent.py --query "Explain ROS2"
```

### Test Queries
```bash
python agent.py --test
```

## Configuration

Create a `.env` file with the following variables:

```env
OPENAI_API_KEY=your_openai_api_key
QDRANT_URL=your_qdrant_url
QDRANT_API_KEY=your_qdrant_api_key
QDRANT_COLLECTION_NAME=chatbot
COHERE_API_KEY=your_cohere_api_key  # Optional, for embeddings
```

## Dependencies

All dependencies are listed in `requirements.txt` and can be installed with:

```bash
pip install -r requirements.txt
```

## Components

- `RAGAgent`: Main class orchestrating the RAG pipeline
- `RetrievedChunk`: Data class representing retrieved content chunks
- `QueryHistoryItem`: Data class for conversation history
- `embed_query()`: Converts queries to embeddings
- `retrieve_context()`: Performs vector search in Qdrant
- `generate_response()`: Creates responses from context
- `validate_response_against_context()`: Ensures responses are grounded in context
- `calculate_confidence_score()`: Calculates response confidence
- `query_with_context()`: Main query method with conversation history support

## Error Handling

- **API Failures**: Retry logic with exponential backoff for OpenAI and Cohere APIs
- **Qdrant Connection**: Graceful degradation when vector database is unavailable
- **Response Validation**: Checks to ensure responses are grounded in provided context
- **Rate Limits**: Handles API rate limiting with appropriate backoff strategies