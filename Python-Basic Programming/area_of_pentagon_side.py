# This program computes the area of a pentagon
from math import tan, pi, radians
# Input the side of a pentagon
S = float(input("Enter the side: "))
if S < 0:
    print("Error: You cannot enter a negative number. "
          "Please proceed and try again")
else:
    # Computed using the given formula
    Area = (5 * (S ** 2)) / (4 * tan(pi / 5))
    # Display the result
    print("The area of the pentagon is", Area)
