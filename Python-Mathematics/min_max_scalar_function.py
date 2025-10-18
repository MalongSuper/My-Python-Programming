# This program finds the minimize and maximize scalar for f(x)
from scipy.optimize import minimize_scalar
import warnings

# Suppress specific warnings (e.g., RuntimeWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)
# Input equation
print("Minimize and Maximize scalar for f(x)")
fx = input("Enter equation f(x): ")
fx_lambda = eval(f"lambda x: {fx}")
# Solve minimize scalar for f(x)
x_minimize = minimize_scalar(fx_lambda)
if not x_minimize.success:
    print("The equation has no minimization")
else:
    # Solve maximize scalar for f(x) by minimizing -f(x)
    x_maximize = minimize_scalar(lambda x: -fx_lambda(x))
    if not x_maximize.success:
        print("The equation has no maximization")
    else:
        # Display the result
        print(f"The function reaches its minimum "
              f"at x = {x_minimize.x}: y = {x_minimize.fun}")
        print(f"The function reaches its maximum "
              f"at x = {x_maximize.x}: y = {x_maximize.fun}")
