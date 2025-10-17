# This program determines whether two circles overlap or are inside each other
from math import sqrt
# Input the values
x1, y1, r1 = eval(input("Enter circle1's center x-, y-coordinates, and radius:\n"))
x2, y2, r2 = eval(input("Enter circle2's center x-, y-coordinates, and radius:\n"))
# Compute the distance between the two centers
Distance_TwoCenters = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
# Circle2 is inside Circle1 if the distance between the two centers <= |r1 - r2|
if Distance_TwoCenters <= abs(r1 - r2):
    print("circle2 is inside circle1")
# Circle2 overlaps Circle1 if the distance between the two centers <= r1 + r2
elif Distance_TwoCenters <= (r1 + r2):
    print("circle2 overlaps circle1")
else:
    print("circle2 does not overlap circle1")
