# Superclass Rectangle and Subclass Box
# Class TestBox to test


class Rectangle:
    def __init__(self, length=0.0, width=0.0):
        self.__length = length
        self.__width = width
        # Default length or width as 0
        # if the value is negative
        if self.__length < 0:
            self.__length = 0.0
        if self.__width < 0:
            self.__width = 0.0

    @property
    def Length(self):
        return self.__length

    @Length.setter
    def Length(self, length):
        if length < 0:
            length = 0.0
        self.__length = length

    @property
    def Width(self):
        return self.__width

    @Width.setter
    def Width(self, width):
        if width < 0:
            width = 0.0
        self.__width = width

    # Protected functions
    def _GetArea(self):
        return self.__length * self.__width

    def _GetPerimeter(self):
        return (self.__length + self.__width) * 2

    def toString(self):
        return f"({self.__length}, {self.__width})"


class Box(Rectangle):  # Inheritance: Rectangle
    def __init__(self, length=0.0, width=0.0, height=0.0):
        super().__init__(length, width)
        self.__height = height
        if height < 0:
            self.__height = 0.0

    @property
    def Height(self):
        return self.__height

    @Height.setter
    def Height(self, height):
        if height < 0:
            self.__height = 0.0
        self.__height = height

    # Override _GetArea function
    def _GetArea(self):
        return 2 * (self.Length * self.Width
                    + self.Width * self.Height
                    + self.Height * self.Length)

    def _GetVolume(self):
        return self.Length * self.Width * self.Height

    # Override toString function
    def toString(self):
        return f"({self.Length}, {self.Width}, {self.Height})"


class TestBox(Box):
    # TestBox(Rectangle, Box) is inconsistent and redundant
    # As the length in the Rectangle is already inherited to the Box
    # Thus, we only need to inherit the TestBox class to the Box class
    def __init__(self, length=0.0, width=0.0, height=0.0):
        # Call the superclasses
        super().__init__(length, width, height)

    # We want to get the Area and Perimeter of Rectangle
    # Here, we call the Box as the superclass of TextBox
    # _GetArea is the overriding method of Box to Rectangle
    # super()._GetArea gets the area of the Box
    # self._GetArea() also gets the area of the Box
    def GetRectangleArea(self):
        # This call gets the area of the rectangle
        return Rectangle._GetArea(self)

    def GetRectanglePerimeter(self):
        return Rectangle._GetPerimeter(self)

    def GetBoxArea(self):
        return self._GetArea()

    def GetBoxVolume(self):
        return self._GetVolume()

    def GetRectangle(self):
        return Rectangle.toString(self)

    def GetBox(self):
        return self.toString()


def main():
    rectangle = TestBox(10, 3)
    print("Rectangle:", rectangle.GetRectangle())
    print("- Perimeter:", rectangle.GetRectanglePerimeter())
    print("- Area:", rectangle.GetRectangleArea())
    box = TestBox(2, 4, 6)
    print("Box:", box.GetBox())
    print("- Area:", box.GetBoxArea())
    print("- Volume:", box.GetBoxVolume())


main()
