# This program will identify whether a year is a leap year
# In a leap year, February will have 29 days
# Input a year
Year = int(input("Enter a year :"))
if Year < 0:
    print("Error: The year has to be a positive. "
          "Please proceed and try again")
# You should type a year within the range of 100 through 3000
elif Year >= 3000:
    print("Error: The year you entered is too far. "
          "Please proceed and try again")
elif Year < 100:
    print("Error: The year you entered is too far. "
          "Please proceed and try again")
else:
    # The year is a leap year when it is divisible to both 100 and 400
    if (Year % 100) == 0 and (Year % 400) == 0:
        print("In",Year,"February has 29 days")
        print("It is a leap year")
    elif (Year % 100) == 0 and (Year % 400) != 0:
        print("In",Year,"February has 28 days")
    # The year is a leap year when it is not divisible to 100 but is divisible to 4
    elif (Year % 100) != 0 and (Year % 4) == 0:
        print("In",Year,"February has 29 days")
        print("It is a leap year")
    elif (Year % 100) != 0 and (Year % 4) != 0:
        print("In",Year,"February has 28 days")
