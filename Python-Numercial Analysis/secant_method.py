# Using Secant Method to find solutions of equation

def function(fx, x):
    return eval(fx, {"x": x})


def secant(fx, x1, x2, tol, maximum):
    for i in range(1, maximum, 1):
        fx1 = function(fx, x1)
        fx2 = function(fx, x2)
        # If either function value is below the tolerance
        if abs(fx2) < tol:
            return x2
        # Division by zero
        if fx2 == fx1:
            print("Division by zero")
            return None
        # Use the Secant method formula
        x3 = x2 - fx2 * ((x2 - x1) / (fx2 - fx1))
        # Update value for the next iteration
        x1 = x2
        x2 = x3

    return x2


def main():
    # Input equation
    print("Secant Method")
    fx = input("Enter equation f(x): ").replace("^", "**")
    a, b = eval(input("Select interval (a, b): "))
    tolerance = float(input("Enter tolerance: "))
    number_iteration = int(input("Enter number of iterations: "))
    root = secant(fx, a, b, tolerance, number_iteration)
    print("Roots:", root)


main()
