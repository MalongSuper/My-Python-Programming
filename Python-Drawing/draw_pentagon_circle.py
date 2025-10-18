# Draw Pentagon Circle
import turtle
import random
screen = turtle.Screen().bgcolor("black")
colors = ["red", "purple", "blue", "green", "orange", "yellow", "magenta", "cyan"]
turtle.speed(30)

for i in range(36):
    choice = random.choice(colors)
    turtle.pencolor(choice)
    turtle.forward(100)
    for _ in range(5):
        turtle.forward(30)
        turtle.right(360/5)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.right(10)

turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
for i in range(50):
    turtle.pencolor("purple")
    turtle.circle(100+i, 45)

turtle.hideturtle()
turtle.done()
