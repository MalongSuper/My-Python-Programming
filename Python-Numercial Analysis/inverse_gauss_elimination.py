# This program finds the inverse matrix
# by solving a set of systems (with Gauss Elimination)
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

    return b


def matrix_inverse(a):
    n = len(a)
    mat_i = np.identity(n)  # Identity matrix
    a_inverse = np.zeros((n, n))
    # Solve the systems of equations Ax = b one by one
    # b is the vector column i of matrix I
    for i in range(n):
        b = mat_i[:, i]
        x = gauss_elimination(a, b)
        a_inverse[:, i] = x
    return a_inverse


def main():
    n = int(input("Enter size of the matrix: "))
    matrix = np.random.randint(0, 10, size=(n, n))
    print("Matrix A:\n", matrix)
    inverse_matrix = matrix_inverse(matrix)
    print("Inverse Matrix A:\n", inverse_matrix)
    # Check the result A * A^-1 = I
    print("A * Inverse A:\n", np.dot(matrix, inverse_matrix))


main()
