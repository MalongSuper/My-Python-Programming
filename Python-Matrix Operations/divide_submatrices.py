# This program reorganizes the matrix after dividing its sub matrices
import numpy as np

# Generate a matrix from 1 to 100
numbers = np.arange(0, 100)
matrix = np.reshape(numbers, (10, 10))
print("Original Matrix:\n", matrix)

# Divide the matrix into four square sub matrices
rows, cols = matrix.shape
half_rows = rows // 2
half_cols = cols // 2
top_left_part = matrix[:half_rows, :half_cols]
top_right_part = matrix[:half_rows, half_cols:]
bottom_left_part = matrix[half_rows:, :half_cols]
bottom_right_part = matrix[half_rows:, half_cols:]

# All sub matrices in a list
sub_matrices = [top_left_part, top_right_part, bottom_left_part, bottom_right_part]

# Shuffle them randomly
np.random.shuffle(sub_matrices)

# Combine them to create a new matrix
new_matrix = np.vstack((np.hstack((sub_matrices[0], sub_matrices[1])),
                        np.hstack((sub_matrices[2], sub_matrices[3]))))

print("New Matrix:\n", new_matrix)
