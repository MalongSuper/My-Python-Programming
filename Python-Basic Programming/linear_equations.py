# This program solves linear equations
# Input the values
a, b, c, d, e, f = eval(input("Enter a, b, c, d, e, f: "))
# If ad – bc is 0, report that the equation has no solution
if (a * d - b * c) == 0:
    print("The equation has no solution")
else:
    # Solve the problem using Cramer’s rule
    x = (e * d - b * f) / (a * d - b * c)
    y = (a * f - e * c) / (a * d - b * c)
    # Display the results
    print("x is", x, "and y is", y)
