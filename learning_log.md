# Learning Log 📚 (WIP)
### General Project Goals
- Scrape articles from OptiSigns website utilizing python
- Build assistant, upload markdown files into OpenAI's vector store via OpenAI API
- Deploy scraper and dockerize it

### Personal Thoughts Before Project
- Prior to receiving this assignment, I had never worked with the OpenAI API at all, never touched Docker besides a few simple tasks required of me at my current work, and have not worked with Python that frequently due to my focus on MERN stack web development. This entire task posed a great challenge for me. I was graciously alloted 2 weeks to work on this assignment after my normal 9-5 hours and my goal is to do my absolute best, learn as fast and efficiently as possible and hopefully get a solid attempt in on this project.

### Bare Minimum Expectations
- Project plan

- Learn the tools

- Demonstrate my commitment to problem solving within a time sensitive environment

## Day 0 - Rubber Ducking 🦆

I begin my journey with a lot of questions and I mean <strong>A LOT</strong> of questions. My current work is within government contracting cyber security, and my coworker and friend is a seasoned software engineer making a big impact at the company. I was able to find some time to ask 1 thing.

1. What is Docker?
> I had a general understanding based on the work we do, but I wanted to see if my coworker has a good way of describing it's use cases and key features to help make it click in my head.

After our discussion, my understanding was that Docker aimed to solve the industry problem of: 
-  "It works on my machine, it should work on yours"

It reminded me of virtual machines, and how you can utilize any OS and load the instance with whatever you need to develop on (dependencies, users, networking specifics, etc.), and even turn that VM into a distributable copy for others to utilize at their discretion. 

