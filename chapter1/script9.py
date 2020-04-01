import random

def Typoglycemia(sentence):
    result=[]
    for word in sentence.split(" "):
        if len(word)>4:
            chr_list=list(word[1:-1])
            random.shuffle(chr_list)
            result.append(word[0]+"".join(chr_list)+word[-1])



        else:
            result.append(word)
    return result

sentence=input("文字列を入力してくだいーーー")

print(Typoglycemia(sentence))