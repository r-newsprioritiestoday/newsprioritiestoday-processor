from requests_html import HTML
from datetime import datetime

def process(raw_html, source):

    html = HTML(html=raw_html)

    result = {
        "datetime": datetime.now(),
        "source": source,
        "articles": []
    }


    # get links and articles in main content
    articles = html.find('article')

    for article in articles:
        _article = {
            "link": "",
            "headline": "",
            "text": "", # optional
            "category": ""
        }
        if len(list(article.links)) != 0:
            _article["link"] = article.links.pop()
            if _article["link"].__contains__("video") or _article["link"].__contains__("show"):
                continue

            _article["headline"] = article.text

            if _article["headline"] != "":
                result["articles"].append(_article)

    return result
