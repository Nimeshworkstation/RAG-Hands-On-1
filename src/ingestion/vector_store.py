import chromadb
import uuid
from langchain_core.documents import Document
from typing import List
import numpy as np

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="my_docs")


def vector_store(chunks: List[Document], embeddings: np.ndarray):
    if len(chunks) != len(embeddings):
        raise RuntimeError("Something went wrong")

    ids = []
    documents = []
    embeddings_list = []
    metadatas = []

    for chunk, embedding in zip(chunks, embeddings):
        ids.append(str(uuid.uuid4()))
        documents.append(chunk.page_content)
        embeddings_list.append(embedding.tolist())
        metadatas.append(chunk.metadata)

    collection.add(
        ids=ids, documents=documents, embeddings=embeddings_list, metadatas=metadatas
    )

    print(f"[INFO] Stored {len(chunks)} chunks in ChromaDB")


def main():
    pass


if __name__ == "__main__":
    main()
