from requests_html import HTMLSession
from datetime import datetime

session = HTMLSession()
r = session.get('https://www.aljazeera.net/')


def scrape():

    result = {
        "datetime": datetime.now(),
        "country": "Qatar",
        "code": "ar",
        "source": "https://www.aljazeera.net/",
        "articles": []
    }

    # on aljazeera we have a top story and many normal stories.
    # the main story has special css, so we create this result seperatly from the rest of the news cards
    main_story = r.html.find('.mainStory', first=True)
    _main_article = {
        "link": "",
        "headline": "",
        "text": "", # optional
        "category": ""
    }
    if len(list(main_story.links)) != 0:
        _main_article["link"] = list(main_story.absolute_links)[0]

        if main_story.find('.mainStory__title', first=True):
            _main_article["headline"] = main_story.find('.mainStory__title', first=True).text

        if main_story.find('.card__text', first=True):
            _main_article["text"] = main_story.find('.card__text', first=True).text

    result["articles"].append(_main_article)

    # now do the normal articles

    articles = r.html.find('div.card')

    for article in articles:
        _article = {
            "link": "",
            "headline": "",
            "text": "", # optional
            "category": ""
        }
        if len(list(article.links)) != 0:
            _article["link"] = list(article.absolute_links)[0]

            _article["headline"] = article.find('.card__title', first=True).text

            if article.find('.card__text', first=True):
                _article["text"] = article.find('.card__text', first=True).text
            
            if _article["headline"] != "":
                result["articles"].append(_article)

    
    return result
