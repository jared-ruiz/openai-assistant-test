from bs4 import BeautifulSoup
import requests
import markdownify

# create plain text of soup data
def html_to_text(html_text):
    soup = BeautifulSoup(html_text, "html.parser")
    return soup.get_text(strip=True)

# return article data from open API endpoint
def get_articles(): 
    
    # use endpoint in zendesk article page for retrieving articles
    url = "https://support.optisigns.com/api/v2/help_center/articles.json"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            articles = response.json()
            return articles
        else:
            print("Error:", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None
    
def main():
    #returns dictionary to then parse through each article and it's key value paies
    item = get_articles()

    # this checks to see if there is actually a dictionary returned and it contains the article key too
    if item and "articles" in item:
        for article in item["articles"]:
            article_html_body = article["body"]
            article_body = html_to_text(article_html_body)
            print(article_body)
    else:
        print("No articles found")
    
main()