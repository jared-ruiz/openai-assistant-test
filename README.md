# **OptiSigns-Backend-Test** - Jared Ruiz

> This project was a ground up, 0-100 learning experience and I documented everything I learned and how I approached my problem solving here if you would like to read through my logs!

> [Learning Log: Jared Ruiz](./learning_log.md)

## Installation Instructions 🌌

```
git pull 
```
<ins>For quick testing but unsafe practice:</ins> In Dockerfile -> Uncomment ENV variable and add your <Strong>OpenAI_API_KEY</Strong>.
```
docker build -t optisigns_test .

docker run optisigns_test
```
<ins>A safer method:</ins> Create a .env file at root and add in your api key:
```
API_KEY_OPENAI={insert your OpenAI API Key Here}
```
> <strong>Note:</strong> This will allow main.py to work without having to add your key into terminal or hard coding it into your Dockerfile which is bad practice and something I mistakenly did originally
<br>

Then, within your docker run command:
```
docker run --env-file .env optisigns_test
```

After successful docker run, go to [OpenAI Playground](https://platform.openai.com/playground)  and input test prompt:

> "How do I add a youtube video?"

Results should populate based on article data