# This program draws lines based on arrow keys
import turtle

screen = turtle.Screen()
head = turtle.Turtle()
pen = turtle.Turtle()
# Head is for telling which key is pressed
head.penup()
head.hideturtle()
# Initial coordinate for head
head.goto(0, 260)
head.write("Press any arrow key (W, A, S, D) in the keyboard",
           align="center", font=("Calibri", 24, "normal"))


# These functions handle which button is pressed
def front():
    y = pen.ycor()
    pen.sety(y + 100)
    head.clear()
    head.write("UP", align="center",
               font=("Calibri", 24, "normal"))


def back():
    y = pen.ycor()
    pen.sety(y - 100)
    head.clear()
    head.write("DOWN", align="center",
               font=("Calibri", 24, "normal"))


def left():
    x = pen.xcor()
    pen.setx(x - 100)
    head.clear()
    head.write("LEFT", align="center",
               font=("Calibri", 24, "normal"))


def right():
    x = pen.xcor()
    pen.setx(x + 100)
    head.clear()
    head.write("RIGHT", align="center",
               font=("Calibri", 24, "normal"))


# Trigger which button is pressed
screen.listen()  # screen.listen(): listens for screen inputs
screen.onkeypress(front, "w")  # When "W" is pressed, go up
screen.onkeypress(back, "s")  # When "S" is pressed, go down
screen.onkeypress(left, "a")  # When "A" is pressed, go left
screen.onkeypress(right, "d")  # When "D" is pressed, go right

turtle.mainloop()
