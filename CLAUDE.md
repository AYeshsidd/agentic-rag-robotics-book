# physical_book2 Development Guidelines

Auto-generated from all feature plans. Last updated: 2026-02-06

## Active Technologies
- Python 3.13 + FastAPI, Uvicorn, existing agent.py (OpenAI, Qdrant Client, Cohere, Python-dotenv) (007-rag-backend-integration)
- N/A (stateless API, uses existing Qdrant vector database) (007-rag-backend-integration)
- TypeScript/JavaScript (React 18+, ES2020+) + React, Docusaurus 2.x theme system, CSS Modules (008-chatbot-ui-polish)
- N/A (UI-only feature, no data persistence) (008-chatbot-ui-polish)
- TypeScript/JavaScript (React 18+, ES2020+) + Docusaurus 2.x, React, CSS Modules (009-home-page-enhancement)

- Python 3.13 + OpenAI Agents SDK, Qdrant Client, Cohere, Python-dotenv, Requests (001-openai-rag-agent)

## Project Structure

```text
src/
tests/
```

## Commands

cd src; pytest; ruff check .

## Code Style

Python 3.13: Follow standard conventions

## Recent Changes
- 009-home-page-enhancement: Added TypeScript/JavaScript (React 18+, ES2020+) + Docusaurus 2.x, React, CSS Modules
- 008-chatbot-ui-polish: Added TypeScript/JavaScript (React 18+, ES2020+) + React, Docusaurus 2.x theme system, CSS Modules
- 007-rag-backend-integration: Added Python 3.13 + FastAPI, Uvicorn, existing agent.py (OpenAI, Qdrant Client, Cohere, Python-dotenv)


<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->
