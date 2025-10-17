# This program plays Math Quiz Game with three single-digit integer
import random
print("Math Quiz Game")
# Randomize three single-digit numbers
Number1 = random.randint(0, 9)
Number2 = random.randint(0, 9)
Number3 = random.randint(0, 9)
# Calculate their correct total
Total = Number1 + Number2 + Number3
# The program prompts the user to enter the answer
# The formula is random with the generated numbers
Answer = eval(input("What is " + str(Number1) +
                    " + " + str(Number2) +
                    " + " + str(Number3) + " ? "))
# Inform the user if the answer is right or wrong
if Answer == Total:
    print(Number1, "+", Number2, "+", Number3, "=", Answer, "is True")
else:
    print(Number1, "+", Number2, "+", Number3, "=", Answer, "is False")
