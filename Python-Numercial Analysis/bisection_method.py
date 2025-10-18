# Bisection Method to find solutions of equation
# With recursion and without recursion
# To understand about this method
# Watch video: https://www.youtube.com/watch?v=wXtswjijp0o
import numpy as np


def bisection_recursion(f, a, b, tol=1.0e-9):  # With recursion
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception(f"No solution found")
    # Compute the mean value
    c = (a + b) / 2.0
    if np.abs(f(c)) < tol:
        # c is the solution
        return c
    elif np.sign(f(a)) == np.sign(f(c)):
        # Solutions in range [c, b]
        return bisection_recursion(f, c, b, tol)
    elif np.sign(f(b)) == np.sign(f(c)):
        # Solutions in range [a, c]
        return bisection_recursion(f, a, c, tol)


def bisection_iteration(f, a, b, tol=1.0e-9):  # With Iteration
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
    print("Bisection Method")
    fx = input("Enter equation f(x): ")
    a, b = eval(input("Select interval (a, b): "))
    func = eval("lambda x:" + fx.replace("^", "**"))
    # Find the solutions
    root1 = bisection_recursion(func, a, b, tol=1.0e-9)
    root2 = bisection_iteration(func, a, b, tol=1.0e-9)
    print(f"(Recursion) Solutions for f(x): {root1}")
    print(f"(Iteration) Solutions for f(x): {root2}")


main()
