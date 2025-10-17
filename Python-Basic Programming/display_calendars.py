# This program displays calendar based on the first day of the year
import calendar
# Input the value
print("Display Calendars")
Year = int(input("Enter the year: "))
First_Day = int(input("Enter the first day of the year (1 for Monday to 7 for Sunday): "))
if Year <= 100 or Year >= 3000:
    print("Error: The year is too far. Please try again")
elif (First_Day < 0) or (First_Day > 7):
    print('Error: The day is invalid. Please try again')
else:
    # Get the first day of every month by loops
    for Month in range(1, 13):
        # Use the Month name to display the calendar
        print("\t\t", calendar.month_name[Month], Year, "\t")
        print("----------------------------------")
        print("Mon  Tue  Wed  Thu  Fri  Sat  Sun")
        # Get the first day of the month
        First_WeekDay = First_Day
        # Display the first line of days
        for CalendarTable in range(First_WeekDay - 1):
            print("    ", end=" ")
        # Display the following days
        for Day in range(1, calendar.monthrange(Year,  Month)[1] + 1):
            print(f'{Day: 3d} ', end=" ")
            First_WeekDay += 1
            # Move to next line if it is Saturday
            if First_WeekDay == 8:
                print()
                First_WeekDay = 1
        print("\n")
        # Find the first day for the next months
        First_Day = First_WeekDay
