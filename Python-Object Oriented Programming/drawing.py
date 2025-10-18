# Class Abstract Drawing Class
# With inheritance and abstract class
from abc import ABC, abstractmethod
import turtle
import math


class Shape(ABC):
    def __init__(self, x=1.0, y=1.0, color='black'):
        self.__x = x
        self.__y = y
        self.__color = color
        print("Shape created")

    @property
    def X(self):
        return self.__x

    @X.setter
    def X(self, x):
        self.__x = x

    @property
    def Y(self):
        return self.__y

    @Y.setter
    def Y(self, y):
        self.__y = y

    @property
    def Color(self):
        return self.__color

    @Color.setter
    def Color(self, color):
        self.__color = color

    @abstractmethod
    def draw(self):
        return NotImplemented


class Circle(Shape):
    def __init__(self, x=1.0, y=1.0, radius=1.0, color='black'):
        super().__init__(x, y, color)
        self.__radius = radius

    def __str__(self):
        return f"Circle: at x={self.X}, y={self.Y}, radius={self.Radius}"

    @property
    def Radius(self):
        return self.__radius

    @Radius.setter
    def Radius(self, radius):
        self.__radius = radius

    def draw(self):
        print(self.__str__())
        turtle.hideturtle()
        turtle.penup()
        turtle.color(self.Color)
        turtle.goto(self.X, self.Y)
        turtle.pendown()
        # Drawing
        turtle.circle(self.Radius)


class Rectangle(Shape):
    def __init__(self, x=1.0, y=1.0, width=1.0, height=1.0, color='black'):
        super().__init__(x, y, color)
        self.__width = width
        self.__height = height

    def __str__(self):
        return (f"Rectangle: at x={self.X}, y={self.Y}, "
                f"width={self.Width}, height={self.Height}")

    @property
    def Width(self):
        return self.__width

    @Width.setter
    def Width(self, width):
        self.__width = width

    @property
    def Height(self):
        return self.__height

    @Height.setter
    def Height(self, height):
        self.__height = height

    def draw(self):
        print(self.__str__())
        turtle.hideturtle()
        turtle.penup()
        turtle.color(self.Color)
        turtle.goto(self.X, self.Y)
        turtle.pendown()
        # Drawing
        turtle.left(90)
        turtle.forward(self.Width)
        turtle.right(90)
        turtle.forward(self.Height)
        turtle.right(90)
        turtle.forward(self.Width)
        turtle.right(90)
        turtle.forward(self.Height)


class Square(Rectangle):
    def __init__(self, x=1.0, y=1.0, side=1.0, color='black'):
        super().__init__(x, y, side, side, color)
        self.__side = side

    def __str__(self):
        return (f"Square: at x={self.X}, y={self.Y}, "
                f"side={self.Side}")

    @property
    def Side(self):
        return self.__side

    @Side.setter
    def Side(self, side):
        self.__side = side


class Triangle(Shape):
    def __init__(self, x=1.0, y=1.0, edge1=1.0, edge2=1.0, edge3=1.0, color='black'):
        super().__init__(x, y, color)
        self.__edge1 = edge1
        self.__edge2 = edge2
        self.__edge3 = edge3

    def __str__(self):
        return (f"Triangle: at x={self.X}, y={self.Y}, "
                f"edge1={self.Edge1}, edge2={self.Edge2}, edge3={self.Edge3}")

    @property
    def Edge1(self):
        return self.__edge1

    @Edge1.setter
    def Edge1(self, edge1):
        self.__edge1 = edge1

    @property
    def Edge2(self):
        return self.__edge2

    @Edge2.setter
    def Edge2(self, edge2):
        self.__edge2 = edge2

    @property
    def Edge3(self):
        return self.__edge3

    @Edge3.setter
    def Edge3(self, edge3):
        self.__edge3 = edge3

    def draw(self):
        # We need to use the law of cosine to
        # determine the angle to draw the triangle
        print(self.__str__())
        a, b, c = self.Edge1, self.Edge2, self.Edge3
        # cos(A) = (b**2 + c**2 - a**2) / (2 * b * c)
        # cos(B) = (a**2 + c**2 - b**2) / (2 * a * c)
        # cos(C) = (b**2 + a** 2 - c**2) / (2 * a * b)
        angleA = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
        angleB = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
        angleC = math.degrees(math.acos((b**2 + a** 2 - c**2) / (2 * a * b)))
        turtle.penup()
        turtle.goto(self.X, self.Y)
        turtle.color(self.Color)
        turtle.pendown()
        # Drawing
        # The first side
        turtle.forward(self.Edge1)
        # Turn right to draw the second side
        turtle.right(180 - angleC)
        turtle.forward(self.Edge2)
        # Turn right to draw the third side
        turtle.right(180 - angleA)
        turtle.forward(self.Edge3)
        # Optional line
        turtle.right(180 - angleB)
        turtle.hideturtle()


def main():
    circle1 = Circle(105, 105, 50, 'blue')
    circle1.draw()
    circle2 = Circle(105, 130, 25, 'blue')
    circle2.draw()
    rectangle1 = Rectangle(25, 45, 200, 300, 'red')
    rectangle1.draw()
    rectangle2 = Rectangle(250, 210, 120, 200, 'red')
    rectangle2.draw()
    square1 = Square(160, 105, 80, 'green')
    square1.draw()
    triangle1 = Triangle(150, 150, 90, 60, 60, "black")
    triangle1.draw()
    # Finalize the turtle window
    turtle.done()


main()
