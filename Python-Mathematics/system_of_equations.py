# This program soles system of equations
# Direct solution
import numpy as np

print("System of Linear Equations (LU)")
# Input number of unknowns and initialize matrix and vector
n = int(input("Enter number of unknowns: "))
matrix_a = np.zeros((n, n))
constants_list, vector_b = [], np.zeros(n)
for i in range(n):
    # Input coefficients
    coefficients = input(f"+ Enter coefficients of row {i + 1} (separated by coma): ").split(",")
    # Add the values to array (matrix row) to create a matrix
    matrix_a[i] = np.array([float(num) for num in coefficients])
    # Input constants
    constants = float(input(f"+ Enter constants of row {i + 1}: "))
    constants_list.append(constants)  # Append input constant to the list
    # then convert it to array
    vector_b = np.array(constants_list)
# Solve for x
x = np.linalg.solve(matrix_a, vector_b)
for i in range(len(x)):
    print(f"x{i + 1} =", x[i])
