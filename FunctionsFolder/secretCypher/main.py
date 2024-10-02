#Gabriel Crozier, secret cypher
def cypher(text,shift):
    sentence = '' # innitializes sentence
    if shift < 0: # if the num to shift by < 0 make it a positive number
        shift = 26 + (shift%26)
    for x in text: # once for EVERY letter in the string
        if x.isalpha(): # checks if it is in the alphabet
            if x.islower(): # checks for lovercase
                ch = ord(x) + (shift%26) # if it is, shift it
                if ch > ord('z') and not ch < ord('a'):
                    ch -= 26 # makes sure if you make a num go above the 'z' value it wraps around
            elif x.isupper(): # same but for uppercase
                ch = ord(x) + (shift%26)
                if ch > ord('Z') and not ch < ord('A'):
                    ch -= 26
        else: ch = ord(x) # checks if it isn't a letter
        sentence += chr(ch)
    return(sentence) # returns combined string

listOfCommon = ['the ','and ','for ','how ','is '] # common words

yn = bool(int(input('Would you like to decode or encode?\nDecode: 1\nEncode: 0\n'))) # asks if you want to encode / decode
if yn == False: # encode
    txt = input("Input sentence:\n")
    num = int(input("What is your shift value:\n"))
    print('\n'+cypher(txt,num)+'\n')
if yn == True: # decode
    txt = input("Input sentence:\n")
    listOfCommon.append(input('Input a word you think is in the cypher:\n'))
    for i in range(25): # 25 for the num of letter in alphabet - 1
        tf = False # resets value
        for li in listOfCommon: # once for each value in common words
            if li in cypher(txt,i+1).lower(): # if its in the cipher
                tf = True # make this true
        if tf: # if its true
            print('\n'+cypher(txt,i+1)[0:50], str(i+1) + '\n') # print a small part of the cipher
    num2 = int(input("\nWhich section seemed the most correct:\n")) # asks you which part looks right
    print('\n'+cypher(txt,num2) + '\n') # prints full version of the part you though looked right

    