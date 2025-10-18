# Linear Equations using Gauss-Jordan Elimination
import numpy as np


def gauss_jordan(mat_a, vect_b):
    n = len(vect_b)
    a = mat_a.copy()
    b = vect_b.copy()
    # Merge the matrix A and vector b
    matrix = np.hstack([a, b.reshape(-1, 1)])  # Vector b reshape as column matrix
    for i in range(n):
        # Make the diagonal element 1
        matrix[i] = matrix[i] / matrix[i, i]
        # Eliminate the i-th column entries of all other rows
        for j in range(n):
            if i != j:
                matrix[j] -= matrix[j, i] * matrix[i]
    # The last column is the solution
    b = matrix[:, -1]
    return b


def main():
    print("Linear Equations (Gauss-Jordan Elimination Method)")
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
    x = gauss_jordan(matrix_a, vector_b)
    print("Result:")
    for result in x:
        print(round(result, 2), end=" ")


main()
