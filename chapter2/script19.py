"""import collections
def count_sort(url):
    with open(url) as data_file:
        lines=data_file.readlines()
        ken=[]
        for line in lines:
            num=(line.split("\t")[0])
            ken.append(num)
        l=collections.Counter(ken)
        dic=sorted(l.items(),key=lambda x:x[1],reverse=True )
        for line in dic:
            print(line)
url="hightemp.txt"
count_sort(url)"""


#解答


from itertools import groupby
fname="hightemp.txt"

lines=open(fname).readlines()
kens=[line.split("\t")[0] for line in lines]

kens.sort()
result=[(ken,(len(list(group)))) for ken,group in groupby(kens)]


result.sort(key=lambda ken: ken[1],reverse=True)
for ken in result:
    print("{ken}({count})".format(ken=ken[0],count=ken[1]))