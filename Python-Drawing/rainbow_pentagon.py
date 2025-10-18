# Draw a rainbow pentagon
import turtle
t = turtle.Turtle()
turtle.title("Rainbow Pentagon")
turtle.bgcolor("black")
t.speed(0.5)
colors = ["red", "yellow", "blue", "green", "yellow", "orange"]
for i in range(300):
    t.pencolor(colors[i % 6])
    t.forward(i * 2)
    t.right(61)
turtle.done()
