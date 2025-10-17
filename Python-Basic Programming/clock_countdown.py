# This program simulates clock countdown to pause for the specified seconds
import time
Time = 0
print("Clock Countdown")
# Input the second
Seconds = int(input("Enter the number of seconds: "))
if Seconds <= 0:
    print("Error: The number of seconds is invalid. Please try again")
else:
    # Since the time goes down, the range is subtracted
    for Time in range(Seconds, 1, -1):
        # Display every second as it is decreasing
        Seconds = Time - 1
        print(Seconds, "seconds remaining")
        # The program stops every 1 seconds
        time.sleep(1)
    # The program terminates when the time expires
    print("Stopped")
