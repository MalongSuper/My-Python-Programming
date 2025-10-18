# This program soles system of equations
# Apply LU Decomposition
import numpy as np


def lu_decomposition(a):
    # Perform LU Decomposition without pivoting
    n = a.shape[0]
    L = np.zeros_like(a)
    U = np.zeros_like(a)
    for i in range(n):
        # Upper triangular matrix U
        U[i, i:] = a[i, i:] - np.dot(L[i, :i], U[:i, i:])
        # Lower triangular matrix L
        L[i + 1:, i] = (a[i + 1:, i] - np.dot(L[i + 1:, :i], U[:i, i])) / U[i, i]
        L[i, i] = 1  # Diagonal entries of L are 1
    return L, U


def lu_solve(a, b):
    # LU Decomposition (without pivoting for expected structure)
    L, U = lu_decomposition(a)
    print("L =\n", L)
    print("U =\n", U)
    # Solve Ly = b (forward substitution)
    y = np.linalg.solve(L, b)
    print("y =\n", y)
    # Solve Ux = y (back substitution)
    x = np.linalg.solve(U, y)
    print("x =\n", x)


def main():
    print("Linear Equations (LU Decomposition)")
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
    lu_solve(matrix_a, vector_b)


main()
