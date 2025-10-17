# This program checks for ISBN-10
import string


def valid_digits(isbn_number):  # Define function for valid digits
    number_list = list(isbn_number)
    if len(number_list) != 9:
        return False
    else:
        return True


def number_only(isbn_number):  # Define function for only digits
    number_list = list(isbn_number)
    punc_list = list(string.punctuation)
    str_list = list(string.ascii_letters)
    if (any(num in number_list for num in punc_list)
            or any(num in number_list for num in str_list)):
        return False
    else:
        return True


def read_number(isbn_number):  # Define function to read ISBN-10
    digit = 0
    number_list = list(isbn_number)
    for num in range(len(number_list)):
        int_num = int(number_list[num])
        # Calculate the digit
        digit += int_num * (num + 1)

    # Calculate the Checksum
    checksum = digit % 11
    # Use append to add the checksum to the number list
    number_list.append(str(checksum))
    if checksum == 10:
        # Change the value in the last index to X
        number_list[len(number_list) - 1] = 'X'
        print("The ISBN-10 Number is", end=" ")
        print(''.join(number_list))
    else:
        print("The ISBN-10 Number is", end=" ")
        print(''.join(number_list))


def main():  # Define main function
    print("Standard International Standard Book Number - ISBN 10")
    isbn_number = str(input("Enter the first nine digits: "))
    if valid_digits(isbn_number) is False:
        print("Invalid Input")
        print("Reason: Must be nine-digit")
    elif number_only(isbn_number) is False:
        print("Invalid Input")
        print("Reason: Must contain only digits")
    else:
        read_number(isbn_number)


# Display the result
main()
