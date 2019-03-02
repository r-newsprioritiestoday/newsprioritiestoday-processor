from requests_html import HTMLSession
from datetime import datetime

session = HTMLSession()
r = session.get('https://www.dr.dk/nyheder')


def scrape():

    result = {
        "datetime": datetime.now(),
        "country": "Denmark",
        "source": "https://www.dr.dk/nyheder",
        "articles": []
    }

    # all links and articles are defined by teaser classes
    # inland = r.html.find('body > div.site-wrapper > div > div:nth-child(6) > div:nth-child(1) > div', first=True)                    
    # abroad = r.html.find('body > div.site-wrapper > div > div:nth-child(6) > div:nth-child(2) > div', first=True)
    
    topstories = r.html.find('body > div.site-wrapper > div > div:nth-child(4) > div.col-lg-4.col-md-4.col-sm-4.col-xs-12', first=True)
    
    articles = topstories.find('.item')

    # inland_articles = inland.find('li.item')
    # abroad_articles = abroad.find('li.item')

    for article in articles:
        _article = {
            "link": "",
            "headline": "",
            "text": "", # optional
            "category": ""
        }

        if len(list(article.links)) != 0:   
            _article["link"] = list(article.links)[0]
            _article["headline"] = article.text

            if "indland" in _article["link"] or "regionale" in _article["link"]:
                _article["category"] = "Inland"

            if "udland" in _article["link"]:
                _article["category"] = "Abroad"
        
            if _article["headline"] != "":
                result["articles"].append(_article)
    
    return result