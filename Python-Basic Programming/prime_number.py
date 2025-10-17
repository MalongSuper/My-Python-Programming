# This program checks if a number is prime
print("Prime Number")
number = int(input("Enter a number: "))
is_prime = True  # Assume the number is prime

# Check for prime number
if number < 0:  # Negative numbers are not prime
    is_prime = False
elif number == 0 or number == 1: # Number 0 and 1 are not prime
    is_prime = False
elif number == 2:  # Number 2 is prime
    is_prime = True
else:
    # Check for factor
    for i in range(2, number):
        if (number % i) == 0:  # If a factor is encountered
            is_prime = False
            break

# Display the result
if is_prime:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
    