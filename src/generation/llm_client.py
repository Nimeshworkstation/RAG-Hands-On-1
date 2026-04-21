import os
from dotenv import load_dotenv
from google import genai
from .prompt_builder import build_prompt

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise RuntimeError("API_KEY not found in environment")


client = genai.Client(api_key=api_key)


def generate_answer(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )
        return response.text or ""

    except Exception as e:
        raise RuntimeError(f"LLM generation failed: {e}") from e


def main():
    pass


if __name__ == "__main__":
    main()
