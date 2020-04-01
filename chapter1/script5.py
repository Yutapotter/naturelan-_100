def n_gram(sentence,n):
    result=[]

    for i in range(0,len(sentence)-n+1):
        result.append(sentence[i:i+n])
    


    
    
    
    return result




sentence="I am an NLPer"
word=sentence.split(" ")

print(n_gram(word,2))
print(n_gram(sentence,2))
