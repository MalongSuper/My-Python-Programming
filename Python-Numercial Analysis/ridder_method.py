# Using Ridder's Method to solve the roots of equations
import numpy as np
import math


def function(fx, x):
    return eval(fx, {"x": x})


def ridder(fx, x1, x2, n, tol):
    x4_before = 0
    x3 = 0.5 * (x1 + x2)
    for i in range(n):
        print(f"Iteration {i + 1}")
        # Find root x based on the Ridder's formula
        x3 = 0.5 * (x1 + x2)
        f1 = function(fx, x1)
        f2 = function(fx, x2)
        f3 = function(fx, x3)
        s = math.sqrt(f3 ** 2 - f1 * f2)
        # The choice of using + or - depends on sign
        if np.sign(f2 - f1) > 0:
            x4 = x3 + (x3 - x1) / s
        else:
            x4 = x3 - (x3 - x1) / s
        # Update f4
        x4_after = x4
        print(f"Difference between two successive values of x4: {abs(x4_before - x4_after)}")
        if abs(x4_before - x4_after) < tol:
            print(f"The algorithm converged")
            break
        # Assign the f4 for the next iteration
        x4_before = x4_after
        if np.sign(f3) == np.sign(f1):
            x1, x2 = x3, x2
        else:
            x1, x2 = x1, x3
        print(f"New Interval: {x1, x2}")
    # Return the midpoint as the approximate result
    return x3


def main():
    # Input equation
    print("Ridder's Method")
    fx = input("Enter equation f(x): ").replace("^", "**")
    a, b = eval(input("Select interval (a, b): "))
    tolerance = float(input("Enter tolerance: "))
    number_iteration = int(input("Enter number of iterations: "))
    root = ridder(fx, a, b, number_iteration, tolerance)
    print("Roots:", root)


main()
