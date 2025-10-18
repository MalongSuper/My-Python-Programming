# Superclass Circle and Subclass Cylinder
import math


class Circle:
    def __init__(self, radius=1.0, color="red"):
        self.__radius = radius
        self.__color = color

    @property
    def Radius(self):
        return self.__radius

    @Radius.setter
    def Radius(self, radius):
        self.__radius = radius

    @property
    def Color(self):
        return self.__color

    @Color.setter
    def Color(self, color):
        self.__color = color

    @property
    def Area(self):
        return self.__radius * self.__radius * math.pi

    # Replace to_string() to __str__
    def __str__(self):
        return f"Circle[Radius = {self.__radius}, Color = {self.__color}]"


class Cylinder(Circle):
    def __init__(self, radius=1.0, height=1.0):
        # Use the radius in the superclass
        super().__init__(radius)
        self.__height = height

    @property
    def Height(self):
        return self.__height

    @Height.setter
    def Height(self, height):
        self.__height = height

    @property
    def Volume(self):
        # Since Cylinder has inherited from Circle
        # the Area can be used as an attribute for Cylinder
        # self.Area is accessible
        return super().Area * self.__height

    @property
    def Area(self):  # Overriding Area for surface area of the cylinder
        return (2 * math.pi * self.Radius *
                (self.Radius + self.__height))

    # With this line, the self.Area above will use this Area
    # When it is supposed to use the area of the circle
    # So, in the volume function, replace self.Area with super().Area
    # Make sure that the Area of the superclass Circle is used


def TestCylinder():
    c1 = Cylinder()
    print(f"Radius: {c1.Radius}, Height {c1.Height}, "
          f"SurfaceArea: {c1.Area}, Volume: {c1.Volume}")
    c2 = Cylinder(height=10.0)
    # c2 = Cylinder(10.0) is radius = 10.0
    print(f"Radius: {c2.Radius}, Height {c2.Height}, "
          f"SurfaceArea: {c2.Area}, Volume: {c2.Volume}")
    c3 = Cylinder(2.0, 10.0)
    print(f"Radius: {c3.Radius}, Height {c3.Height}, "
          f"SurfaceArea: {c3.Area}, Volume: {c3.Volume}")


# Run the main function
TestCylinder()
