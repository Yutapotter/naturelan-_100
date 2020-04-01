import json
import gzip
import re

from script20 import extract_from_json
lines=extract_from_json("イギリス").split("\n")
temp_dict={}
for line in lines:
    target=re.search("^(.*?)\s=\s(.*)",line)
    if target:
        a=re.sub("\'{2,5}","",target.group(2))
        b=re.sub("\[{2}([^|\]]+?\|)*(.+?)\]{2}", "\2",a)#ここわからない
        temp_dict[target.group(1)]=b

print(temp_dict)
