# This program displays the current date and time
import datetime
import time


def current_date():  # Define function for current data
    number_date = datetime.date.today()  # Find the current date
    exact_date = number_date.strftime("%B %d, %Y")  # Convert the date into the exact date
    return exact_date


def current_time():  # Define function for current time
    number_time = time.localtime()  # Find the current time
    exact_time = time.strftime("%H:%M:%S", number_time)  # Convert the time into the exact time
    return exact_time


def main():  # Define main function
    print("Date and Time")
    print("Current Date and Time is", end=" ")
    print(current_date(), end=" ")
    print(current_time())


# Display the result
main()
