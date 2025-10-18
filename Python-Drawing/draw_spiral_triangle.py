# Draw Spiral Triangle
import turtle


def draw_spiral(far, cost):
    if far > 0:
        turtle.forward(far)
        turtle.right(cost)
        draw_spiral(far - 5, cost)


screen = turtle.Screen().bgcolor("black")
turtle.reset()
turtle.pencolor("green")
turtle.pen(speed=10)
turtle.delay(10)
length = 500
turn_by = 121
turtle.penup()
turtle.setpos(-length/2, length/2)
turtle.pendown()

draw_spiral(length, turn_by)
turtle.hideturtle()
turtle.done()
