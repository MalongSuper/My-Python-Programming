# This program finds the number of occurrences of a specified character
def count(s, ch):  # Define function to count the character
    char_count = s.count(ch)
    return char_count


def main():  # Define main function
    print("Occurrences of a specified character")
    s = str(input("Enter a string: "))
    ch = str(input("Enter the character to count: "))
    print(f"The number of occurrences of '{ch}' is", end=" ")
    print(count(s, ch))


# Display the result
main()
