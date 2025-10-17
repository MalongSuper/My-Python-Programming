# This program computes the area of the pentagon
from math import sin, sqrt, pi, radians
# Input the length from the center to a vertex
r = float(input("Enter the length from the center to a vertex: "))
if r < 0:
    print("Error: You cannot use a negative number. "
          "Please proceed and try again")
else:
    s = 2 * r * (sin(pi / 5))
    Area = (((3 * sqrt(3))/2) * (s ** 2))
    print("The area of the pentagon is", round(Area, 2))
