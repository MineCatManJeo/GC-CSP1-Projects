# Gabriel Crozier, What is my grade?

def append(classes,grades):
    classTemp = []
    classTemp.append(input('What is your class?: '))
    classTemp.append(float(input('What is your grade percent in that class?: ')))
    print(classTemp)
    if classTemp[-1] < 60:
        print('You FAILED ):<')
    elif classTemp[-1] >= 60 and classTemp[-1] < 90:
        print('You have low grades... Are you even trying here!!! ):<')
    else:
        print('Showoff ):<')
    for grade in grades:
        if classTemp[-1] >= grade[1] and classTemp[-1] <= grade[2]:
            classTemp.append(grade[0])
            break
    classes.append(classTemp)
grades = [['A',93,100],['A-',90,92],['B+',87,89],['B',83,86],['B-',80,82],['C+',77,79],['C',73,76],['C-',70,72],['D+',67,69],['D',63,66],['D-',60,62],['F',0,59]]

numClasses = int(input('How many classes do you have?: ')) # Hi
classes = []

for i in range(numClasses):
     append(classes,grades)
for class1 in classes:
    print(f'Your grade percent in {class1[0]} is {class1[1]}, so you have a {class1[2]}!')