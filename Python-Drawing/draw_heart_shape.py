import turtle

turtle.bgcolor('pink')


def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)


def heart():
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(113)
    curve()
    turtle.left(120)
    curve()
    turtle.forward(111)
    turtle.end_fill()


def text():
    turtle.penup()
    turtle.goto(0, 200)
    turtle.color('red')
    turtle.write("HAPPY VALENTINE'S DAY",
                 align="center", font=("Verdana", 24, "normal"))


heart()
text()
turtle.hideturtle()
turtle.done()
