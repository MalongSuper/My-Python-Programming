# Integral of a function, using scipy
# Input a function
import numpy as np
import scipy as sp

a, b = eval(input("Enter range [a, b]: "))  # Input "np.pi"
n = 100
x = np.linspace(a, b, n)
# Input equation example "np.sin(x)"
f = input("Enter equation f(x): ")
i_trapezoid = sp.integrate.trapezoid(eval(f), x)
print("Integral with Trapezoid Rule:", i_trapezoid)

# Convert to lambda for quadrature integration
f_lambda = eval(f"lambda x: {f}")
i_quadrature = sp.integrate.quad(f_lambda, a, b)
print("Integral with Gauss Quadrature:", i_quadrature[0], "; Error:", i_quadrature[1])
