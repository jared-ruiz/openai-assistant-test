import os
from openai import OpenAI
from dotenv import load_dotenv

def run_Agent(assistant_id):
    # return env variables
    load_dotenv()

    key = os.getenv("API_KEY_OPENAI")
    # assistant_key = os.getenv("ASSISTANT_ID")

    client = OpenAI(api_key=key)

    # create vector store
    vector_store = client.vector_stores.create(name="Articles")
    print(f"Vector Store ID - {vector_store.id}")

    # upload all .md files
    article_folder = "optisigns_articles"

    file_paths = [
        os.path.join(article_folder, article)
        for article in os.listdir(article_folder)
        if article.endswith(".md")
    ]

    file_streams = [open(path, "rb") for path in file_paths]

    # Add files to vector store
    file_batch = client.vector_stores.file_batches.upload_and_poll(
        vector_store_id = vector_store.id,
        files = file_streams
    )

    # check the status of files 
    print(f"File Status {file_batch.status}")

    # update assistant with vector store
    client.beta.assistants.update(
        assistant_id=assistant_id,
        tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}}
    )

    print("Assistant Updated with Vector Store!")
    

    