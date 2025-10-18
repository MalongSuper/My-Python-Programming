# Calculate the derivative
# by cubic spline interpolation
import numpy as np
import scipy as sp

print("Derivative using Cubic Spline Interpolation")
n = int(input("Enter the size of x and f(x): "))
x = np.random.uniform(0, 3, size=n)  # Random float array
fx = np.random.uniform(0, 3, size=n)
# Round to four decimal piece
x = np.round(x, 4)
fx = np.round(fx, 4)
print("x", x)
print("fx", fx)
# Cubic Spline
s = sp.interpolate.CubicSpline(x, fx, bc_type="natural")
print("s.x =", s.x)
print("Polynomial coefficient of cubic spline (in columns)")
print("Coefficients =\n", s.c)
m = x.shape[0] - 1  # Number of cubic, segment, curves
for i in range(m):
    print(f"Coefficients of S{i} =", s.c[:, i])
# Calculate f'(x) and f"(x)
s_d1 = s.derivative()
s_d2 = s.derivative(2)
x_value = float(input("Enter value: "))
print(f"f'({x_value}) =", s_d1(x_value))
print(f"f''({x_value}) =", s_d2(x_value))
