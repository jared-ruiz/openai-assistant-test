from webscraper import article_Markdown
from assistant_create import create_Assistant
from assistant_run import run_Agent


def main():

    # populate articles
    article_Markdown()

    # return assistant id from assistant create()
    assistant_id = create_Assistant()

    run_Agent(assistant_id)
    
# invoke main
main()