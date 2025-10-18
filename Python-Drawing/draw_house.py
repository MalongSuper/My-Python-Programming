import turtle
import math

screen = turtle.Screen().bgcolor("black")
turtle.speed(18)
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
turtle.width(5)
turtle.speed(2)
turtle.color("white", "orange")
turtle.begin_fill()

# Rectangle
for _ in range(2):
    turtle.forward(300)
    turtle.left(90)
    turtle.forward(170)
    turtle.left(90)
turtle.end_fill()

# Door
turtle.forward(115)
turtle.color("white", "red")
turtle.begin_fill()
turtle.left(90)
turtle.forward(90)
turtle.right(90)
turtle.forward(70)
turtle.right(90)
turtle.forward(90)
turtle.end_fill()
turtle.left(90)
turtle.forward(115)
turtle.left(90)
turtle.forward(172)

# Triangle
turtle.begin_fill()
turtle.left(45)
turtle.forward(210)
turtle.left(90)
turtle.forward(210)
turtle.end_fill()

turtle.hideturtle()

turtle.done()
