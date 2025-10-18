# The Gauss-Seidel method
# We only use this algorithm to solve every system of equations
# with three constants
# This algorithm might be inconsistent
import numpy as np


# Recompute the new values for the vector x after each iteration
def iterative_equations(mat_a, vector_b, vector_x):
    x1 = (vector_b[0] - mat_a[0][1] * vector_x[1] - mat_a[0][2] * vector_x[2]) / mat_a[0][0]
    x2 = (vector_b[1] - mat_a[1][0] * x1 - mat_a[1][2] * vector_x[2]) / mat_a[1][1]
    x3 = (vector_b[2] - mat_a[2][0] * x1 - mat_a[2][1] * x2) / mat_a[2][2]
    return np.array([x1, x2, x3])


def gauss_seidel(mat_a, vect_b, initial_x, num_iters, tolerance):
    x = []
    old_x = initial_x
    converged = False
    print('{:<5}{:<25}{:<25}{:<25}'.format('', 'x1', 'x2', 'x3'))

    for k in range(num_iters):
        x = iterative_equations(mat_a, vect_b, old_x)
        # Compare the difference between two closest calculation of x
        dx = np.sqrt(np.dot(x - old_x, x - old_x))
        print('{:<5}{:<25}{:<25}{:<25}'.format(k, x[0], x[1], x[2]))
        if dx < tolerance:
            converged = True
            print("The algorithm has converged")
            break
        old_x = x

    if not converged:
        print("The algorithm has not converged, consider increasing the number of iterations")

    return x


def main():
    print("Linear Equations (Gauss Seidel))")
    n = 3
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

    initial_x = np.array([0.0, 0.0, 0.0])
    x = gauss_seidel(matrix_a, vector_b, initial_x, num_iters=50, tolerance=0.001)
    print("x:", x)


main()
