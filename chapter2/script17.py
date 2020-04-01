def todouhukenn(url):
    with open(url) as f:
        set_todouhuken=set()
        lines=f.readlines()
        for line in lines:
            col=line.split("\t")
            set_todouhuken.add(col[0])
        print(set_todouhuken)








url="hightemp.txt"
todouhukenn(url)