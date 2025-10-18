# Find the inverse by solving set of system of equations
import numpy as np


def gauss_elimination(mat_a, vect_b):  # Matrix a and vector b
    # Time complexity when eliminate O(n^3/3), replace O(n^2/2)
    n = len(vect_b)
    a = mat_a.copy()
    b = vect_b.copy()
    # Elimination phase
    for i in range(0, n - 1):  # i is pivot
        for j in range(i + 1, n):  # j are rows below column "i" need to eliminate col i
            if a[j, i] != 0.0:
                # Define lambda to eliminate
                lamb = a[j, i] / a[i, i]
                # Calculate new row of the matrix using slicing
                a[j, i: n] = a[j, i: n] - lamb * a[i, i: n]
                # Update vector b
                b[j] = b[j] - lamb * b[i]
    # Backward substitution
    for i in range(n - 1, -1, -1):
        b[i] = (b[i] - np.dot(a[i, i + 1: n], b[i + 1: n])) / a[i, i]
    # Return the solution (vector b)
    return b


def matrix_inverse(mat_A):
    n = len(mat_A)
    identity_matrix = np.identity(n)
    inverse_matA = np.zeros((n, n))
    # Solve the set of the systems of equations
    for i in range(n):
        vect_b = identity_matrix[:, i]
        x = gauss_elimination(mat_A, vect_b)
        inverse_matA[:, i] = x
    return inverse_matA


def main():
    print("Inverse Matrix with Linear Equations")
    n = int(input("Enter the size of the matrix: "))
    matrix_A = np.zeros((n, n))
    for i in range(n):
        entries = input(f"+ Enter entries of row {i + 1} (separated by coma): ").split(",")
        matrix_A[i] = np.array([float(num) for num in entries])
    # Find the inverse matrix
    inverse_matrix_A = matrix_inverse(matrix_A)
    print("Matrix A:\n", matrix_A)
    print("Inverse Matrix A:\n", inverse_matrix_A)
    # Check the result
    print("A.A_inverse:\n", np.dot(matrix_A, inverse_matrix_A))


main()
