# Langrange polynomial interpolation method
# Find a unique nth degree polynomial [curve] passing through (n + 1) distinct points
# Problem given n points (x, y)
# find coefficients "a" of polynomial of degree (n - 1) through all (x, y)
import numpy as np
import numpy.polynomial.polynomial as polynomial
import matplotlib.pyplot as plt
# Coordination with three points
# a = (x0, y0); b = (x1, y1); c = (x2, y2)
print("Langrange Polynomial Interpolation")
x0, x1, x2 = eval(input("Enter three points coordinate-x: "))
y0, y1, y2 = eval(input("Enter three points coordinate-y: "))
x = [x0, x1, x2]
y = [y0, y1, y2]
# Coefficients of L(x) from 0 to 2
L0_coefficients = [1, -1.5, 0.5]
L1_coefficients = [0, 2, -1]
L2_coefficients = [0, -0.5, 0.5]
# Compute L0, L1, L2
L0 = polynomial.Polynomial(L0_coefficients)
L1 = polynomial.Polynomial(L1_coefficients)
L2 = polynomial.Polynomial(L2_coefficients)
# P(x)
P = (y0 * L0) + (y1 * L1) + (y2 * L2)
# Draw a plot
x_new = np.arange(-1.0, 3.1, 0.1)
fig = plt.figure(figsize=(10, 8))
plt.plot(x_new, P(x_new), 'b', x, y, 'ro')
title = f"Langrange Polynomial P(x) = {P}"
plt.title(title)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
