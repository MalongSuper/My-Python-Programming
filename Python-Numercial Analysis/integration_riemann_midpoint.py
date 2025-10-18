# Riemann Integration
import numpy as np
import math
from scipy.integrate import quad


def riemann(f, x, h, n):  # Calculate riemann using numpy
    # Use function values at endpoints
    f_vals = f(x)
    # Left integration, remove the last f(x)
    i_left = h * sum(f_vals[:n - 1])
    # Right integration, remove the first f(x)
    i_right = h * sum(f_vals[1:n])
    # Middle integration -> Use lambda f(x)
    x_midpoints = (x[0:n-1] + x[1:n]) / 2
    i_mid = h * sum(f(x_midpoints))
    return i_left, i_right, i_mid


def error_riemann(f, a, b, i_left, i_right, i_mid):  # Calculate error riemann
    i_exact = quad(f, a, b)
    err_left = np.abs(i_exact[0] - i_left)
    err_right = np.abs(i_exact[0] - i_right)
    err_mid = np.abs(i_exact[0] - i_mid)
    return err_left, err_right, err_mid


def main():
    print("Riemann Integration")
    a, b = eval(input("Enter range [a, b]: "))
    n = eval(input("Enter number of sub-intervals: "))
    # Number of rectangle sub-intervals
    h = (b - a) / (n - 1)
    x = np.linspace(a, b, n)
    # Input equation with lambda: Do not input "n-."
    f_input = input("Enter equation f(x): ")
    f = eval("lambda x:" + f_input.replace("log", "math.log")
             .replace("e", "np.e").replace("sin", "np.sin")
             .replace("cos", "np.cos")
             .replace("tan", "np.tan")
             .replace("pi", "np.pi"))
    # Left, Right, Middle integration
    integration = riemann(f, x, h, n)
    error = error_riemann(f, a, b, integration[0], integration[1], integration[2])
    print("Left Integration:", integration[0])
    print("Error =", error[0])
    print("Right Integration:", integration[1])
    print("Error =", error[1])
    print("Middle Integration:", integration[2])
    print("Error =", error[2])


main()
