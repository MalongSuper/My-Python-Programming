# This program plays the Guessing Number Game (or Higher, Lower Game)
import random
import time
print("Game: Guessing Number")
print("+ In this game, you simply guess the number until you get the correct one")
print("+ The computer will only respond Correct, Lower or Higher")
print("+ Note that you have limited tries:")
print("\t* Easy: The number is from 1 to 100. You have 10 tries")
print("\t* Medium: The number is from 1 to 1000. You have 20 tries")
print("\t* Hard: The number is from 1 to 2000. You have 30 tries")
print("+ If you use all of them, you will lose!!")
time.sleep(5)  # Stop for 5 seconds
game_over = False
number, guess, attempt = 0, 0, 0  # Initialize number, guess, attempt
level = str(input("Select difficulty (E: Easy; M: Medium; H: Hard): "))
while level not in ["E", "M", "H"]:
    print("Invalid Input")
    level = str(input("Select difficulty (E: Easy; M: Medium; H: Hard): "))
# Get the user difficulty choice
if level == "E":  # Easy: Range within 1 to 100
    print("Easy Mode. You have 10 tries")
    attempt = 10  # Number of tries the user has
    number = random.randint(1, 100)
elif level == "M":  # Easy: Range within 1 to 100
    print("Medium Mode. You have 20 tries")
    attempt = 20  # Number of tries the user has
    number = random.randint(1, 1000)
else:
    # Hard: Range within 1 to 100
    print("Hard Mode. You have 30 tries")
    attempt = 30  # Number of tries the user has
    number = random.randint(1, 2000)
# User input
guess = int(input("Guess a number: "))
# If the user guesses the number right at first try
if guess == number:
    print(f"Correct. It is {number}")
    print("Genius!! You got the number")
else:
    attempt = attempt - 1  # Since this is the first guess, the attempt goes down to 9
    while not game_over:
        if attempt == 0:  # Out of tries
            print("Out of attempts. You lose!!")
            game_over = True  # The loop exits
        else:
            if guess > number:  # if the guessing number > the target number
                print("Lower")
                print("Attempts left:", attempt)  # Update attempt
                guess = int(input("Guess a number: "))
                attempt -= 1  # Deduce the number of attempts
            elif guess < number:  # if the guessing number < the target number
                print("Higher")
                print("Attempts left:", attempt)
                guess = int(input("Guess a number: "))
                attempt -= 1  # Deduce the number of attempts
            else:
                # if the guessing number = the target number
                print(f"Correct. It is {number}")
                print("Congratulations!! You got the number")
                game_over = True  # The loop exits
