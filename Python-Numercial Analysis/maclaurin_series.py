# This program solves e^x using Maclaurin Series
# Calculate true value
import math
# Maclaurin Series for e^x = 1 + (x/1!) + (x^2+2!) + (x^3+3!) + ... + + (x^n+n!)
x = 0.5
true_value = math.exp(x)  # True Value
n = 3  # number of significant figures (the number is optional)
# Calculate the stopping criterion (Es)
Es = 0.5 * 10 ** (2 - n)
print(f"True Value = {true_value}")
print(f"Epsilon S = {Es}")
print("Term\tPresent Value\tTrue Error\tApproximate Error")
present_value = 1  # Present Value starts at 1
for i in range(1, 100):  # Use a maximum number to avoid infinite loops
    previous_value = present_value
    present_value = present_value + (x ** i) / math.factorial(i)
    # True Error
    Et = abs((true_value - present_value) / true_value) * 100
    # Approximate Error
    Ea = abs((present_value - previous_value) / present_value) * 100
    # Display the results
    print("{:d}\t\t{:0.3f}\t\t\t{:0.2f} %\t\t{:0.2f} %".
          format(i, present_value, Et, Ea))
    # If Ea is lower than Es
    if Ea < Es:
        break
# Display the result
print(f"e^{x} = {present_value}")
