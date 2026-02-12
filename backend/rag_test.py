#!/usr/bin/env python3
"""
RAG Pipeline Test and Analysis Script
Tests the RAG retrieval pipeline and generates a final synthesized answer
"""

import os
import logging
import cohere
from qdrant_client import QdrantClient
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from cohere.errors import TooManyRequestsError
import json

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

def get_cohere_client():
    """Initializes and returns the Cohere client."""
    api_key = os.getenv("COHERE_API_KEY")
    if not api_key:
        logging.error("COHERE_API_KEY environment variable not set.")
        raise ValueError("COHERE_API_KEY environment variable not set.")
    logging.info("Cohere client initialized.")
    return cohere.Client(api_key)

def get_qdrant_client():
    """Initializes and returns the Qdrant client."""
    url = os.getenv("QDRANT_URL")
    api_key = os.getenv("QDRANT_API_KEY")
    if not url or not api_key:
        logging.error("QDRANT_URL or QDRANT_API_KEY environment variable not set.")
        raise ValueError("QDRANT_URL or QDRANT_API_KEY environment variable not set.")
    logging.info("Qdrant client initialized.")
    return QdrantClient(url=url, api_key=api_key)

@retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=1, min=4, max=10),
    retry=retry_if_exception_type(TooManyRequestsError),
    reraise=True
)
def generate_query_embedding(query: str, cohere_client: cohere.Client) -> list[float]:
    """Generates an embedding for the given query, with retry logic."""
    logging.info(f"Generating embedding for query: '{query}'")
    response = cohere_client.embed(texts=[query], model="embed-english-light-v2.0")
    return response.embeddings[0]

def retrieve_context(query: str, limit: int = 3):
    """Retrieves relevant context from Qdrant."""
    cohere_client = get_cohere_client()
    qdrant_client = get_qdrant_client()

    # Generate the embedding for the user's query
    query_embedding = generate_query_embedding(query, cohere_client)

    # Perform similarity search in Qdrant
    collection_name = os.getenv("QDRANT_COLLECTION_NAME")
    if not collection_name:
        logging.error("QDRANT_COLLECTION_NAME environment variable not set.")
        raise ValueError("QDRANT_COLLECTION_NAME environment variable not set.")

    logging.info(f"Searching collection '{collection_name}' for top {limit} results...")
    search_results = qdrant_client.query_points(
        collection_name=collection_name,
        query=query_embedding,
        limit=limit,
    )

    if not search_results.points:
        logging.info("No relevant documents found.")
        return []

    logging.info(f"Found {len(search_results.points)} results:")
    retrieved_chunks = []
    for i, result in enumerate(search_results.points):
        print(f"\n--- Retrieved Chunk {i+1} ---")
        print(f"Score: {result.score}")
        print(f"Source: {result.payload.get('source_url', 'Unknown')}")
        content_preview = result.payload.get('text_content', '')[:200]
        print(f"Content Preview: {repr(content_preview)}...")
        retrieved_chunks.append(result.payload.get('text_content', ''))

    return retrieved_chunks

def generate_final_answer(query: str, context_chunks: list[str]):
    """Generates a final synthesized answer using the retrieved context."""
    cohere_client = get_cohere_client()

    # Combine all retrieved context
    combined_context = "\n\n".join(context_chunks)

    # Create a prompt for the generative model
    prompt = f"""
Based on the following context, please provide a comprehensive answer to the question "{query}":

Context:
{combined_context}

Answer:
"""

    logging.info("Generating final answer using retrieved context...")
    response = cohere_client.chat(
        message=prompt,
        model="command-r-08-2024",
        temperature=0.3,
        max_tokens=1000
    )

    return response.text

def main():
    """Test the RAG pipeline with the query 'Explain ROS2'."""
    query = "Explain ROS2"
    print(f"Testing RAG pipeline with query: '{query}'\n")

    # Step 1: Retrieve relevant context
    print("=" * 60)
    print("STEP 1: RETRIEVING CONTEXT FROM QDRANT")
    print("=" * 60)
    retrieved_chunks = retrieve_context(query, limit=3)

    if not retrieved_chunks:
        print("No context retrieved. Cannot generate answer.")
        return

    # Step 2: Generate final answer
    print("\n" + "=" * 60)
    print("STEP 2: GENERATING FINAL ANSWER")
    print("=" * 60)
    final_answer = generate_final_answer(query, retrieved_chunks)

    print(f"\nFINAL ANSWER TO '{query}':")
    print("-" * 40)
    print(final_answer)
    print("-" * 40)

    print(f"\nSUMMARY:")
    print(f"- Retrieved {len(retrieved_chunks)} relevant chunks from the knowledge base")
    print(f"- Generated a synthesized answer using the retrieved context")
    print(f"- RAG pipeline is functioning correctly!")

if __name__ == "__main__":
    main()