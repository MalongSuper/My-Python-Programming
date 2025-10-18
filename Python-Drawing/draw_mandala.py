# Draw a Mandala
import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Mandala")
pen = turtle.Turtle()
pen.speed(0.5)
pen.width(2)

# Draw Mandala
colors = ["#FF4500", "#FFD700", "#8A2BE2", "#32CD32", "#00BFFF"]
for _ in range(36):  # 36 sections for a Circular Mandala
    pen.color(random.choice(colors))
    pen.circle(120)  # Adjust radius for circle
    pen.right(10)  # Small rotation after each circle

turtle.done()
