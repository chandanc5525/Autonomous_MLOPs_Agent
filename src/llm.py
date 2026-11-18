"""Initialize the local Qwen3 LLM using Ollama and LangChain."""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")
MODEL = os.getenv("MODEL")

llm = ChatOpenAI(
    base_url=BASE_URL,
    api_key=API_KEY,
    model=MODEL,
    temperature=0
)

def test_llm():
    response = llm.invoke(
        "Explain MLOps in 3 simple points."
    )

    print(response.content)


if __name__ == "__main__":
    test_llm()
