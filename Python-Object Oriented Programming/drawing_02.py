# Class Abstract Drawing Class
# With inheritance and abstract class
# Using Tkinter
from abc import ABC, abstractmethod
from tkinter import *
from math import sqrt


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
    def draw(self, canvas):
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

    def draw(self, canvas):
        print(self.__str__())
        # Draw a circle
        x0 = self.X - self.Radius
        y0 = self.Y - self.Radius
        x1 = self.X + self.Radius
        y1 = self.Y + self.Radius
        canvas.create_oval(x0, y0, x1, y1, fill="white", outline=self.Color)


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

    def draw(self, canvas):
        print(self.__str__())
        x0 = self.X
        y0 = self.Y
        x1 = self.X + self.Width
        y1 = self.Y + self.Height
        canvas.create_rectangle(x0, y0, x1, y1, fill="white", outline=self.Color)


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
    def __init__(self, x1=1.0, y1=1.0, x2=1.0, y2=1.0, x3=1.0, y3=1.0, color='black'):
        super().__init__(0, 0, color)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def __str__(self):
        return (f"Triangle: at A(x1={self.x1}, y1={self.y1}); "
                f"B(x2={self.x2}, y2={self.y2}); "
                f"C(x3={self.x3}, y3={self.y3})")

    def draw(self, canvas):
        # Triangle is drawn based on coordinates
        print(self.__str__())
        x1, y1 = self.x1, self.y1
        x2, y2 = self.x2, self.y2
        x3, y3 = self.x3, self.y3
        points = [x1, y1, x2, y2, x3, y3]
        canvas.create_polygon(points, fill='white', outline=self.Color)

    def get_edges(self):  # Optional: Get size with the coordinates
        edge1 = sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        edge2 = sqrt((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2)
        edge3 = sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2)
        return f"Edge1: {edge1}, Edge2: {edge2}, Edge3: {edge3}"


def main():
    # Initial window
    screen = Tk()
    screen.geometry("600x400")
    screen.resizable(False, False)
    screen['bg'] = 'white'
    # Canvas object
    canvas = Canvas(screen, width=400, height=400, bg="white", borderwidth=0, highlightthickness=0)
    canvas.pack()
    # Draw objects
    rectangle1 = Rectangle(25, 45, 200, 300, 'red')
    rectangle1.draw(canvas)
    rectangle2 = Rectangle(25, 45, 140, 200, 'red')
    rectangle2.draw(canvas)
    square1 = Square(160, 125, 80, 'green')
    square1.draw(canvas)
    circle1 = Circle(105, 105, 50, 'blue')
    circle1.draw(canvas)
    circle2 = Circle(105, 100, 25, 'blue')
    circle2.draw(canvas)
    triangle1 = Triangle(150, 300, 60, 300, 100,230, "black")
    triangle1.draw(canvas)
    print(triangle1.get_edges())
    screen.mainloop()


main()
