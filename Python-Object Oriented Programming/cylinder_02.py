# Class Cylinder Has-A Relationship with Circle
# Has-A Relationship is different from Is-A Relationship
# Is-A Relationship: Simply one subclass inherits from a superclass
# For example: Class Shape then Class Circle(Shape)
# Has-A Relationship: One class is used inside another
# In essence, it can be considered as Circle as
# a data type (similar to class/string type) used in the Cylinder Class.

class Circle:
    def __init__(self, radius=1.0, color="red"):
        self.radius = radius
        self.color = color

    def __str__(self):
        return f"Radius = {self.radius}, Color = {self.color}"


class Cylinder:  # The base: Circle
    def __init__(self, base: Circle, height=1.0):
        self.base = base
        self.height = height

    def __str__(self):
        return (f"Radius = {self.base.radius}, "
                f"Color = {self.base.color}, "
                f"Height = {self.height}")


def main():
    base_circle = Circle()  # Circle object
    # Assign to the cylinder object
    cylinder = Cylinder(base_circle, height=12)
    print("Cylinder:", cylinder)


main()
