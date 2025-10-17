# This program converts feet to meter
Feet = float(input("Enter the value for feet: "))
if Feet < 0:
    print("Error: You cannot enter a negative number. "
          "Please proceed and try again")
else:
    # One foot is 0.305 meters
    One_Foot = 0.305
    Meters = Feet * One_Foot
    print(Feet, "feet is", round(Meters, 4), "meters")
