# Gabriel Crozier, Pig Latin Converter

def pigLatinConv(words):
    vowels = ['a','e','i','o','u']
    words = words.split()
    for x in words:
        for i in range(len(x)):
            if x[i].lower() in vowels:
                start = i
                break
        if x[0].lower() in vowels:
            ay = 'way'
        else:
            ay = 'ay'
        x = x[start:].capitalize() + '-' + x[:start].lower() + ay
        print(x)
    return(words)

print('')
print(pigLatinConv(input('Choose a word:\n')))