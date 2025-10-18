# Combine Root Search with Bisection to find solutions of an equation
import numpy as np


def sign(x):  # Determine the sign of the number
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0


def root_search(f, a, b, dx):
    x1 = a
    f1 = f(x1)
    x2 = a + dx
    f2 = f(x2)
    while sign(f1) == sign(f2):
        if x1 >= b:
            return None, None
        x1 = x2
        f1 = f2
        x2 = x1 + dx
        f2 = f(x2)
    return x1, x2


def bisection(f, a, b, tol=1.0e-9):  # Bisection using recursion
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception(f"No solution found")
    while (b - a) / 2.0 > tol:
        c = (a + b) / 2.0
        if np.abs(f(c)) < tol:
            # c is the solution
            return c
        elif np.sign(f(a)) == np.sign(f(c)):
            # Solutions in range [c, b]
            a = c
        elif np.sign(f(b)) == np.sign(f(c)):
            # Solutions in range [a, c]
            b = c
    return (a + b) / 2.0


def main():
    # Input equation
    print("Root Search and Bisection")
    fx = input("Enter equation f(x): ")
    a, b = eval(input("Select interval (a, b): "))
    dx = float(input("Select dx: "))
    func = eval("lambda x:" + fx.replace("^", "**"))
    # Use the result of root_search function to display the interval roots
    x1, x2 = root_search(func, a, b, dx)
    roots_intervals = []
    while x1 is not None and x2 is not None:
        root = bisection(func, x1, x2)
        roots_intervals.append(root)
        x1, x2 = root_search(func, x2, b, dx)

    for roots in roots_intervals:
        print(f"Solutions for f(x): {roots}")


main()
