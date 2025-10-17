# This program determines the color of a pocket in Roulette Wheel
# Input a pocket number
Pocket = int(input("Enter a pocket number :"))
# The pocket number should be between 0 and 36
if Pocket > 36 or Pocket < 0:
    print("Error: The pocket number cannot be outside the range of 0 through 36. "
          "Please proceed and try again")
else:
    # Number 0 is green
    if Pocket == 0:
        print("Green")
    # From 1 to 10, odd-numbered are red and even-numbered are black
    elif (1 <= Pocket <= 10) and (Pocket % 2) == 0:
        print("Black")
    elif (1 <= Pocket <= 10) and (Pocket % 2) != 0:
        print("Red")
    # From 11 to 18, odd-numbered are black and even-numbered are red
    elif (11 <= Pocket <= 18) and (Pocket % 2) == 0:
        print("Red")
    elif (11 <= Pocket <= 18) and (Pocket % 2) != 0:
        print("Black")
    # From 19 to 28, odd-numbered are red and even-numbered are black
    elif (19 <= Pocket <= 28) and (Pocket % 2) == 0:
        print("Black")
    elif (19 <= Pocket <= 28) and (Pocket % 2) != 0:
        print("Red")
    # From 29 to 36, odd-numbered are black and even-numbered are red
    elif (29 <= Pocket <= 36) and (Pocket % 2) == 0:
        print("Red")
    elif (29 <= Pocket <= 36) and (Pocket % 2) != 0:
        print("Black")





