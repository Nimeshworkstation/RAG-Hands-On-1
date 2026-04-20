from loader import load_documents
from splitter import chunk_documents
from embedder import embed_chunks
from vector_store import vector_store


def run_ingestion_pipeline(data_dir: str):

    print("=" * 50)
    print("Starting Data Ingestion Pipeline")
    print("=" * 50)

    print("\n[Step 1] Loading documents...")
    documents = load_documents(data_dir)

    if not documents:
        print("[ERROR] No documents loaded. Exiting.")
        return

    print("\n[Step 2] Chunking documents...")
    chunks = chunk_documents(documents)

    print("\n[Step 3] Generating embeddings...")
    embeddings = embed_chunks(chunks)

    print("\n[Step 4] Storing in ChromaDB...")
    vector_store(chunks, embeddings)

    print("\n" + "=" * 50)
    print("Pipeline completed successfully!")
    print("=" * 50)


def main():
    DATA_DIR = "../../data"

    # Run the pipeline
    run_ingestion_pipeline(DATA_DIR)


if __name__ == "__main__":
    main()
