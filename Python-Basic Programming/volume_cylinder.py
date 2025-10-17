# This program computes the volume of a cylinder
# Input two values in one line using split()
# The values should be converted to float using the following code
import math
radius, length = [float(RL) for RL in (input("Enter the radius and length of a cylinder: ")).split(",")]
if radius < 0 or length < 0:
    print("Error: You cannot enter a negative number. Please proceed and try again")
else:
    # Calculate using the formula
    area = radius * radius * math.pi
    volume = area * length
    # Display the result
    print("The area is:", round(area, 2))
    print("The volume is:", round(volume, 2))
