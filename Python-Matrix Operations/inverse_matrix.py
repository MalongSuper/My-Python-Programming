# Inverse Matrix
import numpy as np
from numpy.linalg import inv
print("Inverse Matrix")
# Matrix must be square to be inverse
n = eval(input("Enter size of the matrix: "))
matrix = np.random.randint(0, 100, size=(n, n))
print("Matrix:\n", matrix)
inverse_matrix = inv(matrix)
print("Inverse Matrix:\n", inverse_matrix)
