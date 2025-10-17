# Day of Week
print("Day of Week")
day = int(input("Enter a day: "))
month = int(input("Enter a month: "))
year = int(input("Enter a year: "))
# Invalid Input
if day not in range(1, 32):
    print("Day - Invalid Input")
elif month not in range(1, 13):
    print("Month - Invalid Input")
elif month == 2 and day not in range(1, 29):
    print("February Day - Invalid Input")
elif year < 100:
    print("Year - Invalid Input")
else:
    date = {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4,
            "Friday": 5, "Saturday": 6, "Sunday": 0}
    # Determine the day
    if month < 3:
        month = month + 12
        year = year - 1
        n = (day + (2 * month) + (3 * (month + 1)) // 5 + year + year // 4) % 7
        for i, j in date.items():
            if j == n:
                print(f"The date {day}-{month - 12}-{year + 1} is {i}")
    else:
        n = (day + (2 * month) + (3 * (month + 1)) // 5 + year + year // 4) % 7
        for i, j in date.items():
            if j == n:
                print(f"The date {day}-{month}-{year} is {i}")
