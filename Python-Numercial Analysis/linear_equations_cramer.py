# Linear Equations using determinant method (Cramer's Rule)
import numpy as np
from numpy.linalg import det


def cramer_rule(a, b):
    n = len(a)
    det_list = []
    init_a = a.copy()  # Copy matrix A
    for i in range(0, n):
        a = init_a.copy()  # Copy the initial matrix A
        for j in range(0, n):
            a[j][i] = b[j]
            # Get the value in column
            col = a[:, i]
            # If elements in col is equal to vector b
            if np.array_equal(col, b):
                # Get the satisfied matrix and calculate its determinant
                determinant = det(a)
                det_list.append(determinant)  # Store the determinant
                a = init_a  # Return to the initial matrix A
    # Calculate the determinant of matrix A
    det_a = det(init_a)
    # Calculate x = det_subA / det_A
    for k in range(len(det_list)):
        x = det_list[k] / det_a
        print(f"x{k}: {x}")  # Display the results


def main():
    print("Linear Equations (Gauss Elimination)")
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
    cramer_rule(matrix_a, vector_b)


main()
