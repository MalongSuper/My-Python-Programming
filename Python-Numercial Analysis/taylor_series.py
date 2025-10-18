# This program converts an equation using Derivative and Taylor Series
import sympy as sp


def derivative(f, order=100):
    x = sp.symbols('x')
    # Convert the string to a symbolic expression
    fx = sp.sympify(f)
    derivative_fx_list = [fx]
    # Multiple derivative
    for i in range(1, order + 1):  # Set a maximum to avoid infinite loop
        fx = sp.diff(fx, x)
        if fx == 0:  # The derivative ends when 0 is encountered
            break
        derivative_fx_list.append(fx)  # Append the derivative
    return derivative_fx_list


def taylor_series(f, x0, order=100):
    # Taylor series P(x) = P(x0) + (P'(x0) / 1! * (x - x0)) + (P"(x0) / 2! * (x - x0)**2)...
    taylor_expansion = 0  # Initialize taylor expansion
    x = sp.symbols('x')
    derivative_fx_list = derivative(f, order)
    for j in range(len(derivative_fx_list)):
        # Calculate the factorial
        factorial = sp.factorial(j)
        # Evaluate derivative at x0
        derivative_at_x0 = derivative_fx_list[j].subs(x, x0)
        # Add the term to the taylor series
        taylor_expansion += (derivative_at_x0 / factorial) * ((x - x0) ** j)
    return taylor_expansion


def main():
    print("Expand P(x) using Taylor Series")
    f_input = input("Enter equation f(x): ")
    x0 = float(input("Enter x0: "))
    # Replace np. with an empty string
    f_input = f_input.replace("np.", "")
    # Convert to sympify
    fx = sp.sympify(f_input.replace("^", "**"))
    taylor = taylor_series(fx, x0, order=100)
    print("P(x) =", taylor)


main()
