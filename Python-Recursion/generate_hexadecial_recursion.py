# This program generates n digits hexadecimal value using recursion
import random


def hex_generator(n):
    if n == 0:
        return ""
    else:
        hex_digit = random.choice("0123456789ABCDEF")
        return hex_digit + hex_generator(n - 1)


def main():
    print("Generate Hexadecimal Number (Recursion)")
    number = int(input("Enter number of digits: "))
    result = hex_generator(number)
    print("The Hexadecimal Number:", result, end="\n")


main()

