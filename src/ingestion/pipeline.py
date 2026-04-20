from loader import load_documents
from splitter import chunk_documents
from embedder import embed_chunks
from vector_store import vector_store


def run_ingestion_pipeline(data_dir: str):
    docs = load_documents(data_dir)
    chunks = chunk_documents(docs)
    embeddings = embed_chunks(chunks)
    vector_store(chunks, embeddings)


def main():
    breakpoint()
    run_ingestion_pipeline(".data/document.pdf")


if __name__ == "__main__":
    main()
