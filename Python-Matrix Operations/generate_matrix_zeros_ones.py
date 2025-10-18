# Create matrix with 0s and 1s
import numpy as np
print("Matrix with 0s and 1s")
m, n = eval(input("Enter size of the matrix: "))
ones_array = np.ones((m, n))
zeros_array = np.zeros((m, n))
print("Matrix Ones:\n", ones_array)
print("Matrix Zeros:\n", zeros_array)
