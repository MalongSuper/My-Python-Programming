# Linear Equations using Doolittle (LU method)
import numpy as np


# Input: Matrix A
# Output: Upper/Lower Triangular Matrix (L, U)
def doolittle(mat_a):
    n = len(mat_a)
    L = np.zeros([n, n])
    U = mat_a.copy()
    # Similar to Gauss Elimination
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if U[j, i] != 0:
                # Define lambda to eliminate
                lamb = U[j, i] / U[i, i]
                U[j, i: n] = U[j, i: n] - lamb * U[i, i: n]
                # Save the value in Lij (lambda) to form the matrix L
                L[j, i] = lamb
    # Add diagonal 1 to matrix L
    for i in range(0, n):
        L[i, i] = 1

    return L, U


def lu_solve(mat_a, b):
    n = len(mat_a)
    # Decompose Matrix A = LU
    L, U = doolittle(mat_a)
    # Solve Ly = b
    y = np.zeros(n)
    for k in range(0, n):
        b[k] = b[k] - np.dot(L[k, 0:k], b[0:k])
        # Because the new b[k] is used for later step
        # we don't directly define to y[k]
        y[k] = b[k]
    # Solve Ux = y
    x = np.zeros(n)
    # Back substitution
    for k in range(n - 1, -1, -1):
        y[k] = (y[k] - np.dot(U[k, k + 1: n], y[k + 1: n])) / U[k, k]
        x[k] = y[k]

    return x


def main():
    print("Linear Equations (Doolittle Method)")
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
