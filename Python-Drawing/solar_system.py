# This program simulates a Solar System
import turtle as tr
from math import *
# Create GUI Screen
screen = tr.Screen()
screen.tracer(50)
screen.title("Solar System")

# Create the sun
sun = tr.Turtle()
sun.shape('circle')
sun.color('yellow')


# Create the planets
class Planet(tr.Turtle):
    def __init__(self, name, radius, color):  # Initialize function
        super().__init__(shape='circle')
        self.name = name
        self.radius = radius
        self.c = color
        self.color(self.c)
        self.up()
        self.pd()
        self.angle = 0

    def move(self):
        x = self.radius * cos(self.angle)  # Angle in radians
        y = self.radius * sin(self.angle)
        self.goto(sun.xcor() + x, sun.ycor() + y)


def main():
    # Making the planets
    mercury = Planet("Mercury", 40, 'light blue')
    venus = Planet("Venus", 80, 'orange')
    earth = Planet("Earth", 100, 'blue')
    mars = Planet("Mars", 150, 'red')
    jupiter = Planet("Jupiter", 180, 'green')
    saturn = Planet("Saturn", 230, 'purple')
    uranus = Planet("Uranus", 250, 'dark blue')
    neptune = Planet("Neptune", 280, "dark green")

    # Create a list of planets
    planets_list = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

    while True:
        screen.update()  # Update the scree
        for planet in planets_list:
            planet.move()  # Move the elements of the list

        # Increase the angle by 0.0x radians
        mercury.angle += 0.05
        venus.angle += 0.03
        earth.angle += 0.01
        mars.angle += 0.007
        jupiter.angle += 0.02
        saturn.angle += 0.018
        uranus.angle += 0.016
        neptune.angle += 0.005


main()

