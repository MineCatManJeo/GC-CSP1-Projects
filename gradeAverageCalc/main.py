# Gabriel Crozier, Average Grade Calculator

numClasses = int(input("How many classes would you like to use in your average grade?:\n"))
grades = []

letters = ["A+",100,"A",96,"A-",92,"B+",89,"B",86,"B-",82,"C+",79,"C",76,"C-",72,"D+",69,"D",66,"D-",61,"F",60]

averageGrade = 0

if numClasses > 50:
    numClasses = 50
for i in range(numClasses):
    grades.append(input("Input your letter grade:\n").upper())
    print("")
for grade in grades:
    if grade in letters:
        averageGrade += letters[letters.index(grade)+1]
averageGrade /= numClasses
print(averageGrade)
for i in range(0,len(letters),2):
    print(letters[i+1]-averageGrade)