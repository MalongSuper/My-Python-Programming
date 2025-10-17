# This program simulates Rock-Paper-Scissor Game
# The Game ends when either the user or the computer has won more than twice
import random
UserWin = 0
ComputerWin = 0
print("Rock-Paper-Scissor Game (Winner if won more than two times)")
while True:
    RPS = ('Scissor', 'Rock', 'Paper')
    # The computer randomly chooses a string among Rock-Paper-Scissor
    Random_RPS = random.choice(RPS)
    # The user input a number represents a string among Rock-Paper-Scissor
    User_RPS = int(input("Scissor(0), Rock(1), Paper(2): "))
    RPS_Number = {0: 'Scissor', 1: 'Rock', 2: 'Paper'}
    if User_RPS not in RPS_Number:
        print("You entered an invalid value. Not Count.")
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
            UserWin += 1
            if UserWin > 2:
                print("Game Over: The User Won")
                break
        # In RPS, Rock beats Scissor
        elif (Random_RPS == 'Scissor') and (RPS_Number.get(User_RPS) == 'Rock'):
            print("The computer is", Random_RPS, end=" . ")
            print("You are", RPS_Number.get(User_RPS), end=" . ")
            print("You Won.")
            UserWin += 1
            if UserWin > 2:
                print("Game Over: The User Won")
                break
        # In RPS, Scissor beats Paper
        elif (Random_RPS == 'Paper') and (RPS_Number.get(User_RPS) == 'Scissor'):
            print("The computer is", Random_RPS, end=" . ")
            print("You are", RPS_Number.get(User_RPS), end=" . ")
            print("You Won.")
            UserWin += 1
            if UserWin > 2:
                print("Game Over: The User Won")
                break
        else:
            # Display whether the computer wins
            print("The computer is", Random_RPS, end=" . ")
            print("You are", RPS_Number.get(User_RPS), end=" . ")
            print("You Lose.")
            ComputerWin += 1
            if ComputerWin > 2:
                print("Game Over: The Computer Won")
                break
