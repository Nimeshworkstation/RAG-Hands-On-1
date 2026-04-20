from typing import Any
import chromadb
from chromadb.api.types import QueryResult


client = chromadb.PersistentClient(path="../ingestion/chroma_db")
collection = client.get_collection("my_docs")


def get_result(query_embedding: list[float]) -> QueryResult:
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3,
        include=["documents", "metadatas", "distances"],
    )
    return results


def main():
    pass


if __name__ == "__main__":
    main()
