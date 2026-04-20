from pathlib import Path
from typing import List
from langchain_core.documents import Document
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    CSVLoader,
    UnstructuredMarkdownLoader,
)

SUPPORTED_EXTENSIONS = {".pdf", ".txt", ".md", ".csv"}


def load_documents(data_dir: str) -> List[Document]:

    docs: List[Document] = []
    base_path = Path(data_dir)
    print(base_path)

    if not base_path.exists():
        print(f"[WARN] Data directory not found: {data_dir}")
        return []

    for file_path in base_path.rglob("*"):
        if not file_path.is_file():
            continue

        ext = file_path.suffix.lower()
        if ext not in SUPPORTED_EXTENSIONS:
            continue

        try:
            if ext == ".pdf":
                loader = PyPDFLoader(str(file_path))
            elif ext == ".txt":
                loader = TextLoader(str(file_path), encoding="utf-8")
            elif ext == ".csv":
                loader = CSVLoader(file_path=str(file_path))
            elif ext == ".md":
                loader = UnstructuredMarkdownLoader(str(file_path))

            else:
                continue

            file_docs = loader.load()
            for item in file_docs:
                item.metadata.update(
                    {
                        "source": str(file_path),
                        "filename": file_path.name,
                        "extension": ext,
                    }
                )
            docs.extend(file_docs)
        except Exception as e:
            print(f"Error occured while loading {file_path},{e}")
    print(f"[INFO] Loaded {len(docs)} documents from {data_dir}")
    return docs


def main():
    docs = load_documents(r"..\..\data")


if __name__ == "__main__":
    main()
