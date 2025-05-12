# **OptiSigns-Backend-Test** - Jared Ruiz

> This project was a ground up, 0-100 learning experience and I documented everything I learned and how I approached my problem solving here if you would like to read through my logs!

> [Learning Log: Jared Ruiz](./learning_log.md)

## Installation Instructions 🌌

```
git pull 
```

In Dockerfile -> Uncomment ENV variable and add your <Strong>OpenAI_API_KEY</Strong>.
```
docker build -t optisigns_test .

docker run optisigns_test
```
After successful docker run, go to [OpenAI Playground](https://platform.openai.com/playground)  and input test prompt:

> "How do I add a youtube video?"

Results should populate based on article data