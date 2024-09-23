# Gabriel Crozier, Palendrome Assignment

# input your word
word = input("This will check to see if you input a palendrome or not,\nInput a word:\n").lower().strip()


# Gets the first and second half of the word
word1 = word[0:int(len(word)/2)]
word2 = word[-int(len(word)/2):len(word)+1]

# Gets the middle letter if it has an odd amount
if len(word) % 2 != 0:
    word3 = word[int(len(word)/2)]
else:
    word3 = ''

# Checks if the reversed first half of the word is the same as the socond half or checks if the second word is the same as the third (this just makes a one letter word work)
if word1[::-1] == word2 or word2 == word3:
    print(word + " is a palendrome!")
else:
    print(word + " is not a palendrome!")