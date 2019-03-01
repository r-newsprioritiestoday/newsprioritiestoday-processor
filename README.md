# /r/newsprioritiestoday
Official news scraper bot for [reddit.com/r/newsprioritiestoday](reddit.com/r/newsprioritiestoday)

## How does it work?

The goal is to post the main headlines from all over the world in a concentrated matter over on [reddit.com/r/newsprioritiestoday](reddit.com/r/newsprioritiestoday).

To achieve this, two scripts are running indepently from eachother.
- ```webscraper.py``` is scraping the big news sites for their headlines and converts the info into easier to handle structure
- ```redditbot.py``` is using the data to post a news summary once a day on the subreddit.

## Contributions

Contributions are very welcome. Feel free to submit a pull request for a newssource of your choice. The more news sites the better.

### How to add a news source

1. Add a new source under the ```lib``` directory. Name the file something appropriate for the news source, e.g. it's name.
2. Use the following template in the file. I use the [requests-html](https://github.com/kennethreitz/requests-html) library to parse the news sites. Feel free to use your own favourite lib.
```
from requests_html import HTMLSession
from datetime import datetime

session = HTMLSession()
r = session.get('https://www.mynewssite.com/')


def scrape():

    result = {
        "datetime": str(datetime.now()),
        "country": "COUNTRY OF NEWSSITE",
        "source": "https://www.mynewssite.com/",
        "articles": []
    }

    // ENTER YOUR SCRAPE LOGIC HERE

    return result
```
Your scrape function must return the result object. The articles array should contain objects with the following structure:
```
{
    "link":     ""
    "headline": "",
    "infotext": "" # optional
    "category": "" # optional
}
```
3. Create your pull request. I will check out your code and add your scrape function to the main loop.

Thank you very much. :)

## Licence

The MIT License (MIT)

Copyright (c) 2019 G710

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
