def replace(url):
    with open(url) as f:
        
        for i in f:
            i.replace("\t"," ")
            print(i,end="")








url="hightemp.txt"
replace(url)