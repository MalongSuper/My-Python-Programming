# This program displays prime numbers between 2 and 1,000
# Assume these for lines of the table
from math import sqrt
Number_per_Line = 10
Count = 0
print("\t\t\t\tPrime Number Table")
print("---------------------------------------------------")
# Display the table
for Number in range(2, 1001):
    isPrime = True   # Checks if the current number is prime
    # Use distance between 2 and sqrt(n) to find prime numbers
    for Prime in range(2, int(sqrt(Number)) + 1):
        if (Number % Prime) == 0:
            # If true, the number is not prime
            isPrime = False
            break  # Exit the for loop
    # If number is prime, display the prime number and increase the count
    if isPrime:
        print(format(Number, '4d'), end=" ")
        Count += 1
        if (Count % Number_per_Line) == 0:
            print()
