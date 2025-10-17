# This program makes a table of conversion from kilograms to pounds
Pounds = 0
print("Table of Conversion from Kilograms to Pounds")
print("Kilograms\t\tPounds")
# Display the table
for Kilograms in range(1, 200, 2):
    Pounds = Kilograms * 2.2
    print(f'{Kilograms}\t\t\t\t{round(Pounds, 2)}')
