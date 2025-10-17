# This program calculates the lap times run in a racetrack
# Assume the number
Total_Time = 0
Slowest = 0
Fastest = 1000
# The user must enter the number of times that they have run around a racetrack
Number_of_Time = int(input("Enter the number of times you have run around a racetrack :"))
if Number_of_Time < 0:
    print("Error: The number of times cannot be negative. Please proceed and try again")
else:
    for Number_of_Lap in range(Number_of_Time):
        Number_of_Lap = float(input("Enter the lap time for lap" + " " + str(Number_of_Lap + 1) + ":"))
        while Number_of_Lap <= 0:
            Number_of_Lap = float(input("Error: Only positive number is allowed. Please enter again :"))
        # Calculate the total time
        Total_Time += Number_of_Lap
        # Find the fastest and the slowest lap
        # The program will find the biggest number in the loop
        if Number_of_Lap > Slowest:
            Slowest = Number_of_Lap
        # The program will find the lowest number in the loop
        if Number_of_Lap < Fastest:
            Fastest = Number_of_Lap
    # Calculate the average
    Average = Total_Time / Number_of_Time
    # Display the results
    print("The time of your fastest lap :", Fastest)
    print("The time of your slowest lap :", Slowest)
    print("The average lap time :", Average)
    # The bigger number means the slower time
    # The smaller number means the faster time
