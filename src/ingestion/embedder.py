from typing import List
from langchain_core.documents import Document
from sentence_transformers import SentenceTransformer
import numpy as np
from loader import load_documents
from splitter import chunk_documents

model = SentenceTransformer("all-MiniLM-L6-v2")


def embed_chunks(chunks: List[Document]) -> np.ndarray:
    texts = [chunk.page_content for chunk in chunks]

    embeddings = model.encode(texts, show_progress_bar=True, convert_to_numpy=True)
    print(f"Embeddings shape: {embeddings.shape}")

    return embeddings


def main():
    print("*" * 50)
    docs = load_documents(r"..\..\data")
    print("*" * 50)
    chunks = chunk_documents(docs)
    print("*" * 50)
    embed_chunks(chunks)


if __name__ == "__main__":
    main()
