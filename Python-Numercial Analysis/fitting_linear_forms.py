# Fit Linear Forms: Y = AB
# f1(x); f2(x) = 1 -> f(x) = a0 * x + a1
import numpy as np

# Prepare data points
print("Fitting Linear Forms")
x = list(map(float, input("Enter the x values: ").split(",")))
y = list(map(float, input("Enter the y values: ").split(",")))

if len(x) != len(y):
    raise ValueError("The length of x and y does not match")

# Set matrix A, vector Y
A = np.array([[x[i], 1] for i in range(len(x))])
A_transpose = A.T
Y = np.array(y).T
# Compute A^T * A
Ata = np.dot(A_transpose, A)
print("A^T * A:\n", Ata)
# Compute A^T * Y
Aty = np.dot(A_transpose, Y)
print("A^T * Y:\n", Aty)
# Inverse Matrix of (At_a)^-1
inverse_Ata = np.linalg.inv(Ata)
print("(A^T * A)^-1:\n", inverse_Ata)
# Compute beta
beta = np.dot(inverse_Ata, Aty)
print("Beta:\n", beta)
