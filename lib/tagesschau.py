from requests_html import HTMLSession
from datetime import datetime

session = HTMLSession()
r = session.get('https://www.tagesschau.de/')


def scrape():

    result = {
        "datetime": datetime.now(),
        "country": "Germany",
        "code": "de",
        "source": "https://www.tagesschau.de/",
        "articles": []
    }

    # all links and articles are defined by teaser classes
    articles = r.html.find('div.box > div.teaser')

    for article in articles:
        _article = {
            "link": "",
            "headline": "",
            "text": "", # optional
            "category": ""
        }
        if len(list(article.links)) != 0:
            if "multimedia" not in list(article.links)[0] and "100sekunden" not in list(article.links)[0]:
                _article["link"] = list(article.absolute_links)[0]
                if article.find('p.dachzeile', first=True):
                    _article["headline"] = article.find('p.dachzeile', first=True).text

                if article.find('p.teasertext', first=True):
                    _article["text"] = article.find('p.teasertext', first=True).text
                
                if "inland" in _article["link"]:
                    _article["category"] = "Inland"

                if "ausland" in _article["link"]:
                    _article["category"] = "Abroad"

                if _article["headline"] != "":
                    result["articles"].append(_article)

    
    return result
