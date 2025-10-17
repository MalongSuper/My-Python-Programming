# This program displays prime numbers that are also palindrome numbers
def is_prime(number):  # Define function for prime numbers
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            # If true, number is not prime
            return False  # Not a prime number
        divisor += 1
    return True  # Prime number


def is_palindrome(number):
    if is_prime(number) is True:
        original_number = number  # Reserve the original number
        reverse_number = 0
        while number > 0:  # Reverse the number
            digit = number % 10
            reverse_number = (reverse_number * 10) + digit
            number = number // 10
        # The prime number is a palindrome when its reverse is the same as its original
        if reverse_number == original_number:
            return True


def main():  # Define main function
    count = 0
    count_number = 0
    number_per_line = 10
    print("\t\t\t\t\tPalindromic Prime")
    print("-------------------------------------------------------------")
    for number in range(2, 100001):  # Assume the range
        if is_palindrome(number) is True:
            count_number += 1
            count += 1
            print(format(number, '6d'), end="")
            if (count % number_per_line) == 0:
                print()
            if count_number == 100:  # Display the first 100 numbers
                break


# Display the result
main()
