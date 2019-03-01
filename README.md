# newsprioritiestoday
Official news scraper bot for reddit.com/r/newsprioritiestoday



# data structure
```
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

```