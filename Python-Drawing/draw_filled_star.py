# Draw a filled star
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
    turtle.hideturtle()
    turtle.done()
    return


size = float(input("Size: "))
color = input("Fill with: ")
draw_star(size, color)
