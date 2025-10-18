# Trapezoidal Rule for Integration
import numpy as np
import scipy as sp


def trapezoid(f, a, b, n):  # Accuracy: O(h^2)
    # n: number of trapezoids
    # Formula: Ii = [f(xi) + f(xi + 1)] * h/2
    h = (b - a) / (n - 1)
    x = a
    S = 0.0
    # Divide into n panel of trapezoids equal to (n+1) of x
    for i in range(0, n):
        S += f(x) + f(x + h)
        x = x + h
    integration = S * h / 2.0
    return integration


def trapezoid_scipy(f, x):  # Using Scipy
    i_trapezoid = sp.integrate.trapezoid(f, x)
    return i_trapezoid


def main():
    print("Trapezoidal Rule Integration")
    a, b = eval(input("Enter range [a, b]: "))  # Input "np.pi"
    n = eval(input("Enter number of trapezoids: "))
    x = np.linspace(a, b, n)
    # Input equation example "np.sin(x)"
    f = input("Enter equation f(x): ")
    # Convert to lambda for manual integration
    f_lambda = eval(f"lambda x: {f}")
    integration = trapezoid(f_lambda, a, b, n)
    print("Integration:", integration)
    # Integration trapezoid using scipy
    integration_trap = trapezoid_scipy(eval(f), x)
    print("Trapezoid Integration:", integration_trap)


main()
