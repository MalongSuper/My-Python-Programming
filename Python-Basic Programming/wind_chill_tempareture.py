# This program computes the wind-chill temperature
# Input the outside temperature and the wind speed
Temperature = float(input("Enter the temperature in Fahrenheit between -58 and 41: "))
WindSpeed = float(input("Enter the wind speed in miles per hour: "))
# The outside temperature must be in the range between –58°F and 41°F
if (Temperature > 41) or (Temperature < -58):
    print("Error: The temperature has exceeded the limit")
# The wind speed must be greater or equal to 2
elif WindSpeed < 2:
    print("Error: The wind speed must be greater or equal to 2")
else:
    # Compute the wind-chill temperature using the given formula
    WindSpeed_Temperature = (35.74 + (0.6215 * Temperature) - (35.75 * (WindSpeed ** 0.16)) +
                             (0.4275 * Temperature * (WindSpeed ** 0.16)))
    # Display the result
    print("The wind chill temperature is", WindSpeed_Temperature)
