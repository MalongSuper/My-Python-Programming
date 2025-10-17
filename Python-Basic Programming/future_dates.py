# This program looks for the future dates of the week
# Input the day of the week
Today_Day = int(input("Enter a number: "))  # Sunday is 0, Monday is 1 and Saturday is 6
Number_Days_After = int(input("Enter the number of days elapsed since today: "))
if (Today_Day < 0) or (Today_Day > 6):
    print("Invalid number. Please proceed and try again")
elif Number_Days_After < 0:
    print("Invalid number. Please proceed and try again")
else:
    # Make a list and the program should get the days based on the numbers from this list
    # This function replaces the if-else statement
    List = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
            4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
    # Calculate the future dates
    Future_Day = (Today_Day + Number_Days_After) % 7
    # Display the today's dates and future dates
    if Future_Day == 0:
        print("Today is", List.get(Today_Day), "and the future day is Sunday")
    if Future_Day == 1:
        print("Today is", List.get(Today_Day), "and the future day is Monday")
    if Future_Day == 2:
        print("Today is", List.get(Today_Day), "and the future day is Tuesday")
    if Future_Day == 3:
        print("Today is", List.get(Today_Day), "and the future day is Wednesday")
    if Future_Day == 4:
        print("Today is", List.get(Today_Day), "and the future day is Thursday")
    if Future_Day == 5:
        print("Today is", List.get(Today_Day), "and the future day is Friday")
    if Future_Day == 6:
        print("Today is", List.get(Today_Day), "and the future day is Saturday")
        