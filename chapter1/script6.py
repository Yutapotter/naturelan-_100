def n_gram(sentence,n):
    answer=[]
    for i in range(0,len(sentence)-n+1):
        answer.append(sentence[i:i+n])

    return answer

sentence="paraparaparadise"
X=n_gram(sentence,2)

sentence="paragraph"
Y=n_gram(sentence,2)

#XとYの和集合

print(set(X)|set(Y))

#XとYの積集合
print(set(X)&set(Y))

#XとYの差集合
print(set(X)-set(Y))

print("se" in set(X))
print("se" in set(Y))
