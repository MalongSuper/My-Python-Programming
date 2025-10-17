# This program finds the prime factors of an integer
from math import sqrt
print('Find the prime factors of an integer')
Number = int(input("Enter an integer: "))
if Number <= 1:
    print("The prime factors are not found")
else:
    print("The prime factors: ", end="")
    for Factor in range(2, Number + 1):
        isPrime = True   # Checks if the current number is prime
        # Use distance between 2 and sqrt(n) to find prime numbers
        for Prime in range(2, int(sqrt(Factor)) + 1):
            if (Factor % Prime) == 0:
                # If true, the number is not prime
                isPrime = False
                break
        # If the first number is prime and is divided to the input number
        if isPrime and (Number % Factor) == 0:
            # Use a loop to divide the number
            while (Number % Factor) == 0:
                # Display the numbers that are prime factors (can be repeated)
                print(Factor, end=" ")
                # Continue the loop until it can no longer divide
                Number //= Factor
