# This program finds Rank of a matrix
# First, converts a matrix to its row echelon form
import sympy as sp
import numpy as np
print("Rank of Matrix")
n = int(input("Enter size of matrix: "))
matrix = np.random.randint(0, 10, size=(n, n))
print("Matrix:\n", matrix)
# Convert the numpy matrix to sympy
matrix = sp.Matrix(matrix)
matrix_rref = matrix.rref()  # Change to RREF
# Convert it to numpy for displaying
echelon_matrix = np.matrix(matrix_rref[0])
print("RREF:\n", echelon_matrix)
print("Rank:", matrix_rref[1][2] + 1)
