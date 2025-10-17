# This program indicates intersecting point
# Input the points
x1, y1, x2, y2, x3, y3, x4, y4 = eval(input("Enter x1, y1, x2, y2, x3, y3, x4, y4:\n "))
# Solving the given linear equation
# Find the a, b, c, d, e, f
a = y1 - y2
b = -1 * (x1 - x2)
e = (y1 - y2) * x1 - (x1 - x2) * y1
c = y3 - y4
d = -1 * (x3 - x4)
f = (y3 - y4) * x3 - (x3 - x4) * y3
# The point are parallel when it is divided to zero
if (a * d - b * c) == 0:
    print("The two lines are parallel")
else:
    # Solved the x, y using Cramer’s rule
    x = (e * d - b * f) / (a * d - b * c)
    y = (a * f - e * c) / (a * d - b * c)
    # Display the result
    x = round(x, 5)
    y = round(y, 5)
    print("The intersecting point is at", "(", x, ",", y, ")")
