# Gabriel Crozier, Number Guessing Game / SDLC Documentation

#----------------------------------------------------------------------------------------------------
#
# Goals: The file needs to makes the user guess a random number between 1 - 10 and tell them if they are correct
# Features: A random number generator between 1 - 10, user input allowing the user to guess random number, print statements telling them if they got the number correct 
# Optional Features: Tells user if their number was above or below the generated number, lets them try again to get the correct number
# Required Resources: An ide to run the program, a computer, power, code. a person to use the progam
#
#----------------------------------------------------------------------------------------------------

# Psuedocode

# Asks user for difficulty range (number)
"""
SET difficulty to GET difficulty number (1 through difficulty number)
"""
# Generate number
"""
USE random
SET randomNum to a random number 1-10
"""
# Let user guess number
"""
SET num to GET number from user
"""
# Check if user was correct
"""
CHECK IF user number = random number
    DISPLAY "Success"
ELSE
    DISPLAY "FAIL"
"""
# Optional: Checks if users number was higher or lower than the real number also lets user try again
"""
FOREVER LOOP
    USER GUESS FUNCTION
    CHECK IF user number GREATER than random number
        DISPLAY 'lower'
    ELSE IF user number LESS than random number
        DISPLAY 'higher'
    ELSE
        DISPLAY 'YOU DID IT'
        BREAK OUT OF LOOP
"""

# Implementation
import random

difficulty = abs(int(input('What range of numbers would you like to guess from?: ')))
randNum = random.randint(1,difficulty)

def guessFunc():
    guess = int(input(f'Guess a number between 1 and {difficulty}: '))
    return guess

while True:
    guess = guessFunc()
    if guess > randNum:
        print('Try a lower number!\n')
    elif guess < randNum:
        print('Try a higher number!\n')
    else:
        print('You did it!')
        break

# Friend Comments:
#
#
#
#


# Maintenence