As per the Docker Website:
``` A Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings.```
<br> > [Docker: What Are Containers?](https://www.docker.com/resources/what-container/)

This revelation was very interesting to me. This allows everyone to be able to develop on the same working version of a particular application without the fear of running into frequent compatibility issues. Perfect. Now how do I incorporate that into my project?

Realistically, I would want to wait until my web scrapper is complete before I Dockerize it, but I could move on to learning how to work with Python and Web Scrapping, get something simple going and then practice Dockerizing that? I believe extrapolating the objective into pieces would be good for me and my learning so I will do just that.


## Day 1 - Python and Web Scrapping 101 🖥️

My previous experience with web scrapping was probably back when I was in college and my friend and I wanted a way to pull data off of our favorite gaming website to see our hiscores update daily. I had no coding experience besides some exposure to C through Harvard's free online course and I was not able to fully implement my vision.

Fast forward today, where I have soley been focusing on web development and digital marketing, so this serves to be a fun and challenging reintroduction to what I had originally wanted to learn many years back.

### Learning Process Begins

- I've been learning my entire life and the way I have always approached new topics or projects is to watch others either build something I am interested in, or explain it to me with visuals. I am a very visually guided learner. I turned to YouTube and introduced the topic to myself with this video:
<br> > [Beginners Guide To Web Scraping with Python - All You Need To Know](https://youtu.be/QhD015WUMxE?si=LqAna1kFAnqY-k3q)

- Before attempting to scrape the [support.optisigns.com](https://support.optisigns.com/hc/en-us), I wanted to do some tests and document my results. I'm going to attempt and scrape some simple websites and return a markdown version of the content without issue, then build up to the desired 30+ amount requested in the instructions.

- I first created my python file titled <strong>webscraper.py</strong>, and set up my virtual environment. I already knew that it would be much more organized and convenient to have a requirements.txt accompanied with it easy cloning and use on the user's end.  

### Notes for Virtual Environment Management
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
 
- I followed along with the video above and realized that scrapping a static website was not as hard as it initially looked. Beautiful soup has a lot of options for you to parse through your html data and return the core bits that you want. I need to read through the documentation a bit more to get a handle on what I may or may not need in my returned information. 

- After seeing how I could get this script to run how I want, I decided to just jump in head first and try and parse through the OptiSigns website. I realized this would require a lot more knowledge of the libraries I'm using and possibly more since I want to travel through all the assorted article links to their designated article pages, <strong>THEN</strong> extract the html from those pages and export them somehow into a folder locally. It seems there's a native library that can handle directory creation so I will try and use that.

- After an hour or so of research and trial and error, it seems requests is not able to get the correct information from the website. It seems it's because OptiSigns is using a dynamically rendered site that simply does not allow requests to function on it's own. A stack overflow post suggests "selenium" to scrape the page but I decided to explore the option presented in the instructions utilizing Zendesk. With some work, I was able to return an array of article objects from OptiSigns zendesk api and that really helped me click things in my head. I havent done a lot of API calls with python so I would need to look up the structure online, which shouldn't be too far off from javascript's syntax.

- I read through this [python api tutorial](https://www.geeksforgeeks.org/how-to-make-api-calls-using-python/) and structured my initial test similarly. I was able to return a lot of article data from the API endpoint and now that I know there is successful content being reached, I can figure out how to parse it and organize it properly. I'm imagining I can loop through the array of objects and somehow turn them into .md files with each pass.

- I took some time reviewing dictionary handling with python and I was able to return all the article information I needed but it was loaded with HTML elements. So I got to return to what I was originally studying and use beautiful soup to remove the html elements and return plain text. This site helped me review some of my dictionary questions. [W3School] (https://www.w3schools.com/python/python_dictionaries_access.asp)

### End of Day 1 - Thoughts 💡

This was a very eventful day of studying and trial and error. I believe I had over 30 tabs open trying to search for all sorts of solutions to questions I had. Lots of visits to discussion boards, youtube videos, and more. I am ending the day with my web scraper not necessarily scraping a static website anymore, but pulling article data from an available API via OptiSign and Zendesk, parsing it's json data for all the info I need and returning it via terminal output. I will try and see how I can use existing libraries to create a directory within my project folder and output individual markdown files for each article. That would be a good next milestone. There are instructions to keep relative links, code blocks and heading and just remove navs and ads. There is bound to be something within the beautiful soup documentation to remove those items, or maybe through other means as well. 

## Day 2 - Creating and Writing to New Directories Via Python ✏️

Picking up from my previous development day, I want to continue exploring the potential solution of using this API to pull all the 30+ articles I need, creating a new directory, and writing each article into it's own .MD file within it. I've seen it done via JavaScript before in my 4 years being exposed to the language, and I assume it's very similar. I will begin researching if there is a library that handles this function or if it needs to be hardcoded into the function. I will also begin researching how to utilize markdownify to turn the html page into markdown files. 

### Goals for Today

- Confirm the correct information is being returned from my api call
- Learn how to create and write to a new directory via Python
- Learn how to turn each article into a markdown file and place each into the designated directory with unique naming schemes for each <strong>(i.e 0_article.md - 29_article.md)</strong>

> [Refer to Virtual Environment Management Notes Before Beginning Development](#notes-for-virtual-environment-management)

### Creating Directories Via Python

The first step I feel I need to be able to do is upon data acquisition, I need to create a named directory to house the markdown files. I introduced this topic to myself through this video
> [Python Tutorial #36 - Directory & File Management in Python Programming](https://youtu.be/-Z5nWDtSkPc?si=BHBDy7PXl-RCkHsy)
<br>

The video focused on the <strong>os module</Strong> which allows you to interact with the operating system, which is exactly what we need for this step.
> [W3 Schools: Python os Module ](https://www.w3schools.com/python/module_os.asp)
<br>

### os File Handling

 - <Strong>open() Function:</Strong> Function takes two parameters, <ins> filename and mode.</ins> 
 <br>
 - <Strong>makedirs() Function:</Strong> Creates a directory recursively
> [Python File Handling](https://www.w3schools.com/python/python_file_handling.asp)
<br>

 4 Methods for Opening Files: 

> "r" - Read - Default value. Opens a file for reading, error if the file does not exist
<br>
> "a" - Append - will create a file if the specified file does not exist
<br>
> "x" - Create - will create a file, returns an error if the file exists
<br>
> "w" - Write - will create a file if the specified file does no exist 

I initially placed the makedirs() function in the loop but quickly realized it would want to create a new directory every loop and cause a lot of issues. I opted to place the directory creation right after returning the dictionary of articles, then go into the key value verification and begin returning the data.

I managed to successfully create a directory titled "optisigns_articles" upon running. Big step toward writing markdown files into them.