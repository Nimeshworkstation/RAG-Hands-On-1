from src.retrieval.embed_query import embed_query
from src.retrieval.search_query import get_context
from src.generation.prompt_builder import build_prompt
from src.generation.llm_client import generate_answer
from src.generation.response_parser import parse_response


def run_rag(query: str) -> str:
    query_embedding = embed_query(query)[0]  # shape: (384,)
    results = get_context(query_embedding)
    breakpoint()
    documents = results.get("documents")
    docs = documents[0] if documents else []
    metadatas = results.get("metadatas")
    metas = metadatas[0] if metadatas else []
    if not docs:
        return "I don't have enough context."

    # 3) Build prompt
    prompt = build_prompt(query, docs)

    # 4) Generate answer
    raw_answer = generate_answer(prompt)

    # 5) Parse/clean answer
    final_answer = parse_response(raw_answer)

    # 6) Optional citations block
    sources = []
    for m in metas:
        source = m.get("source", "unknown")
        page = m.get("page", "N/A")
        sources.append(f"{source} (page: {page})")

    if sources:
        final_answer += "\n\nSources:\n" + "\n".join(f"- {s}" for s in sources)

    return final_answer


def main():
    query = "What experience do I have with Docker and Nginx?"

    # Temporarily print retrieved docs
    query_embedding = embed_query(query)[0]
    results = get_context(query_embedding)
    documents = results.get("documents")
    docs = documents[0] if documents else []

    print("\n=== Retrieved Documents ===")
    for i, doc in enumerate(docs, 1):
        print(f"\nDoc {i}:\n{doc[:300]}...")

    # Comment out the LLM part until you fix the API
    # answer = run_rag(query)
    # print("\nFinal Answer:\n")
    # print(answer)


if __name__ == "__main__":
    main()
