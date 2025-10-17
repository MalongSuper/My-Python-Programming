# This program counts the occurrence of a specified string

def count(s1, s2):  # Define function to count the occurrence
    counter = 0
    start = 0  # Starting index
    # Use loop to check until it reaches the end of String 1
    while start < len(s1):
        # Find value in string1 in string2 starting from index 0
        find_occur = s1.find(s2, start)
        # Move to another index
        if find_occur != -1:
            start = find_occur + 1
            counter += 1  # Count the occurrence
        else:
            # If there is no substring, it returns -1
            break

    return counter


def main():  # Define main function
    print('Occurrence of Specified String')
    s1 = str(input("Enter String 1: "))
    s2 = str(input("Enter String 2: "))
    print(f"The occurrence of '{s2}' in '{s1}' is", count(s1, s2))


# Display the result
main()
