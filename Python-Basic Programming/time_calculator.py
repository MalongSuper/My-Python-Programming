# This program will convert the number of seconds and works to days, hours, minutes and seconds
# Input the number of seconds
print("Time Calculator")
Number_Seconds = int(input("Enter a number of seconds and works: "))
if Number_Seconds < 0:
    print("Error: The number of seconds and works cannot be negative. "
          "Please proceed and try again")
else:
    if Number_Seconds < 60:
        print(Number_Seconds, "seconds")
    # 60 seconds = 1 minute
    # If it is greater than or equal to 60, converts to minutes and seconds
    elif (Number_Seconds >= 60) and (Number_Seconds < 3600):
        Minute = Number_Seconds // 60
        Second = Number_Seconds % 60
        print(Number_Seconds, "seconds =", Minute, "minutes", Second, "seconds")
    # 3600 seconds = 1 hour
    # If it is greater than or equal to 3,600, converts to hours, minutes, and seconds
    elif (Number_Seconds >= 3600) and (Number_Seconds < 86400):
        Hour = Number_Seconds // 3600
        Minute = Number_Seconds % 3600 // 60 % 3600
        Second = Number_Seconds % 60
        print(Number_Seconds, "seconds =", Hour, "hours",
              Minute, "minutes", Second, "seconds")
    # 86400 seconds = 1 day
    # If it is greater than or equal to 86400, converts to days, hours, minutes, and seconds
    elif Number_Seconds >= 86400:
        Day = Number_Seconds // 86400
        Hour = Number_Seconds % 86400 // 3600 % 86400
        Minute = Number_Seconds % 3600 // 60 % 3600
        Second = Number_Seconds % 60
        print(Number_Seconds, "seconds =", Day, "days", Hour, "hours",
              Minute, "minutes", Second, "seconds")
