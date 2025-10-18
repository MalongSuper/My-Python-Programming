# Create a Matrix and transpose it
import numpy as np
print("Transpose Matrix")
m, n = eval(input("Enter size of the matrix: "))
matrix = np.random.randint(0, 100, size=(m, n))
print("Matrix:\n", matrix)
transpose_matrix = np.transpose(matrix)
print("Transpose Matrix:\n", transpose_matrix)
