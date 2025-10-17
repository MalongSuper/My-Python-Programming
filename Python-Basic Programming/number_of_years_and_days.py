# This program finds the number of years and days for the minutes
# Input the minutes
Minutes = int(input("Enter the number of minutes: "))
if Minutes < 0:
    print("Error: You cannot use a negative number. "
          "Please proceed and try again")
else:
    # Assume 1 year = 525600 minutes
    # Assume 1 day = 1440 minutes
    # Only displays the minutes
    if Minutes < 1440:
        print("Exactly", Minutes, "minutes")
    # If it is less, only displays the day
    elif Minutes < 525600:
        Days = Minutes // 1440
        print(Minutes, "minutes is approximately", Days, "days")
    # Only displays the year when it does not exceed the limit
    elif (Minutes == 525600) or (Minutes < (525600 + 1440)):
        Year = Minutes // 525600
        print(Minutes, "minutes is approximately", Year, "year")
    # If it is more, displays the approximate years and days
    elif Minutes > 525600:
        Year = Minutes // 525600
        Days = (Minutes % 525600) // 1440
        print(Minutes, "minutes is approximately", Year, "years", Days, "days")
