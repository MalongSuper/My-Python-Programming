# Finite Difference Approximations
# Find f'(x) and f''(x) at x
import sympy as sp


# Get the derivative level one and level two
def derivative_one_two(f):
    x = sp.symbols('x')
    # Convert the string to a symbolic expression
    fx = sp.sympify(f)
    derivative_one_fx = sp.diff(fx, x)
    derivative_two_fx = sp.diff(derivative_one_fx, x)
    return derivative_one_fx, derivative_two_fx


def difference_first(f, h, x, method='forward'):
    if method == "forward":
        return (f(x + h) - f(x)) / h
    elif method == "backward":
        return (f(x) - f(x - h)) / h
    elif method == "center":
        return (f(x + h) - f(x - h)) / (2 * h)


def difference_second(f, h, x, method='forward'):
    if method == "forward":
        return (f(x) - 2 * f(x + h) + f(x + 2 * h)) / (h ** 2)
    elif method == "backward":
        return (f(x - 2 * h) - 2 * f(x - h) + f(x)) / (h ** 2)
    elif method == "center":
        return (f(x + h) - 2 * f(x) + f(x - h)) / (h ** 2)


def main():
    print("Finite Difference Approximations")
    f_input = input("Enter equation f(x): ").replace("^", "**")
    x = float(input("Enter x: "))
    h = 0.01
    f = eval("lambda x:" + f_input.replace("^", "**"))
    # Get the actual result
    df1, df2 = derivative_one_two(sp.sympify(f_input.replace("^", "**")))
    df1, df2 = eval(f"lambda x: {df1}"), eval(f"lambda x: {df2}")
    f1_result, f2_result = df1(x), df2(x)
    # Forward difference approximation
    f1_forward = difference_first(f, h, x, 'forward')
    f2_forward = difference_second(f, h, x, 'forward')
    # Backward difference approximation
    f1_backward = difference_first(f, h, x, 'backward')
    f2_backward = difference_second(f, h, x, 'backward')
    # Central difference approximation
    f1_center = difference_first(f, h, x, 'center')
    f2_center = difference_second(f, h, x, 'center')
    # Display result
    print("{:<10} {:<20} {:<35}".format("f'(x)", "Result", "Difference"))
    print("{:<10} {:<20} {:<35}".format("Exact", f1_result, abs(f1_result - f1_result)))
    print("{:<10} {:<20} {:<35}".format("Forward", f1_forward, abs(f1_result - f1_forward)))
    print("{:<10} {:<20} {:<35}".format("Backward", f1_backward, abs(f1_result - f1_backward)))
    print("{:<10} {:<20} {:<35}".format("Center", f1_center, abs(f1_result - f1_center)))
    # Display result
    print()
    print("{:<10} {:<20} {:<35}".format("f''(x)", "Result", "Differences"))
    print("{:<10} {:<20} {:<35}".format("Exact", f2_result, abs(f2_result - f2_result)))
    print("{:<10} {:<20} {:<35}".format("Forward", f2_forward, abs(f2_result - f2_forward)))
    print("{:<10} {:<20} {:<35}".format("Backward", f2_backward, abs(f2_result - f2_backward)))
    print("{:<10} {:<20} {:<35}".format("Center", f2_center, abs(f2_result - f2_center)))


main()
