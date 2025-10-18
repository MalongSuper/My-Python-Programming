# Linear Equations using Vandermonde Matrix
# Given a data set of points (xi, yi) and polynomial P(x)
# Has a form: a0 + (a1 * x) + (a2 * x^2) + ... + (an * x^n)
# The task is to solve a0, a1, a2, ..., an
import numpy as np


def gauss_elimination(p):  # Matrix a and vector b
    # Time complexity when eliminate O(n^3/3), replace O(n^2/2)
    a, b = vandermonde_matrix(p)  # Use Vandermonde matrix
    n = len(b)
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


def vandermonde_matrix(p):
    matrix = []
    n = len(p)
    for i in range(n):
        for j in range(n):
            entry = pow(p[i][0], j)  # Get the xi elements, power by each j
            matrix.append(entry)
    mat_v = np.array(matrix).reshape(n, n)  # Get Vandermonde matrix
    vect_b = np.array([p[i][1] for i in range(n)])  # Get vector b
    return mat_v, vect_b


def main():
    print("Linear Equations (Vandermonde Matrix)")
    number = int(input("Enter number of points: "))
    xy = []
    for n in range(number):
        xi, yi = eval(input(f"Enter (x{n}, y{n}): "))
        xy.append([xi, yi])
    points = np.array(xy, dtype=float)
    solution = gauss_elimination(points)
    print("x =", solution)


main()
