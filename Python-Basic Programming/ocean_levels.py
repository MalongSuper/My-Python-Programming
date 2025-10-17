# This program calculates ocean's level for the next 25 years
# Assume the ocean's level rises about 1.6 millimeters per year
Millimeters = 0
# Display the table
print('Year\t\t\tMillimeters')
print("---------------------------")
# Calculates the ocean's level up to 25 years
for Year in range(1, 26):
    Year += Millimeters
    Millimeters_per_Year = Year * 1.6
    # Rounded the number
    Round_Millimeters = round(Millimeters_per_Year, 2)
    # Display result
    print(f'{Year}\t\t\t\t{Round_Millimeters}')
