# Calculate the derivative
# by interpolation through the 3 nearest neighboring points
import numpy as np


def nearest_neighbor_points(x_data, fx_data):
    # Least square fit
    A = x_data[:, np.newaxis] ** [0, 1, 2]
    Y = fx_data.T  # Select f0(x) = 1; f1(x) = x, f2(x) = x^2
    a = np.linalg.lstsq(A, Y, rcond=None)
    return a[0]  # Return the coefficients


def main():
    print("Nearest neighboring points")
    n = int(input("Enter the size of x and f(x): "))
    x = np.random.uniform(0, 3, size=n)  # Random float array
    fx = np.random.uniform(0, 3, size=n)
    # Round to four decimal piece
    x = np.round(x, 4)
    fx = np.round(fx, 4)
    print("x", x)
    print("fx", fx)
    coefficients = nearest_neighbor_points(x, fx)
    a, b, c = coefficients[0], coefficients[1], coefficients[2]
    # Put those coefficients to the equation
    # f(x) = (a) + (b) * x + (c) * x ^ 2
    # f'(x) = (b) + 2 * (c) * x
    # f''(x) = 2 * (c)
    # Replace x = 2.5
    x_value = float(input("Enter value: "))
    f_first = b + 2 * c * x_value
    f_second = 2 * c
    print(f"f'({x_value}) =", f_first)
    print(f"f''({x_value}) =", f_second)


main()
