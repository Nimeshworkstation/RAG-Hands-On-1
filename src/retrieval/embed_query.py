from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")


def embed_query(query: str) -> np.ndarray:
    embeddings = model.encode([query], show_progress_bar=True, convert_to_numpy=True)
    print(f"Embeddings shape: {embeddings.shape}")
    return embeddings


def main():
    query: str = " nginx, docker and oop"
    embed_query(query)


if __name__ == "__main__":
    main()
