# This program computes the area of a polygon using function
from math import tan, pi


def area(n, side):  # Define function for calculation
    area_polygon = (n * (side ** 2)) / (4 * tan(pi / n))
    return area_polygon


def main():  # Define main function
    print("Area of Regular Polygon")
    n = int(input("Number of Sides: "))
    side = float(input("Sides: "))
    if n < 0 or side < 0:
        print("Error: Negative number is not allowed. Please try again")
    else:
        print("The Polygon Area:", area(n, side))


# Display the result
main()
