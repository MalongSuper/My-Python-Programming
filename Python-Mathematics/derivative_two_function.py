# This program calculates derivative two of a function
import sympy as sp


def derivative_two(f):
    x = sp.symbols('x')
    # Convert the string to a symbolic expression
    fx = sp.sympify(f)
    derivative_fx = sp.diff(fx, x)  # Derivative one
    derivative_two_fx = sp.diff(derivative_fx, x)  # Derivative two
    return derivative_two_fx


def main():
    print("Derivative Two of f(x)")
    f_input = input("Enter equation f(x): ")
    # Replace np. with an empty string
    f_input = f_input.replace("np.", "")
    # Convert to sympify
    fx = sp.sympify(f_input.replace("^", "**"))
    dfx = derivative_two(fx)
    print("Derivative Two:", dfx)


main()
