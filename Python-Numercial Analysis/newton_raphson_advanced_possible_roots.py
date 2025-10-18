# Upgrade Newton-Raphson method to find all positive real roots of the equation
import sympy as sp
import numpy as np


# df: derivative of function f
# tol: tolerance
def newton_raphson(f, df, x0, tol=1.0e-9):
    x = x0
    for i in range(30):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:  # Avoid division by 0
            return None
        dx = -fx / dfx
        x = x + dx
        if abs(dx) < tol * max(abs(x), 1.0):
            return x
    return None  # If no convergence


def find_positive_roots(f, df, start, end, step):
    roots = []
    x = start
    while x < end:
        if f(x) * f(x + step) < 0:  # Check for different sign
            root = newton_raphson(f, df, x + step / 2)  # Find solution between x and x + step
            if root is not None and root > 0:
                roots.append(root)
        x += step
    return roots


def derivative(f):
    x = sp.symbols('x')
    # Convert the string to a symbolic expression
    fx = sp.sympify(f)
    derivative_fx = sp.diff(fx, x)
    return derivative_fx


def main():
    print("Newton-Raphson Method Advanced (Find all positive real roots)")
    f_input = input("Enter equation f(x): ")
    # Replace np. with an empty string
    f_input = f_input.replace("np.", "")
    # Convert to sympify
    x = sp.symbols('x')
    fx = sp.sympify(f_input.replace("^", "**"))
    dfx = derivative(fx)
    # Convert to lambda
    fx_lambda = sp.lambdify(x, fx, 'numpy')
    dfx_lambda = sp.lambdify(x, dfx, 'numpy')
    positive_roots = find_positive_roots(fx_lambda, dfx_lambda, 0, 100, 0.1)
    print("All possible real roots of f(x):")
    for i in positive_roots:
        print(i)


main()
