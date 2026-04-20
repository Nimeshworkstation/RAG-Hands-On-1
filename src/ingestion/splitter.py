from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List
from langchain_core.documents import Document
from loader import load_documents


def chunk_documents(documents: List[Document]) -> List[Document]:

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        separators=["\n\n", "\n", " ", ""],
    )
    chunks = splitter.split_documents(documents)
    print(f"Splitted {len(documents)} into {len(chunks)} chunks")

    return chunks


def main():
    docs = load_documents(r"..\..\data")
    print("*" * 50)

    chunk_documents(docs)


if __name__ == "__main__":
    main()
