# Using Euler's method to solve Initial Value Problem
import numpy as np
import matplotlib.pyplot as plt


def euler_method(f, x_init, x_stop, y_init, h):
    x = np.arange(x_init, x_stop + h, h)  # Array from initial x to the stopping x
    n = len(x)
    y = np.zeros(n)
    y[0] = y_init  # Take y[0] as y0 (initial y)
    for i in range(n - 1):  # Formula y[n + 1] = y[n] + h * F(y'n)
        # F(y'[n]) = F(x[n], y[n]) = y[n] - x[n]
        y[i + 1] = y[i] + h * f(x[i], y[i])
    return x, y


def main():
    print("Euler's Method")
    f_approximate = input("Enter approximate equation f(x0, y0): ")
    f_exact = input("Enter exact equation f(x): ")
    fx_lambda = eval(f"lambda x, y: {f_approximate}")
    fex_lambda = eval(f"lambda x: {f_exact}")
    x_init = float(input("Enter beginning x: "))
    x_stop = float(input("Enter stopping x: "))
    y_init = float(input("Enter beginning y: "))
    x, y = euler_method(fx_lambda, x_init, x_stop, y_init, h=0.1)
    print("n\tx(n)\ty(n)\t\tExact Solution\t\tAbsolute Error")
    for i in range(1, len(y)):
        # Find the exact solution, absolute error
        ex = fex_lambda(x[i])
        ab = y[i] - ex
        print("{:d}\t{:0.1f}\t\t{:0.6f}\t\t{:0.6f}\t\t\t{:0.6f}"
              .format(i, x[i], y[i], ex, ab))
    # Draw a plot for illustration
    # Exact Solution using Integral
    plt.plot(x, y, "-r", label="Approximate")
    # Approximate Solution using Euler's method
    plt.plot(x, fex_lambda(x), "-b", label="Exact")
    plt.title(f"Differential equation: y' = {f_approximate}, y({x_init}) = {y_init}")
    plt.xlabel("x")
    plt.ylabel("y(x)")
    plt.grid()
    plt.legend(loc="lower right")
    plt.show()


main()
