# Solve the system of non-linear equations f(x) = 0
# By Newton-Raphson with initial vector {x}
# The result {f} and {x} are vectors
import numpy as np
import sympy as sp
import math


# Swap row i and j in vector/matrix v
def swap_row(v, i, j):
    if len(v.shape) == 1:  # v is vector
        v[i], v[j] = v[j], v[i]
    else:  # v is matrix
        v[[i, j], :] = v[[j, i], :]


def swap_column(v, i, j):
    v[:, [i, j]] = v[:, [j, i]]


# tol (tolerance): true or false
def gauss_elimination_pivot(mat_a, b, tol=1.0e-12):
    n = len(b)
    # Calculating the scale factor in each row
    s = np.zeros(n)
    for i in range(n):
        s[i] = max(np.abs(mat_a[i, :]))

    for k in range(0, n - 1):
        # Find row p with maximum relative size to swap with row k
        # argmax() returns index with the maximum,
        # so we must add k to get the absolute index in matrix A
        # Only find on column k with row from k to n - 1
        p = np.argmax(np.abs(mat_a[k: n, k]) / s[k:n]) + k
        if abs(mat_a[p, k]) < tol:
            print("Singular Matrix")
        if p != k:  # choose row p as pivot
            swap_row(b, k, p)  # Swap two elements in vector b
            swap_row(s, k, p)  # Swap two elements in matrix/ vector scale factor
            swap_row(mat_a, k, p)  # Swap two elements in matrix A

        # Basic Gauss Elimination
        for i in range(k + 1, n):  # i are rows
            if mat_a[i, k] != 0:
                # Use lambda
                lamb = mat_a[i, k] / mat_a[k, k]
                # Use slicing to re-calculate the values in one row
                mat_a[i, k: n] = mat_a[i, k: n] - lamb * mat_a[k, k: n]
                b[i] = b[i] - lamb * b[k]

    # If the values is too small
    if abs(mat_a[n - 1, n - 1]) < tol:
        print("Singular Matrix")

    # Back substitution
    b[n - 1] = b[n - 1] / mat_a[n - 1, n - 1]
    for k in range(n - 2, -1, -1):
        b[k] = (b[k] - np.dot(mat_a[k, k + 1: n], b[k + 1: n])) / mat_a[k, k]

    return b


# f: array of the equations
# x: array of the approximate roots
def newton_raphson(f, x, n, tol=1.0e-9):
    def jacobian(f, x):
        h = 1.0e-4
        n = len(x)
        jacobi = np.zeros((n, n))
        f0 = f(x)
        for i in range(n):
            temp = x[i]
            x[i] = temp + h
            f1 = f(x)
            x[i] = temp
            jacobi[:, i] = (f1 - f0) / h
        return jacobi, f0

    for i in range(n):
        jacobi, f0 = jacobian(f, x)
        if math.sqrt(np.dot(f0, f0) / len(x)) < tol:
            return x
        dx = gauss_elimination_pivot(jacobi, -f0)
        x = x + dx
        if math.sqrt(np.dot(dx, dx)) < (tol * max(max(abs(x)), 1.0)):
            return x
    print("Maximum number of iterations reached but still no convergence")


def main():
    print("The system of non-linear equations with Newton-Raphson")
    # Choose an initial guess
    f1 = input("Enter the first equation: ")
    f2 = input("Enter the second equation: ")
    # Convert to sympify
    x, y = sp.symbols('x y')
    fx1 = sp.sympify(f1.replace("^", "**"))
    fx2 = sp.sympify(f2.replace("^", "**"))
    # Convert to lambda
    fx1_lambda = sp.lambdify((x, y), fx1, 'numpy')
    fx2_lambda = sp.lambdify((x, y), fx2, 'numpy')

    # Vector function
    def f(vector):
        x, y = vector
        return np.array([fx1_lambda(x, y), fx2_lambda(x, y)])

    # Initial Guess to begin the algorithm
    x0, y0 = eval(input("Enter initial guess: "))
    x = np.array([x0, y0])
    x = newton_raphson(f, x, 100)
    print("Approximation results:\nx =", x)


main()
