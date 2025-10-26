# Laplace expansion for determinant of matrix
import numpy as np
from numpy.linalg import det


def laplace_expansion_row(matrix, row):
    if row >= len(matrix):
        raise ValueError('Out of Range. The program cannot proceed any further')
    cofactor_matrix = []
    for i in range(len(matrix)):
        # Take sub matrix for every iteration
        sub_matrix = np.delete(np.delete(matrix, row, axis=0), i, axis=1)
        cofactor = (-1) ** (row + i) * det(sub_matrix)
        cofactor_matrix.append(cofactor)
        print(f"matrix[{row}, {i}] = {matrix[row, i]}, cofactor = {cofactor}")
    determinant = sum(matrix[row, k] * cofactor_matrix[k] for k in range(len(matrix)))
    return determinant


def laplace_expansion_col(matrix, col):
    if col >= len(matrix):
        raise ValueError('Out of Range. The program cannot proceed any further')
    cofactor_matrix = []
    for i in range(len(matrix)):
        # Take sub matrix for every iteration
        sub_matrix = np.delete(np.delete(matrix, i, axis=0), col, axis=1)
        cofactor = (-1) ** (i + col) * det(sub_matrix)
        cofactor_matrix.append(cofactor)
        print(f"matrix[{i}, {col}] = {matrix[i, col]}, cofactor = {cofactor}")
    determinant = sum(matrix[k, col] * cofactor_matrix[k] for k in range(len(matrix)))
    return determinant


# Random n x n matrix
print("Laplace expansion")
n = int(input("Enter size of the matrix: "))
matrix3 = np.random.randint(0, 10, size=(n, n))
print("Matrix 3:\n", matrix3)
# Select nth row and nth column
row, col = map(int, input("Enter row and column: ").split(','))
print("+ Determinant of Matrix 3 (based on the row):", laplace_expansion_row(matrix3, row))
print("+ Determinant of Matrix 3 (based on the column):", laplace_expansion_row(matrix3, col))
# Compare with det()
print("+ Determinant of Matrix 3 (actual):", det(matrix3))
