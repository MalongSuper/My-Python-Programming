# Linear Equations using Cholesky Decomposition
import numpy as np
import math


# [A] = [L][L]transpose
def cholesky_decompose(mat_a):
    n = len(mat_a)
    for i in range(n):  # i: column
        try:
            # Elements in diagonal
            mat_a[i, i] = math.sqrt(mat_a[i, i] - np.dot(mat_a[i, 0: i], mat_a[i, 0: i]))
        except ValueError:  # Square root of negative numbers
            print("Matrix is not positive definite")
        # The remaining elements
        for j in range(i + 1, n):  # j: row
            mat_a[j, i] = (mat_a[j, i] - np.dot(mat_a[j, 0: i], mat_a[i, 0: i])) / mat_a[i, i]
    # Elements in upper triangular matrix = 0
    for i in range(1, n):  # i: column
        mat_a[0: i, i] = 0.0
    return mat_a


def cholesky_solve(mat_a, b):
    n = len(b)
    lower = cholesky_decompose(mat_a)
    # Solve [L]{y} = {b}, after calculating vector b is y
    for k in range(n):
        b[k] = (b[k] - np.dot(lower[k, 0: k], b[0: k])) / lower[k, k]
    # Solve [L_transpose]{x} = {y}
    # Back substitution
    for k in range(n - 1, -1, -1):
        b[k] = (b[k] - np.dot(lower[k + 1: n, k], b[k + 1: n])) / lower[k, k]

    return b


def main():
    print("Linear Equations (Cholesky Decomposition)")
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
    # Compute and display the result
    x = cholesky_solve(matrix_a, vector_b)
    print("Result:")
    for result in x:
        print(result, end=" ")


main()
