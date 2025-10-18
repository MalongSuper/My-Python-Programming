# Integration using Romberg
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


# Return the approximate integration and number of panels needed
def romberg(f, a, b, tol=1.0e-6):
    # r: An array storing all best Richardson values
    # k: The extrapolation for k round
    def richardson(r, k):
        for j in range(k - 1, 0, -1):
            # Constants for each round is 4^(k - j)
            constant = 4 ** (k - j)
            r[j] = (constant * r[j + 1] - r[j]) / (constant - 1.0)
        return r

    n = 21
    r = np.zeros(n)
    r[1] = recursive_trapezoid(f, a, b, 0.1, 1)
    r_old = r[1]

    for k in range(2, n):
        r[k] = recursive_trapezoid(f, a, b, r[k - 1], k)
        r = richardson(r, k)
        if abs(r[1] - r_old) < tol * max(abs(r[1]), 1.0):
            return r[1], 2 ** (k - 1)  # Number of panels needed
        r_old = r[1]
    print("The algorithm is not convergent")


def main():
    print("Romberg Integration")
    a, b = eval(input("Enter range [a, b]: "))  # Input "np.pi"
    # Input equation example "np.sin(x)"
    f = input("Enter equation f(x): ")
    # Convert to lambda for manual integration
    f_lambda = eval(f"lambda x: {f}")
    integration, number_panels = romberg(f_lambda, a, b)
    print("Integration:", integration)
    print("Number of panels:", number_panels)


main()
