from requests_html import HTML
from datetime import datetime

def process(raw_html, source):

    html = HTML(html=raw_html)

    result = {
        "datetime": datetime.now(),
        "source": source,
        "articles": []
    }


    # all links and articles are defined by teaser classes
    # inland = r.html.find('body > div.site-wrapper > div > div:nth-child(6) > div:nth-child(1) > div', first=True)                    
    # abroad = r.html.find('body > div.site-wrapper > div > div:nth-child(6) > div:nth-child(2) > div', first=True)
    
    # topstories = html.find('body > div.site-wrapper > div > div:nth-child(4) > div.col-lg-4.col-md-4.col-sm-4.col-xs-12', first=True)
    
    articles = html.find('.dre-teaser')

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
            _article["link"] = article.links.pop()
            _article["headline"] = article.text

            if "indland" in _article["link"] or "regionale" in _article["link"]:
                _article["category"] = "Inland"

            if "udland" in _article["link"]:
                _article["category"] = "Abroad"
        
            if _article["headline"] != "":
                result["articles"].append(_article)
    
    return result
