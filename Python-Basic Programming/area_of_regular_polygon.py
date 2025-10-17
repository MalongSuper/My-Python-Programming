# This program computes area of a regular polygon
from math import tan, pi, radians
# Input the number of sides and their length of a regular polygon
N = int(input("Enter the number of sides: "))
S = float(input("Enter the sides: "))
if (N < 0) or (S < 0):
    print("Error: You cannot enter a negative number. "
          "Please proceed and try again")
else:
    # Computes using the given formula
    Area = (N * (S ** 2)) / (4 * tan(pi / N))
    # Display the result
    print("The area of the polygon is", Area)
