# Find eigenvalues and eigenvectors of a matrix
import numpy as np

size = int(input("Enter size of the matrix: "))
values = []  # Array to store values
for i in range(size):
    print(f"Row {i + 1}")
    for j in range(size):
        val = int(input(f"Enter value in column {j + 1}: "))
        values.append(val)

matrix = np.array(values).reshape(size, size)
# Calculate eigenvalues and eigenvectors
eig_val, eig_vec = np.linalg.eig(matrix)
print("Eigenvalues: ", eig_val)
print("Eigenvectors:", eig_vec)
