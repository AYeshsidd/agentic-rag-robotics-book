import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient
import numpy as np

load_dotenv()

def debug_qdrant_query():
    """A minimal script to debug the Qdrant query method."""
    print("Initializing Qdrant client...")
    client = QdrantClient(
        url=os.getenv("QDRANT_URL"),
        api_key=os.getenv("QDRANT_API_KEY"),
    )
    print("Qdrant client initialized.")

    collection_name = os.getenv("QDRANT_COLLECTION_NAME")
    if not collection_name:
        print("Error: QDRANT_COLLECTION_NAME not set.")
        return

    print(f"Attempting to query collection: '{collection_name}'")

    try:
        query_results = client.query(
            collection_name=collection_name,
            query_text="What is a ROS 2 Node?",
            limit=1
        )
        print("Query method call was successful.")
        print("Results:", query_results)
    except Exception as e:
        print(f"An error occurred: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    debug_qdrant_query()
