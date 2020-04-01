import gzip
import json

def extract_from_json(title):
    with open("jawiki-country.json","r",encoding="utf-8") as data_file:
        

        for line in data_file:
            
            data_json = json.loads(line)
            if data_json['title'] == title:
                return data_json['text']
            
                