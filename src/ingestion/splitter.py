from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List, Any
from langchain_core.documents import Document


def chunk_documents(documents: List[Document]) -> List[Document]:

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        separators=["\n\n", "\n", " ", ""],
    )
    chunks = splitter.split_documents(documents)
    print(f"Splitted {documents} into {len(chunks)} chunks")

    return chunks


def main():
    pass


if __name__ == "__main__":
    main()
