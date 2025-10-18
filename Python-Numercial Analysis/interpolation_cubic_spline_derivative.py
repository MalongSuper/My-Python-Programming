# Use the natural cubic spline connecting all adjacent data points.
import numpy as np
import scipy as sp


# Each cubic spline connects two points x[i] and x[i + 1]
# with the form: S_i(x) = a_i(x – x[i])^3 + b_i(x – x[i]) ^2 + c_i(x – x[i]) + d[i]
# According to this form, d[i] is y[i]
# Result are c: cubic, matrix wit coefficients, and x is sorted in increasing order
# Sample input:
# Enter x: 1.5, 1.9, 2.1, 2.4, 2.6, 3.1
# Enter f(x): 1.0628,1.3961,1.5432,1.7349,1.8423,2.0397
print("Natural Cubic Spline")
x = eval(input("Enter x: "))
fx = eval(input("Enter f(x): "))
x = np.array(x)
fx = np.array(fx)
# Cubic Spline
s = sp.interpolate.CubicSpline(x, fx, bc_type="natural")
print("s.x =", s.x)
print("Polynomial coefficient of cubic spline (in columns)")
print("Coefficients =\n", s.c)
m = x.shape[0] - 1  # Number of cubic, segment, curves
for i in range(m):
    print(f"Coefficients of S{i} =", s.c[:, i])

# Return every derivative up to order 3
print("The coefficients of each derivative polynomial of each cubic spline")
print("Derivative at level 0 =\n", s.derivative(0).c)  # Is the polynomial itself
print("Derivative at level 1 =\n", s.derivative().c)  # Default is 1 of not specified
print("Derivative at level 2 =\n", s.derivative(2).c)
print("Derivative at level 3 =\n", s.derivative(3).c)
# Calculate f'(x) and f"(x)
s_d1 = s.derivative()
s_d2 = s.derivative(2)
# Sample x = 2
x_value = float(input("Enter evaluate x: "))
print(f"f'({x_value}) =", s_d1(x_value))
print(f"f''({x_value}) =", s_d2(x_value))
