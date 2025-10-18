# Simpson's 3/8 Rule for Integration
# Another approach
import math
import numpy as np  # The module is used to convert to formula
# It is not used in this code
from scipy.integrate import quad


# n: even number of trapezoids, (n + 1) points xi
def simpson(f, a, b, n):
    h = (b - a) / n
    # List of every value in the interval with step size
    x_value = [a + (i * h) for i in range(n + 1)]
    total = []
    for k in range(0, len(x_value) - 1, 3):
        sub_intervals = x_value[k:k+4]
        x = sub_intervals[0]
        if len(sub_intervals) == 4:
            print("Interval:", sub_intervals)
            I_value = (((3 * h) / 8)
                       * (f(x) + 3 * f(x + h) + 3 * f(x + 2 * h) + f(x + 3 * h)))
            print("Simpson's 8/3 Rule:", I_value)
            total.append(I_value)
        elif len(sub_intervals) == 3:
            print("Interval:", sub_intervals)
            I_value = (h / 3) * (f(x) + 4 * f(x + h) + f(x + 2 * h))
            print("Simpson's 1/3 Rule:", I_value)
            total.append(I_value)
        else:
            raise ValueError("Not enough points to apply Simpson's rule. "
                             "The algorithm cannot find the solution\nSuggestion: n should be a multiple of 3")
    integration = sum(total)
    error_integration = (quad(f, a, b)[0] - integration)
    return integration, error_integration


def main():
    print("Simpson's 8/3 Rule Integration")
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
