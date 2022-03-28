import os
import csv

import importlib
import json

def get_sources():
    sources = []
    with open("../newsprioritiestoday-data/sources.csv", "r") as file:
        reader = csv.reader(file, delimiter=",")
        header = next(reader)

        for row in reader:
            entry = {}
            for index, item in enumerate(header):
                entry[item] = row[index]
            sources.append(entry)
    
    return sources

sources = get_sources()
for source in sources:
    processor = importlib.import_module("processors." + source["directory"])

    source_directory = "../newsprioritiestoday-data/raw/" + source["directory"]
    target_directory = "../newsprioritiestoday-data/processed/" + source["directory"]

    if not os.path.exists(source_directory):
        continue

    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    for entry in os.scandir(source_directory):

        if(os.path.exists(target_directory + "/" + entry.name  + ".json")):
            continue

        print("Processing: " + entry.name)
        with open(entry.path, "r") as file:
            content = file.read()
            result = processor.process(content, source)
            
            if len(result["articles"]) == 0:
                continue

            with open(target_directory + "/" + entry.name + ".json", "w") as target:
                target.write(json.dumps(result, indent=2, default=str))