# This program converts Binary to Hexadecimal
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


def binary_to_hexadecimal(binary_string):  # Define function to convert binary to hexadecimal
    hex_value = ''
    true_hex = 0
    # Use the decimal of the binary
    decimal_value = binary_to_decimal(binary_string)
    if decimal_value is not False:
        list_value = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6',
                      7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: "E", 15: "F"}
        while decimal_value > 0:
            not_hex = decimal_value % 16
            decimal_value = decimal_value // 16
            not_hex = round(not_hex)
            # Combine all the Hex value
            # Convert the number to the string in the list given above
            hex_value += list_value.get(not_hex)
            true_hex = hex_value[::-1]
        return true_hex
    else:
        return False


def main():  # Define main function
    print("Binary to Hexadecimal")
    bin_string = str(input("Enter a Binary String: "))
    hex_result = binary_to_hexadecimal(bin_string)
    if hex_result is False:
        print("Error: The string is not binary. Please proceed and try again")
    else:
        print("The Hexadecimal is", hex_result)


# Display the result
main()
