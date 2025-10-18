# Arrangement in Mathematics
from math import factorial
print("Arrangement")
try:
    n = int(input("Enter n: "))
    k = int(input("Enter k: "))
    A = factorial(n) // factorial(n - k)
except ValueError as v:
    print("Error:", v)
else:
    print(f"A({n}, {k}) = {A}")
