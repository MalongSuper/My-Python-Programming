# This program converts between feet and meters
def foot_to_meter(foot):  # Define function
    meter = 0.305 * foot
    meter = round(meter, 3)
    return meter


def meter_to_foot(meter):  # Define function
    foot = meter / 0.305
    foot = round(foot, 3)
    return foot


def main():  # Define main function
    # Display the table
    print("Table of Conversions between Feet and Meters")
    print("{:<15}{:<15}{:<5}{:<15}{:<15}".format("Feet", "Meters", "|", "Meters", "Feet"))
    # Use for in range() multiple times to display the right table
    feet = 0
    # Assume the value for each part of the table
    meters = 14
    for table in range(1, 3):
        feet = feet + 1
        feet = feet / 1
        print("{:<15}{:<15}".format(feet, foot_to_meter(feet)), end="")
        meters = meters + 6
        meters = meters / 1
        print("{:<5}{:<15}{:<25}".format("|", meters, meter_to_foot(meters)))

    meters = 24
    for table in range(4, 6):
        feet = feet + 1
        feet = feet / 1
        print("{:<15}{:<15}".format(feet, foot_to_meter(feet)), end="")
        meters = meters + 6
        meters = meters / 1
        print("{:<5}{:<15}{:<25}".format("|", meters, meter_to_foot(meters)))

    meters = 34
    for table in range(7, 9):
        feet = feet + 1
        feet = feet / 1
        print("{:<15}{:<15}".format(feet, foot_to_meter(feet)), end="")
        meters = meters + 6
        meters = meters / 1
        print("{:<5}{:<15}{:<25}".format("|", meters, meter_to_foot(meters)))

    meters = 44
    for table in range(9, 11):
        feet = feet + 1
        feet = feet / 1
        print("{:<15}{:<15}".format(feet, foot_to_meter(feet)), end="")
        meters = meters + 6
        meters = meters / 1
        print("{:<5}{:<15}{:<25}".format("|", meters, meter_to_foot(meters)))

    meters = 54
    for table in range(12, 14):
        feet = feet + 1
        feet = feet / 1
        print("{:<15}{:<15}".format(feet, foot_to_meter(feet)), end="")
        meters = meters + 6
        meters = meters / 1
        print("{:<5}{:<15}{:<25}".format("|", meters, meter_to_foot(meters)))


# Display the result
main()
