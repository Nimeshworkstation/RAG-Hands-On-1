import chromadb
import uuid
from langchain_core.documents import Document
from typing import List
import numpy as np
from loader import load_documents
from splitter import chunk_documents
from embedder import embed_chunks

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
    print("*" * 50)
    docs = load_documents(r"..\..\data")
    print("*" * 50)
    chunks = chunk_documents(docs)
    print("*" * 50)
    embeddings = embed_chunks(chunks)
    print("*" * 50)
    vector_store(chunks, embeddings)


if __name__ == "__main__":
    main()
