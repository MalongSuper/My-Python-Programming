# Solve the Initial Value Problem - IVP
import numpy as np
from scipy.integrate import solve_ivp

# Sample: np.exp(-1); x_init = 0, y_init = -1, x_stop = 1
f = input("Enter equation f(x): ")
f_lambda = eval(f"lambda x, y: {f}")
x_init = float(input("Enter initial x: "))
y, v = eval(input("Enter initial y and initial y': "))
y_init = np.array([y, v])
x_stop = float(input("Enter stopping x: "))
h = 0.1
# Assign the coefficients to use solve_ivp
x_span = (x_init, x_stop)  # Similar to x_init and x_stop
x_eval = np.arange(x_init, x_stop + h, h)  # Step size of xi
# RK45: Adaptive Runge Kutta Method
sol = solve_ivp(fun=f_lambda, t_span=x_span, y0=y_init, method='RK45', t_eval=x_eval)
# Note: The approximate y is stored in the matrix y the first column y[0]
# The remaining columns store the approximate solution of the derivative of every order of y
X, Y = sol.t, sol.y[0]
print("X =", X, "\nY =", Y)
