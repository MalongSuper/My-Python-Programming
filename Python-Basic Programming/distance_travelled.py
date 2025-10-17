# This program will calculate the distance
# the vehicle has traveled for each hour of the time period
# Assume the hour
Number_of_Hour = 0
# Input the speed of a vehicle and the number of hours
Speed = float(input("Enter the speed of a vehicle (in MpH) :"))
Time = int(input("Enter the number of hours it has travelled :"))
if Speed < 0 or Time < 0:
    print("Error: You cannot enter a negative number. Please proceed and try again")
else:
    print("Hour\tDistance Travelled")
    print("---------------------------")
    for Hour in range(1, Time + 1):
        Hour += Number_of_Hour
        # Distance = Speed * Time
        Distance = Speed * Hour
        print(f'{Hour}\t\t\t\t{Distance}')
