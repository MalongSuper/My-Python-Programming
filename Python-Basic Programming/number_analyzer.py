# This program will display an interger
# Input
x = int(input("Enter an interger :"))
# Display Positive or Negative number
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
elif x == 0:
    print("Equal")
# Display Even or Odd number
if (x % 2) == 0:
    print("Even")
else:
    print("Odd")