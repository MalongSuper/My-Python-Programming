# Find the inverse by solving set of system of equations
# Improve the system of equations calculation with pivoting
import numpy as np


# Swap row i and j in vector/matrix v
def swap_row(v, i, j):
    if len(v.shape) == 1:  # v is vector
        v[i], v[j] = v[j], v[i]
    else:  # v is matrix
        v[[i, j], :] = v[[j, i], :]


def swap_column(v, i, j):
    v[:, [i, j]] = v[:, [j, i]]


# tol (tolerance): true or false
def gauss_elimination_pivot(mat_a, b, tol=1.0e-12):
    n = len(b)
    # Calculating the scale factor in each row
    s = np.zeros(n)
    for i in range(n):
        s[i] = max(np.abs(mat_a[i, :]))

    for k in range(0, n - 1):
        # Find row p with maximum relative size to swap with row k
        # argmax() returns index with the maximum,
        # so we must add k to get the absolute index in matrix A
        # Only find on column k with row from k to n - 1
        p = np.argmax(np.abs(mat_a[k: n, k]) / s[k:n]) + k
        if abs(mat_a[p, k]) < tol:
            print("Singular Matrix")
        if p != k:  # choose row p as pivot
            swap_row(b, k, p)  # Swap two elements in vector b
            swap_row(s, k, p)  # Swap two elements in matrix/ vector scale factor
            swap_row(mat_a, k, p)  # Swap two elements in matrix A

        # Basic Gauss Elimination
        for i in range(k + 1, n):  # i are rows
            if mat_a[i, k] != 0:
                # Use lambda
                lamb = mat_a[i, k] / mat_a[k, k]
                # Use slicing to re-calculate the values in one row
                mat_a[i, k: n] = mat_a[i, k: n] - lamb * mat_a[k, k: n]
                b[i] = b[i] - lamb * b[k]

    # If the values is too small
    if abs(mat_a[n - 1, n - 1]) < tol:
        print("Singular Matrix")

    # Back substitution
    b[n - 1] = b[n - 1] / mat_a[n - 1, n - 1]
    for k in range(n - 2, -1, -1):
        b[k] = (b[k] - np.dot(mat_a[k, k + 1: n], b[k + 1: n])) / mat_a[k, k]

    return b


def matrix_inverse(mat_A):
    n = len(mat_A)
    identity_matrix = np.identity(n)
    inverse_matA = np.zeros((n, n))
    # Solve the set of the systems of equations
    for i in range(n):
        # We need to save a copy of the matrix so that
        # the algorithm works on with the copy matrix
        vect_b = np.copy(identity_matrix[:, i])
        x = gauss_elimination_pivot(np.copy(mat_A), np.copy(vect_b))
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
