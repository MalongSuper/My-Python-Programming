# This program sorts three integers in increasing order
def display_sorted_number(num1, num2, num3):  # Define function
    # Make a list contains the numbers
    number_list = [num1, num2, num3]
    # Sort the numbers from the list
    sorted_number = sorted(number_list)
    return sorted_number


def main():  # Define main function
    # Input value
    num1, num2, num3 = eval(input("Enter three numbers:"))
    print("The sorted numbers are", display_sorted_number(num1, num2, num3))


# Display the result
main()
