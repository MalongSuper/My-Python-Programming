# This program displays emirp numbers
def is_prime(number):  # Define function for prime numbers
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            # If true, number is not prime
            return False  # Not a prime number
        divisor += 1
    return True  # Prime number


def emirp(number):
    if is_prime(number) is True:
        original_number = number
        reverse_number = 0
        while number > 0:  # Reverse the number
            digit = number % 10
            reverse_number = (reverse_number * 10) + digit
            number = number // 10
        # The number is a emirp when its reverse is also a prime
        # Exclude the palindrome numbers
        if reverse_number != original_number and is_prime(reverse_number):
            return True


def main():  # Define main function
    count = 0
    count_number = 0
    number_per_line = 10
    print("\t\t\tNon-palindromic Prime Number (Emirp)")
    print("-------------------------------------------------------------")
    for number in range(1, 10001):  # Assume the range
        if emirp(number) is True:
            count += 1
            count_number += 1
            print(format(number, '6d'), end="")
            if (count % number_per_line) == 0:
                print()
            if count_number == 100:  # Display the first 100 numbers
                break


# Display the result
main()
