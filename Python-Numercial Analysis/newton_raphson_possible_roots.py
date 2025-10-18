# Using Newton-Raphson method to find all positive real roots of the equation
import numpy as np
import sympy as sp


# df: derivative of function f
# tol: tolerance
def newton_raphson(f, df, x0, tol=1.0e-9, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x  # Solution found
        dfx = df(x)
        if dfx == 0:
            break  # Terminate if derivative zero
        x = x - fx / dfx
    return None  # Solution not found


def find_positive_roots(f, df, lower_bound, upper_bound, tol=1.0e-9):
    roots = []
    # Find all intervals with changing sign
    x = lower_bound
    step = (upper_bound - lower_bound) / 100  # Divide to 100 parts
    while x < upper_bound:
        if f(x) * f(x + step) < 0:  # Check changing sign
            root = newton_raphson(f, df, x, tol=tol)
            if root is not None and root > 0:  # Only save the positive roots
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
    print("Newton-Raphson Method (Find all positive real roots")
    f_input = input("Enter equation f(x): ")
    lower_bound, upper_bound = 0, 100
    x = sp.symbols('x')
    fx = sp.sympify(f_input.replace("^", "**"))
    dfx = derivative(fx)
    # Convert to lambda
    fx_lambda = sp.lambdify(x, fx, 'numpy')
    dfx_lambda = sp.lambdify(x, dfx, 'numpy')
    positive_roots = find_positive_roots(fx_lambda, dfx_lambda, lower_bound, upper_bound)
    print("All possible real roots of f(x):", positive_roots)


main()
