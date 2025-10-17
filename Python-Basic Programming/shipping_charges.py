# This program will display shipping charges based on the weight of a package
# Input the weight of a package
Weight_of_packages = float(input("Enter the weight of a package in pounds :"))
if Weight_of_packages < 0:
    print("Error: The weight of a package cannot be negative. "
          "Please proceed amd try again")
else:
    # If the weight is 0 pounds, then there is no charge
    if Weight_of_packages == 0:
        print("No shipping charges")
    # If the weight is 2 pounds or less, the rate is $1.50
    elif Weight_of_packages <= 2:
        print("The shipping charges : $1.50")
    # If the weight is over 2 pounds but not more than 6 pounds, the rate is $3.00
    elif (Weight_of_packages > 2) and (Weight_of_packages <= 6):
        print("The shipping charges : $3.00")
    # If the weight is over 6 pounds but not more than 10 pounds, the rate is $4.00
    elif (Weight_of_packages > 6) and (Weight_of_packages <= 10):
        print("The shipping charges : $4.00")
    # If the weight is over 10 pounds, the rate is $4.75
    elif Weight_of_packages > 10:
        print("The shipping charges : $4.75")

