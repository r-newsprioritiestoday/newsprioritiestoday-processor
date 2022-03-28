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
    articles = html.find('div.teaser')
    
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
                
                _article["headline"], _article["text"] = article.text.split("\n", 1)


                if "inland" in _article["link"]:
                    _article["category"] = "Inland"

                if "ausland" in _article["link"]:
                    _article["category"] = "Abroad"

                if _article["headline"] != "":
                    result["articles"].append(_article)

    
    return result
