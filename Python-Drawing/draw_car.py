# Draw a simple car
import turtle

screen = turtle.Screen().bgcolor("light green")
turtle.width(6)


def circle():  # Draw a circle
    turtle.pendown()
    turtle.color("black", "orange")
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    turtle.penup()


turtle.penup()
turtle.setx(-200)
turtle.sety(0)
turtle.pendown()
turtle.forward(50)
turtle.penup()
turtle.goto(-100, -50)
circle()
turtle.penup()
turtle.setx(-50)
turtle.sety(0)
turtle.pendown()
turtle.forward(100)
turtle.penup()
turtle.goto(100, -50)
circle()

for i in range(10):  # Draw lines in circle
    turtle.penup()
    turtle.goto(-100, 0)
    turtle.pendown()
    turtle.left(36)
    turtle.forward(50)

for j in range(10):  # Draw lines in circle
    turtle.penup()
    turtle.goto(100, 0)
    turtle.pendown()
    turtle.left(36)
    turtle.forward(50)

# Draw the body of the car
turtle.forward(50)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(80)
turtle.right(45)
turtle.forward(100)
turtle.left(45)
turtle.forward(100)
turtle.left(45)
turtle.forward(100)
turtle.left(135)
turtle.forward(120)
turtle.left(90)
turtle.forward(70)
turtle.left(180)
turtle.forward(70)
turtle.left(90)
turtle.forward(120)
turtle.penup()
turtle.goto(-120, 100)
turtle.pendown()
turtle.left(180)
turtle.forward(80)
turtle.left(90)
turtle.forward(100)
# Draw a road line
turtle.penup()
turtle.goto(-250, -50)
turtle.pendown()
turtle.left(90)
turtle.forward(500)

turtle.hideturtle()
turtle.done()
