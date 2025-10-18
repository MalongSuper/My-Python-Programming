# Using Euler's method to solve Initial Value Problem
# For second level differentiation equations (Second-Order ODEs)
import numpy as np
import matplotlib.pyplot as plt


def euler_method(f, x_init, x_stop, y_init, v_init, h):
    x = np.arange(x_init, x_stop + h, h)  # Array from initial x to the stopping x
    n = len(x)
    # y is a 2D array with [y, v] (y and its derivative v = y')
    y = np.zeros((n, 2))  # 2 columns: column 0 is y(x), column 1 is y'(x)
    y[0, 0] = y_init  # Initial condition for y
    y[0, 1] = v_init  # Initial condition for y'
    for i in range(n - 1):
        # y' = v, v' = f(x, y, v)
        y[i + 1, 0] = y[i, 0] + h * y[i, 1]  # y[n + 1] = y[n] + h * v[n]
        y[i + 1, 1] = y[i, 1] + h * f(x[i], y[i, 0], y[i, 1])  # v[n + 1] = v[n] + h * f(x[n], y[n], v[n])
    return x, y


# Main function
def main():
    print("Euler's Method for Second-Order ODEs")
    # Input functions and parameters. For example:
    # f_approximate = 'np.exp(-x) + (x * np.exp(-x)) + x - 2'
    # f_exact_one = 'x * np.exp(-x) + (3 * np.exp(-x)) + (x ** 3) / 6 - x ** 2 + 3 * x - 3'
    # f_exact_two = '-x * np.exp(-x) - 2 * np.exp(-x) + (x ** 2) / 2 - 2 * x + 3'
    f_approximate = input("Enter approximate equation y'' = f(x, y, y'): ")
    f_exact_one = input("Enter exact equation y(x): ")
    f_exact_two = input("Enter exact equation y'(x): ")
    fx_lambda = eval(f"lambda x, y, v: {f_approximate}")  # f(x, y, y')
    fex_lambda = eval(f"lambda x: {f_exact_one}")  # Exact solution y(x)
    fedx_lambda = eval(f"lambda x: {f_exact_two}")
    # x_init = 0.0, x_stop = 2.0
    # y_init = 0.0, v_init = 1.0
    x_init = float(input("Enter initial x: "))
    x_stop = float(input("Enter stopping x: "))
    y_init = float(input("Enter initial y: "))
    v_init = float(input("Enter initial y': "))  # Initial condition for y'
    # Call Euler method
    x, y = euler_method(fx_lambda, x_init, x_stop, y_init, v_init, h=0.01)
    # Display results
    print("n\tx(n)\t\ty(n)\t\t\tExact y(n)\t\t\tError")
    for i in range(len(y)):
        ex, exd = fex_lambda(x[i]), fedx_lambda(x[i])  # Exact solution at x[i]
        err_ex = abs(y[i, 0] - ex)  # Absolute error for y(x)
        print("{:d}\t{:0.2f}\t\t{:0.6f}\t\t{:0.6f}\t\t{:0.6f}"
              .format(i, x[i], y[i, 0], ex, err_ex))
    print()
    print("n\tx(n)\t\ty'(n)\t\t\tExact y'(n)\t\t\tError")
    for i in range(len(y)):
        exd = fedx_lambda(x[i])
        err_exd = abs(y[i, 1] - exd)
        print("{:d}\t{:0.2f}\t\t{:0.6f}\t\t{:0.6f}\t\t{:0.6f}"
              .format(i, x[i], y[i, 1], exd, err_exd))

    # Plot results
    plt.plot(x, y[:, 0], "-r", label="Approximate y(x)")
    plt.plot(x, fex_lambda(x), "-b", label="Exact y(x)")
    plt.title(f"Differential equation: y'' = {f_approximate}, y({x_init}) = {y_init}")
    plt.xlabel("x")
    plt.ylabel("y(x)")
    plt.grid(True)
    plt.legend(loc="lower right")
    plt.show()


main()
