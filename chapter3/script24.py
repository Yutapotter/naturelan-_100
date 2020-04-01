import json
import gzip
import re

from script20 import extract_from_json
lines=extract_from_json("イギリス").split("\n")

for line in lines:
    target=re.search("(ファイル|File):(.*?)\|(.*?)",line)
    if target:
        print(target.group(2))
