#!/usr/bin/env python3
"""
OpenAI RAG Agent for Book Knowledge Base

This agent uses OpenAI's API to process user queries, retrieve relevant content
from Qdrant vector database, and generate responses based on retrieved context.
"""

import os
import sys
import time
import logging
import argparse
from typing import List, Dict, Optional
from dataclasses import dataclass
from qdrant_client import QdrantClient
from qdrant_client.http import models
import cohere
from dotenv import load_dotenv
from openai import OpenAI

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables
load_dotenv()

@dataclass
class RetrievedChunk:
    """Represents a chunk of content retrieved from the vector database."""
    chunk_id: str
    content: str
    source_url: str
    similarity_score: float
    metadata: Dict

@dataclass
class QueryHistoryItem:
    """Represents an item in the query history."""
    query: str
    response: str
    timestamp: str
    context_used: List[str]  # IDs of chunks used


class RAGAgent:
    """RAG Agent that retrieves information from Qdrant and generates responses using OpenAI."""

    def __init__(self, max_history_items: int = 5):
        """Initialize the RAG Agent with necessary clients and configurations."""
        # Initialize OpenAI client
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set.")
        self.openai_client = OpenAI(api_key=openai_api_key)

        # Initialize Qdrant client
        qdrant_url = os.getenv("QDRANT_URL")
        qdrant_api_key = os.getenv("QDRANT_API_KEY")
        if not qdrant_url or not qdrant_api_key:
            raise ValueError("QDRANT_URL or QDRANT_API_KEY environment variable not set.")

        self.qdrant_client = QdrantClient(url=qdrant_url, api_key=qdrant_api_key)
        self.collection_name = os.getenv("QDRANT_COLLECTION_NAME", "chatbot")

        # Initialize Cohere client for embeddings (to match existing backend)
        cohere_api_key = os.getenv("COHERE_API_KEY")
        if cohere_api_key:
            self.cohere_client = cohere.Client(cohere_api_key)
        else:
            # Fallback: use OpenAI for embeddings if Cohere not available
            self.cohere_client = None

        # Initialize query history for conversation context
        self.max_history_items = max_history_items
        self.query_history = []

        logging.info("RAG Agent initialized successfully.")

    def embed_query(self, query: str) -> List[float]:
        """Generate embedding for the query using Cohere or OpenAI."""
        if self.cohere_client:
            # Use Cohere for embedding (matches existing backend)
            response = self.cohere_client.embed(texts=[query], model="embed-english-light-v2.0")
            return response.embeddings[0]
        else:
            # Fallback to OpenAI embeddings
            response = openai.Embedding.create(
                input=query,
                model="text-embedding-ada-002"
            )
            return response['data'][0]['embedding']

    def retrieve_context(self, query: str, limit: int = 3) -> List[RetrievedChunk]:
        """Retrieve relevant chunks from Qdrant based on the query."""
        logging.info(f"Retrieving context for query: '{query[:50]}{'...' if len(query) > 50 else ''}'")

        try:
            # Generate embedding for the query
            query_embedding = self.embed_query(query)

            # Perform similarity search in Qdrant
            search_results = self.qdrant_client.query_points(
                collection_name=self.collection_name,
                query=query_embedding,
                limit=limit,
            )

            # Convert results to RetrievedChunk objects
            chunks = []
            for point in search_results.points:
                chunk = RetrievedChunk(
                    chunk_id=str(point.id),
                    content=point.payload.get('text_content', ''),
                    source_url=point.payload.get('source_url', 'Unknown'),
                    similarity_score=point.score,
                    metadata=point.payload
                )
                chunks.append(chunk)

            logging.info(f"Retrieved {len(chunks)} chunks from Qdrant.")
            return chunks
        except Exception as e:
            logging.error(f"Error retrieving context from Qdrant: {str(e)}")
            return []

    def generate_response(self, query: str, retrieved_chunks: List[RetrievedChunk]) -> str:
        """Generate a response based on the query and retrieved context."""
        logging.info("Generating response based on retrieved context.")

        # Combine all retrieved context
        context_text = "\n\n".join([
            f"Source: {chunk.source_url}\nContent: {chunk.content}"
            for chunk in retrieved_chunks
        ])

        # Create a prompt that forces the model to use only the provided context
        prompt = f"""You are a helpful assistant that answers questions based only on the provided context.
Do not use any prior knowledge or information not contained in the context below.

CONTEXT:
{context_text}

QUESTION: {query}

INSTRUCTIONS:
- Answer the question using ONLY the information provided in the CONTEXT section.
- If the context does not contain sufficient information to answer the question, say "I don't have enough information in the provided context to answer this question."
- Do not make up or hallucinate any information.
- Be concise and factual in your response."""

        # Use OpenAI's Chat Completions API to generate the response
        try:
            start_time = time.time()
            response = self.openai_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that answers questions based only on the provided context."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=1000
            )

            generated_text = response.choices[0].message.content
            response_time = time.time() - start_time
            logging.info(f"Response generated successfully in {response_time:.2f}s.")

            # Validate that the response is grounded in the context
            if not self.validate_response_against_context(generated_text, retrieved_chunks):
                logging.warning("Generated response may not be fully grounded in context")

            return generated_text
        except Exception as e:
            logging.error(f"Error generating response: {str(e)}")
            return f"Error generating response: {str(e)}"

    def validate_response_against_context(self, response: str, retrieved_chunks: List[RetrievedChunk]) -> bool:
        """Validate that the response is grounded in the provided context."""
        logging.info("Validating response against retrieved context.")

        # Simple validation: check if the response contains content that's related to the context
        context_combined = " ".join([chunk.content for chunk in retrieved_chunks])

        # This is a basic validation - in a real implementation, we'd use more sophisticated techniques
        # like semantic similarity comparison or fact-checking against the context
        if len(retrieved_chunks) == 0:
            # If no context was retrieved, the response should acknowledge this
            return "enough information" in response.lower() or "not enough information" in response.lower()

        # For now, we'll consider it valid if the response is not claiming to have no information
        # when context is available
        no_info_phrases = [
            "don't have enough information",
            "not enough information",
            "cannot answer",
            "not found in context"
        ]

        response_lower = response.lower()
        has_no_info_response = any(phrase in response_lower for phrase in no_info_phrases)
        has_context = len(context_combined.strip()) > 0

        # If there's context but the response claims no info, it's invalid
        if has_context and has_no_info_response:
            return False

        # Otherwise, consider it valid for now
        return True

    def calculate_confidence_score(self, response: str, retrieved_chunks: List[RetrievedChunk]) -> float:
        """Calculate a confidence score based on context relevance and response quality."""
        logging.info("Calculating confidence score for response.")

        if not retrieved_chunks:
            return 0.0

        # Calculate average similarity score of retrieved chunks
        avg_similarity = sum(chunk.similarity_score for chunk in retrieved_chunks) / len(retrieved_chunks)

        # Basic confidence calculation - could be enhanced with more sophisticated metrics
        confidence = avg_similarity

        # Adjust confidence based on response validation
        if not self.validate_response_against_context(response, retrieved_chunks):
            confidence *= 0.5  # Reduce confidence if response is not well-grounded

        return max(0.0, min(1.0, confidence))

    def query(self, query: str, limit: int = 3) -> Dict:
        """Process a query through the RAG pipeline."""
        logging.info(f"Processing query: '{query}'")

        # Step 1: Retrieve relevant context
        retrieved_chunks = self.retrieve_context(query, limit)

        if not retrieved_chunks:
            return {
                "query": query,
                "answer": "No relevant information found in the knowledge base.",
                "retrieved_chunks": [],
                "confidence": 0.0
            }

        # Step 2: Generate response based on retrieved context
        answer = self.generate_response(query, retrieved_chunks)

        # Calculate improved confidence score based on context relevance and response validation
        confidence = self.calculate_confidence_score(answer, retrieved_chunks)

        # Add to query history for potential follow-up questions
        self.add_to_history(query, answer, [chunk.chunk_id for chunk in retrieved_chunks])

        return {
            "query": query,
            "answer": answer,
            "retrieved_chunks": [
                {
                    "chunk_id": chunk.chunk_id,
                    "content": chunk.content[:200] + "..." if len(chunk.content) > 200 else chunk.content,
                    "source_url": chunk.source_url,
                    "similarity_score": chunk.similarity_score
                }
                for chunk in retrieved_chunks
            ],
            "confidence": confidence
        }

    def add_to_history(self, query: str, response: str, chunk_ids: List[str]):
        """Add a query-response pair to the history for follow-up context."""
        from datetime import datetime
        history_item = QueryHistoryItem(
            query=query,
            response=response,
            timestamp=datetime.now().isoformat(),
            context_used=chunk_ids
        )
        self.query_history.append(history_item)

        # Limit history size to prevent memory issues
        if len(self.query_history) > self.max_history_items:
            self.query_history.pop(0)  # Remove oldest item

    def get_conversation_context(self) -> str:
        """Get the conversation context from recent history."""
        if not self.query_history:
            return ""

        context_parts = ["Previous conversation context:"]
        for i, item in enumerate(reversed(self.query_history[-3:])):  # Use last 3 interactions
            context_parts.append(f"Q{i+1}: {item.query}")
            context_parts.append(f"A{i+1}: {item.response}")
            context_parts.append("---")

        return "\n".join(context_parts)

    def query_with_context(self, query: str, limit: int = 3) -> Dict:
        """Process a query through the RAG pipeline with conversation context."""
        logging.info(f"Processing query with context: '{query}'")

        # Get conversation context
        conversation_context = self.get_conversation_context()

        # Step 1: Retrieve relevant context from Qdrant
        retrieved_chunks = self.retrieve_context(query, limit)

        # Combine current query with conversation context for better understanding
        if conversation_context.strip():
            enhanced_prompt = f"{conversation_context}\n\nCurrent Query: {query}"
        else:
            enhanced_prompt = query

        if not retrieved_chunks:
            return {
                "query": query,
                "answer": "No relevant information found in the knowledge base.",
                "retrieved_chunks": [],
                "confidence": 0.0,
                "conversation_context": conversation_context
            }

        # Step 2: Generate response based on retrieved context and conversation history
        answer = self.generate_response(enhanced_prompt, retrieved_chunks)

        # Calculate improved confidence score based on context relevance and response validation
        confidence = self.calculate_confidence_score(answer, retrieved_chunks)

        # Add to query history for potential follow-up questions
        self.add_to_history(query, answer, [chunk.chunk_id for chunk in retrieved_chunks])

        return {
            "query": query,
            "answer": answer,
            "retrieved_chunks": [
                {
                    "chunk_id": chunk.chunk_id,
                    "content": chunk.content[:200] + "..." if len(chunk.content) > 200 else chunk.content,
                    "source_url": chunk.source_url,
                    "similarity_score": chunk.similarity_score
                }
                for chunk in retrieved_chunks
            ],
            "confidence": confidence,
            "conversation_context": conversation_context
        }

