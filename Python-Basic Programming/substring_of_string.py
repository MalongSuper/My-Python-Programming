# This program checks whether a string is a substring of another string
def find_string(string1, string2):  # Define function for finding substring
    # Check if the value in string 1 is also in string 2
    if string1 in string2:
        return True
    else:
        return False


def main():  # Define main function
    print("Check for Substrings")
    string1 = str(input("Enter the first string: "))
    string2 = str(input("Enter the second string: "))
    if find_string(string1, string2) is True:
        print("=> True. String 1 is a substring of String 2")
    else:
        print("=> False. String 1 is not a substring of String 2")


# Display the result
main()
