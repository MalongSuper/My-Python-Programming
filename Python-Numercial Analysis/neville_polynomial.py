# Polynomial Interpolation and Linear Regression
# Neville's polynomial interpolation method
import numpy as np


# Only compute polynomial interpolation of an unknown point
# based on already known points
# Different from Newton method is calculating the general equations
def neville(x_data, y_data, x):
    m = len(x_data)
    y = y_data.copy() * 1.0

    for k in range(1, m):
        y[0: m - k] = (((x - x_data[k:m]) * y[0: m - k]
                        + (x_data[0: m - k] - x) * y[1: m - k + 1])
                       / (x_data[0: m - k] - x_data[k:m]))
    return y[0]


def main():
    print("Neville Polynomial Interpolation")
    x0, x1, x2, x3 = eval(input("Enter four points coordinate-x: "))
    y0, y1, y2, y3 = eval(input("Enter four points coordinate-y: "))
    x_data = np.array([x0, x1, x2, x3])
    y_data = np.array([y0, y1, y2, y3])
    # Compute interpolation y for 1 unknown x in x_data
    x = float(input("Enter unknown x: "))
    y = neville(x_data, y_data, x)
    print("y =", y)


main()
