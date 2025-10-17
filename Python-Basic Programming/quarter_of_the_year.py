# This program displays quarter of the year
x = int(input("Enter a month :"))
# One year only has 12 months
if x < 1 or x > 12:
    print("Error: The month of a year should be between 1 and 12. Please proceed and try again")
# Indicating the month in quarter of the year
elif x == 1 or x == 2 or x == 3:
    print("The month is in the first quarter")
elif x == 4 or x == 5 or x == 6:
    print("The month is in the second quarter")
elif x == 7 or x == 8 or x == 9:
    print("The month is in the third quarter")
elif x == 10 or x == 11 or x == 12:
    print("The month is in the fourth quarter")