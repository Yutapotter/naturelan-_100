from script30 import *
import collections
 

lines=neko_lines()
count=[]
for line in lines:
    count.append(line["surface"])

c=collections.Counter(count).most_common()
print(c[:10])