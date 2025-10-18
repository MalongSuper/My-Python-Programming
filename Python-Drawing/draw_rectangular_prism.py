# Draw a Rectangular Prism (Cuboid)
import turtle

# Move the pen
turtle.penup()
turtle.goto(-150, 25)
turtle.pendown()
# Draw the upper rectangle
turtle.left(50)
turtle.forward(100)
turtle.right(50)
turtle.forward(250)
turtle.right(125)
turtle.forward(95)
turtle.right(55)
turtle.forward(260)
# From that rectangle draw the first side rectangle
turtle.left(90)
turtle.forward(120)
turtle.left(90)
turtle.forward(260)
turtle.left(90)
turtle.forward(120)
# Move to the corner of the upper rectangle
# to draw the second side rectangle
turtle.penup()
turtle.goto(165, 102)
turtle.pendown()
turtle.left(180)
turtle.forward(120)
turtle.right(35)
turtle.forward(95)
# Move to the corner of the upper rectangle
# to draw the third side rectangle
turtle.right(145)
turtle.penup()
turtle.goto(-85, 102)
turtle.pendown()
turtle.right(180)
turtle.forward(120)
turtle.right(40)
turtle.forward(100)
# Move to the corner of the side rectangle
# to draw the final side rectangle
turtle.right(145)
turtle.penup()
turtle.goto(-85, -18)
turtle.pendown()
turtle.right(85)
turtle.forward(250)
turtle.hideturtle()

turtle.done()
