# This program displays two tables of conversion between Miles and Kilometers
print("Table of Conversion between Miles and Kilometers")
print("Miles\t\tKilometers  |  Kilometers\t\tMiles")
# Display the first number of the tables
Reverse_Kilometers = 1
for Miles in range(1, 2):
    # Display 1 and 1.609
    Kilometers = Miles * 1.609
    print(f'{Miles}\t\t\t{round(Kilometers, 3)}\t\t|', end="")
    # Display 1 and 0.622
    Reverse_Miles = Reverse_Kilometers * 0.62152
    print(f'\t{Reverse_Kilometers}\t\t\t\t{round(Reverse_Miles, 3)}')
# Display the remaining numbers of the table
Reverse_Kilometers = 20
for Miles in range(2, 11):
    # Display the first table
    Kilometers = Miles * 1.609
    print(f'{Miles}\t\t\t{round(Kilometers, 3)}\t\t|', end="")
    # Display the second table
    Reverse_Kilometers += 5
    Reverse_Miles = Reverse_Kilometers * 0.62152
    # The table displayed is already even, we don't use format()
    print(f'\t{Reverse_Kilometers}\t\t\t\t{round(Reverse_Miles, 3)}')
