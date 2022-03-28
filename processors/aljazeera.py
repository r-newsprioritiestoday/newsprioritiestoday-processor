from requests_html import HTML
from datetime import datetime

def process(raw_html, source):

    html = HTML(html=raw_html)

    result = {
        "datetime": datetime.now(),
        "source": source,
        "articles": []
    }

    articles = html.find('article')

    for article in articles:
        _article = {
            "link": "",
            "headline": "",
            "text": "", # optional
            "category": ""
        }
        if len(list(article.links)) != 0:
            if article.find('h3', first=True):
                if len(article.find('h3', first=True).links) != 0:
                    _article["link"] = article.find('h3', first=True).links.pop()

            if article.find('h3', first=True):
                _article["headline"] = article.find('h3', first=True).text

            if article.find('p', first=True):
                _article["text"] = article.find('p', first=True).text

            if _article["headline"] != "":
                result["articles"].append(_article)

    
    return result
