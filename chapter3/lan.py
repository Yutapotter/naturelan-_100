import gzip
import json
fname = 'jawiki-country.json.gz'
with gzip.open(fname,"rt") as data_file:
    for data in data_file:
        json_data=json.loads(data)
        if json_data["title"]=="イギリス":
            print(json_data["text"])