# Jacobi Method for System of Linear Equations
import numpy as np


def jacobi(mat_a, vect_b, initial_x, num_iters, tolerance):
    x = initial_x
    converged = False

    print('{:<5}{:<25}{:<25}{:<25}'.format('', 'x1', 'x2', 'x3'))

    for k in range(num_iters):
        new_x = np.zeros_like(x, dtype=float)

        new_x[0] = (vect_b[0] - mat_a[0][1] * x[1] - mat_a[0][2] * x[2]) / mat_a[0][0]
        new_x[1] = (vect_b[1] - mat_a[1][0] * x[0] - mat_a[1][2] * x[2]) / mat_a[1][1]
        new_x[2] = (vect_b[2] - mat_a[2][0] * x[0] - mat_a[2][1] * x[1]) / mat_a[2][2]

        dx = np.sqrt(np.dot(new_x - x, new_x - x))

        print('{:<5}{:<25}{:<25}{:<25}'.format(k + 1, new_x[0],
                                               new_x[1], new_x[2]))

        if dx < tolerance:
            converged = True
            print("The algorithm has converged")
            x = new_x
            break

        x = new_x

    if not converged:
        print("The algorithm has not converged, consider increasing the number of iterations")

    return x


def main():
    print("Linear Equations (Jacobi Method)")
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
    x = jacobi(matrix_a, vector_b, initial_x, num_iters=50, tolerance=0.001)
    print("x:", x)


main()
