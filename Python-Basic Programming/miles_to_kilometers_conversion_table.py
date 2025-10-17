# This program makes a table of conversion from miles to kilometers
Kilometers = 0
print("Table of conversion from miles to kilometers")
print("Miles\t\tKilometers")
# Display the table
for Miles in range(1, 11):
    Kilometers = Miles * 1.609
    print(f'{Miles}\t\t\t{round(Kilometers, 3)}')
