# Create a Matrix and sort the elements
# Based on the order of the flattened array
import numpy as np
print("Sort Flattened Matrix")
m, n = eval(input("Enter size of the matrix: "))
matrix = np.random.randint(0, 100, size=(m, n))
print("Matrix:\n", matrix)
# Flatten matrix to array
# Sort the array then reshape it to the original matrix
array = np.sort(matrix.flatten()).reshape(m, n)
print("Sorted Flattened Matrix:\n", array)
