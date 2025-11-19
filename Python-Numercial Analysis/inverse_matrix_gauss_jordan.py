# Inverse Matrix with gauss jordan elimination
import numpy as np


def gauss_jordan_inverse(mat_a):
    n = mat_a.shape[0]
    # Form augmented matrix [A | I]
    matrix = np.hstack([mat_a.astype(float), np.eye(n)])
    for i in range(n):
        # Make the diagonal element 1
        matrix[i] = matrix[i] / matrix[i, i]
        # Eliminate the i-th column entries of all other rows
        for j in range(n):
            if i != j:
                matrix[j] -= matrix[j, i] * matrix[i]
    # The last column is the solution
    inv_a = matrix[:, n:]
    return inv_a


def main():
    print("Inverse Matrix (Gauss-Jordan Elimination Method)")
    n = int(input("Enter size of the matrix: "))
    # Form a matrix of order n
    matrix = np.random.randint(0, 10, size=(n, n))
    print("Matrix A:\n", matrix)
    inverse_matrix = gauss_jordan_inverse(matrix)
    print("Inverse of A:\n", inverse_matrix)


main()
