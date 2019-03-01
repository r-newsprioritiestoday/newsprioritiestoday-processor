from requests_html import HTMLSession
from datetime import datetime

session = HTMLSession()
r = session.get('https://www.foxnews.com/')


def scrape():

    result = {
        "datetime": str(datetime.now()),
        "country": "USA",
        "source": "https://www.foxnews.com/",
        "articles": []
    }

    # get main content div
    main = r.html.find('main.main-content', first=True)
    
    # get links and articles in main content
    articles = main.find('h2.title > a')

    for article in articles:
        _article = {
            "link": "",
            "headline": "",
            "text": "", # optional
            "category": ""
        }

        _article["link"] = list(article.links)[0]
        _article["headline"] = article.text

        result["articles"].append(_article)
    return result

print(scrape())