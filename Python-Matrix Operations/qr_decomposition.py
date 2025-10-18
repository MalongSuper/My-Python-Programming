# This program performs QR Decomposition with NumPy
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
Q, R = np.linalg.qr(matrix)
print("Q:\n", Q)
print("R:\n", R)
print("QR:\n", np.dot(Q, R))
