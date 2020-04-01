def element_symbol(x):
    words=x.split(" ")
    result={}
    for num,word in enumerate(words,1):
        if num in (1,5,6,7,8,9,15,16,19):
            result[word[0:1]]=num
        else:
            result[word[0:2]]=num

    return result

x="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."


print(element_symbol(x))