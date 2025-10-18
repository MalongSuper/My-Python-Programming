# Draw Circular Star - Vietnam Flag
import turtle


def draw_star(size, color):
    angle = 145
    turtle.fillcolor(color)
    turtle.begin_fill()

    for side in range(5):
        turtle.forward(size)
        turtle.right(angle)
        turtle.forward(size)
        turtle.right(72 - angle)
    turtle.end_fill()
    return


def draw_rectangle(h, w, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(w)
    turtle.right(90)
    turtle.forward(h)
    turtle.right(90)
    turtle.forward(w)
    turtle.right(90)
    turtle.forward(h)
    turtle.end_fill()
    return


# Draw star and rectangle
turtle.penup()
turtle.goto(-200, -50)
turtle.pendown()
draw_rectangle(400, 280, "red")
turtle.penup()
turtle.goto(-24, 120)
turtle.pendown()
turtle.right(108)
draw_star(80, "yellow")

turtle.penup()
turtle.goto(-5, -100)
turtle.write("HAPPY 80TH INDEPENDENCE DAY OF VIETNAM",
             align="center", font=("Verdana", 22, "normal"))
turtle.pendown()

turtle.penup()
turtle.goto(-12, -140)
turtle.write("2/9/1945 - 2/9/2025",
             align="center", font=("Verdana", 22, "normal"))
turtle.pendown()


turtle.hideturtle()
turtle.done()
