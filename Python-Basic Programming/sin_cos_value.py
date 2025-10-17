# This program displays table of the Sin value and Cos value of Degrees
from math import sin, cos, radians
print("Table of the Sin value and Cos value of Degrees ")
print("{:<10}{:<10}{:<20}".format("Degree", "Sin", "Cos"))
for Degree in range(0, 361, 10):
    # Calculate the Sin
    # Convert to Degree using radians()
    Sin = sin(radians(Degree))
    # Calculate the Cos
    Cos = cos(radians(Degree))
    # Display the table
    # The numbers should be even space by using format()
    print("{:<10}{:<10}{:<20}".format(Degree, round(Sin, 4), round(Cos, 4)))
