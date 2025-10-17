# This program displays prime numbers that are less than 10000
def is_prime(number):
    # Determine prime number
    for prime in range(1, 10001):
        divisor = 2
        while divisor <= number / 2:
            if number % divisor == 0:
                # If true, number is not prime
                return False  # Not a prime number
            divisor += 1

        return True  # Prime number


def print_prime_numbers(number_of_primes):
    number_per_line = 10  # Display 10 per line
    count = 0  # Count the number of prime numbers
    number = 2  # A number to be tested for primeness

    # Repeatedly find prime numbers
    while count < number_of_primes:
        # Print the prime number and increase the count
        if is_prime(number):
            count += 1  # Increase the count
            # Display the table
            print(format(number, '5d'), end=" ")
            if count % number_per_line == 0:
                # Print the number and advance to the new line
                print()

        # Check if the next number is prime
        number += 1


def main():  # Define main function
    number = 1229  # The number of prime numbers that are less than 10000
    print("\t\t\t\tPrime Number less than 10000")
    print("------------------------------------------------------------")
    print_prime_numbers(number)


# Display the result
main()
