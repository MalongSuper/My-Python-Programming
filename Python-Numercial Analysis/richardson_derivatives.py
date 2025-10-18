# Richardson Extrapolation: Improve the accuracy of the finite difference results
import math


def richardson_extrapolation(f, x, h, diff):

    # The function to use the central difference formula
    def central_finite_difference(f, x, h, diff=1):
        if diff == 1:
            return (f(x + h) - f(x - h)) / (2 * h)
        elif diff == 2:
            return (f(x + h) - 2 * f(x) + f(x - h)) / (h ** 2)
        else:
            print("Only first and second derivatives are supported")

    h1 = h
    h2 = h1 / 2
    p = 2
    # Find the central finite difference at h1 and h2 = h1/2
    gh1 = central_finite_difference(f, x, h1, diff)
    gh2 = central_finite_difference(f, x, h2, diff)
    # Compute the result with Richardson Extrapolation
    G = ((2 ** p) * gh2 - gh1) / (2 ** p - 1)
    return G


def main():
    print("Richardson Extrapolation")
    f_input = input("Enter equation f(x): ").replace("^", "**")
    x = float(input("Enter x: "))
    h = float(input("Enter h: "))
    f = eval("lambda x:" + f_input.replace("log", "math.log")
             .replace("e", "math.e").replace("sin", "math.sin")
             .replace("cos", "math.cos")
             .replace("tan", "math.tan")
             .replace("pi", "math.pi"))
    G1 = richardson_extrapolation(f, x, h, diff=1)
    G2 = richardson_extrapolation(f, x, h, diff=2)
    print("First Derivative f'(x):", G1)
    print("Second Derivative f''(x):", G2)


main()
