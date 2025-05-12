import os
from openai import OpenAI
from dotenv import load_dotenv

def create_Assistant():
    # loads in env variables like api key
    load_dotenv()

    key = os.getenv("API_KEY_OPENAI")

    client = OpenAI(api_key=key)

    description = """
    You are OptiBot, the customer-support bot for OptiSigns.com.
    • Tone: helpful, factual, concise.
    • Only answer using the uploaded docs.
    • Max 5 bullet points; else link to the doc.
    • Cite up to 3 "Article URL:" lines per reply.
    """

    assistant = client.beta.assistants.create(
        name= "OptiSigns Backend Test",
        description= description,
        # instructions= instructions,
        model= "gpt-4o",
        tools= [{"type": "file_search"}]
    )

    # print(assistant)
    return(assistant.id)