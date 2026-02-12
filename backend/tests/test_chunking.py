import pytest
from ..main import chunk_text

def test_chunk_text_basic():
    """
    Tests that chunk_text correctly splits a simple string into chunks
    with the expected size and overlap.
    """
    long_text = "This is a very long string that needs to be chunked. " * 10
    
    # Assuming chunk_size=1000, chunk_overlap=200 from main.py
    chunks = chunk_text(long_text)
    
    assert isinstance(chunks, list)
    assert len(chunks) > 0
    
    # Verify chunk sizes are within expected limits (considering overlap)
    for chunk in chunks:
        assert len(chunk) <= 1000 + 200 # Max possible chunk size with overlap
        assert len(chunk) > 0

    # Verify overlap (check a couple of middle chunks)
    if len(chunks) > 1:
        # The end of the first chunk should match the beginning of the second chunk's overlap
        # This is a simplified check, actual overlap logic can be more complex
        overlap_start = len(chunks[0]) - 200
        if overlap_start > 0: # Ensure there's enough text for overlap
             assert chunks[0][overlap_start:] in chunks[1] # Check if the overlap part of chunk0 is in chunk1

def test_chunk_text_empty():
    """
    Tests that chunk_text handles an empty string.
    """
    chunks = chunk_text("")
    assert chunks == [] # Langchain's splitter returns [] for empty input

def test_chunk_text_short_text():
    """
    Tests that chunk_text handles a text shorter than the chunk size.
    """
    short_text = "This is a short text."
    chunks = chunk_text(short_text)
    assert len(chunks) == 1
    assert chunks[0] == short_text
