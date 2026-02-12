#!/usr/bin/env python3
"""
Simple test script to verify the RAG Agent functionality
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from agent import RAGAgent

def test_basic_functionality():
    """Test basic agent functionality."""
    print("Testing RAG Agent basic functionality...")

    try:
        # Initialize the agent
        agent = RAGAgent()
        print("[OK] Agent initialized successfully")

        # Test a simple query
        result = agent.query("Explain ROS2", limit=2)

        print(f"[OK] Query processed successfully")
        print(f"  - Query: {result['query']}")
        print(f"  - Answer length: {len(result['answer'])} characters")
        print(f"  - Retrieved chunks: {len(result['retrieved_chunks'])}")
        print(f"  - Confidence: {result['confidence']:.2f}")

        # Test with a follow-up query
        follow_up_result = agent.query_with_context("What are ROS2 nodes?", limit=2)
        print(f"[OK] Follow-up query processed successfully")
        print(f"  - Retrieved {len(follow_up_result['retrieved_chunks'])} chunks")
        print(f"  - Confidence: {follow_up_result['confidence']:.2f}")

        return True

    except Exception as e:
        print(f"[ERROR] Error during testing: {e}")
        return False

if __name__ == "__main__":
    success = test_basic_functionality()
    if success:
        print("\n[OK] All tests passed!")
    else:
        print("\n[ERROR] Some tests failed!")
        sys.exit(1)