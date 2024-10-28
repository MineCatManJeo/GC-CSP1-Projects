# Gabriel Crozier, List of classes 

classes = []
numClass = int(input('How many classes do you have?: '))
for i in range(numClass):
    classes.append(input(f'What is your class?: '))
classes[-1] = 'and ' + classes[-1]
print(f'Your classes are {", ".join(classes)}!')