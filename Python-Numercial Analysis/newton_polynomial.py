# Polynomial Interpolation and Linear Regression
# Newton's polynomial interpolation method
import numpy as np
import matplotlib.pyplot as plt


def divided_difference_table(x_data, y_data):
    n = len(x_data)
    table = np.zeros((n, n))  # Initialize zero table
    table[:, 0] = y_data  # First column is y values
    for i in range(1, n):
        for j in range(n - i):
            table[j][i] = ((table[j + 1][i - 1] - table[j][i - 1])
                           / (x_data[j + i] - x_data[j]))
    return table


# Compute a through divided difference table
def coefficients(x_data, y_data):
    n = len(x_data)
    # Array storing all the divided differences, initially a = y
    # Error may occur when the values are integer -> round
    # Convert "a" to float
    a = y_data.copy() * 1.0

    for k in range(1, n):
        a[k:n] = (a[k:n] - a[k - 1]) / (x_data[k:n] - x_data[k - 1])
    # The result of vector "a" is the coefficient of Newton's polynomial interpolation
    return a


# Newton's polynomial interpolation can be written as summation of calculus
# a: coefficient of Newton's polynomial interpolation
def evaluate_poly(a, x_data, x):
    # n is the highest exponential degree of the polynomial = interpolation point - 1
    n = len(x_data) - 1
    p = a[n]
    for k in range(1, n + 1):
        p = a[n - k] + (x - x_data[n - k]) * p
    return p


def main():
    print("Newton Polynomial Interpolation")
    x0, x1, x2, x3 = eval(input("Enter three points coordinate-x: "))
    y0, y1, y2, y3 = eval(input("Enter three points coordinate-y: "))
    x_data = np.array([x0, x1, x2, x3])
    y_data = np.array([y0, y1, y2, y3])
    coefficient_a = coefficients(x_data, y_data)
    table = divided_difference_table(x_data, y_data)
    interval = 0.1
    x_plot = np.arange(x_data[0], x_data[len(x_data) - 1] + interval, interval)
    y_plot = evaluate_poly(coefficient_a, x_data, x_plot)
    print("Divided Difference Table:\n", table)
    print("\na =", coefficient_a)
    # Draw a plot
    plt.figure(figsize=(12, 8))
    # Draw coordinate (x, y)
    plt.plot(x_data, y_data, "bo")
    # Draw the curve equation
    plt.title(f"Newton's Polynomial Interpolation")
    plt.plot(x_plot, y_plot)
    plt.xlabel('x')  # x-coordinate
    plt.ylabel('y = f(x)')  # y-coordinate
    plt.grid(True)
    plt.show()


main()
