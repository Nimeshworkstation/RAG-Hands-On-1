from typing import Any
import numpy as np
import chromadb
from chromadb.api.types import QueryResult
from .embed_query import embed_query
import json
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[1] / "ingestion" / "chroma_db"
print(DB_PATH)

client = chromadb.PersistentClient(path=str(DB_PATH))
collection = client.get_collection("my_docs")


def get_context(query_embedding: np.ndarray, n_results: int = 3) -> QueryResult:
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
        include=["documents", "metadatas", "distances"],
    )
    return results


def main():
    query: str = " nginx, docker and oop"
    query_embedding = embed_query(query)[0]
    result = get_context(query_embedding)
    print(result)
    print(f"Total chunks in database: {collection.count()}")


if __name__ == "__main__":
    main()
