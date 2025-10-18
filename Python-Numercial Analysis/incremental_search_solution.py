# Incremental Search Method to find solutions of equation
# Find the incremental, each increment is a dx
# To understand about this method
# Watch this video: https://www.youtube.com/watch?v=Dl5NkWdLTEE
import numpy as np


def root_search(f, a, b, dx):
    x1 = a
    f1 = f(x1)
    x2 = a + dx
    f2 = f(x2)
    while np.sign(f1) == np.sign(f2):
        if x1 >= b:
            return None, None
        x1 = x2
        f1 = f2
        x2 = x1 + dx
        f2 = f(x2)

    print(f"Sign changes at: ({x1}, {x2})")
    return (x1 + x2) / 2.0


def main():
    print("Incremental Search Method")
    # Input equation
    fx = input("Enter equation f(x): ")
    a, b = eval(input("Select interval (a, b): "))
    dx = float(input("Select dx: "))
    # Draw a plot
    func = eval("lambda x:" + fx.replace("^", "**"))
    # Find the solutions
    root = root_search(func, a, b, dx)
    if root != (None, None):
        print(f"Solutions for f(x): {root}")
    else:
        print("The equation has no solution")


main()
