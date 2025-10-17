# This program calculates interest rate
# Given formula: interest = balance * (annual interest rate / 1200)
# Input
# e.g. interest rate 3 means 3%
print("Interest Rate")
balance, interest_rate = eval(input("Enter balance and interest rate: "))
# Calculate
interest = balance * (interest_rate / 1200)
print("The interest", round(interest, 4))
