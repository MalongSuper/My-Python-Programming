# This program reverses a String
def reverse(s):
    return s[::-1]


def main():  # Define main function
    print("Reversed String")
    string = str(input("Enter a String: "))
    print("The Reverse String is", reverse(string))


# Display the result
main()
