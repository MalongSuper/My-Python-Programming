# This program converts Binary to Decimal
import string


def binary_to_decimal(binary_string):  # Define function for finding decimal value
    not_bin1 = list(string.punctuation)
    not_bin2 = list(string.ascii_letters)
    not_bin3 = {'2', '3', '4', '5', '6', '7', '8', '9'}
    list_string = list(binary_string)
    # Check for valid input
    if (any(val in binary_string for val in not_bin1)
            or any(val in binary_string for val in not_bin2)
            or any(val in binary_string for val in not_bin3)):
        return False
    else:
        result_bin = 0
        for bina in range(len(binary_string)):
            binr = int(list_string[bina])
            start_val = len(binary_string) - 1  # Find the starting index
            # Use given formula to find binary
            result_bin += binr * (2 ** (start_val - bina))
        return result_bin


def main():  # Define main function
    print("Binary to Decimal")
    bin_string = str(input("Enter a Binary String: "))
    if binary_to_decimal(bin_string) is False:
        print("Error: The string is not binary. Please proceed and try again")
    else:
        print("The Decimal is", binary_to_decimal(bin_string))


# Display the result
main()
