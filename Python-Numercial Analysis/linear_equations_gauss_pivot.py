# Linear Equations using Gauss Elimination with scaled pivot row
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


def main():
    print("Linear Equations (Gauss Elimination with scaled pivot row)")
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
    x = gauss_elimination_pivot(matrix_a, vector_b)
    print("Result:")
    for result in x:
        print(round(result, 2), end=" ")


main()
