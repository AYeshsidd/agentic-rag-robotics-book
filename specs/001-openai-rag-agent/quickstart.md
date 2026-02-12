# Quickstart Guide: OpenAI RAG Agent

## Prerequisites

- Python 3.13+
- OpenAI API key
- Access to Qdrant Cloud instance with book content indexed
- Existing environment file with QDRANT_URL, QDRANT_API_KEY, and OPENAI_API_KEY

## Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies**
   ```bash
   pip install -r backend/requirements.txt
   pip install openai
   ```

3. **Configure environment**
   Ensure your `.env` file contains:
   ```
   OPENAI_API_KEY=your_openai_api_key
   QDRANT_URL=your_qdrant_cloud_url
   QDRANT_API_KEY=your_qdrant_api_key
   QDRANT_COLLECTION_NAME=chatbot
   ```

## Running the Agent

1. **Start the agent**
   ```bash
   cd backend
   python agent.py
   ```

2. **Interactive mode**
   The agent will start in interactive mode where you can enter queries:
   ```
   RAG Agent Ready! Enter your queries (type 'quit' to exit):
   > Explain ROS2
   ```

3. **Batch testing**
   Run predefined test queries:
   ```bash
   python agent.py --test
   ```

## Sample Queries

Try these sample queries to test the agent:
- "Explain ROS2"
- "What is a ROS2 node?"
- "How do ROS2 topics work?"
- "Compare ROS2 and ROS1"

## Troubleshooting

- **Connection errors**: Verify QDRANT_URL and QDRANT_API_KEY in your .env file
- **API errors**: Check OPENAI_API_KEY is properly set
- **No results**: Confirm that book content has been indexed in Qdrant
- **Slow responses**: May indicate network latency or large vector database

## Expected Output

For a query like "Explain ROS2", the agent should:
1. Retrieve relevant content chunks from Qdrant
2. Show the retrieved chunks and their sources
3. Generate a response based strictly on the retrieved content
4. Indicate the confidence level of the response