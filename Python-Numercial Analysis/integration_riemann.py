# Riemann Integration
import numpy as np
import scipy as sp


def riemann_numpy(f, x, h, n):  # Calculate riemann using numpy
    # Left integration, remove the last f(x)
    i_left = h * sum(f[:n - 1])
    # Right integration, remove the first f(x)
    i_right = h * sum(f[1:n])
    # Middle integration
    i_mid = h * sum(np.sin((x[0:n-1] + x[1:n]) / 2))
    return i_left, i_right, i_mid


def error_riemann(i_left, i_right, i_mid):  # Calculate error riemann
    err_left = 2 - i_left  # Formula I = -cos(pi) + cos(0.0) = 1 + 1 =2
    err_right = 2 - i_right
    err_mid = 2 - i_mid
    return err_left, err_right, err_mid


def riemann_scipy(f, x):  # Calculate integration of trapezoid using scipy
    i_trapezoid = sp.integrate.trapezoid(f, x)
    err_trapezoid = 2 - i_trapezoid
    return i_trapezoid, err_trapezoid


def main():
    print("Riemann Integration")
    a, b = eval(input("Enter range [a, b]: "))
    n = eval(input("Enter number of sub-intervals: "))
    # Number of rectangle sub-intervals
    h = (b - a) / (n - 1)
    x = np.linspace(a, b, n)
    # Input equation with "np."
    f = eval(input("Enter equation f(x): "))
    # Left, Right, Middle integration
    integration = riemann_numpy(f, x, h, n)
    error = error_riemann(integration[0], integration[1], integration[2])
    print("Left Integration:", integration[0])
    print("Error =", error[0])
    print("Right Integration:", integration[1])
    print("Error =", error[1])
    print("Middle Integration:", integration[2])
    print("Error =", error[2])
    # Trapezoid integration
    trap_integration = riemann_scipy(f, x)
    print("Trapezoid Integration:", trap_integration[0])
    print("Error =", trap_integration[1])


main()
