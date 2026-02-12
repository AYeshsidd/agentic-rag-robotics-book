import os
import logging
import typer
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

app = typer.Typer()

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

@app.command()
def validate(query: str, limit: int = 3):
    """
    Connects to Qdrant, performs a similarity search for the given query,
    and displays the top N results to validate the ingestion pipeline.
    """
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
        raise typer.Exit()

    logging.info(f"Found {len(search_results.points)} results:")
    for i, result in enumerate(search_results.points):
        print(f"\n--- Result {i+1} ---")
        print(f"Score: {result.score}")
        print("Payload:")
        # Pretty print the payload
        print(json.dumps(result.payload, indent=2))


if __name__ == "__main__":
    app()
    