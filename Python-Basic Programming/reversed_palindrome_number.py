# This program reverses a number then determines if it is a palindrome number
def reverse(number):  # Define function
    # Find the reverse number
    reverse_number = 0
    while number > 0:
        digit = number % 10
        reverse_number = (reverse_number * 10) + digit
        number = number // 10
    return reverse_number


def is_palindrome(number):  # Define function
    reverse_number = reverse(number)  # Use the result above
    # The number is palindrome when its reverse is the same as its original
    if reverse_number == number:
        return True
    else:
        return False


def main():  # Define main function
    print("Reversed Palindrome Number")
    # Input value
    number = int(input("Enter a number: "))
    print("The reversed number is", reverse(number))
    if is_palindrome(number) is True:
        print("It is a palindrome number")
    elif is_palindrome(number) is False:
        print("It is not a palindrome number")


# Display the result
main()
