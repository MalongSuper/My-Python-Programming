# LU Decomposition
import numpy as np
from scipy.linalg import lu
# Define a matrix
print("LU Decomposition")
n = eval(input("Enter size of the matrix: "))
matrix = np.random.randint(1, 100, size=(n, n))
print("Matrix:\n", matrix)
# Compute LU Composition
# U = upper triangular matrix
# L = lower triangular matrix
P, L, U = lu(matrix)
print("P:\n", P)
print("L:\n", L)
print("U:\n", U)
# Calculation
print("LU:\n", np.dot(L, U))
