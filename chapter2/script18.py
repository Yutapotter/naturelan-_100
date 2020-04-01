"""fname = 'hightemp.txt'
lines = open(fname).readlines()
lines.sort(key=lambda line: float(line.split('\t')[2]), )

for line in lines:
    print(line, end='')"""

url='hightemp.txt'
lines=open(url).readlines() #データファイルを１行ずつリスト化
lines.sort(key=lambda line:line.split("\t")[2],reverse=True)
for line in lines:
    print(line,end="")#末尾に改行コードがついているから


