# This program checks for a valid Social Security Number
import string


def number_only(d1, d2, d3):  # Define function for valid number
    d1_list = list(d1)
    d2_list = list(d2)
    d3_list = list(d3)
    string_list_punc = list(string.punctuation)
    string_list_let = list(string.ascii_letters)
    # If any letter is found, the SSN is invalid
    if (any(char in d1_list for char in string_list_let)
            or any(char in d2_list for char in string_list_let)
            or any(char in d3_list for char in string_list_let)):
        return False
    # If punctuation is found, the SSN is invalid
    elif (any(char in d1_list for char in string_list_punc)
          or any(char in d2_list for char in string_list_punc)
          or any(char in d3_list for char in string_list_punc)):
        return False
    else:
        return True


def valid_number(d1, d2, d3):  # Define function for valid format
    # Determine number of digits by counting them
    if d1.count('') != 4 or d2.count('') != 3 or d3.count('') != 5:
        return False
    else:
        return True


def main():  # Define main function
    print("Social Security Number")
    d1, d2, d3 = [str(d123) for d123 in (input("Enter Social Security Number: ")).split("-")]
    if number_only(d1, d2, d3) is False:
        print("The SSN is Invalid")
        print("Reason: Must only contain digits")
    elif valid_number(d1, d2, d3) is False:
        print("The SSN is Invalid")
        print("Reason: Must follow the format ddd-dd-dddd")
    else:
        print("The SSN is Valid")


# Display the result
main()
