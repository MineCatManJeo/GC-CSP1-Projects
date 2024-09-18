# Gabriel Crozier, Average Grade Calculator

# Input the amount of grades you want to average, Also declares 2 lists
numClasses = int(input("How many classes would you like to use in your average grade?:\n"))
grades = []
averages = []

# This list gives the letter grades values.
letters = ["A+",100,"A",96,"A-",92,"B+",89,"B",86,"B-",82,"C+",79,"C",76,"C-",72,"D+",69,"D",66,"D-",62,"F",45]

averageGrade = 0

# Ensures you don't calculate 10000 grades.
if numClasses > 50:
    numClasses = 50
# This is where you type in your grades
for i in range(numClasses):
    grades.append(input("Input your letter grade:\n").upper())
    print("")
# This is what gets the average grades USING MATH
for grade in grades:
    if grade in letters:
        averageGrade += letters[letters.index(grade)+1]
averageGrade /= numClasses
# This adds all of the differences between your average grade and the grade for a letter and when it does that it then finds the minimum diference between each letter and your average grade.
# Finally it prints your average grade in a letter
# Quick note the grades aren't fully acurate because you don't input a number you input a grade the grades could differ a lot.
for i in range(0,len(letters),2):
    averages.append(round(abs(letters[i+1]-averageGrade),2))
print('Your average letter grade is a: ' + letters[averages.index(min(averages))*2] + "!")