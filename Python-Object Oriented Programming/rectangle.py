# Class Rectangle

class Rectangle:
    def __init__(self, length=1.0, width=1.0):  # Initial values
        print("A rectangle is successfully initiated")
        self.length = length
        self.width = width

    def get_length(self):  # Get the length
        return self.length

    def set_length(self, length):  # Change the length of the instance
        self.length = length

    def get_width(self):  # Get the width
        return self.width

    def set_width(self, width):  # Change the width of the instance
        self.width = width

    def get_area(self):
        return self.width * self.length

    def get_perimeter(self):
        return 2 * (self.width + self.length)

    def to_string(self):  # Display the information as String
        print(f"Rectangle["
              f"Length = {str(self.length)}, "
              f"Width = {str(self.width)}, "
              f"Area = {self.get_area()}, "
              f"Perimeter = {self.get_perimeter()}]")


def main():
    rect = Rectangle(12, 24)
    print(f"Length: {rect.get_length()}, Width: {rect.get_width()}")
    print(f"Area: {rect.get_area()}")
    print(f"Perimeter: {rect.get_perimeter()}")
    # Display everything as string
    rect.to_string()
    # Set a different length and width
    rect = Rectangle(12, 24)
    rect.set_length(15.5)
    rect.set_width(30)
    print(f"Length: {rect.get_length()}, Width: {rect.get_width()}")
    print(f"Area: {rect.get_area()}")
    print(f"Perimeter: {rect.get_perimeter()}")
    # Display everything as string
    rect.to_string()


main()
