# Dockerfile, Image and Container

FROM python:3.13

ADD webscraper.py assistant_run.py assistant_create.py vector_store_delete.py main.py requirements.txt /

# uncomment below and add api key for openai playground
# ENV API_KEY_OPENAI=""

RUN pip install -r requirements.txt

CMD ["python", "main.py"] 
