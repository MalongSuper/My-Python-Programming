# Probability and Statistics problem
# Knowing the probability for one trial is p
# Given selecting n elements, find the minimum number of elements
# So that the probability of selecting at least 1 element that
# satisfies a condition is better than M (user's input)
from math import factorial
print("Maximum Probability")
maximum = float(input("Enter maximum probability M: "))
if maximum > 1 or maximum < 0:
    print("Error: Invalid Input")
else:
    p = float(input("Enter probability of one trial p: "))
    n = 1  # Initialize n
    # We have P(X ≥ 1) is the probability of at least 1 satisfied element
    # Solve this by trying n then find P(X ≥ 1) with that n
    # Using Bernoulli
    while True:
        res = 0  # Initial result
        for k in range(1, n):
            C = factorial(n) // (factorial(k) * factorial(n - k))
            P = C * (p ** k) * ((1 - p) ** (n - k))
            res += P
        if res >= maximum:
            print("The maximum probability is reached when:")
            print(f"n = {n} => P(X ≥ 1) = {res}")
            break
        n += 1
