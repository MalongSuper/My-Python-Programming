# This program computes the area of triangle using module
import math


def is_valid(side1, side2, side3):  # Define function to check numbers
    # The sum of any two sides must greater than the third side
    if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
        return True


def area(side1, side2, side3):  # Define function for the formula
    if is_valid(side1, side2, side3) is True:
        s = (side1 + side2 + side3) / 2
        area_triangle = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
        return area_triangle


def main():  # Define main function
    print("Module: My Triangle")
    # Input value
    side1, side2, side3 = eval(input("Enter three sides in double: "))
    if is_valid(side1, side2, side3) is not True:
        print("Error: The input is invalid. Please try again")
    else:
        print("The area of the triangle is", area(side1, side2, side3))


# Display the result
main()
