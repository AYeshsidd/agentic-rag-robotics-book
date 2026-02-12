import React, { useState } from 'react';
import styles from './ChatInterface.module.css';

interface SourceReference {
  url: string;
  score: number;
  chunk_id?: string;
  content_preview?: string;
}

interface QueryResponse {
  answer: string;
  confidence: number;
  sources: SourceReference[];
  conversation_context?: string;
}

interface ErrorResponse {
  detail: string;
}

const ChatInterface: React.FC = () => {
  const [query, setQuery] = useState<string>('');
  const [response, setResponse] = useState<QueryResponse | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!query.trim()) {
      setError('Please enter a question');
      return;
    }

    setLoading(true);
    setError(null);
    setResponse(null);

    try {
      const res = await fetch('http://localhost:8001/api/query', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          query: query.trim(),
          limit: 3,
        }),
      });

      if (!res.ok) {
        const errorData: ErrorResponse = await res.json();
        throw new Error(errorData.detail || `HTTP error! status: ${res.status}`);
      }

      const data: QueryResponse = await res.json();
      setResponse(data);
    } catch (err) {
      if (err instanceof Error) {
        setError(err.message);
      } else {
        setError('An unexpected error occurred. Please try again.');
      }
    } finally {
      setLoading(false);
    }
  };

  const handleClear = () => {
    setQuery('');
    setResponse(null);
    setError(null);
  };

  return (
    <div className={styles.chatContainer}>
      <div className={styles.chatHeader}>
        <h2>Ask a Question About the Book</h2>
        <p>Get answers based on the book content with source references</p>
      </div>

      <form onSubmit={handleSubmit} className={styles.queryForm}>
        <div className={styles.inputGroup}>
          <textarea
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Enter your question here..."
            className={styles.queryInput}
            rows={3}
            disabled={loading}
          />
        </div>

        <div className={styles.buttonGroup}>
          <button
            type="submit"
            className={styles.submitButton}
            disabled={loading || !query.trim()}
          >
            {loading ? 'Processing...' : 'Ask Question'}
          </button>
          {(response || error) && (
            <button
              type="button"
              onClick={handleClear}
              className={styles.clearButton}
              disabled={loading}
            >
              Clear
            </button>
          )}
        </div>
      </form>

      {error && (
        <div className={styles.errorMessage}>
          <strong>Error:</strong> {error}
        </div>
      )}

      {response && (
        <div className={styles.responseContainer}>
          <div className={styles.answerSection}>
            <h3>Answer</h3>
            <p className={styles.answerText}>{response.answer}</p>
          </div>

          <div className={styles.metadataSection}>
            <div className={styles.confidenceScore}>
              <strong>Confidence:</strong>{' '}
              <span
                className={
                  response.confidence >= 0.7
                    ? styles.confidenceHigh
                    : response.confidence >= 0.4
                    ? styles.confidenceMedium
                    : styles.confidenceLow
                }
              >
                {(response.confidence * 100).toFixed(1)}%
              </span>
            </div>
          </div>

          {response.sources && response.sources.length > 0 ? (
            <div className={styles.sourcesSection}>
              <h4>Sources ({response.sources.length})</h4>
              <ul className={styles.sourcesList}>
                {response.sources.map((source, index) => (
                  <li key={index} className={styles.sourceItem}>
                    <a
                      href={source.url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className={styles.sourceLink}
                    >
                      {source.url}
                    </a>
                    <span className={styles.sourceScore}>
                      Score: {(source.score * 100).toFixed(1)}%
                    </span>
                  </li>
                ))}
              </ul>
            </div>
          ) : (
            <div className={styles.noSources}>
              <p>No relevant information found in the knowledge base.</p>
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default ChatInterface;
