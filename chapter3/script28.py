import json
import gzip
import re

def remove_markup(str):
    str = re.sub(r"'{2,5}", r"", str)
    str = re.sub(r"\[{2}([^|\]]+?\|)*(.+?)\]{2}", r"\2", str)
    str = re.sub(r"\{{2}.+?\|.+?\|(.+?)\}{2}", r"\1 ", str)
    str = re.sub(r"<.*?>", r"", str)
    str = re.sub(r"\[.*?\]", r"", str)
    return str

from script20 import extract_from_json
lines=extract_from_json("イギリス").split("\n")
temp_dict={}
for line in lines:
    target=re.search("^(.*?)\s=\s(.*)",line)
    if target:
        
        temp_dict[target.group(1)]=remove_markup(target.group(2))

print(temp_dict)







