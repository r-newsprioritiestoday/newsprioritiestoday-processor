from requests_html import HTMLSession
from datetime import datetime

session = HTMLSession()
r = session.get('https://www.dr.dk/nyheder')


def scrape():

    result = {
        "datetime": str(datetime.now()),
        "country": "Denmark",
        "source": "https://www.dr.dk/nyheder",
        "articles": []
    }

    # all links and articles are defined by teaser classes
    inland = r.html.find('body > div.site-wrapper > div > div:nth-child(6) > div:nth-child(1) > div', first=True)
    abroad = r.html.find('body > div.site-wrapper > div > div:nth-child(6) > div:nth-child(2) > div', first=True)
    
    inland_articles = inland.find('li.item')
    abroad_articles = abroad.find('li.item')

    for article in inland_articles:
        _article = {
            "link": "",
            "headline": "",
            "text": "", # optional
            "category": "Inland"
        }

        if len(list(article.links)) != 0:   
            _article["link"] = list(article.links)[0]
            _article["headline"] = article.text
            
            if _article["headline"] != "":
                result["articles"].append(_article)
    
    for article in abroad_articles:
        _article = {
            "link": "",
            "headline": "",
            "text": "", # optional
            "category": "Abroad"
        }
        
        if len(list(article.links)) != 0:   
            _article["link"] = list(article.links)[0]
            _article["headline"] = article.text
            
            if _article["headline"] != "":
                result["articles"].append(_article)
    
    return result
