# This program determines whether the user has a sleep debt
Hour_of_Sleep = 0
Amount_of_Sleep = 0
# Assume 8 hours per day as the desirable amount of sleep
Desire_Sleep = 8 * 7
# The desired total hours of sleep per week is 56 hours
# Create a loop
Day_in_Week = ('Monday', 'Tuesday', 'Wednesday',
               'Thursday', 'Friday', 'Saturday', 'Sunday')
for Day in Day_in_Week:
    # Input the number of hours the user slept each day
    Hour_of_Sleep = int(input("Enter the number of hours you have slept on" + " " + str(Day) + ":"))
    while Hour_of_Sleep < 0:
        Hour_of_Sleep = int(input("Error: You have to enter a positive number. Please enter again:"))
    # Calculate the total hours of sleep
    Amount_of_Sleep += Hour_of_Sleep
print("The total amount of sleep you got over seven days:", Amount_of_Sleep)
# Calculate the sleep debt
Sleep_Debt = Amount_of_Sleep - Desire_Sleep
print("Your sleep debt difference:", Sleep_Debt)
# Determine if the user has a sleep debt or not
if Sleep_Debt < 0:
    print("You have a sleep debt")
elif Sleep_Debt >= 0:
    print("You don't have a sleep debt")
