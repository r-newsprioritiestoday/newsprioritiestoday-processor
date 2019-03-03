from tinydb import TinyDB, Query
from tinydb_serialization import Serializer, SerializationMiddleware
from datetime import datetime

from lib import tagesschau
from lib import drdk
from lib import foxnews
from lib import rt
from lib import aljazeera

class DateTimeSerializer(Serializer):
    OBJ_CLASS = datetime

    def encode(self, obj):
        return obj.strftime('%Y-%m-%dT%H:%M:%S')

    def decode(self, s):
        return datetime.strptime(s, '%Y-%m-%dT%H:%M:%S')



# setup database
# path is relative to the execution path (not the path, this script is in)
serialization = SerializationMiddleware()
serialization.register_serializer(DateTimeSerializer(), 'TinyDate')

db = TinyDB('../newsprioritytoday-data/db.json', storage=serialization)

# TODO: make this dynamic so contributor don't have to touch this file anymore.

results = []
results.append(tagesschau.scrape())
results.append(drdk.scrape())
results.append(foxnews.scrape())
results.append(rt.scrape())
results.append(aljazeera.scrape())

# add results to database
for result in results:
    db.insert(result)
