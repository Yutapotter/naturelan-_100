import json
import gzip
import re

from script20 import extract_from_json
lines=extract_from_json("イギリス").split("\n")

for line in lines:
    category_line=re.search("^\[\[Category:(.*?)(|\|.*)\]\]$",line)
    if category_line:
        print(category_line.group(1))