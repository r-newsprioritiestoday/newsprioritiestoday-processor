import os

from lib import tagesschau
from lib import drdk

# TODO: make this dynamic so contributor don't have to touch this file anymore.

results = []
results.append(tagesschau.scrape())
results.append(drdk.scrape())

print(results)
