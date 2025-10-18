# Superclass GeometricObject and Subclasses Rectangle and Circle
# Inheritance classes
# from GeometricObject import GeometricObject
import math


class GeometricObject:  # This is the superclass
    def __init__(self, color='blue', filled=True):
        self.__color = color
        self.__filled = filled

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def is_filled(self):
        return self.__filled

    def set_filled(self, filled):
        self.__filled = filled

    def __str__(self):
        return 'color:' + self.__color + ', filled: ' + str(self.__filled)


class Circle(GeometricObject):  # Subclass Circle
    def __init__(self, radius):
        # Call the __init__ method from the superclass
        super().__init__()  # Without this line, error will occur
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def get_area(self):
        return self.__radius * self.__radius * math.pi

    def get_diameter(self):
        return 2 * self.__radius

    def get_perimeter(self):
        return 2 * self.__radius * math.pi

    def print_circle(self):
        print(self.__str__() + 'radius: ' + str(self.__radius))


class Rectangle(GeometricObject):  # Subclass Rectangle
    def __init__(self, width=1, height=1):
        super().__init__()
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def get_area(self):
        return self.__width * self.__height

    def get_perimeter(self):
        return 2 * (self.__width + self.__height)


def main():
    # Input
    r = float(input("(Circle) Enter a Radius: "))
    w, h = map(float, input("(Rectangle) Enter Width, Height: ").split(","))
    # Circle
    circle = Circle(r)
    print('\nA Circle', circle)
    print("The radius is", circle.get_radius())
    print("The area is", circle.get_area())
    print("The diameter is", circle.get_perimeter())
    # Rectangle
    rectangle = Rectangle(w, h)
    print("\nA rectangle", rectangle)
    print("The area is", rectangle.get_area())
    print("The diameter is", rectangle.get_perimeter())


main()
