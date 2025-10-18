# Using Newton-Raphson method to find all roots of the equation from interval [a,b]
import numpy as np
import sympy as sp


# df: derivative of function f
# tol: tolerance
def newton_raphson(f, df, a, b, tol=1.0e-9):
    fa = f(a)
    if fa == 0.0:
        return a
    fb = f(b)
    if fb == 0.0:
        return b
    if np.sign(fa) == np.sign(fb):
        raise Exception("No solution found")
    # Estimate one initial x
    x = (a + b) / 2.0
    while abs(f(x)) >= tol:
        x = x - f(x) / df(x)
    return x


def derivative(f):
    x = sp.symbols('x')
    # Convert the string to a symbolic expression
    fx = sp.sympify(f)
    derivative_fx = sp.diff(fx, x)
    return derivative_fx


def main():
    print("Newton-Raphson Method")
    f_input = input("Enter equation f(x): ")
    a, b = eval(input("Select interval (a, b): "))
    x = sp.symbols('x')
    fx = sp.sympify(f_input.replace("^", "**"))
    dfx = derivative(fx)
    print(dfx)
    # Convert to lambda
    fx_lambda = sp.lambdify(x, fx, 'numpy')
    dfx_lambda = sp.lambdify(x, dfx, 'numpy')
    root = newton_raphson(fx_lambda, dfx_lambda, a, b, tol=1.0e-9)
    print(f"x = {root: 6.4f}")


main()
