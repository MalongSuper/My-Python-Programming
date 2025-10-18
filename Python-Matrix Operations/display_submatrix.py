# This program takes a sub matrix from original matrix
import numpy as np

# Generate a matrix from 1 to 100
numbers = np.arange(0, 100)
matrix = np.reshape(numbers, (10, 10))
print('Original Matrix:')
print(matrix)

# Divide the matrix into four square sub matrices
rows, cols = matrix.shape
half_rows = rows // 2
half_cols = cols // 2

parts = int(input("Select the block you want to display: "))
if parts == 1:
    print("Sub Matrix:")
    top_left_part = matrix[:half_rows, :half_cols]
    print(top_left_part)
elif parts == 2:
    print("Sub Matrix:")
    top_right_part = matrix[:half_rows, half_cols:]
    print(top_right_part)
elif parts == 3:
    print("Sub Matrix:")
    bottom_left_part = matrix[half_rows:, :half_cols]
    print(bottom_left_part)
elif parts == 4:
    print("Sub Matrix:")
    bottom_right_part = matrix[half_rows:, half_cols:]
    print(bottom_right_part)
else:
    print("Error: Out of Range")
