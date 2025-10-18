# Compute derivative with formulas
import math


def derivative_one(f, x, h=None):  # h is optional
    if h is None:
        h = 0.0001
    df = (f(x + h) - f(x)) / h
    return df


def derivative_two(f, x, h=None):
    if h is None:
        h = 0.0001
    df2 = (f(x - h) - 2 * f(x) + f(x + h)) / (h ** 2)
    return df2


def main():
    print('Derivative one and two')
    # Compute derivative of quadratic equation at x = 5
    fx = input("Enter exact equation f(x): ")
    fx = eval(f"lambda x: {fx}")
    df = derivative_one(fx, 5)
    df2 = derivative_two(math.sin, 5)
    print("First Derivative of quadratic equation:", df)
    print("Second Derivative of quadratic equation:", df2)


main()
