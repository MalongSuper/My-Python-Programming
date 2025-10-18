# This program calculates integral of a function
import sympy as sp


def integral(f):
    x = sp.symbols('x')
    # Convert the string to a symbolic expression
    fx = sp.sympify(f)
    integral_fx = sp.integrate(fx, x)
    return integral_fx


def main():
    print("Integral of f(x)")
    f_input = input("Enter equation f(x): ")
    # Replace np. with an empty string
    f_input = f_input.replace("np.", "")
    # Convert to sympify
    fx = sp.sympify(f_input.replace("^", "**"))
    dfx = integral(fx)
    print("Integral:", dfx)


main()
