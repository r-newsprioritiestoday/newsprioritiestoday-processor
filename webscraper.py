import os

from lib import tagesschau

# TODO: make this dynamic so contributor don't have to touch this file anymore.

results = []
results.append(tagesschau.scrape())


print(results)
