# This program find inverse matrix using Cofactor method
# Formula: A^-1 = (1 / det(A)) * PA
# det(A): Determinant of matrix
# PA: Adjugate matrix of A
# Obtained by transposing the matrix formed by the cofactors of the matrix A
import numpy as np
from numpy.linalg import det
# Input size
print("Inverse Matrix")
n = int(input("Enter size of the matrix: "))
# Form a matrix of order n
matrix = np.random.randint(0, 10, size=(n, n))
cofactors = []  # Store the cofactors
print("Matrix:\n", matrix)
# Find the adjugate matrix by finding the cofactors
# Formula: Aij = (-1)^(i + j) * det(Mij)
# Mij: matrix obtained from matrix A by removing row i, column j
for i in range(1, len(matrix) + 1):  # Iterate each element in the matrix
    for j in range(1, len(matrix) + 1):
        M = np.delete(matrix, i - 1, 0)  # Remove row
        M = np.delete(M, j - 1, 1)  # Remove column
        A = ((-1) ** (i + j)) * det(M)
        cofactors.append(round(A))  # Append the cofactors
# Transpose to get the adjugate matrix
cofactors = np.array(cofactors).reshape(n, n)
adjugate_matrix = np.transpose(cofactors)
print("Adjugate Matrix:\n", adjugate_matrix)
# Using the first row to find determinant of matrix A
det_matrix = round(det(matrix))
# Find the inverse matrix
try:
    inverse_matrix = (1 / det_matrix) * adjugate_matrix
except ZeroDivisionError:  # det(A) ≠ 0
    print("Determinant is 0, the matrix is non-invertible")
else:
    print("Inverse Matrix:\n", np.round(inverse_matrix, 2))
