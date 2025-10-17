# This program computes approximate Euler
print("Compute Euler")
print("i\t\t\te")
# Simplify the series with nested loops
for i in range(10000, 100001, 10000):
    # Initialize e and item to be 1
    e = 1
    term = 1
    for n in range(1, i + 1):
        e += term
        term *= 1 / (n + 1)
    print(f'{i}\t\t{e}')
