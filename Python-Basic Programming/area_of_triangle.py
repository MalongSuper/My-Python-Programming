# This program computes the area of a triangle
# Input the three points of a triangle
from math import sqrt
x1, y1, x2, y2, x3, y3 = [float(XY123) for XY123 in (input("Enter three points for a triangle : ")).split(",")]
# Assume a triangle ABC has vector AB, vector BC and vecto CA
# These are the side of the triangle
# Apply the vector method to solve this problem
Side1 = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
Side2 = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
Side3 = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
# Calculate using the given formula
S = (Side1 + Side2 + Side3) / 2
Area = sqrt(S * (S - Side1) * (S - Side2) * (S - Side3))
print("The area of the triangle is", round(Area, 3))
