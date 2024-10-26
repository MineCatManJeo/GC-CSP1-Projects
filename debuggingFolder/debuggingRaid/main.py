import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        guess = input("Enter your guess: ") # Needs an int() thing to make it run, logic error, no matter what user types in it won't work because it needs to be a number
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        if guess == number_to_guess: # need to make this an elif to ensuer the user doesn't get one extra attempt, runtime error, if the user gets one more attempt it would be wrong
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
        elif guess < number_to_guess:
            print("Too low! Try again.")
        # attempts += 1 (you need to allow for attemps to go up), runtime error, the program would run indefinently for however long you fail
        continue # you dont need a continue at the end of the loop, logic error, thius line of code is completely redundent
    print("Game Over. Thanks for playing!")
start_game()