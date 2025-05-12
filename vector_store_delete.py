import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("API_KEY_OPENAI")
client = OpenAI(api_key=key)
vs_id = os.getenv("VECTOR_STORE_ID")

# use this to delete vector store after testing or troubleshooting locally
deleted_vector_store = client.vector_stores.delete(
    vector_store_id=vs_id
)

print(deleted_vector_store)