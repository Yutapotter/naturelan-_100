import json
import gzip
import re

from script20 import extract_from_json
lines=extract_from_json("イギリス").split("\n")
for line in lines:
    if "Category" in line:
        print(line)

