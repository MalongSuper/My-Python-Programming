# Incremental Search Method to find solutions of equation
# Find the incremental, each increment is a dx
# Improve the calculations by starting from a large dx
# to find the rough interval when the root exists.
# Then, from that interval, narrow down to the smaller dx to increase precision.
# The process continues until the desired precision is achieved.
import numpy as np


def root_search_improved(f, a, b, final_dx):
    dx = 0.1  # Start with an initial dx
    while dx >= final_dx:
        x1 = a
        while x1 + dx <= b:
            x2 = x1 + dx
            f1, f2 = f(x1), f(x2)
            if np.sign(f1) != np.sign(f2):
                print(f"dx = {dx}; Interval: {x1, x2}")
                # Assign with the new interval for the next iteration
                a, b = x1, x2
                break
            x1 += dx
        dx /= 10  # Reduce the dx
    return (a + b) / 2.0


def main():
    print("Incremental Search Method")
    # Input equation
    fx = input("Enter equation f(x): ")
    a, b = eval(input("Select interval (a, b): "))
    dx = float(input("Select dx: "))
    # Draw a plot
    func = eval("lambda x:" + fx.replace("^", "**"))
    # Find the solutions
    root = root_search_improved(func, a, b, dx)
    if root != (None, None):
        print(f"Solutions for f(x): {root}")
    else:
        print("The equation has no solution")


main()
