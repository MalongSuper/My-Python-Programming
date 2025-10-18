# Create Square Matrix Ones then change some index to 0
import numpy as np
print("Square Matrix Ones")
n = eval(input("Enter size of matrix: "))
matrix_one = np.ones((n, n))
matrix_two = np.ones((n, n))
matrix_three = np.zeros((n, n))
# Change all the interior elements to 0
matrix_one[1:-1, 1:-1] = 0
print("Matrix A:\n", matrix_one)
# Change all the corner elements to 0
matrix_two[0, :] = 0
matrix_two[:, 0] = 0
matrix_two[-1, :] = 0
matrix_two[:, -1] = 0
print("Matrix B:\n", matrix_two)
# Create matrix with 0s and 1s alternatively
matrix_three[1::2, ::2] = 1  # Fill 1s in odd rows, even columns
matrix_three[::2, 1::2] = 1  # Fill 1s in even rows, odd columns
print("Matrix C:\n", matrix_three)
