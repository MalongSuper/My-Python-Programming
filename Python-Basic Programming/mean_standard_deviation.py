# This program computes mean and standard deviation
from math import sqrt
# Assume the value
TotalValue = 0
NumberMean = 0
Mean = 0
Deviation = 0
Total = 0
# Assume the list
NumberList = []
print("Mean and Standard Deviation")
print("Enter ten numbers: ", end="")
# The input repeats ten times
for Number in range(1, 11):
    NumberValue = float(input(""))
    # Make a list contain these numbers
    NumberList.append(NumberValue)
    TotalValue += NumberValue
# Compute the mean using given formula
Mean = TotalValue / 10
for Number in NumberList:
    Number = Number ** 2
    NumberMean += Number
# Compute the deviation using given formula
Deviation = (NumberMean - ((TotalValue ** 2) / 10)) / (10 - 1)
# Negative number cannot calculate square root
if Deviation < 0:
    print("Error: The Standard Deviation is unpredictable. Please re-enter the numbers")
else:
    Deviation = sqrt(Deviation)
    print("The Mean is", Mean)
    print("The Standard Deviation is", Deviation)
