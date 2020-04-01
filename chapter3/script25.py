import json
import gzip
import re

from script20 import extract_from_json
lines=extract_from_json("イギリス").split("\n")

temp_dict = {}


for line in lines:
    temp_line = re.search("^(.*?)\s=\s(.*)", line)

    if temp_line:
        temp_dict[temp_line.group(1)] = temp_line.group(2)

print(temp_dict)