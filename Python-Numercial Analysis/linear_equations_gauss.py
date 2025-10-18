# Linear Equations using Gauss Elimination
import numpy as np


def gauss_elimination(mat_a, vect_b):  # Matrix a and vector b
    # Time complexity when eliminate O(n^3/3), replace O(n^2/2)
    n = len(vect_b)
    a = mat_a.copy()
    b = vect_b.copy()
    # Elimination phase
    for i in range(0, n - 1):  # i is pivot
        for j in range(i + 1, n):  # j are rows below column "i" need to eliminate col i
            if a[j, i] != 0.0:
                # Define lambda to eliminate
                lamb = a[j, i] / a[i, i]
                # Calculate new row of the matrix using slicing
                a[j, i: n] = a[j, i: n] - lamb * a[i, i: n]
                # Update vector b
                b[j] = b[j] - lamb * b[i]
    # Backward substitution
    for i in range(n - 1, -1, -1):
        b[i] = (b[i] - np.dot(a[i, i + 1: n], b[i + 1: n])) / a[i, i]
    # Return the solution (vector b)
    return b


def main():
    print("Linear Equations (Gauss Elimination Method)")
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
    # Compute and display the result
    x = gauss_elimination(matrix_a, vector_b)
    print("Result:")
    for result in x:
        print(round(result, 2), end=" ")


main()
