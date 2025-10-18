# Draw Christmas Tree
from turtle import *
from math import sin, cos
from random import randint
from time import perf_counter

bgcolor(0, 0, 0)
setup(500, 500)
hideturtle()
title("Christmas Tree")
tracer(False)
penup()


def star(x=0, y=0, size=100, points=5):
    goto(x, y)
    angle = 360 / points
    outer_radius = size
    inner_radius = size / 2

    begin_fill()
    for _ in range(points * 2):
        forward(outer_radius) if _ % 2 == 0 else forward(inner_radius)
        left(angle)
    end_fill()


def rect(x=0, y=0, w=100):
    goto(x, y)
    begin_fill()
    [forward(w) or left(90) for _ in range(4)]
    end_fill()


def snowflake(x, y):
    color(1, 1, 1)
    size = randint(5, 15)
    rect(x, y, size)


def _loop():
    update()
    clear()

    t = perf_counter() / 2

    for i in range(200):
        a = i + t + sin(t * 2)
        y = -25 * i ** 0.5
        w = (5 + 4 * sin(8 * t * cos(i ** 5))) * (1 + cos(a))
        color(1, 0.1, 0.2) if i % 2 else color(1, 1, 1)
        (i == 0) and color(1, 1, 0)
        star(y * sin(a) / 2 - w / 2, 200 + y + y * cos(a) / 9 - w / 2, int(w), points=3)
    for _ in range(10):
        snowflake(randint(-250, 250), randint(0, 250))

    ontimer(_loop, 30)


_loop()


mainloop()
