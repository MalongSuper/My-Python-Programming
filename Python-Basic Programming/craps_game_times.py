# This program simulates Craps game 10000 times
import random


def two_dice():  # Define random dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    return total


def called_craps_naturals():  # The first roll
    total = two_dice()
    print("First Roll:", end=" ")
    print("You Rolled", total)
    craps_list = [2, 3, 12]
    natural_list = [7, 11]
    # If it is in the crap numbers, you lose
    if total in craps_list:
        print("Crap Number. You Lose")
        return False, None  # Return two values
    # If it is in the natural numbers, you win
    elif total in natural_list:
        print("Natural Number. You Win")
        return True, None  # Return two values
    else:
        return None, total  # If not, the point is established


def point_established(point):  # If it is another value, continue dicing
    print("Winning Point is", point)
    while True:
        total = two_dice()
        print("You Rolled", total)
        if total == 7:  # If the dice is 7, you lose
            print("Seven Number. You Lose")
            return False
        elif total == point:  # If the dice is the same number, you win
            print("Same Number. You Win")
            return True


def main():  # Define main function
    count_win = 0
    for time in range(1, 10001):
        print("Game", time)
        win, point = called_craps_naturals()  # Use two variables
        if win is True:  # Count the natural number win (True value)
            count_win += 1
        elif point is not None:  # Use the None value
            if point_established(point) is True:  # Count all the win games
                count_win += 1
    print()
    print("Game: Craps (10000 times)")
    print("Winning Times:", count_win)


# Display the result
main()
