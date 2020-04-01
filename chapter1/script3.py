def pi(x):

    pi=[]
    
   
    z=x.split(" ")
    
    
    for word in z:
       
        pi.append(len(word)-word.count(",")-word.count("."))
    return pi






x="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

print(pi(x))