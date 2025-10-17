# This program indicates whether a point is inside a right triangle
from math import fabs
X, Y = eval(input("Enter a point's x- and y-coordinates: "))
# The right angle point of the rectangle is at (0, 0)
X0, Y0 = 0, 0
# The other two points are at (200, 0) and (0, 100)
X1, Y1 = 200, 0
X2, Y2 = 0, 100
# The triangle is divided into three triangles with the intersecting point
# Compute the area of the big triangle with the given numbers
Area_BigTriangle = 1/2 * 100 * 200
# Compute the area of the three small triangles
Area1 = fabs((X * (Y0 - Y1) + X0 * (Y1 - Y) + X1 * (Y - Y0)) / 2)
Area2 = fabs((X * (Y1 - Y2) + X1 * (Y2 - Y) + X2 * (Y - Y1)) / 2)
Area3 = fabs((X * (Y0 - Y2) + X0 * (Y2 - Y) + X2 * (Y - Y0)) / 2)
Area_SmallTriangle = Area1 + Area2 + Area3
# The total of three small area must be equal to the big area
# The point would be in the triangle
if Area_BigTriangle == Area_SmallTriangle:
    print("The point is in the triangle")
else:
    print("The point is not in the triangle")
