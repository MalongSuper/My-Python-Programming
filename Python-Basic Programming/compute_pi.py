# This program computes pi by the given series
print("The Pi value table")
Pi = 0
# The value is from 10000 to 100000, add 10000 each
print("i\t\t\t\t\tPi")
for m in range(10000, 100001, 10000):
    # Initial Pi
    Pi = 0
    # Using the formula with i as the value
    for i in range(1, m + 1):
        Pi += ((-1) ** (i + 1)) / (2 * i - 1)
    # Multiply to 4
    Pi *= 4
    # Display the result
    print(f'{m}\t\t\t{Pi}')
