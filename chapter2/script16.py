import math
def file_nsplit(url,n):
    with open(url) as f:
        lines=f.readlines()
    

    count=len(lines)
    unit=math.ceil(count/n)#１行あたりの行数
    
    for i,offset in enumerate(range(0,count,unit),1):
       with open("chile_{:02d}.txt".format(i),"w") as out_file:
           for line in lines[offset:offset+unit]:
               out_file.write(line)
    



n=int(input("数字を入力してください"))
url="hightemp.txt"
file_nsplit(url,n)