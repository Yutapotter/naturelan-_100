def output(url,n):
    with open(url) as f:
        i=0
        for line in f:
            if i>=n:
                break
            i+=1
            print(line.rstrip())




url="hightemp.txt"
output(url,5)

#解答
fname = 'hightemp.txt'
n = int(input('N--> '))

with open(fname) as data_file:
    for i, line in enumerate(data_file):
        if i >= n:
            break
        print(line.rstrip())