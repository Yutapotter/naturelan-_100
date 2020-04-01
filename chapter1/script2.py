def cross_str(x,y):
    
    answer=""
    for (i,j) in zip(x,y):
        answer += i+j

    return answer


x="パトカー"
y="タクシー"

print(cross_str(x,y))