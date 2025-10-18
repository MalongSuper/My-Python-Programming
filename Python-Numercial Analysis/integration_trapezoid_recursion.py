# Integration using Recursive trapezoid rule
import numpy as np  # The module is used to convert to formula
# It is not used in this code


def recursive_trapezoid(f, a, b, i_old, k):
    # k: number of panels is 2 ** (k - 1)
    if k == 1:
        i_new = (f(a) + f(b)) * (b - a) / 2.0
    else:
        n = 2 ** (k - 2)
        h = (b - a) / n
        x = a + h / 2.0
        S = 0.0
        for i in range(n):
            S = S + f(x)
            x = x + h
        i_new = (i_old + h * S) / 2.0
    return i_new


def main():
    print("Recursive Trapezoidal Rule Integration")
    a, b = eval(input("Enter range [a, b]: "))   # Input "np.pi"
    # Input equation example "np.sin(x)"
    f = input("Enter equation f(x): ")
    # Convert to lambda for manual integration
    f_lambda = eval(f"lambda x: {f}")
    integration = 0.0
    for k in range(1, 9):
        integration = recursive_trapezoid(f_lambda, a, b, integration, k)
    print("Integration:", integration)


main()
