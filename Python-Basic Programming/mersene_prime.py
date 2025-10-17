# This program displays all Mersenne primes
def is_prime(number):  # Define function for prime numbers
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            # If true, number is not prime
            return False  # Not a prime number
        divisor += 1
    return True  # Prime number


def mersenne_prime(number):  # Define function for Mersenne Prime
    number_list = []
    if is_prime(number) is True:
        number_list.append(number)
        for p in number_list:
            n = (2 ** p) - 1
            if is_prime(p):
                print(f'{p}\t\t\t{n}')


def main():  # Define the main function
    print("Mersenne Prime")
    print("p\t\t(2 ** p) - 1")
    for n in range(2, 501):  # Display the prime numbers that are less than 500
        if mersenne_prime(n):
            print(n)


# Display the result
main()
