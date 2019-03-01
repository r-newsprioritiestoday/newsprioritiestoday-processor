from requests_html import HTMLSession
from datetime import datetime

session = HTMLSession()
r = session.get('https://www.washingtonpost.com/')


def scrape():

    result = {
        "datetime": str(datetime.now()),
        "country": "USA",
        "source": "https://www.washingtonpost.com/",
        "articles": []
    }

    # ENTER YOUR SCRAPE LOGIC HERE

    return result