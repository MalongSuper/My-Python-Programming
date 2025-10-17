# This program plays Addition Quiz by generating two integers under 100
import random
print("Math Quiz Game")
Number1 = random.randint(0, 99)
Number2 = random.randint(0, 99)
# Calculate the correct total
Total = Number1 + Number2
# The program prompts the user to enter the answer
# The formula is random with the generated numbers
Answer = eval(input("What is " + str(Number1) + " + " + str(Number2) + " ? "))
# Inform the user if the answer is right or wrong
if Answer == Total:
    print(Number1, "+", Number2, "=", Answer, "is True")
else:
    print(Number1, "+", Number2, "=", Answer, "is False")
