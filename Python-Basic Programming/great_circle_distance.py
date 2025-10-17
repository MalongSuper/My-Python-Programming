# This program computes the distance between two points in a circle
from math import sin, cos, acos
import math
# Input latitude and longitude of two points on the earth in degrees
x1, y1 = [float(Point1) for Point1 in (input("Enter point 1 (latitude and longitude) in degrees: ")).split(",")]
x2, y2 = [float(Point2) for Point2 in (input("Enter point 2 (latitude and longitude) in degrees: ")).split(",")]
# Convert the values from degrees to radians
x1, x2 = math.radians(x1), math.radians(x2)
y1, y2 = math.radians(y1), math.radians(y2)
# Compute using the given formula
Radius = 6371.01
D = Radius * acos(sin(x1) * sin(x2) + cos(x1) * cos(x2) * cos(y1 - y2))
# Display the result
print("The distance between the two points is", D, "km")
