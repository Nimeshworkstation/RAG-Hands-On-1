from typing import List


def build_prompt(query: str, context_doc: List[str]) -> str:

    context_part: List[str] = []
    for i, doc in enumerate(context_doc):
        cleaned_context = doc.strip()
        if not cleaned_context:
            continue
        context_part.append(f"[Context {i+1}] -> \t {cleaned_context}")
    context = "\n\n".join(context_part)

    return f"""You are a helpful assistant. Answer ONLY from the provided context.
If the context is not enough, say exactly: "I don't have enough context."
Keep the answer concise and factual.
        
Context:

{context}

Question:
{query}

Answer: 

"""


def main():
    print(build_prompt("I", ["nimesh", "niket", "madhu"]))


if __name__ == "__main__":
    main()
