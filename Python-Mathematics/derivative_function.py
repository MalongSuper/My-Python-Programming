# This program calculates derivative of a function
import sympy as sp


def derivative(f):
    x = sp.symbols('x')
    # Convert the string to a symbolic expression
    fx = sp.sympify(f)
    derivative_fx = sp.diff(fx, x)
    return derivative_fx


def main():
    print("Derivative of f(x)")
    f_input = input("Enter equation f(x): ")
    # Replace np. with an empty string
    f_input = f_input.replace("np.", "")
    # Convert to sympify
    fx = sp.sympify(f_input.replace("^", "**"))
    dfx = derivative(fx)
    print("Derivative:", dfx)


main()
