# Determinant Matrix
import numpy as np
from numpy.linalg import det
print("Determinant Matrix")
# Matrix must be square to have determinant
n = eval(input("Enter size of the matrix: "))
matrix = np.random.randint(0, 100, size=(n, n))
print("Matrix:\n", matrix)
determinant = det(matrix)
print("Determinant:", determinant)
