# Draw Function Plot
import numpy as np
import matplotlib.pyplot as plt

# Input function as a string
print("Draw Plot of a Function")
function_input = input("Enter f(x): ")

# Replace e with np.e for evaluation
function_input = function_input.replace("e", str(np.e))
# Replace 'log' with 'np.log' to use numpy logarithm function
function_input = function_input.replace("log", "np.log")

# Create a lambda function from the input
f = eval("lambda x: " + function_input.replace("^", "**"))

# Define the range for x
x_values = np.linspace(-20, 20, 400)  # Start from 0.1 to avoid log(0)
y_values = f(x_values)

# Plot the function
plt.plot(x_values, y_values, label=f"f(x) = {function_input}")
plt.title(f"Function f(x) {function_input}")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid()
plt.legend()
plt.show()
