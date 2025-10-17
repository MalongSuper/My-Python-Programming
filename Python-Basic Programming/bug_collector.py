# This program calculates the total number of bugs collected for five days
# When it starts
Total_Bugs = 0
# Limit in 5 days, Repeat five times
for Day in range(5):
    Bugs = int(input("Enter the number of bugs collected in day" + " " + str(Day + 1) + ":"))
# Stop the program the moment the user enter a negative number
    while Bugs < 0:
        # Ask the user to enter a positive number
        Bugs = int(input("Error: Only positive number is allowed, Please enter again :"))
    # Calculate the number of bugs
    Total_Bugs += Bugs
    print(Total_Bugs, "bugs collected")
print("The total bugs collected :", Total_Bugs)
