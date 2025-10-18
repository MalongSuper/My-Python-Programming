# Create a Matrix and sort the elements in the rows and columns
import numpy as np
print("Sort Rows and Columns Matrix")
m, n = eval(input("Enter size of the matrix: "))
matrix = np.random.randint(0, 100, size=(m, n))
print("Matrix:\n", matrix)
# Sort the element in rows and columns
sorted_col = np.sort(matrix, axis=0)
sorted_row = np.sort(matrix, axis=1)
print("Columns Matrix:\n", sorted_col)
print("Rows Matrix:\n", sorted_row)
