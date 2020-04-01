from script30_1 import *

sentences =read_mecab_file("neko.txt.mecab")
for sentence in sentences:
    for word in sentence:
    
        if word['pos'] == "名詞" and word["pos1"]=="サ変接続":
            print(word["base"])