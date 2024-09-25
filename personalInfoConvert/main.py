# Gabriel Crozier, Personal info converter

# Initializing variables
name = input('What is your name?\n')
age = input('How old are you?\n')
height = input('What is your height in meters?\n')
favNum = input('What is your favorite number?\n')

# printing them
print("Origional Values:\n")
print(name)
print(age)
print(height)
print(favNum)

# changing to correct data type
name = str(name)
age = int(age)
height = float(height)
favNum = int(favNum)

# printing new data
print("\n\nConverted Values:\n")
print(name)
print(age)
print(height)
print(favNum)