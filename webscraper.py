import os

results = []

# walk all files in subdirectory and run the scrape functions
countries = os.listdir("sources")

for country in countries:
    sources = os.listdir("sources/" + country)
    
    for f in sources:
        scrape = getattr(__import__("sources/" + country + "/" + f), "scrape")
        result = scrape()
        results.append(result)


print(results)



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
            "category": ""
        }
    ]
}

'''