# Learning Log (WIP)
### General Project Goals
- Scrape articles from OptiSigns website utilzing python
- Build assistnat, upload markdown files into OpenAI's vector store via OpenAI API
- Deploy scrapper and dockerize it

### Personal Thoughts Before Project
- Prior to recieving this assignment, I had never worked with the OpenAI API at all, never touched Docker besides a few simple tasks required of me at my current work, and have not worked with Python that frequently due to my focus on MERN stack web development. This entire task posed a great challenge for me. I was gratiously alloted 2 weeks to work on this assignment after my normal 9-5 hours and my goal is to do my absolute best, learn as fast and efficiently as possible and hopefully get a solid attempt in on this project.

### Bare Minimum Expectations
> Project plan

> Learn the tools

> Demonstrate my commitment to problem solving within a time sensetive enviornment

## Day 0 - Rubber Ducking

I begin my journey with a lot of questions and I mean <strong>ALOT</strong> of questions. My current work is within government contracting cyber security, and my coworker and friend is a seasoned software engineer making a big impact at the company. I was able to find some time to ask 1 thing.

1. What is Docker?
> I had a general understanding based on the work we do, but I wanted to see if my coworker has a good way of describing it's use cases and key features to help make it click in my head.

After our discussion, my understanding was that Docker aimed to solve the industry problem of: 
-  "It works on my machine, it should work on yours"

It reminded me of virutal machines, and how you can utilize any OS and load the instance with whatever you need to develop on (dependencies, users, networking specifics, etc.), and even turn that VM into a distributable copy for others to utilize at their discretion. 

As per the Docker Website:
``` A Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings.```
<br> > [Docker: What Are Containers?](https://www.docker.com/resources/what-container/)

This revalation was very interesting to me. This allows everyone to be able to develop on the same working version of a particular application without the fear of running into frequent compatability issues. Perfect. Now how do I incorporate that into my project?

Realistically, I would want to wait until my web scrapper is complete before I Dockerize it, but I could move on to learning how to work with Python and Web Scrapping, get something simple going and then practice Dockerizing that? I believe extrapolating the objective into pieces would be good for me and my learning so I will do just that.


## Day 1 - Python and Web Scrapping 101

