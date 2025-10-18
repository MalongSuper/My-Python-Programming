# Prime Factorization Method for Greatest Common Divisor
# For three integers
from math import sqrt


def prime_factors(n):  # Find all the prime factors of the numbers
    factors = []
    for i in range(2, n + 1):
        isPrime = True  # reset here
        for p in range(2, int(sqrt(i)) + 1):
            if i % p == 0:
                # If true, the number is not prime
                isPrime = False
                break
        # If the first number is prime and is divided to the input number
        if isPrime and (n % i) == 0:
            # Use a loop to divide the number
            while (n % i) == 0:
                # Display the numbers that are prime factors (can be repeated)
                factors.append(i)
                # Continue the loop until it can no longer divide
                n //= i
    return factors


print("Greatest Common Divisor - Prime Factorization Method")
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))
# Find all similar prime factors, including duplicate
pa, pb, pc = prime_factors(a), prime_factors(b), prime_factors(c)
# Return as a list
print("Prime Factors of", a, "are", pa)
print("Prime Factors of", b, "are", pb)
print("Prime Factors of", c, "are", pc)
# Step 1: Find the factors that are common in both lists
# By intersection
common_factors = list(set(pa) & set(pb) & set(pc))
print("Common Factors", common_factors)
# Step 2: Find the occurrence of each of the common factors
# In both lists, and then takes the minimum one
# Use the values to power the common factors
gcd = 1
for c in common_factors:
    gcd *= c ** min(pa.count(c), pb.count(c), pc.count(c))

print("GCD is", gcd)
