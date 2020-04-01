from script30 import *

lines=neko_lines()

for i in range(0,len(lines)-1):
    if lines[i]["pos"]=="名詞"and\
        lines[i+1]["pos"]=="名詞":
        print("{}{}".format(lines[i]["surface"],lines[i+1]["surface"]),end=" ")

#別解
nouns=[]
list_series_noun=[]
for line in lines:
    if line["pos"]=="名詞":
        nouns.append(line["surface"])
    else:
        if len(nouns)>1:
            list_series_noun.append("".join(nouns))
        nouns=[]
if len(nouns)>1:
    list_series_noun.append("".join(nouns))

series_noun=set(list_series_noun)
print(series_noun)


    