# Gabriel Crozier, Pig Latin Converter

def pigLatinConv(words):
    # Storage Info {What are the vowels? What is the puncuation?}
    vowels = ['a','e','i','o','u']
    syntax = [',','.','!','?']
    sentence = [] # List for combining your sentence together in the end!
    words = words.split() # Splits your sentence in a bunch of words
    start = "NaN"

    # Goes through each word in your sentence
    for x in words:
        x = x.lower()
        # Repeats for the length of the individual word
        for i in range(len(x)):
            if x[i] in vowels: # checks if the letter is in the vowels list
                start = i # If it is save the position of the letter
                break # Stop checking if there was a vowel (Allows for multiple vowels in a word)
        if start == "NaN": # If there was no vowels
            for i in range(1,len(x),1): # start from the second letter
                if x[i] in 'y': # if the letter is y
                    start = i # make the start value the position of that letter
                    break
        if start == "NaN": # if it's still Nan
            start = 0 # make it zero (This prevents breaking when you input a single letter "d")
        if x[0] in vowels: # if the first letter is a vowel
            ay = 'yay' # make the end just yay
        else:
            ay = 'ay' # if not make it ay
        x = x[start:] + x[:start] + ay # the word after the first vowel + the first letters + ay/yay
        for y in syntax:
            if y in x:
                x = x.replace(y,'') # Checks if there is punctuation in your word and puts it to the end
                x += y
        sentence.append(x) # adds the translated word to the list
    sentence1 = ' '.join(sentence).lower() # Combines the word to a sentence
    return(sentence1) # returns the translated sentence

while True:
    print('\n')
    print(pigLatinConv(input('Write a sentence!:\n'))) # the function
    try: 
        if int(input('Input 1 to continue converting!: ')) == 1:
            continue
        else:
            print('Input was not 1, Breaking now')
            break
    except: 
        print('Input was not 1, Breaking now')
        break