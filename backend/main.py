import os
import logging
from dataclasses import dataclass
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
from langchain_text_splitters import RecursiveCharacterTextSplitter
import cohere
import uuid
from qdrant_client import QdrantClient, models
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from cohere.errors import TooManyRequestsError

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

@dataclass
class ContentChunk:
    source_url: str
    section_identifier: str
    chunk_index: int
    text_content: str

def fetch_html(url: str) -> str:
    """Fetches the HTML content of a given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        logging.info(f"Successfully fetched HTML from {url}")
        return response.text
    except requests.RequestException as e:
        logging.error(f"Error fetching {url}: {e}")
        return ""

def extract_text_from_html(html: str) -> str:
    """Extracts the main text content from a Docusaurus page HTML, prioritizing the <main> tag."""
    soup = BeautifulSoup(html, "html.parser")
    
    # Try to find the <main> tag which typically contains the primary content
    main_content = soup.find("main")
    if main_content:
        logging.info("Successfully found <main> tag for text extraction.")
        return main_content.get_text(separator=" ", strip=True)
    
    # Fallback to extracting from the body if no <main> tag is found
    body_content = soup.find("body")
    if body_content:
        logging.warning("No <main> tag found, falling back to <body> for text extraction.")
        return body_content.get_text(separator=" ", strip=True)
        
    logging.warning("No <main> or <body> tag found for text extraction.")
    return ""

def chunk_text(text: str) -> list[str]:
    """Splits a long text into smaller chunks."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    chunks = text_splitter.split_text(text)
    logging.info(f"Chunked text into {len(chunks)} parts.")
    return chunks

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
def generate_embeddings(chunks: list[ContentChunk], co_client: cohere.Client) -> list[dict]:
    """Generates embeddings for a list of text chunks and prepares them for Qdrant."""
    texts = [chunk.text_content for chunk in chunks]
    logging.info(f"Generating embeddings for {len(texts)} text chunks.")
    response = co_client.embed(texts=texts, model="embed-english-light-v2.0")
    
    records = []
    for i, chunk in enumerate(chunks):
        records.append({
            "id": str(uuid.uuid4()),
            "vector": response.embeddings[i],
            "payload": {
                "source_url": chunk.source_url,
                "section_identifier": chunk.section_identifier,
                "chunk_index": chunk.chunk_index,
                "text_content": chunk.text_content,
            }
        })
    logging.info(f"Generated {len(records)} embedding records.")
    return records


def upsert_vectors_to_qdrant(records: list[dict], qdrant_client: QdrantClient):
    """Upserts a list of vector records into the Qdrant collection."""
    collection_name = os.getenv("QDRANT_COLLECTION_NAME")
    if not collection_name:
        logging.error("QDRANT_COLLECTION_NAME environment variable not set.")
        raise ValueError("QDRANT_COLLECTION_NAME environment variable not set.")

    # Check if collection exists, create it if not
    if not qdrant_client.collection_exists(collection_name=collection_name):
        logging.info(f"Collection '{collection_name}' not found. Creating it.")
        qdrant_client.create_collection(
            collection_name=collection_name,
            vectors_config=models.VectorParams(size=1024, distance=models.Distance.COSINE),
        )
        logging.info(f"Collection '{collection_name}' created.")
    else:
        logging.info(f"Collection '{collection_name}' already exists.")

    # Upsert records in batches
    qdrant_client.upsert(
        collection_name=collection_name,
        points=[
            models.PointStruct(id=record["id"], vector=record["vector"], payload=record["payload"])
            for record in records
        ],
        wait=True,
    )
    logging.info(f"Successfully upserted {len(records)} vectors to collection '{collection_name}'.")

import time
from qdrant_client import QdrantClient, models
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from cohere.errors import TooManyRequestsError
def main():
    """Main function to run the ingestion pipeline."""
    source_urls_str = os.getenv("SOURCE_URLS")
    if not source_urls_str:
        logging.error("SOURCE_URLS environment variable not set.")
        raise ValueError("SOURCE_URLS environment variable not set.")
    
    source_urls = [url.strip() for url in source_urls_str.split(",") if url.strip()]
    
    cohere_client = get_cohere_client()
    qdrant_client = get_qdrant_client()

    for i, url in enumerate(source_urls):
        logging.info(f"Processing URL {i+1}/{len(source_urls)}: {url}...")
        html = fetch_html(url)
        if not html:
            logging.warning(f"Skipping {url} due to failed HTML fetch.")
            continue

        text = extract_text_from_html(html)
        if not text:
            logging.warning(f"Skipping {url} due to no text extracted.")
            continue

        text_chunks = chunk_text(text)
        
        content_chunks = [
            ContentChunk(
                source_url=url,
                section_identifier="main", # Simplified for now
                chunk_index=i,
                text_content=chunk,
            )
            for i, chunk in enumerate(text_chunks)
        ]

        records = generate_embeddings(content_chunks, cohere_client)
        upsert_vectors_to_qdrant(records, qdrant_client)
        logging.info(f"Finished processing {url}. {len(records)} chunks stored.")
        
        # Add a delay between processing each URL to avoid rate limiting
        if i < len(source_urls) - 1:
            logging.info("Waiting for 60 seconds before processing the next URL...")
            time.sleep(60)


if __name__ == "__main__":
    main()