def main():
    """Main function to run the RAG agent."""
    parser = argparse.ArgumentParser(description="RAG Agent for Book Knowledge Base")
    parser.add_argument("--query", "-q", type=str, help="Direct query to process")
    parser.add_argument("--test", action="store_true", help="Run test queries")
    args = parser.parse_args()

    # Initialize the agent
    try:
        agent = RAGAgent()
    except ValueError as e:
        print(f"Error initializing agent: {e}")
        sys.exit(1)

    if args.test:
        # Run predefined test queries
        test_queries = [
            "Explain ROS2",
            "What is a ROS2 node?",
            "How do ROS2 topics work?",
            "Compare ROS2 and ROS1"
        ]

        print("Running test queries...\n")
        for query in test_queries:
            print(f"Query: {query}")
            result = agent.query_with_context(query, limit=3)  # Use context-aware query
            print(f"Answer: {result['answer']}")
            print(f"Confidence: {result['confidence']:.2f}")
            print(f"Retrieved {len(result['retrieved_chunks'])} chunks")
            if 'conversation_context' in result and result['conversation_context']:
                print(f"Using conversation context: Yes")
            print("-" * 80)

    elif args.query:
        # Process a single query from command line
        result = agent.query_with_context(args.query, limit=3)  # Use context-aware query
        print(f"Query: {result['query']}")
        print(f"Answer: {result['answer']}")
        print(f"Confidence: {result['confidence']:.2f}")
        print(f"Retrieved {len(result['retrieved_chunks'])} chunks")
        if 'conversation_context' in result and result['conversation_context']:
            print(f"Using conversation context: Yes")

        for i, chunk in enumerate(result['retrieved_chunks'], 1):
            print(f"\nChunk {i} (Score: {chunk['similarity_score']:.2f}):")
            print(f"Source: {chunk['source_url']}")
            print(f"Preview: {chunk['content'][:100]}...")

    else:
        # Interactive mode
        print("RAG Agent Ready! Enter your queries (type 'quit' to exit):")
        print("(Supports follow-up queries with conversation context)")
        while True:
            try:
                query = input("\n> ").strip()
                if query.lower() in ['quit', 'exit', 'q']:
                    print("Goodbye!")
                    break

                if not query:
                    continue

                result = agent.query_with_context(query, limit=3)  # Use context-aware query
                print(f"\nAnswer: {result['answer']}")
                print(f"Confidence: {result['confidence']:.2f}")

                if result['retrieved_chunks']:
                    print(f"\nBased on {len(result['retrieved_chunks'])} sources:")
                    for i, chunk in enumerate(result['retrieved_chunks'], 1):
                        print(f"  {i}. {chunk['source_url']} (Score: {chunk['similarity_score']:.2f})")

                if 'conversation_context' in result and result['conversation_context']:
                    print(f"Using conversation context from previous interactions")

            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"Error processing query: {e}")

if __name__ == "__main__":
    main()