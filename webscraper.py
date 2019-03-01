from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://www.tagesschau.de/')

top10 = r.html.find('#content > div > div:nth-child(4) > div > div > div > div > div > div.teaser')

print(len(top10))


# data structure
'''
scraper_result = {
    "datetime": "",
    "country": "",
    "source": "",
    articles: [ # should be max 10 articles
        {
            "link": ""
            "headline": "",
            "infotext": "" # optional
        }
    ]
}

'''