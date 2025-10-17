# This program simulates Craps game
import random
import time


def two_dice():  # Define random dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    return total


def called_craps_naturals():  # The first dice
    total = two_dice()
    print("First Roll:", end=" ")
    time.sleep(3)
    print("You Rolled", total)
    craps_list = [2, 3, 12]
    natural_list = [7, 11]
    # If it is in the crap numbers, you lose
    if total in craps_list:
        print("Crap Number. You Lose")
        return True
    # If it is in the natural numbers, you win
    elif total in natural_list:
        print("Natural Number. You Win")
        return True
    else:
        return total  # If not, the point is established


def point_established(point):  # Define function for point established
    print("Winning Point is", point)
    while True:  # Use loop to continue dicing
        total = two_dice()
        print("You Rolled", total)
        if total == 7:  # If the dice is 7, you lose
            print("Seven Number. You Lose")
            return False
        elif total == point:  # If the dice is the same number, you win
            print("Same Number. You Win")
            return True
        time.sleep(3)  # Display the value timely


def main():  # Define main function
    print("Game: Craps")
    point = called_craps_naturals()
    if point is not True:
        point_established(point)


# Display the result
main()
