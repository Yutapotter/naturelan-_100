def chiper(sentence):
    result=""
    for word in sentence:

        if word.islower():
            result+=chr(219-ord(word))
        else:
            result+=word
    return result


sentence=input("文字列を入力してくださいーーー")

result=chiper(sentence)
print("暗号化"+result)

print("復号化"+chiper(result))
