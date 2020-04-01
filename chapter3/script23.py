import json
import gzip
import re

from script20 import extract_from_json
lines=extract_from_json("イギリス").split("\n")

for line in lines:
    search_line=re.search("^(=+)(.*?)(=+)$",line)
    if search_line:
        print(search_line.group(2),(len(search_line.group(1))-1))