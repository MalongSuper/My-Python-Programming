# This program compares the costs of the two packages
Weight1, Price1 = [float(WP1) for WP1 in input("Enter weight and price for package 1: ").split(",")]
Weight2, Price2 = [float(WP2) for WP2 in input("Enter weight and price for package 2: ").split(",")]
if (Weight1 < 0) or (Weight2 < 0):
    print("Error: Invalid values detected. Please proceed and try again")
elif (Price1 < 0) or (Price2 < 0):
    print("Error: Invalid values detected. Please proceed and try again")
else:
    # Compare the two packages by the sum of their weight and price
    Package1 = Weight1 + Price1
    Package2 = Weight2 + Price2
    # Display whether the package has the better price
    if Package1 == Package2:
        print("Both packages have the same prices")
    elif Package1 > Package2:
        print("Package 1 has the better price")
    elif Package1 < Package2:
        print("Package 2 has the better price")
