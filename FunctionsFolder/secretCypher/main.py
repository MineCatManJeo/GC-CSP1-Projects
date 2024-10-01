#Gabriel Crozier, secret cypher
def cypher(text,num):
    sentence = ''
    for x in text:
        if ord(x) >= 65 and ord(x) <= 90:
            x = ord(x) + num + 1000
        elif ord(x) >= 97 and ord(x) <= 122:
            x = ord(x) + num + 2000
        else:
            x = ord(x)
        print(x)

        if x >= 1065 and x <= 1090 or x >= 2097 and x <= 2122:
            if not (x >= 1065 and x <= 1090 or x >= 2097 and x <= 2122):
                x -= int(26*(num/abs(num)))
        if x > 2000:
            sentence += chr(x-2000)
        elif x < 200:
            sentence += chr(x)
        else:
            sentence += chr(x-1000)
    return(sentence)
txt = input("Input sentence:\n")
print('\n'+cypher(txt,int(input("How many places would you like to shift your text?\n")))+'\n')