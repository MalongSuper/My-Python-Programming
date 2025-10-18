# Calculate Dot Product manually
import numpy as np

print("Dot Product of two matrices (by hand)")
m, p1 = map(int, input("Enter size of Matrix 1: ").split(','))
p2, n = map(int, input("Enter size of Matrix 2: ").split(','))
# In order to compute the dot product of two matrices,
# the number of columns in matrix A must be equal
# to the number of rows in matrix B
if p1 != p2:
    print(f"Cannot compute Dot Product since the shape is invalid: "
          f"({m}, {p1}) and ({p2}, {n})")
else:
    matrix1 = np.random.randint(1, 100, (m, p1))
    matrix2 = np.random.randint(1, 100, (p2, n))
    # Display the matrices
    print("Matrix 1:\n", matrix1)
    print("Matrix 2:\n", matrix2)
    # Get the row of matrix 1 x col of matrix 2 -> The shape of the result matrix
    result_matrix = np.zeros((matrix1.shape[0], matrix2.shape[1]))
    # Find the dot product
    for i in range(len(matrix1)):  # Iterate through each row of matrix 1
        temp = []  # Temporary list to store products for this element (i,j)
        for j in range(len(matrix2[i])):  # Iterate through each column of matrix2
            for k in range(len(matrix2)):  # Iterate through each element in the row of matrix1 and column of matrix2
                # Multiply the ith row element of matrix1 with the corresponding kth row, jth column element of matrix2
                temp.append(matrix1[i][k] * matrix2[:, j][k])
                if k == len(matrix2) - 1:
                    # Sum the products to get the (i, j)th element of the result matrix
                    result_matrix[i][j] = sum(temp)
                    temp = []
    # Print the manually computed result matrix
    print("Result Matrix:\n", result_matrix)
    # Check with np.dot()
    print("Result Matrix with np.dot():\n", np.dot(matrix1, matrix2))
    # Check if the results are the same
    print("The same result?", np.array_equal(result_matrix, np.dot(matrix1, matrix2)))
