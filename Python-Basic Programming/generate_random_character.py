# This program displays uppercase letters and digits
from random import randint


def get_random_letter(chr1, chr2):  # Define function to generate letter
    random_letter = randint(chr1, chr2)
    return chr(random_letter)


def get_random_digit(num1, num2):  # Define function to generate digit
    random_digit = randint(num1, num2)
    return random_digit


def main():  # Define main function
    print("\t\tRandom Character Table")
    print("--------------------------------------")
    count = 0
    number_per_line = 10
    chr1 = ord('A')
    chr2 = ord('Z')
    num1 = 0
    num2 = 9
    for table in range(100):
        print(get_random_letter(chr1, chr2), end="\t")
        count += 1
        if (count % number_per_line) == 0:
            print()
    for table in range(100):
        print(get_random_digit(num1, num2), end="\t")
        count += 1
        if (count % number_per_line) == 0:
            print()


# Display the result
main()
