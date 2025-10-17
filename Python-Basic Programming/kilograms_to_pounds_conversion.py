# This program displays two tables of conversion between Kilograms and Pounds
print("Table of Conversion between Kilograms and Pounds")
print("{:<15}{:<10}{:<5}{:<15}{:<10}".format("Kilograms", "Pounds", "|", "Pounds", "Kilograms"))
# The number of values of both table are 200
# Display the first number of the tables
Reverse_Pounds = 1
for Kilograms in range(1, 2):
    # Display 1 and 2.2
    Pounds = Kilograms * 2.2
    print("{:<15}{:<10}".format(Kilograms, round(Pounds, 2)), end="")
    # Display 1 and 0.45
    Reverse_Kilogram = Reverse_Pounds * 0.4544
    print("{:<5}{:<15}{:<20}".format("|", Reverse_Pounds, round(Reverse_Kilogram, 2)))
# Display the remaining of the tables
Reverse_Pounds = 20
for Kilograms in range(3, 200, 2):
    # Display the first table
    Pounds = Kilograms * 2.2
    print("{:<15}{:<10}".format(Kilograms, round(Pounds, 2)), end="")
    # Display the second table
    Reverse_Pounds += 5
    Reverse_Kilogram = Reverse_Pounds * 0.4544
    # Make the table of numbers placed evenly using format()
    print("{:<5}{:<15}{:<20}".format("|", Reverse_Pounds, round(Reverse_Kilogram, 2)))
