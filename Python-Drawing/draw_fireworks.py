# New Year 2025 Fireworks
import turtle
import random

turtle.Screen().bgcolor("black")


def pen(color):
    turtle.color(color)


def fireworks(distance):
    for _ in range(20):
        turtle.forward(distance)
        turtle.right(180-(360/20))


def move():  # Move the firework in random coordinates
    turtle.penup()
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    turtle.goto(x, y)
    turtle.pendown()


def display():
    turtle.penup()
    turtle.goto(0, 300)
    turtle.color('white')
    turtle.write("HAPPY NEW YEAR 2025",
                 align="center", font=("Verdana", 24, "normal"))


turtle.speed(0)
colors = ["red", "purple", "green", "blue", "orange", "yellow", "cyan"]
for i in range(30):
    color = random.choice(colors)
    pen(color)
    fireworks(random.randint(50, 100))
    move()

display()
turtle.hideturtle()
turtle.done()
