def div(url):
    with open(url) as f,\
        open("col1.txt","w") as col1_file,\
        open("col2.txt","w") as col2_file:
        for i in f:
            col=i.split("\t")
            col1=col[0]
            col2=col[1]
            col1_file.write(col1+"\n")
            col2_file.write(col2+"\n")










url="hightemp.txt"
print(div(url))