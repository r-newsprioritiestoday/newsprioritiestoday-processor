from tinydb import TinyDB, Query

from lib import tagesschau
from lib import drdk
from lib import foxnews

# setup database
# path is relative to the execution path (not the path, this script is in)
db = TinyDB('data/db.json')

# TODO: make this dynamic so contributor don't have to touch this file anymore.

results = []
results.append(tagesschau.scrape())
results.append(drdk.scrape())
results.append(foxnews.scrape())

# add results to database
for result in results:
    db.insert(result)