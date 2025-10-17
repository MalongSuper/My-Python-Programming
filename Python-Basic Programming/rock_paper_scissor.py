# This program simulates rock-paper-scissor game
import random
RPS = ('Scissor', 'Rock', 'Paper')
# The computer randomly chooses a string among Rock-Paper-Scissor
Random_RPS = random.choice(RPS)
# The user input a number represents a string among Rock-Paper-Scissor
print("Rock-Paper-Scissor Game")
User_RPS = int(input("Scissor(0), Rock(1), Paper(2): "))
RPS_Number = {0: 'Scissor', 1: 'Rock', 2: 'Paper'}
if User_RPS not in RPS_Number:
    print("You entered an invalid value. You Lose.")
else:
    # If both the user and the computer prompt the same, displays a draw
    if Random_RPS == RPS_Number.get(User_RPS):
        print("The computer is", Random_RPS, end=" . ")
        print("You are", RPS_Number.get(User_RPS), "too", end=" . ")
        print("It is a Draw.")
    # Display whether the user wins
    # In RPS, Paper beats Rock
    elif (Random_RPS == 'Rock') and (RPS_Number.get(User_RPS) == 'Paper'):
        print("The computer is", Random_RPS, end=" . ")
        print("You are", RPS_Number.get(User_RPS), end=" . ")
        print("You Won.")
    # In RPS, Rock beats Scissor
    elif (Random_RPS == 'Scissor') and (RPS_Number.get(User_RPS) == 'Rock'):
        print("The computer is", Random_RPS, end=" . ")
        print("You are", RPS_Number.get(User_RPS), end=" . ")
        print("You Won.")
    # In RPS, Scissor beats Paper
    elif (Random_RPS == 'Paper') and (RPS_Number.get(User_RPS) == 'Scissor'):
        print("The computer is", Random_RPS, end=" . ")
        print("You are", RPS_Number.get(User_RPS), end=" . ")
        print("You Won.")
    else:
        # Display whether the computer wins
        print("The computer is", Random_RPS, end=" . ")
        print("You are", RPS_Number.get(User_RPS), end=" . ")
        print("You Lose.")
