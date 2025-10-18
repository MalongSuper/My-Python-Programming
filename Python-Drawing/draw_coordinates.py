# This program display co-ordinates upon clicking
import turtle


def button_click(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(f"{x}: {y}")


# Trigger clicking the screen
turtle.onscreenclick(button_click, 1)
turtle.listen()  # listen to incoming connections
turtle.speed(10)

turtle.done()
