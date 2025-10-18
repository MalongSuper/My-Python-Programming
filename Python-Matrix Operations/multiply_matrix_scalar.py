# Multiply Matrix A with k values
# B = k x A
# The value are inputted by the user
import numpy as np
A_Matrix = []
print("Multiply k values with Matrix")
# Size m x n = Size Row x Column
m, n = map(int, input("Enter size n x n of Matrix A: ").split("x"))
k = int(input("Enter k: "))
for i in range(m):
    print(f"Row {i + 1}")
    for j in range(n):
        p = float(input(f"Enter value for column {j + 1}: "))
        A_Matrix.append(int(p))
# Display the matrices
A = np.array(A_Matrix).reshape(m, n)
B = k * A
print(f"Matrix A\n{A}")
print(f"Matrix B\n{B}")
