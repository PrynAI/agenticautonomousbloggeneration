from langchain_groq import ChatGroq
from dotenv import load_dotenv


class GroqLLM:
    def __init__(self):
        load_dotenv()

    def load_llm(self):
        try:
            llm=ChatGroq(model="openai/gpt-oss-120b")
            return llm
        except Exception as e:
            raise ValueError("Error occurred with exception: {e}")