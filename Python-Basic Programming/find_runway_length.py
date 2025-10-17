# Calculate the runway length needed for an airplane
# Given formula: length = (v ** 2) / 2a
# Input
print("Runway Length")
speed, accel = eval(input("Enter speed and acceleration: "))
# Calculate
length = (speed ** 2) / (2 * accel)
# Display the result
print("The minimum runaway length for this airplane is", round(length, 3), "meters")
