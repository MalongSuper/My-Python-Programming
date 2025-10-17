# This program checks whether a point is within a circle
# The center point of the circle
from math import sqrt
X0, Y0 = 0, 0
# Input a point with two coordinates (x, y)
X, Y = eval(input("Enter a point with two coordinates: "))
# Compute the distance from the point to the center
Distance = sqrt((X - X0) ** 2 + (Y - Y0) ** 2)
# The point is in the circle if its distance to (0, 0) is less than or equal to 10
if Distance <= 10:
    X = X / 1
    Y = Y / 1
    print("Point", "(", X, ",", Y, ")", "is in the circle")
else:
    X = X / 1
    Y = Y / 1
    print("Point", "(", X, ",", Y, ")", "is not in the circle")
