# This program calculates day of the week using Keller's congruence
# Input the values
from math import fabs
Year = int(input("Enter year (e.g., 2008): "))
Month = int(input("Enter month (1-12): "))
Day_Month = int(input("Enter the day of a month: "))
# The input values must be valid
if (Year < 100) or (Year >= 3000):
    print("Error: Invalid year. Please try again")
# One year only has 12 months
elif (Month < 1) or (Month > 12):
    print("Error: Invalid month. Please try again")
# One month has 31 days
elif (Day_Month > 31) or (Day_Month < 1):
    print("Error: Invalid day of month. Please try again")
# Some months have less than 31 days
elif ((Month == 4 and Day_Month > 30) or (Month == 6 and Day_Month > 30)
      or (Month == 9 and Day_Month > 30) or (Month == 11 and Day_Month > 30)):
    print("Error: The month you entered has less than 31 days."
          "Please try again")
elif (Month == 2) and (Day_Month >= 30):
    print("Error: February only has 28 days or 29 days (leap year)."
          "Please try again")
else:
    # January is counted as 13 in the formula with previous year
    if Month == 1:
        Year = Year - 1
        M = 13
        Q = Day_Month
        K = Year % 100
        J = fabs(Year // 100)
        # Using the given formula
        H = (Q + fabs((26 * (M + 1)) // 10) + K + fabs(K // 4) + fabs(J // 4) + (5 * J)) % 7
        List = {0: 'Saturday', 1: 'Sunday', 2: 'Monday',
                3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday'}
        # Display result
        print("Day of the week is", List.get(int(H)))
    # February is counted as 14 in the formula with previous year
    elif Month == 2:
        if Day_Month <= 28:
            Year = Year - 1
            M = 14
            Q = Day_Month
            K = Year % 100
            J = fabs(Year // 100)
            # Using the given formula
            H = (Q + fabs((26 * (M + 1)) // 10) + K + fabs(K // 4) + fabs(J // 4) + (5 * J)) % 7
            List = {0: 'Saturday', 1: 'Sunday', 2: 'Monday',
                    3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday'}
            # Display result
            print("Day of the week is", List.get(int(H)))
        # With February in the leap year
        elif ((Year % 100) == 0 and (Year % 400) == 0) or ((Year % 100) != 0 and (Year % 4) == 0) and (Day_Month <= 29):
            Year = Year - 1
            M = 14
            Q = Day_Month
            K = Year % 100
            J = fabs(Year // 100)
            # Using the given formula
            H = (Q + fabs((26 * (M + 1)) // 10) + K + fabs(K // 4) + fabs(J // 4) + (5 * J)) % 7
            List = {0: 'Saturday', 1: 'Sunday', 2: 'Monday',
                    3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday'}
            # Display result
            print("Day of the week is", List.get(int(H)))
        else:
            print("Error: February cannot have 29 days when it is not a leap year. Please try again")
    else:
        # If it is not special month, computes normally
        Year = Year
        M = Month
        Q = Day_Month
        K = Year % 100
        J = fabs(Year // 100)
        # Using the given formula
        H = (Q + fabs((26 * (M + 1)) // 10) + K + fabs(K // 4) + fabs(J // 4) + (5 * J)) % 7
        List = {0: 'Saturday', 1: 'Sunday', 2: 'Monday',
                3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday'}
        # Display result
        print("Day of the week is", List.get(int(H)))
