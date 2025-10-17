# This program indicates whether a point is in a rectangle
from math import sqrt
X0, Y0 = 0, 0
# Input a point with two coordinates (x, y)
X, Y = eval(input("Enter a point with two coordinates: "))
# Compute the distance in the horizontal side
X, Axis = X, 0
Horizontal_Distance = sqrt((X - X0) ** 2 + (Axis - Y0) ** 2)
# Compute the distance in the vertical side
Axis, Y = 0, Y
Vertical_Distance = sqrt((Axis - X0) ** 2 + (Y - Y0) ** 2)
# The horizontal distance must be less than or equal to 10 / 2
# The vertical distance must be less than or equal to 5.0 / 2
if (Horizontal_Distance <= 10 / 2) and (Vertical_Distance <= 5.0 / 2):
    # The point would be in the rectangle
    X = X / 1
    Y = Y / 1
    print("Point", "(", X, ",", Y, ")", "is in the rectangle")
else:
    X = X / 1
    Y = Y / 1
    print("Point", "(", X, ",", Y, ")", "is not in the rectangle")

