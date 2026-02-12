# Quickstart: Frontend–Backend Integration for RAG Chatbot

**Feature**: 007-rag-backend-integration
**Date**: 2026-02-07

## Overview

This guide provides a quick start for setting up and running the FastAPI backend that exposes RAG agent functionality and integrating it with the Docusaurus frontend.

## Prerequisites

- Python 3.13 installed
- Node.js and npm installed (for Docusaurus)
- Existing RAG agent implementation in `backend/agent.py`
- Environment variables configured in `backend/.env`:
  - `OPENAI_API_KEY`
  - `QDRANT_URL`
  - `QDRANT_API_KEY`
  - `QDRANT_COLLECTION_NAME`
  - `COHERE_API_KEY` (optional)

## Backend Setup

### 1. Install Dependencies

```bash
cd backend
pip install fastapi uvicorn pydantic python-multipart
```

### 2. Run the FastAPI Server

```bash
# From the backend directory
uvicorn api:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

### 3. Verify API is Running

```bash
# Health check
curl http://localhost:8000/health

# Test query
curl -X POST http://localhost:8000/api/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What is ROS2?", "limit": 3}'
```

### 4. View API Documentation

Open your browser and navigate to:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Frontend Setup

### 1. Install Docusaurus (if not already installed)

```bash
# From the project root
npm install
```

### 2. Add Chat Component

The chat interface component will be added to `docs/src/components/ChatInterface.tsx`

### 3. Run Docusaurus Development Server

```bash
npm start
```

The frontend will be available at `http://localhost:3000`

## Testing the Integration

### 1. Start Both Servers

Terminal 1 (Backend):
```bash
cd backend
uvicorn api:app --reload --port 8000
```

Terminal 2 (Frontend):
```bash
npm start
```

### 2. Test End-to-End Flow

1. Open browser to `http://localhost:3000`
2. Navigate to the page with the chat interface
3. Submit a query: "Explain ROS2 nodes"
4. Verify that:
   - Response appears within 10 seconds
   - Answer is displayed
   - Confidence score is shown
   - Source references are listed with URLs

### 3. Test Error Handling

Test with invalid inputs:
- Empty query string
- Very long query (>1000 characters)
- Invalid limit values (0, 11, -1)

Verify appropriate error messages are displayed.

## API Usage Examples

### Basic Query

```bash
curl -X POST http://localhost:8000/api/query \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What is ROS2?",
    "limit": 3
  }'
```

Expected response:
```json
{
  "answer": "ROS2 is the next generation of the Robot Operating System...",
  "confidence": 0.85,
  "sources": [
    {
      "url": "https://example.com/book/ros2-basics",
      "score": 0.92
    }
  ]
}
```

### Query with Custom Limit

```bash
curl -X POST http://localhost:8000/api/query \
  -H "Content-Type: application/json" \
  -d '{
    "query": "Explain ROS2 topics and nodes",
    "limit": 5
  }'
```

### Health Check

```bash
curl http://localhost:8000/health
```

Expected response:
```json
{
  "status": "healthy",
  "timestamp": "2026-02-07T10:30:00Z"
}
```

## Frontend Integration Example

### Using Fetch API

```typescript
async function queryAgent(query: string, limit: number = 3) {
  try {
    const response = await fetch('http://localhost:8000/api/query', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ query, limit }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Query failed:', error);
    throw error;
  }
}

// Usage
const result = await queryAgent('What is ROS2?');
console.log('Answer:', result.answer);
console.log('Confidence:', result.confidence);
console.log('Sources:', result.sources);
```

## Troubleshooting

### Backend Issues

**Problem**: API returns 503 Service Unavailable
- **Solution**: Check that Qdrant is accessible and environment variables are set correctly
- **Verify**: `curl $QDRANT_URL` should return a response

**Problem**: API returns 500 Internal Server Error
- **Solution**: Check backend logs for detailed error messages
- **Verify**: Ensure all dependencies are installed and agent.py is working

**Problem**: CORS errors in browser console
- **Solution**: Verify CORS middleware is configured correctly in api.py
- **Verify**: Check that frontend origin matches allowed origins

### Frontend Issues

**Problem**: Network request fails
- **Solution**: Ensure backend is running on port 8000
- **Verify**: `curl http://localhost:8000/health` should return healthy status

**Problem**: Response not displaying
- **Solution**: Check browser console for JavaScript errors
- **Verify**: Response structure matches expected format

## Performance Considerations

- First query may take longer due to agent initialization
- Subsequent queries should complete within 5-10 seconds
- Confidence scores below 0.5 may indicate poor retrieval quality
- Empty sources array indicates no relevant content found

## Next Steps

1. Run unit tests: `pytest backend/tests/test_api.py`
2. Run integration tests: `pytest backend/tests/test_integration.py`
3. Test with various query types and edge cases
4. Monitor response times and confidence scores
5. Adjust retrieval limit based on response quality

## Development Workflow

1. Make changes to `backend/api.py`
2. FastAPI auto-reloads (if using `--reload` flag)
3. Test changes using curl or Swagger UI
4. Make changes to frontend components
5. Docusaurus auto-reloads
6. Test end-to-end flow in browser

## Production Considerations (Future)

This quickstart is for local development only. For production deployment, consider:
- Authentication and authorization
- Rate limiting
- HTTPS/TLS
- Environment-specific CORS configuration
- Monitoring and logging
- Error tracking
- Performance optimization
- Caching strategies