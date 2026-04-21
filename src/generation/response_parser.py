import re


def parse_response(raw_text: str) -> str:
    if not raw_text:
        return "I don't have enough context."

    text = raw_text.strip()

    # Remove markdown code fences if model wraps answer in them
    text = re.sub(r"^```[a-zA-Z]*\n?", "", text)
    text = re.sub(r"\n?```$", "", text)

    # Normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()

    # Safety fallback
    if not text:
        return "I don't have enough context."

    return text


def main():
    pass


if __name__ == "__main__":
    main()
