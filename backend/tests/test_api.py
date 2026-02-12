"""
Unit tests for FastAPI endpoints
"""

import pytest
from fastapi.testclient import TestClient
from unittest.mock import Mock, patch
from backend.api import app, get_agent


@pytest.fixture
def client():
    """Create a test client for the FastAPI app."""
    return TestClient(app)


@pytest.fixture
def mock_agent():
    """Create a mock RAGAgent instance."""
    agent = Mock()
    agent.query_with_context.return_value = {
        'answer': 'Test answer',
        'confidence': 0.85,
        'retrieved_chunks': [
            {
                'source_url': 'https://example.com/test',
                'similarity_score': 0.92,
                'chunk_id': 'chunk_123',
                'content': 'Test content preview'
            }
        ],
        'conversation_context': None
    }
    return agent


def test_query_endpoint_success(client, mock_agent):
    """Test successful query to /api/query endpoint."""
    with patch('backend.api.get_agent', return_value=mock_agent):
        response = client.post(
            "/api/query",
            json={"query": "What is ROS2?", "limit": 3}
        )

        assert response.status_code == 200
        data = response.json()
        assert "answer" in data
        assert "confidence" in data
        assert "sources" in data
        assert data["answer"] == "Test answer"
        assert data["confidence"] == 0.85
        assert len(data["sources"]) == 1
        assert data["sources"][0]["url"] == "https://example.com/test"
        assert data["sources"][0]["score"] == 0.92


def test_query_endpoint_with_default_limit(client, mock_agent):
    """Test query endpoint with default limit parameter."""
    with patch('backend.api.get_agent', return_value=mock_agent):
        response = client.post(
            "/api/query",
            json={"query": "Explain ROS2 nodes"}
        )

        assert response.status_code == 200
        mock_agent.query_with_context.assert_called_once_with("Explain ROS2 nodes", 3)


def test_query_endpoint_with_custom_limit(client, mock_agent):
    """Test query endpoint with custom limit parameter."""
    with patch('backend.api.get_agent', return_value=mock_agent):
        response = client.post(
            "/api/query",
            json={"query": "What are ROS2 topics?", "limit": 5}
        )

        assert response.status_code == 200
        mock_agent.query_with_context.assert_called_once_with("What are ROS2 topics?", 5)


def test_query_endpoint_validation_empty_query(client):
    """Test query endpoint with empty query string."""
    response = client.post(
        "/api/query",
        json={"query": "", "limit": 3}
    )

    assert response.status_code == 422  # Validation error


def test_query_endpoint_validation_invalid_limit(client):
    """Test query endpoint with invalid limit values."""
    # Test limit too low
    response = client.post(
        "/api/query",
        json={"query": "test", "limit": 0}
    )
    assert response.status_code == 422

    # Test limit too high
    response = client.post(
        "/api/query",
        json={"query": "test", "limit": 11}
    )
    assert response.status_code == 422


def test_query_endpoint_no_sources(client, mock_agent):
    """Test query endpoint when no sources are found."""
    mock_agent.query_with_context.return_value = {
        'answer': 'No relevant information found in the knowledge base.',
        'confidence': 0.0,
        'retrieved_chunks': [],
        'conversation_context': None
    }

    with patch('backend.api.get_agent', return_value=mock_agent):
        response = client.post(
            "/api/query",
            json={"query": "Unknown topic"}
        )

        assert response.status_code == 200
        data = response.json()
        assert data["confidence"] == 0.0
        assert len(data["sources"]) == 0


def test_query_endpoint_value_error(client, mock_agent):
    """Test query endpoint handling of ValueError."""
    mock_agent.query_with_context.side_effect = ValueError("Invalid input")

    with patch('backend.api.get_agent', return_value=mock_agent):
        response = client.post(
            "/api/query",
            json={"query": "test query"}
        )

        assert response.status_code == 400
        assert "Invalid input" in response.json()["detail"]


def test_query_endpoint_connection_error(client, mock_agent):
    """Test query endpoint handling of ConnectionError."""
    mock_agent.query_with_context.side_effect = ConnectionError("Service unavailable")

    with patch('backend.api.get_agent', return_value=mock_agent):
        response = client.post(
            "/api/query",
            json={"query": "test query"}
        )

        assert response.status_code == 503
        assert "unavailable" in response.json()["detail"].lower()


def test_query_endpoint_generic_error(client, mock_agent):
    """Test query endpoint handling of generic exceptions."""
    mock_agent.query_with_context.side_effect = Exception("Unexpected error")

    with patch('backend.api.get_agent', return_value=mock_agent):
        response = client.post(
            "/api/query",
            json={"query": "test query"}
        )

        assert response.status_code == 500
        assert "Internal server error" in response.json()["detail"]


def test_health_endpoint_healthy(client, mock_agent):
    """Test health endpoint when service is healthy."""
    with patch('backend.api.get_agent', return_value=mock_agent):
        response = client.get("/health")

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert "timestamp" in data


def test_health_endpoint_unhealthy(client):
    """Test health endpoint when service initialization fails."""
    with patch('backend.api.get_agent', side_effect=Exception("Connection failed")):
        response = client.get("/health")

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "unhealthy"
        assert "error" in data
        assert "timestamp" in data
