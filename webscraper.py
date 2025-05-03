from bs4 import BeautifulSoup
import requests
import markdownify

# page to test scrape [https://quotes.toscrape.com/]
page_to_scrape = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

quotes = soup.find_all("span", attrs={"class": "text"})
authors = soup.find_all("small", attrs={"class": "author"})

for quote, author in zip(quotes, authors):
    print(quote.text + " - " + author.text)