# Superclass Shape, with Subclasses Rectangle, Square, Circle
# With TestShape --> take user's input
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


# This class tests all the methods in all the above classes
class TestShape:
    def testShape(self):
        shape = Shape()
        color = str(input("Enter color: "))
        filled = int(input("Is the shape filled or not filled (yes-1, no-0): "))
        if filled not in [0, 1]:
            raise Exception(f"Invalid Input for filled = {filled}")
        shape.Color = color
        shape.Filled = filled
        print(shape)

    def testCircle(self):
        circle = Circle()
        radius = float(input("Enter Radius: "))
        circle.Radius = radius
        print(circle)
        print("Circle Area:", circle.getArea())
        print("Circle Perimeter:", circle.getPerimeter())

    def testRectangle(self):
        rectangle = Rectangle()
        width, length = map(float, input("Enter Width, Length: ").split(","))
        rectangle.Width = width
        rectangle.Length = length
        print(rectangle)
        print("Rectangle Area:", rectangle.getArea())
        print("Rectangle Perimeter:", rectangle.getPerimeter())

    def testSquare(self):
        square = Square()
        side = float(input("Enter side: "))
        square.Side = side
        print(square)
        print("Square Area:", square.getArea())
        print("Square Perimeter:", square.getPerimeter())


def main():
    # Call the TestShape
    # Select a shape
    print("0 - Shape, 1 - Circle, 2 - Rectangle, 3 - Square")
    option = int(input("Select shape (0-3): "))
    test_shape = TestShape()
    if option == 0:
        test_shape.testShape()
    if option == 1:
        test_shape.testCircle()
    if option == 2:
        test_shape.testRectangle()
    if option == 3:
        test_shape.testSquare()


main()
