# Linear Equations using inverse matrix method
import numpy as np
from numpy.linalg import det


def cofactor_method(mat_a):
    # Apply cofactor method to find the inverse matrix
    # Formula: A^-1 = (1 / det(A)) * PA
    n = len(mat_a)
    cofactors = []  # Store the cofactors
    # Find the adjugate matrix by finding the cofactors
    # Formula: Aij = (-1)^(i + j) * det(Mij)
    # Mij: matrix obtained from matrix A by removing row i, column j
    for i in range(1, n + 1):  # Iterate each element in the matrix
        for j in range(1, n + 1):
            M = np.delete(mat_a, i - 1, 0)  # Remove row
            M = np.delete(M, j - 1, 1)  # Remove column
            A = ((-1) ** (i + j)) * det(M)
            cofactors.append(round(A))  # Append the cofactors
    # Transpose to get the adjugate matrix
    cofactors = np.array(cofactors).reshape(n, n)
    adjugate_mat_a = np.transpose(cofactors)
    det_a = round(det(mat_a))
    if det_a == 0:  # det(A) ≠ 0
        print("Determinant is 0. Non-invertible matrix")
        return None
    else:
        inverse_matrix = (1 / det_a) * adjugate_mat_a
        return inverse_matrix


def solve_equations(mat_a, b):
    # Formula X = A^-1 * B
    inverse_a = cofactor_method(mat_a)
    X = np.dot(inverse_a, b)
    for i in X:
        print(f"{i}")  # Display the results


def main():
    print("Linear Equations (Inverse Matrix Method)")
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
    # Use the determinant method
    print("Result:")
    solve_equations(matrix_a, vector_b)


main()
