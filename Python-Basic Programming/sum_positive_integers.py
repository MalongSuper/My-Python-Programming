# This program calculates sum of the positive integer
def sum_digits(n):  # Define function
    total = 0
    while n > 0:
        # Use the % operator to extract digits
        d = n % 10
        # Calculate the digits
        total += d
        # Use the // operator to remove the extracted digit
        n = n // 10
        # The program will continue until the Number has reached zero
    print("The sum of the number digits is", total)


def main():  # Main function
    print("Sum of Digits")
    # Input value
    n = int(input("Enter an integer: "))
    if n < 0:
        print("Error: The number should be positive. Please try again")
    elif n <= 9:
        print("Error: The number you entered should have more than two digits. Please try again")
    else:
        sum_digits(n)


# Display the result
main()
