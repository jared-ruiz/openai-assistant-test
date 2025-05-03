# Learning Log 📚 (WIP)
### General Project Goals
- Scrape articles from OptiSigns website utilzing python
- Build assistnat, upload markdown files into OpenAI's vector store via OpenAI API
- Deploy scrapper and dockerize it

### Personal Thoughts Before Project
- Prior to recieving this assignment, I had never worked with the OpenAI API at all, never touched Docker besides a few simple tasks required of me at my current work, and have not worked with Python that frequently due to my focus on MERN stack web development. This entire task posed a great challenge for me. I was gratiously alloted 2 weeks to work on this assignment after my normal 9-5 hours and my goal is to do my absolute best, learn as fast and efficiently as possible and hopefully get a solid attempt in on this project.

### Bare Minimum Expectations
- Project plan

- Learn the tools

- Demonstrate my commitment to problem solving within a time sensetive enviornment

## Day 0 - Rubber Ducking 🦆

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


## Day 1 - Python and Web Scrapping 101 🖥️

My previous experience with web scrapping was probably back when I was in college and my friend and I wanted a way to pull data off of our favorite gaming website to see our hiscores update daily. I had no coding experience besides some exposure to C through Harvards free online course and I was not able to fully implement my vision.

Fast forward today, where I have soley been focusing on web development and digital marketing, so this serves to be a fun and challenging reintroduction to what I had originally wanted to learn many years back.

### Learning Process Begins

- I've been learning my entire life and the way I have always approached new topics or proejcts is to watch others either build something I am interested in, or explain to me with visuals. I am a very visually guided learner. I turned to YouTube and introduced the topic to myself with this video 
<br> > [Beginners Guide To Web Scraping with Python - All You Need To Know](https://youtu.be/QhD015WUMxE?si=LqAna1kFAnqY-k3q)

- Before attempting to scrape the [support.optisigns.com](https://support.optisigns.com/hc/en-us), I wanted to do some tests and document my results. I'm going to attempt and scrape some simple websites and return a markdown version of the content without issue, then build up to the desired 30+ amount requested in the instructions.

- I first created my python file titled <strong>webscraper.py</strong>, and set up my virtual enviornment. I already knew that it would be much more organized and convenient to have a requirements.txt accompanied with it easy cloning and use on the user's end.  

### Notes for Virtual Enviornment Management
> <strong>Activating virtual enviornment:</strong> env\Scripts\activate
<br>
> <strong>Deactivating virtual enviornment:</strong> deactivate
<br>
> <strong>List currently installed dependencies:</strong> pip list
<br>
> <strong>Output requirements.txt:</strong> pip freeze > requirements.txt
<br>
> <strong>Install requirements.txt</strong> pip install -r requirements.txt

### Dependencies Used

- <strong>requests:</strong> Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your PUT & POST data — but nowadays, just use the json method! [pypi.com](https://pypi.org/project/requests/)<br>

- <strong>beautifulsoup4:</strong> Beautiful Soup is a library that makes it easy to scrape information from web pages. It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree. [pypi.com](https://pypi.org/project/beautifulsoup4/)
<br>

- <strong>markdownify:</strong> Convert some HTML to Markdown. [pypi.com](https://pypi.org/project/markdownify/)

I also thought ahead in finding a library that would help me translate the returned information from beautiful soup into markdown, hence the discover of markdownify.

### Initial Scraper Testing
 
