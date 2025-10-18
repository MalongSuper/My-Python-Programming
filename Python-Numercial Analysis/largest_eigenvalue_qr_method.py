# Find the largest eigenvalue of a matrix
# Using QRr method
import numpy as np


def qr_method(matrix_a, iterations=10):
    A = matrix_a
    for i in range(iterations):
        Q, R = np.linalg.qr(A)
        A = np.dot(R, Q)
    # Return the upper triangular matrix
    # The diagonal entries are the eigenvalues
    return np.diagonal(A)


def main():
    print("Largest Eigenvalue (QR Method)")
    n = int(input("Enter size: "))
    matrix = np.random.randint(0, 10, size=(n, n))
    x = np.random.randint(0, 2, size=n)
    print("Matrix:\n", matrix)
    print("Vector:", x)
    lamb = qr_method(matrix)
    print("Eigenvalues:", lamb)


main()
