# Draw the Olympic Games logo
import turtle

turtle.color("blue")
turtle.penup()  # penup(): Pick the pen up
turtle.goto(-150, 25)  # goto(): Move the pen to a different position
turtle.pendown()   # pendown(): Mark the pen into the target for drawing
turtle.circle(45)

turtle.color("black")
turtle.penup()
turtle.goto(-50, 25)
turtle.pendown()
turtle.circle(45)

turtle.color("red")
turtle.penup()
turtle.goto(50, 25)
turtle.pendown()
turtle.circle(45)

turtle.color("green")
turtle.penup()
turtle.goto(0, -25)
turtle.pendown()
turtle.circle(45)

turtle.color("#D5B60A")  # Dark Yellow
turtle.penup()
turtle.goto(-100, -25)
turtle.pendown()
turtle.circle(45)

turtle.hideturtle()

turtle.done()
