# This program reverses an integer
def reverse(integer_num):  # Define function
    # Find the reverse integer
    reverse_integer = 0
    while integer_num > 0:
        digit = integer_num % 10
        reverse_integer = (reverse_integer * 10) + digit
        integer_num = integer_num // 10
    return reverse_integer


def main():  # Define main function
    print("Reversed Integer")
    # Input value
    integer = int(input("Enter an integer: "))
    if integer < 10:
        print("The integer cannot be reversed")
    else:
        print("The reversed integer is", reverse(integer))


# Display the result
main()
