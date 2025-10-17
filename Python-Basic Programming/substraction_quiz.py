# This program plays subtraction quiz by randomly generating a subtraction question
# The two integers are less than 100
import random
print("Subtraction Quiz Game")
# Generate two random two-digits integers
Number1 = random.randint(0, 99)
Number2 = random.randint(0, 99)
# Input the answer for the random generated subtracted question
if Number1 > Number2:
    Answer = eval(input("What is " + str(Number1) + " - " + str(Number2) + " ? "))
    if Answer == (Number1 - Number2):
        print("Your answer is Correct")
    else:
        # Display whether the answer is right or wrong
        print("Your answer is Wrong")
        print("Correct Answer:\t" + str(Number1) + " - " + str(Number2) + "", "=", Number1 - Number2)
# The subtraction only relevant when the higher number is the first
# When Number 2 is better than Number 1
if Number1 < Number2:
    Answer = eval(input("What is " + str(Number2) + " - " + str(Number1) + " ? "))
    if Answer == (Number2 - Number1):
        print("Your answer is Correct")
    else:
        # Display whether the answer is right or wrong
        print("Your answer is Wrong")
        print("Correct Answer:\t" + str(Number2) + " - " + str(Number1) + "", "=", Number2 - Number1)
