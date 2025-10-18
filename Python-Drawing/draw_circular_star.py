# Draw Circular Star
import turtle

screen = turtle.Screen().bgcolor("black")
turtle.color("red", "yellow")

turtle.begin_fill()
while True:
    turtle.forward(250)
    turtle.left(170)
    if abs(turtle.pos()) < 1:
        break
turtle.end_fill()

turtle.hideturtle()
turtle.done()
