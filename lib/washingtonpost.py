from requests_html import HTMLSession
from datetime import datetime

session = HTMLSession()
r = session.get('https://www.washingtonpost.com/')


def scrape():

    result = {
        "datetime": datetime.now(),
        "country": "USA",
        "code": "en",
        "source": "https://www.washingtonpost.com/",
        "articles": []
    }

    # ENTER YOUR SCRAPE LOGIC HERE

    return result
