# This program multiply matrix A, B with the sane size n x n
# The value are inputted by the user
import numpy as np
A_Matrix = []
B_Matrix = []
print("Multiply two matrices A and B")
n = int(input("Enter size n x n of Matrix A and B: "))
print("Matrix A")
for iA in range(n):
    row = []
    print(f"Row {iA + 1}")
    for jA in range(n):
        pA = float(input(f"Enter value for column {jA + 1}: "))
        row.append(int(pA))
    A_Matrix.append(row)
print("Matrix B")
for iB in range(n):
    row = []
    print(f"Hàng {iB + 1}")
    for jB in range(n):
        pB = float(input(f"Enter value for column {jB + 1}: "))
        row.append(int(pB))
    B_Matrix.append(row)
# Create matrixes and display the result
A = np.array(A_Matrix)
B = np.array(B_Matrix)
C = np.dot(A, B)
print(f"Matrix A\n{A}")
print(f"Matrix B\n{B}")
print(f"Matrix C\n{C}")
