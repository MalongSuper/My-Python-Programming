# Linear Equations using Crout's decomposition
import numpy as np


def crout(mat_a):
    n = len(mat_a)
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    for i in range(0, n):
        U[i, i] = 1  # Set diagonal of U to 1
        # Calculate L
        for j in range(i, n):
            sum_0 = sum([L[j, s] * U[s, i] for s in range(0, i)])
            L[j, i] = mat_a[j, i] - sum_0
        # Calculate U
        for j in range(i + 1, n):
            sum_1 = sum([L[i, s] * U[s, j] for s in range(0, i)])
            U[i, j] = (mat_a[i, j] - sum_1) / L[i, i]
    return L, U


def lu_solve(a, b):
    # LU Decomposition (without pivoting for expected structure)
    L, U = crout(a)
    print("L =\n", L)
    print("U =\n", U)
    # Solve Ly = b (forward substitution)
    y = np.linalg.solve(L, b)
    # Solve Ux = y (back substitution)
    x = np.linalg.solve(U, y)
    return x


def main():
    print("Linear Equations (Crout Decomposition)")
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
    x = lu_solve(matrix_a, vector_b)
    print("Result:")
    for result in x:
        print(result, end="\n")


main()
