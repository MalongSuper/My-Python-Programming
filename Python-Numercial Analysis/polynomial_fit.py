# Polynomial Fit
import numpy as np
from numpy.linalg import lstsq
import matplotlib.pyplot as plt

# Find the best-fitting quadratic polynomial for the set of points (x, y)
print("Polynomial Fit")
x = list(map(float, input("Enter the x values: ").split(",")))
y = list(map(float, input("Enter the y values: ").split(",")))

if len(x) != len(y):
    raise ValueError("The length of x and y does not match")

# Y = AB, select f0(x) = x^2, f1(x) = x, f2(x) = 1
# Construct the matrix A with three columns
# Basic function: x^2, x^1, x^0
# The first column is the value of f0(x), the second column is f1(x)
# the third column is 1
x, y = np.array(x), np.array(y)
A = np.vstack([x ** 2, x, np.ones(len(x))]).T
Y = y.T
# Use numpy.linalg.lstsq
beta = np.linalg.lstsq(A, Y, rcond=None)[0]
# The result is from a_n, a_{n - 1}, to a0
print("Beta:", beta)

# Draw the points (x, y)
plt.scatter(x, y, marker=".")
# Draw the fitting line for f(x) =  a_2x^2 + a_1 * x + a_0
x_plot = np.linspace(0, 10, 20)
y_plot = beta[2] + beta[1] * x_plot + beta[0] * x_plot ** 2
plt.plot(x_plot, y_plot, color='red')
plt.title(f"f(x) = ({beta[2]:.3f}) + ({beta[1]:.3f}) * x + ({beta[0]:.3f}) * x^2")
plt.show()
