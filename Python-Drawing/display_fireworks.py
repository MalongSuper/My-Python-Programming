# Display fireworks
import turtle
import random

# Main screen
screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor('black')
screen.title("New Year Firework")

my_turtle = turtle.Turtle()
my_turtle.speed(0)
my_turtle.hideturtle()
# Colors for fireworks
colors = ['blue', 'red', 'yellow', 'orange',
          'purple', 'magenta', 'pink', 'lime',
          'green', 'gold', 'silver', 'violet']


def draw_firework(t):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(random.choice(colors))  # Randomize the colors
    d = random.randint(20, 100)

    for i in range(36):
        t.forward(d)
        t.backward(d)
        t.right(10)


def main():
    for i in range(10):
        draw_firework(my_turtle)

    # Display "Happy New Year" message
    my_turtle.penup()
    my_turtle.goto(0, 200)
    my_turtle.color('white')
    my_turtle.write("HAPPY NEW YEAR",
                    align="center", font=("Verdana", 24, "normal"))
    screen.mainloop()


main()
