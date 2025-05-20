import requests
import markdownify
import os
import slugify

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
    
def article_Markdown():
    # returns dictionary to then parse through each article and it's key value pairs
    article_data = get_articles()
    
    # create directory for articles 
    directory_name = "tech_articles"
    os.makedirs(directory_name, exist_ok=True)

    # this checks to see if there is actually a dictionary returned and it contains the article key too. Should loop 30 times minimum
    if article_data and "articles" in article_data:
        for article in article_data["articles"]:
            article_title = article["title"]
            article_body = article["body"]
            markdownBody = markdownify.markdownify(article_body)
            
            # create file path to save the below created file to - use created directory + file name
            title = slugify.slugify(article_title)
            file_path = os.path.join(directory_name, title + '.md')
            
            # assign title to md file name and body written onto file
            with open(file_path, "w", encoding="utf-8") as article:
                article.write(markdownBody)
    
    else:
        print("No articles found")