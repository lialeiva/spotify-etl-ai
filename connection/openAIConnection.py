"""
Establish a connection to the OpenAI API

"""

from openai import OpenAI
from cfg import OPENAI_API_KEY

def openai_connection():
    try:
        api_key = OPENAI_API_KEY
        client = OpenAI(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1"
        )
        return client
    except Exception as e:
        print(f"❌ OpenAI connection error: {e}")
        return None

