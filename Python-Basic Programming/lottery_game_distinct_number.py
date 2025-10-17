# This program simulates lottery game with two-digit number
# The two digits in the generated number should be distinct
import random
print("Lottery Game (Distinct Number)")
# Generate the Digit 1
Digit1 = random.randint(1, 9)
# Assume Digit 2
Digit2 = 0
# When use loop, the program will check to ensure the two digits are different
while Digit2 != Digit1:
    # Then the program should generate Digit 2
    Digit2 = random.randint(1, 9)
    # Input the number
    GuessNumber = int(input("What is your pick? "))
    if GuessNumber <= 0 or GuessNumber > 99:
        print("The number is invalid. Please enter again")
    else:
        # For distinct digits number, only "match one digit" is valid
        print("The lottery number is", str(Digit1) + str(Digit2))
        GuessDigit1 = GuessNumber // 10
        GuessDigit2 = GuessNumber % 10
        if GuessDigit1 == Digit1 or GuessDigit1 == Digit2 or GuessDigit2 == Digit1 or GuessDigit2 == Digit2:
            print("Match one digit")
            break
        else:
            print("No match found")
            break
