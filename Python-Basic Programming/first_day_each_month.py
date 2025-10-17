# This program displays the days of every first day in the months of a year
print("Display the first day of each month")
# Input the values
Year = int(input("Enter the year: "))
First_Day = int(input("Enter the first day of the year (1 for Monday to 7 for Sunday): "))
if Year <= 100 or Year >= 3000:
    print("Error: The year is too far. Please try again")
elif (First_Day < 0) or (First_Day > 7):
    print('Error: The day is invalid. Please try again')
else:
    # Assume the list of months
    Month_List = {1: 'January', 2: 'February', 3: 'March', 4: 'April',
                  5: 'May', 6: 'June', 7: 'July', 8: 'August',
                  9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    # Assume the list of days
    Day_List = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
                4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
    # Get the first day of every month by loops
    for Month in range(1, 13):
        print(f'{Month_List.get(Month)} 1, {str(Year)} is a {Day_List.get(First_Day)}')
        # Determine the months
        if Month == 2:  # February is a special month
            if ((Year % 100) == 0 and (Year % 400) == 0) or ((Year % 100) != 0 and (Year % 4) == 0):
                Day = 29  # Leap Year
            else:
                Day = 28
        elif Month in [4, 6, 9, 11]:  # Months with 30 days
            Day = 30
        else:
            Day = 31
        # Calculates the first day for the next month
        First_Day = (First_Day + Day) % 7
        # When it is 0, display Sunday
        if First_Day == 0:
            First_Day = 7
