"""
Integration tests for the full query flow
"""

import pytest
from fastapi.testclient import TestClient
from unittest.mock import Mock, patch, MagicMock
from backend.api import app


@pytest.fixture
def client():
    """Create a test client for the FastAPI app."""
    return TestClient(app)


@pytest.fixture
def mock_qdrant_response():
    """Mock Qdrant search results."""
    return {
        'points': [
            MagicMock(
                id='chunk_001',
                score=0.92,
                payload={
                    'text_content': 'ROS2 is the next generation of the Robot Operating System.',
                    'source_url': 'https://example.com/book/ros2-intro',
                    'chunk_id': 'chunk_001'
                }
            ),
            MagicMock(
                id='chunk_002',
                score=0.85,
                payload={
                    'text_content': 'ROS2 provides improved performance and real-time capabilities.',
                    'source_url': 'https://example.com/book/ros2-features',
                    'chunk_id': 'chunk_002'
                }
            )
        ]
    }


@pytest.fixture
def mock_openai_response():
    """Mock OpenAI chat completion response."""
    mock_response = MagicMock()
    mock_response.choices = [
        MagicMock(
            message=MagicMock(
                content="ROS2 is the next generation of the Robot Operating System, providing improved performance and real-time capabilities."
            )
        )
    ]
    return mock_response


def test_full_query_flow_integration(client, mock_qdrant_response, mock_openai_response):
    """Test the complete query flow from request to response."""

    # Mock the RAGAgent's dependencies
    with patch('backend.agent.QdrantClient') as mock_qdrant_client, \
         patch('backend.agent.cohere.Client') as mock_cohere, \
         patch('backend.agent.OpenAI') as mock_openai_class:

        # Setup mocks
        mock_qdrant_instance = MagicMock()
        mock_qdrant_instance.query_points.return_value = mock_qdrant_response
        mock_qdrant_client.return_value = mock_qdrant_instance

        mock_cohere_instance = MagicMock()
        mock_cohere_instance.embed.return_value = MagicMock(embeddings=[[0.1] * 384])
        mock_cohere.return_value = mock_cohere_instance

        mock_openai_instance = MagicMock()
        mock_openai_instance.chat.completions.create.return_value = mock_openai_response
        mock_openai_class.return_value = mock_openai_instance

        # Make the request
        response = client.post(
            "/api/query",
            json={"query": "What is ROS2?", "limit": 3}
        )

        # Verify response
        assert response.status_code == 200
        data = response.json()

        # Check response structure
        assert "answer" in data
        assert "confidence" in data
        assert "sources" in data

        # Check answer content
        assert len(data["answer"]) > 0
        assert "ROS2" in data["answer"]

        # Check confidence score
        assert 0.0 <= data["confidence"] <= 1.0

        # Check sources
        assert len(data["sources"]) == 2
        assert data["sources"][0]["url"] == "https://example.com/book/ros2-intro"
        assert data["sources"][0]["score"] == 0.92
        assert data["sources"][1]["url"] == "https://example.com/book/ros2-features"
        assert data["sources"][1]["score"] == 0.85


def test_integration_with_no_results(client):
    """Test integration when no relevant results are found."""

    with patch('backend.agent.QdrantClient') as mock_qdrant_client, \
         patch('backend.agent.cohere.Client') as mock_cohere:

        # Setup mocks to return empty results
        mock_qdrant_instance = MagicMock()
        mock_qdrant_instance.query_points.return_value = MagicMock(points=[])
        mock_qdrant_client.return_value = mock_qdrant_instance

        mock_cohere_instance = MagicMock()
        mock_cohere_instance.embed.return_value = MagicMock(embeddings=[[0.1] * 384])
        mock_cohere.return_value = mock_cohere_instance

        # Make the request
        response = client.post(
            "/api/query",
            json={"query": "Unknown topic that doesn't exist"}
        )

        # Verify response
        assert response.status_code == 200
        data = response.json()

        # Should return a "no information found" message
        assert "No relevant information" in data["answer"] or data["confidence"] == 0.0
        assert len(data["sources"]) == 0


def test_integration_qdrant_connection_failure(client):
    """Test integration when Qdrant connection fails."""

    with patch('backend.agent.QdrantClient') as mock_qdrant_client:
        # Simulate connection failure
        mock_qdrant_client.side_effect = ConnectionError("Cannot connect to Qdrant")

        # Make the request
        response = client.post(
            "/api/query",
            json={"query": "What is ROS2?"}
        )

        # Should return 503 Service Unavailable or 500 Internal Server Error
        assert response.status_code in [500, 503]


def test_integration_conversation_context(client, mock_qdrant_response, mock_openai_response):
    """Test integration with conversation context across multiple queries."""

    with patch('backend.agent.QdrantClient') as mock_qdrant_client, \
         patch('backend.agent.cohere.Client') as mock_cohere, \
         patch('backend.agent.OpenAI') as mock_openai_class:

        # Setup mocks
        mock_qdrant_instance = MagicMock()
        mock_qdrant_instance.query_points.return_value = mock_qdrant_response
        mock_qdrant_client.return_value = mock_qdrant_instance

        mock_cohere_instance = MagicMock()
        mock_cohere_instance.embed.return_value = MagicMock(embeddings=[[0.1] * 384])
        mock_cohere.return_value = mock_cohere_instance

        mock_openai_instance = MagicMock()
        mock_openai_instance.chat.completions.create.return_value = mock_openai_response
        mock_openai_class.return_value = mock_openai_instance

        # First query
        response1 = client.post(
            "/api/query",
            json={"query": "What is ROS2?"}
        )
        assert response1.status_code == 200

        # Second query (should have conversation context)
        response2 = client.post(
            "/api/query",
            json={"query": "Tell me more about it"}
        )
        assert response2.status_code == 200

        # Both queries should succeed
        data1 = response1.json()
        data2 = response2.json()
        assert "answer" in data1
        assert "answer" in data2


def test_health_check_integration(client):
    """Test health check endpoint integration."""
    response = client.get("/health")

    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert "timestamp" in data
    assert data["status"] in ["healthy", "unhealthy"]
