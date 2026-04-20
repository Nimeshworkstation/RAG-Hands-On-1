from typing import List
from langchain_core.documents import Document
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")


def embed_chunks(chunks: List[Document]) -> np.ndarray:
    texts = [chunk.page_content for chunk in chunks]

    embeddings = model.encode(texts, show_progress_bar=True, convert_to_numpy=True)
    print(f"Embeddings shape: {embeddings.shape}")

    return embeddings


def main():
    pass


if __name__ == "__main__":
    main()
