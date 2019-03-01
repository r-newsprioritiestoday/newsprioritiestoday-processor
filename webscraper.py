from tinydb import TinyDB, Query

from lib import tagesschau
from lib import drdk


# setup database
db = TinyDB('db.json')

# TODO: make this dynamic so contributor don't have to touch this file anymore.

results = []
results.append(tagesschau.scrape())
results.append(drdk.scrape())

# add results to database
for result in results:
    db.insert(result)