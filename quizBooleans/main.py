# Gabriel Crozier, Booleans Testing with a Quiz!

# Every question is in this variable! It splits each string by the DDD and then will split it again at the | allowing for the answerSS to be inside of the string as well!
quizQuestions = ["How many diamonds do you need to craft a diamond pickaxe?\nDDD3|three","You can craft golden apples and golden carrots but can you craft golden potatoes?\nDDDno|n","What large structure spawns down \
in the deep dark?\nDDDancient city|the ancient city","Can rain fall in the desert?\nDDDno|n","What do you get when you kill a blaze?\nDDDblaze rod|blaze rods|a blaze rod","What's the final boss in Minecraft?\nDDDender dragon|the ender dragon"]

# initializes score
score = 0

# Welcomes you to the quiz
print("Welcome to my MINECRAFT quiz of GREATNESS!\n")

# Asks you the questions
for i in range(len(quizQuestions)):
    questions = quizQuestions[i].split('DDD')
    if input(questions[0]).lower().strip() in questions[1].split('|'): # this is just asking you the question from the list and then checkig to see if your answer was in the answer key
        score += 1
        print('Correct!\n')
    else:
        print('Sorry, but that was wrong ):\n')
# prints your score
print('You got ' + str(score) + ' out of ' + str(len(quizQuestions)) + '!')