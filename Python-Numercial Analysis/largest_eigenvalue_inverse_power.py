# Find the smallest eigenvalue of a matrix
# Using inverse power method
import numpy as np


def normalize(x):  # Vector x
    # Take the maximum absolute value out of vector
    lamb = x[abs(x).argmax()]  # argmax() returns index
    # scale by coefficient
    x_normal = x / lamb
    return lamb, x_normal


def inverse_power_method(matrix_a, x_init, iterations=50, tol=1.0e-16):
    # Basically, similar to power method
    global lamb
    A = np.linalg.inv(matrix_a)
    x = x_init
    lamb_old = 0.0
    for i in range(iterations):
        x = np.dot(A, x)
        lamb, x = normalize(x)
        # Display each iteration
        print(i + 1, lamb, x)
        if abs(lamb_old - lamb) < tol:  # Check for convergence
            break
        lamb_old = lamb
    # Return eigenvalue, eigenvector
    return lamb, x


def main():
    print("Smallest Eigenvalue (Inverse Power Method)")
    n = int(input("Enter size: "))
    matrix = np.random.randint(0, 10, size=(n, n))
    x = np.random.randint(0, 2, size=n)
    print("Matrix:\n", matrix)
    print("Vector:", x)
    eigenvalue, eigenvector = inverse_power_method(matrix, x)
    print("Smallest Eigenvalue:", eigenvalue)
    print("Eigenvector:", eigenvector)


main()
