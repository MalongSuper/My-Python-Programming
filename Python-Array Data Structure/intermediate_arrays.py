# Intermediate Array
import numpy as np

A = np.arange(1, 17, 1).reshape(4, 4)
print("A:\n", A)
# Use A[i, j] and A[i][j] to see the difference
# Return only one element, same results
print("A[1, 2] =", A[1, 2])
print("A[1][2] =", A[1][2])
# Consider these cases
print("Col 2:\n", A[:, 2])  # Return column 2
print("Row 2:\n", A[:][2])  # Return row 2
print("All of rows:\n", A[:])  # Return all rows

# Return B with row 1, 2, 3; then take row 1
print("Row 1:\n", A[1:4][0])
# Return B with row 3, 1, 2; then take row 1
print("Row 3:\n", A[[3, 1, 2]][0])
# Return discontinuous row 0, 2, 3
print("Row 0, 2, 3:\n", A[[0, 2, 3], :])
# Return discontinuous column 0, 2, 3
print("Col 0, 2, 3:\n", A[:, [0, 2, 3]])
# Use tuple
print("A[(1, 3)]:", A[(1, 3)])

# Get the intersecting elements of row 1, 2 and col 1, 2, 3
print("Rows 1, 2 & Cols 1, 2, 3:\n", A[1:3, 1:4])
# Get the elements A[1, 0] and A[3, 1]
print("A[1, 0] and A[3, 1]:\n", A[[1, 0], [3, 1]])  # Or A[(1, 0), (3, 1)]
# Get the intersecting elements in the corner  of row 0, 2, 3 and col 1, 3
print("Rows 0, 2, 3 & Cols 1, 3:\n", A[[0, 2, 3]][:, [1, 3]])
