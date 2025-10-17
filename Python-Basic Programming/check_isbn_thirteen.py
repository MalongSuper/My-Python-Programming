# This program checks for ISBN-13
import string


def valid_digits(isbn_number):  # Define function for valid digits
    number_list = list(isbn_number)
    if len(number_list) != 12:
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


def read_number(isbn_number):  # Define function to read ISBN-13
    digit = 0
    three_num = [1, 3, 5, 7, 9, 11]  # The index which the value multiply to 3
    number_list = list(isbn_number)
    for num in range(len(number_list)):
        isbn = int(number_list[num])
        if num in three_num:
            isbn = int(number_list[num]) * 3
        # Calculate the digit
        digit += isbn

    # Calculate the Checksum
    checksum = 10 - digit % 10
    number_list.append(str(checksum))
    if checksum == 10:
        # Change the value in the last index to 0
        number_list[len(number_list) - 1] = '0'
        print("The ISBN-13 Number is", end=" ")
        print(''.join(number_list))
    else:
        print("The ISBN-13 Number is", end=" ")
        print(''.join(number_list))


def main():  # Define main function
    print("Advanced International Standard Book Number - ISBN 13")
    isbn_number = str(input("Enter the first twelve digits: "))
    if valid_digits(isbn_number) is False:
        print("Invalid Input")
        print("Reason: Must be twelve-digit")
    elif number_only(isbn_number) is False:
        print("Invalid Input")
        print("Reason: Must contain only digits")
    else:
        read_number(isbn_number)


# Display the result
main()
