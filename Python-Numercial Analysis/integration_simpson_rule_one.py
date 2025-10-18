# Simpson's Rule for Integration
import math
import numpy as np  # The module is used to convert to formula
# It is not used in this code
from scipy.integrate import quad


# n: even number of trapezoids, (n + 1) points xi
def simpson(f, a, b, n):
    h = (b - a) / n
    x = a
    S = 0.0
    # Each iteration increases two jumps
    for i in range(0, n, 2):
        S += f(x) + 4 * f(x + h) + f(x + 2 * h)
        x += 2 * h
    integration = (h / 3) * S
    error_integration = (quad(f, a, b)[0] - integration)
    return integration, error_integration


def main():
    print("Simpson's Rule Integration")
    a, b = eval(input("Enter range [a, b]: "))  # Input "np.pi"
    n = int(input("Enter n: "))
    # Input equation example "np.sin(x)"
    f = input("Enter equation f(x): ")
    # Convert to lambda for manual integration
    f_lambda = eval(f"lambda x: {f}")
    integration, error_integration = simpson(f_lambda, a, b, n)
    print("Integration:", integration)
    print("Error:", error_integration)


main()