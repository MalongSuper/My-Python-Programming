# This program converts decimal to binary as a string

def decimal_to_binary(number):  # Define function for calculating binary
    # For number contain fraction values
    if number.replace(".", "").isnumeric():
        print("The Binary is", end=" ")
        if '.' in number:
            number_parts = number.split('.')  # List contains integer and fraction parts
            int_parts = int(number_parts[0])  # Take integer part
            frac_parts = int(number_parts[1])  # Take fraction part
            # Subtract and get the true fraction part
            take_frac = round(float(number) - int_parts, len(str(frac_parts)))
            # Use bin() to convert to binary
            binary_int = bin(int_parts)[2:]  # Use [2:] to only display from index 2
            print(binary_int, end=".")
            while take_frac > 0:
                # Use formula to find binary of the fraction part
                take_frac = take_frac * 2
                int_frac = int(take_frac)  # Use int() to handle 0 and 1
                print(int_frac, end="")
                take_frac = take_frac - int_frac
        else:
            binary_list = []
            # For non-fraction integer
            number = int(number)
            while number > 0:
                binary = number % 2
                number = number // 2
                binary_list.append(str(binary))
            # Display the result
            print("".join(binary_list[::-1]))
    else:
        print("Invalid Input. Please try again")


def main():  # Define main function
    print("Decimal to Binary as String")
    number = str(input("Enter a decimal integer: "))
    if number == '0':
        print("The Binary is 0")
    else:
        decimal_to_binary(number)


# Display the result
main()
