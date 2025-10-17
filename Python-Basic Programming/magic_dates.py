# This program will determine if a specific date is a magic date
Month = int(input("Enter a month :"))
Day = int(input("Enter a day :"))
Year = int(input("Enter a two-digit year :"))
# There are only 12 months in the year
if Month > 12 or Month < 1:
    print("Error: You have to enter the month with a number between 1 and 12."
          "Please proceed and try again")
# There are only 31 days at maximum in most years
elif Day > 31 or Day < 1:
    print("Error: You have to enter the day with a number between 1 and 31. "
          "Please proceed and try again")
# Some months have less than 31 days
elif ((Month == 4 and Day > 30) or (Month == 6 and Day > 30)
      or (Month == 9 and Day > 30) or (Month == 11 and Day > 30)):
    print("Error: The month you typed in has less than 31 days."
          "Please proceed and try again")
elif Month == 2 and Day > 28:
    print("Error: February only has 28 days in the month."
          "Please proceed and try again")
# User should only be allowed to enter two numbers in the year
elif Year > 100 or Year < 10:
    print("Error: You have to enter the two last number of the year."
          "Please proceed and try again")
# The date is magic when the month times the day equal the year
else:
    Date = Month * Day
    if Date == Year:
        print("The date you type in is", Month, "/", Day, "/", Year)
        print("The date is magic")
    else:
        print("The date you type in is", Month,"/", Day, "/", Year)
        print("The date is not magic")