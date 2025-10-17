# This program displays a table of distances in miles
# and their equivalent distances in kilometers
# Assume the number
Distance = 0
Miles = 0
# Display the table
print("Miles\t\tKilometers")
print("-----------------------")
# Display the loop
for Miles in range(10, 90, 10):
    Miles += Distance
    # One mile is equivalent to 1.60934 kilometers
    Kilometers = (Miles * 1.60934)
    # Rounded to 2 decimal places
    Round_Kilometers = round(Kilometers, 2)
    print(f'{Miles}\t\t\t{Round_Kilometers}')
