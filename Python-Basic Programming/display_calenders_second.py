# This program finds the day and the first day of the month using Keller's congruence
from math import fabs
import calendar


def congruence(year, month, day_month):  # Define function for calculation
    # January is counted as 13 in the formula with previous year
    if month == 1:
        year = year - 1
        m = 13
        q = day_month
        k = year % 100
        j = fabs(year // 100)
        # Using the given formula
        h = (q + fabs((26 * (m + 1)) // 10) + k + fabs(k // 4) + fabs(j // 4) + (5 * j)) % 7
        day_list = {0: 'Saturday', 1: 'Sunday', 2: 'Monday',
                    3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday'}
        # Take the result
        return day_list.get(int(h))
    # February is counted as 14 in the formula with previous year
    elif month == 2:
        if day_month <= 28:
            year = year - 1
            m = 14
            q = day_month
            k = year % 100
            j = fabs(year // 100)
            # Using the given formula
            h = (q + fabs((26 * (m + 1)) // 10) + k + fabs(k // 4) + fabs(j // 4) + (5 * j)) % 7
            day_list = {0: 'Saturday', 1: 'Sunday', 2: 'Monday',
                        3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday'}
            # Display result
            return day_list.get(int(h))
        # With February in the leap year
        elif ((year % 100) == 0 and (year % 400) == 0) or ((year % 100) != 0 and (year % 4) == 0) and (day_month <= 29):
            year = year - 1
            m = 14
            q = day_month
            k = year % 100
            j = fabs(year // 100)
            # Using the given formula
            h = (q + fabs((26 * (m + 1)) // 10) + k + fabs(k // 4) + fabs(j // 4) + (5 * j)) % 7
            day_list = {0: 'Saturday', 1: 'Sunday', 2: 'Monday',
                        3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday'}
            # Display result
            return day_list.get(int(h))
        else:
            print("Error: February cannot have 29 days when it is not a leap year. Please try again")
            return None
    else:
        # If it is not special month, computes normally
        year = year
        m = month
        q = day_month
        k = year % 100
        j = fabs(year // 100)
        # Using the given formula
        h = (q + fabs((26 * (m + 1)) // 10) + k + fabs(k // 4) + fabs(j // 4) + (5 * j)) % 7
        day_list = {0: 'Saturday', 1: 'Sunday', 2: 'Monday',
                    3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday'}
        # Display result
        return day_list.get(int(h))


def calendar_of_day(year, month):  # Define function for calendar
    calendar_day = calendar.month(year, month)
    return calendar_day


def main():  # Define main function
    print("Day of the Week Calendar")
    year = int(input("Enter year (e.g., 2008): "))
    month = int(input("Enter month (1-12): "))
    day_month = int(input("Enter the day of a month: "))
    # The input values must be valid
    if (year < 100) or (year >= 3000):
        print("Error: Invalid year. Please try again")
    # One year only has 12 months
    elif (month < 1) or (month > 12):
        print("Error: Invalid month. Please try again")
    # One month has 31 days
    elif (day_month > 31) or (day_month < 1):
        print("Error: Invalid day of month. Please try again")
    # Some months have less than 31 days
    elif ((month == 4 and day_month > 30) or (month == 6 and day_month > 30)
          or (month == 9 and day_month > 30) or (month == 11 and day_month > 30)):
        print("Error: The month you entered has less than 31 days."
              "Please try again")
    elif (month == 2) and (day_month >= 30):
        print("Error: February only has 28 days or 29 days (leap year)."
              "Please try again")
    else:
        list_month = {1: 'January', 2: 'February', 3: 'March',
                      4: 'April', 5: 'May', 6: 'June',
                      7: 'July', 8: 'August', 9: 'September',
                      10: 'October', 11: 'November', 12: 'December'}
        result = congruence(year, month, day_month)
        # Day Month is assumed as 1 for the first day
        first_day = 1
        first_day_result = congruence(year, month, first_day)
        print()
        print(calendar_of_day(year, month))
        if first_day_result is not None:
            print("First Day :", first_day_result)
        if result is not None:  # If the input is valid to February
            print("Day of", list_month.get(month), day_month, ":",  result)


# Display the result
main()
