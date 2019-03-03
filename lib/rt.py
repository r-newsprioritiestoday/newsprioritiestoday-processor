from requests_html import HTMLSession
from datetime import datetime

session = HTMLSession()
r = session.get('https://russian.rt.com/')


def scrape():

    result = {
        "datetime": datetime.now(),
        "country": "Russia",
        "code": "ru",
        "source": "https://russian.rt.com/",
        "articles": []
    }

    # rt is tricky, as they have a live news feed in the middle of their headlines. This must be ignored, otherwise we get alot of random crap as main header
    # that's why we first get the main promo box and all articles in it. 
    # Then we get all later articles by looking to the rows class.
    
    main_promo_box = r.html.find('div.rows__column_main_promobox', first=True)
    articles = main_promo_box.find('li.listing__column')
        
    articles.extend(r.html.find('.rows__column_three-three-three-one'))

    for article in articles:

        _article = {
            "link": "",
            "headline": "",
            "text": "",
            "category": ""
        }

        if len(list(article.links)) != 0:

            # ignore links to video only articles
            if "inotv" not in list(article.links)[0]:
                _article["link"] = list(article.absolute_links)[0]

                _article["headline"] = article.find('.card__heading', first=True).text

                if article.find('.card__summary', first=True):
                    _article["text"] = article.find('.card__summary', first=True).text
                
                if _article["headline"] != "":
                    result["articles"].append(_article)
    
    
    return result
