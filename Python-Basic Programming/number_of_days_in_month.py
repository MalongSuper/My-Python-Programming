# This program finds the number of days in a month of a year
print("Number of days in the month and year")
# Input the month
Month = int(input("Enter the month: "))
Year = int(input("Enter the year: "))
if (Month <= 0) or (Month > 12):
    print("Error: Invalid number of month. Please proceed and try again")
elif (Year >= 3000) or (Year < 100):
    print("Error: The number you entered is too far. "
          "Please proceed and try again")
else:
    # List of numbers represent the months
    List = {1: 'January', 2: 'February', 3: 'March',
            4: 'April', 5: 'May', 6: 'June',
            7: 'July', 8: 'August', 9: 'September',
            10: 'October', 11: 'November', 12: 'December'}
    # When it is the month with 30 days
    Month_30days = (4, 6, 9, 11)
    if Month in Month_30days:
        print(List.get(Month), Year, "has 30 days")
    # When it is the month with 31 days
    Month_31days = (1, 3, 5, 7, 8, 10, 12)
    if Month in Month_31days:
        print(List.get(Month), Year, "has 31 days")
    # When it is February, the month either has 28 or 29 days based on the year
    if Month == 2:
        # The program has to indicate the leap year
        if ((Year % 100) == 0 and (Year % 400) == 0) or ((Year % 100) != 0 and (Year % 4) == 0):
            print(List.get(Month), Year, "has 29 days")
        else:
            print(List.get(Month), Year, "has 28 days")
