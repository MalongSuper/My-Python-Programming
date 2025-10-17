# This program displays uppercase letters and count the occurrence
from random import randint


def get_random_character(chr1, chr2):  # Define function to generate characters
    random_letter = randint(chr1, chr2)
    return chr(random_letter)


def get_table(chr1, chr2, number_per_line):  # Define function for the table
    count = 0
    count_a = 0
    for table in range(10000):  # Generate 10000 times
        # Assume value for the function
        random_character = get_random_character(chr1, chr2)
        print(random_character, end=" ")
        count += 1
        if random_character == 'A':  # Count the occurrence of 'A'
            count_a += 1
        if (count % number_per_line) == 0:
            print()
    # Display the occurrence
    print("Result:")
    print("Occurrence of A:", count_a)


def main():  # Define main function
    # Display the table
    chr1 = ord('A')
    chr2 = ord('Z')
    number_per_line = 50
    print("\t\t\t\t\t\t\t\t\tRandom Uppercase Letter")
    print("-----------------------------------------"
          "----------------------------------------------------------")
    get_table(chr1, chr2, number_per_line)


# Display the result
main()
