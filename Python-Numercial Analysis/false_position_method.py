# Using False Position Method to find solutions of equation

def function(fx, x):
    return eval(fx, {"x": x})


def false_position_method(func, a, b, tol_accept):
    fa = function(func, a)
    fb = function(func, b)

    if fa * fb >= 0:
        print("The method is not valid at this stage "
              "since no root of multiple roots present")
        return None

    c_before = a
    c_after = ""
    tol = float('inf')  # Initial tolerance to infinity
    while tol > tol_accept:
        # Calculate c using the secant formula
        c_after = (a * fb - b * fa) / (fb - fa)
        fc = function(func, c_after)
        # Update the interval based on the sign of f(c)
        if fc * fa < 0:
            b, fb = c_after, fc  # c is in [a, b]
        else:
            a, fa = c_after, fc  # c is in [a, b]
        # Compute the tolerance
        tol = abs(c_after - c_before)
        c_before = c_after  # Update c_before

    return c_after  # Return the root


def main():
    # Input equation
    print("False Position Method")
    fx = input("Enter equation f(x): ").replace("^", "**")
    a, b = eval(input("Select interval (a, b): "))
    tolerance = float(input("Enter tolerance: "))
    root = false_position_method(fx, a, b, tolerance)
    print("Roots:", root)


main()
