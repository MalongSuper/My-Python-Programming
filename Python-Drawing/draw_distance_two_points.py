# This program computes distance of two points
# Then draw them in turtle
import turtle
import math
# Enter two points
print("Draw distance of two points")
x1, y1 = eval(input("Enter (x1, y1) for Point 1: "))
x2, y2 = eval(input("Enter (x2, y2) for Point 2: "))
# Compute the distance
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("Distance:", distance)
# Display two points
turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.write("P1")  # Point 1
turtle.goto(x2, y2)
turtle.write("P2")  # Point 2
# Move to the center point of the line
turtle.penup()
turtle.goto((x1 + x2) / 2, (y1 + y2) / 2)
turtle.write(distance)

turtle.done()
