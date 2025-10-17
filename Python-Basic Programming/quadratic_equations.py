# This program solves quadratic equations
from math import sqrt
# Input the values for a, b, c
a, b, c = eval(input("Enter a, b, c: "))
# In quadratic equations, the variable a cannot be a zero
if a == 0:
    print("Error: The variable a cannot be a zero. "
          "Please proceed and try again")
else:
    # Calculate the discriminant
    Discriminant = (b ** 2) - (4 * a * c)
    # If the discriminant is negative, the equation has no real roots.
    if Discriminant < 0:
        print("The equation has no real boots")
    # If the discriminant is zero, the equation has one root
    elif Discriminant == 0:
        One_Root = -b / (2 * a)
        print("The root is", One_Root)
    # If the discriminant is positive, the equation has two real
    elif Discriminant > 0:
        Root1 = (-b + sqrt(Discriminant)) / (2 * a)
        Root2 = (-b - sqrt(Discriminant)) / (2 * a)
        print("The roots are", Root1, "and", Root2)
