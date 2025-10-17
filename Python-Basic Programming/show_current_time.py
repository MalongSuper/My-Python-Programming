# This program displays the current date and time
import time
import datetime


def date_and_time():  # Define function
    current_date = datetime.date.today()  # Use this function to find the date
    current_time = time.time()  # Show current time

    # Obtain the total second since midnight, Jan 1 1970
    total_seconds = int(current_time)

    # Get the current second
    current_second = total_seconds % 60

    # Obtain the total minutes
    total_minutes = total_seconds // 60

    # Compute te current minute in the hour
    current_minute = total_minutes % 60

    # Obtain the total hours
    total_hours = total_minutes // 60

    # Compute the current hour
    current_hour = total_hours % 24

    # Display the final result
    print("Date:", current_date)
    print("Time:", str(current_hour) + ":" + str(current_minute) + ":" + str(current_second), "GMT")


def main():  # Define main function
    print("Current Date and Time (GMT)")
    date_and_time()


# Display the result
main()
