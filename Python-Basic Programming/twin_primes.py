# This program displays twin prime numbers
def is_prime(number):  # Define function for prime numbers
    for prime in range(1, 10001):
        divisor = 2
        while divisor <= number / 2:
            if number % divisor == 0:
                # If true, number is not prime
                return False  # Not a prime number
            divisor += 1
        return True  # Prime number


def twin_prime(number):  # Define function for Twin Primes
    number_list = []
    if is_prime(number) is True:
        number_list.append(number)
        for p1 in number_list:
            p2 = p1 + 2
            # Twin primes are pairs of prime numbers that differ by 2
            if is_prime(p2) and p2 - p1 == 2:
                return p1, p2


def main():  # Define main function
    print("Twin Primes")
    for number in range(2, 1001):  # Display twin primes that are fewer than 1000
        if twin_prime(number):
            print(twin_prime(number))


# Display the result
main()
