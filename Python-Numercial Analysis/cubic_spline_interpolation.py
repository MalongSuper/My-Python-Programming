# Find natural cubic splines passing through points
# With n points, there are (n - 1) natural cubic splines
# There are 4 * (n - 1) equations
# In this case, there are 2 natural cubic splines passing through 3 points
# => 8 linear equations
import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

print("Cubic Spline Interpolation")
x0, x1, x2 = eval(input("Enter three points coordinate-x: "))
y0, y1, y2 = eval(input("Enter three points coordinate-y: "))
x = np.array([x0, x1, x2])
y = np.array([y0, y1, y2])
# Calculate the linear equation and display equations
f = CubicSpline(x, y, bc_type='natural')
x_co = float(input("Enter x for f(x): "))
print("y =", f(x_co))
# Each cubic spline connects 2 points x[i] and x[i + 1]
# as f_i(x) = a_i(x - x[i])^3 + b_i(x - x[i])^2 + c_i(x - x[i]) + d[i]
# using this method, d[i] is y[i]
# The result of Cubic Spline Interpolation is a PPoly with two attributes:
# Cubic: Matrix; # x: x value in ascending order
m = x.shape[0] - 1  # Number of curves, clusters, segments
for i in range(m):
    print(f"Coefficients {i}: \n", f.c[:, i])
# Draw the Cubic Spline
x_new = np.linspace(0, 2, 100)
y_new = f(x_new)
plt.figure(figsize=(10, 8))
plt.plot(x_new, y_new, 'b')
plt.plot(x, y, 'ro')
plt.title("Cubic Spline Interpolation")
plt.xlabel('x')
plt.ylabel('y')
plt.show()
