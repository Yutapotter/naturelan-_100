def output(n):
    with open("hightemp.txt") as f:
        out=[]
        for i in f:
            out.append(i.rstrip())

        reverse=out[-n:]
        for j in reverse:
            print(j)
        

output(3)


#解答

fname = 'hightemp.txt'
n = int(input('N--> '))

if n > 0:
    with open(fname) as data_file:
        lines = data_file.readlines()

    for line in lines[-n:]:
        print(line.rstrip())