# This program displays characters from 1 to Z
def print_char(chr1, chr2, number_per_line):  # Define funtion
    count = 0
    # Display the table
    for table in range(chr1, chr2 + 1):
        print(format(chr(table)), end="\t")
        # Count the next number
        count += 1
        # When the count reaches 10
        if (count % number_per_line) == 0:
            # Display the next ten numbers into the next line
            print()


def main():  # Define main function
    print("\t\tASCII Code Table")
    print("--------------------------------------")
    # Convert characters to numbers in ASCII Code
    chr1 = ord('1')
    chr2 = ord('Z')
    number_per_line = 10
    print_char(chr1, chr2, number_per_line)


# Display the result
main()
