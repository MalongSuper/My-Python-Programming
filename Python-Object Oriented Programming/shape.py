# Superclass Shape, with Subclasses Rectangle, Square, Circle
from math import pi


class Shape:
    def __init__(self, color='red', filled=True):
        self.__color = color
        self.__filled = filled

    @property
    def Color(self):
        return self.__color

    @Color.setter
    def Color(self, color):
        self.__color = color

    @property
    def Filled(self):
        return self.__filled

    @Filled.setter
    def Filled(self, filled):
        self.__filled = filled

    def __str__(self):
        return (f"Shape[color={self.__color}, "
                f"filled={self.__filled}]")


class Circle(Shape):
    def __init__(self, radius=1.0):
        super().__init__()
        self.__radius = radius

    @property
    def Radius(self):
        return self.__radius

    @Radius.setter
    def Radius(self, radius):
        self.__radius = radius

    def getArea(self):
        return self.__radius * self.__radius * pi

    def getPerimeter(self):
        return 2 * self.__radius * pi

    def __str__(self):
        return (f"Circle[Shape[color={self.Color}, "
                f"filled={self.Filled}], radius={self.__radius}]")


class Rectangle(Shape):
    def __init__(self, width=1.0, length=1.0):
        super().__init__()
        self.__width = width
        self.__length = length

    @property
    def Width(self):
        return self.__width

    @Width.setter
    def Width(self, width):
        self.__width = width

    @property
    def Length(self):
        return self.__length

    @Length.setter
    def Length(self, length):
        self.__length = length

    def getArea(self):
        return self.__width * self.__length

    def getPerimeter(self):
        return 2 * (self.__width + self.__length)

    def __str__(self):
        return (f"Rectangle[Shape[color={self.Color}, "
                f"filled={self.Filled}], width={self.__width}, "
                f"length={self.__length}]")


class Square(Rectangle):
    def __init__(self, side=1.0):
        super().__init__(side, side)
        self.__side = side

    @property
    def Side(self):
        return self.__side

    @Side.setter
    def Side(self, side):
        self.__side = side

    # Overridden Width and Length
    @property
    def Width(self):
        return self.__side

    @Width.setter
    def Width(self, width):
        self.__side = width

    @property
    def Length(self):
        return self.__side

    @Length.setter
    def Length(self, length):
        self.__side = length

    # Overridden getArea(self), getPerimeter(self)
    def getArea(self):
        # Or self.Width * self.Length
        return self.__side * self.__side

    def getPerimeter(self):
        # Or 2 * (self.Width + self.Length)
        return 4 * self.__side

    def __str__(self):
        return (f"Square[Rectangle[Shape[color={self.Color}, "
                f"filled={self.Filled}], width={self.Width}, "
                f"length={self.Length}]")


def main():
    circle = Circle(4)
    rect = Rectangle(4.5, 6)
    square = Square(3)
    print(circle)
    print(rect)
    print(square)
    square.Width = 4
    print(square)
    square.Length = 5
    print(square)
    # Compute
    print("Circle Area:", circle.getArea())
    print("Circle Perimeter:", circle.getPerimeter())
    print("Rectangle Area:", rect.getArea())
    print("Rectangle Perimeter:", rect.getPerimeter())
    print("Square Area:", square.getArea())
    print("Square Perimeter:", square.getPerimeter())


main()
