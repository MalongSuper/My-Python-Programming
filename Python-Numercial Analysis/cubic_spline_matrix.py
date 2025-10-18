# Cubic Spline Matrix -> Solve the system of linear equations
# The result are the coefficients of the cubic polynomial having the form
# S(x) = ax^3 + bx^2 + cx + d
# While the result of the scipy.interpolate.CubicSpline the cubic polynomial having the form
# S(x) = a(x-xi)^3 + b(x-xi)^2 + c(x-xi) + d
# But when simplified, the results are the same
import numpy as np


def cubic_spline_matrix(matrix_a, vector_b, n):
    x = np.dot(np.linalg.inv(matrix_a), vector_b)
    # If the result is 8 coefficients (a vector with 8 values), equivalent to 2 cubic splines
    # Formula: 4(3-1) = 8; So general formula is 4(n-1), reshape to
    # Each cubic spline correspond to (n - 1) number of splines
    result_x = x.reshape((n // 4), 4)
    print("coefficients =\n", result_x)
    return result_x


def main():
    print("Cubic Spline Matrix")
    # Input number of unknowns and initialize matrix and vector
    n = int(input("Enter number of unknowns: "))
    matrix_a = np.zeros((n, n))
    constants_list, vector_b = [], np.zeros(n)
    for i in range(n):
        # Input coefficients
        coefficients = input(f"+ Enter coefficients of row {i + 1} (separated by coma): ").split(",")
        # Add the values to array (matrix row) to create a matrix
        matrix_a[i] = np.array([float(num) for num in coefficients])
        # Input constants
        constants = float(input(f"+ Enter constants of row {i + 1}: "))
        constants_list.append(constants)  # Append input constant to the list
        # then convert it to array
        vector_b = np.array(constants_list)
    # Find the coefficients
    cubic_spline_matrix(matrix_a, vector_b, n)


main()
