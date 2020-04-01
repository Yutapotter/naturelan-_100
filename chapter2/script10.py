def count(url):
    with open(url,"r") as f:
        result=[]
        
        for i in f:
            result.append(i)
    
    return len(result)




url="hightemp.txt"

print(count(url))


#別解

def count(url):
    count=0
    with open(url,"r") as f:
        for i in f:
            count +=1

    return count

url="hightemp.txt"

print(count(url))