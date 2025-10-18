# Draw Virus
import turtle
# Initial window screen
screen = turtle.Screen().bgcolor("black")
turtle.goto(0, 200)
a, b = 0, 0
turtle.speed(10)
turtle.pencolor('green')
while True:
    turtle.forward(a)
    turtle.right(b)
    a = a + 3
    b = b + 1
    if b == 210:
        break
    turtle.hideturtle()
# Maintain the visibility of the program
turtle.done()
