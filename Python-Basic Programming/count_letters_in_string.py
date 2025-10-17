# This program counts the letters in a string
import string


def count_letters(s):  # Define function to count the letters
    count = 0
    list_s = list(s)
    list_letters = list(string.ascii_letters)
    for let in list_s:
        if let in list_letters:
            count += 1
    return count


def main():  # Define main function
    print("Count Letters in a String")
    s = str(input("Enter a String: "))
    print("The number of letters is", end=" ")
    print(count_letters(s))


# Display the result
main()
