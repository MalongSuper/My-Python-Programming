# Combination in Mathematics
from math import factorial
print("Combination")
try:
    n = int(input("Enter n: "))
    k = int(input("Enter k: "))
    C = factorial(n) // (factorial(k) * factorial(n - k))
except ValueError as v:
    print("Error:", v)
else:
    print(f"C({n}, {k}) = {C}")
