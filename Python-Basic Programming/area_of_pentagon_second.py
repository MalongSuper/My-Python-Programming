# This program computes the area of a pentagon using function
from math import tan, pi


def area(s):  # Define function for calculation
    area_pentagon = (5 * (s ** 2)) / (4 * tan(pi / 5))
    return area_pentagon


def main():  # Define main function
    print("Area of Pentagon")
    s = eval(input("Side: "))
    if s < 0:
        print("Error: Negative number is not allowed. Please try again")
    else:
        print("The Pentagon Area:", area(s))


# Display the result
main()
