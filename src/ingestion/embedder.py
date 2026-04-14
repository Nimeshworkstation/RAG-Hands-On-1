from typing import List
from langchain_core.documents import Document
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def embed_chunks(chunks: List[Document]):
    texts = [chunk.page_content for chunk in chunks]
    embeddings = model.encode(texts, show_progress_bar=True)
    print(f"Embeddings shape: {embeddings.shape}")

    return embeddings


def main():
    pass


if __name__ == "__main__":
    main()
