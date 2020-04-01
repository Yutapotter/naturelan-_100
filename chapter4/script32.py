from script30 import *
sentences=neko_lines()
for word in sentences:
    
    if word['pos'] == '動詞':
       
        print(word["base"])