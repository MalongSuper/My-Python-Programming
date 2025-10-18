# Using Runge-Kutta 4th method to solve Initial Value Problem
import numpy as np
import matplotlib.pyplot as plt


def runge_kutta_4th(f, x, y, h):
    K0 = h * f(x, y)
    K1 = h * f(x + h / 2.0, y + K0 / 2.0)
    K2 = h * f(x + h / 2.0, y + K1 / 2.0)
    K3 = h * f(x + h, y + K2)
    res = (K0 + 2 * K1 + 2 * K2 + K3) / 6.0
    return res


def main():
    print("Runge-Kutta 4th Method")
    f_approximate = input("Enter approximate equation f(x0, y0): ")
    f_exact = input("Enter exact equation f(x): ")
    fx_lambda = eval(f"lambda x, y: {f_approximate}")
    fex_lambda = eval(f"lambda x: {f_exact}")
    x_init = float(input("Enter beginning x: "))
    x_stop = float(input("Enter stopping x: "))
    y_init = float(input("Enter beginning y: "))
    h = 0.1
    # Set initial list X, Y and add x, y to them
    x, y = x_init, y_init
    X = [x]
    Y = [y]
    while x < x_stop:
        h = min(h, x_stop - x)
        y = y + runge_kutta_4th(fx_lambda, x, y, h)
        x = x + h
        X.append(x)
        Y.append(y)

    array_X = np.array(X)
    array_Y = np.array(Y)
    print("n\tx(n)\ty(n)\t\tExact Solution\t\tAbsolute Error")
    for i in range(1, len(Y)):
        # Find the exact solution, absolute error
        ex = fex_lambda(array_X[i])
        ab = array_Y[i] - ex
        print("{:d}\t{:0.1f}\t\t{:0.5f}\t\t{:0.6f}\t\t\t{:0.6f}"
              .format(i, array_X[i], array_Y[i], ex, ab))

    # Draw a plot for illustration
    # Exact Solution using Integral
    x_exact_vals = np.linspace(x_init, x_stop, 500)
    y_exact_vals = fex_lambda(x_exact_vals)
    plt.plot(x_exact_vals, y_exact_vals, '-b', label="Exact Solution")
    plt.plot(array_X, array_Y, '-r', label="Approximate Solution (RK4)")
    plt.title(f"Differential equation: y' = {f_approximate}, y({x_init}) = {y_init}")
    plt.xlabel("x")
    plt.ylabel("y(x)")
    plt.grid(True)
    plt.legend(loc="lower right")
    plt.show()


main()
