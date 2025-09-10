# models/llm_config.py
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = "gpt-3.5-turbo"

def get_model_config():
    return {
        "api_key": OPENAI_API_KEY,
        "model": OPENAI_MODEL,
        "temperature": 0.7,
        "max_tokens": 500,
    }
