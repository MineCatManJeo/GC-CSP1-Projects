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
import random # Allows for use of random functions

difficulty = abs(int(input('How difficult would you like your guessing game to be (You will guess betweeen 1 and your number of choosing): '))) # Lets the user choose their own difficulty level (Improved, More clear)
randNum = random.randint(1,difficulty) # Generates a random number between 1 and the number of choise

def guessFunc(): # Guess function
    guess = int(input(f'Guess a number between 1 and {difficulty}: ')) # lets user guess number
    return guess # returns the guess as a value

while True: # Repeats forever
    guess = guessFunc() # sets guess
    if guess > randNum: # if guess is greater than random number
        print('Try a lower number!\n') # Tells user to try a lower number
    elif guess < randNum: # if guess is less than random number
        print('Try a higher number!\n') # Tells user to try a higher number
    else: # If guess is not greater than or less than the answer
        print('You did it!') # print you did it ans stop the infinite loop
        break

# Friend Comments:
"""
Does the program run?
Did you do something that made the program stop working, if so then what?
Were you able to use the program without any help from the programmer (Meaning nothing had to be explained to you)
If you needed further explanation on things, what explanations did you need? 
"""
# Mom:
"""
Yes. Yes. The question asked for which range of numbers I'd like to guess from, which made my think I needed to put in a range like 1-10 or something similar. I also pressed the run button instead of enter when I guessed a number later. No. I needed clarification on what the question was asking.
"""

# Dad
"""
Yes
No
Very little help required.
How to start the program and the num lock key was off.
"""

# Maintenence
# 1: I should make sure to make the questions more clear
# 2: I could make sure you can't input a number higher than 10,000
# 3: I could ask if the user would like to do it again
# 4: I could add a lose feature if you don't correctly guess in a required amount of attempts