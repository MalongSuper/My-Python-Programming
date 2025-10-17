# This program checks for valid password
import string


def valid_characters(password):  # Define function for valid number of characters
    if password.count("") < 9:
        return False
    else:
        return True


def letters_and_digits(password):  # Define function for only letters and digits
    list_password = list(password)
    list_punc = list(string.punctuation)
    if any(punc in list_password for punc in list_punc):
        return False
    else:
        return True


def two_digits(password):  # Define function to check the number of digits
    count = 0
    list_password = list(password)
    list_dig = list(string.digits)
    for dig in list_password:
        if dig in list_dig:
            count += 1
    if count < 2:
        return False
    else:
        return True


def main():  # Define main function
    print("Check for Password")
    password = str(input("Password: "))
    if valid_characters(password) is False:
        print("Invalid Password")
        print("Reason: Must have at least eight characters")
    elif letters_and_digits(password) is False:
        print("Invalid Password")
        print("Reason: Must only contain letters and digits")
    elif two_digits(password) is False:
        print("Invalid Password")
        print("Reason: Must contain at least two digits")
    else:
        print("Confirmed. Valid Password")


# Display the result
main()
