# Simple Class Rectangle (Constructor & Destructor)

class Rectangle:  # Instance of class 'type'
    count = 0

    def __init__(self, width, height):  # Initial values (constructor)
        print("I'm initializing a new Rectangle instance")
        self.width = width
        self.height = height
        Rectangle.count += 1  # Increment the count to inserted object

    def __del__(self):  # Destructor
        print("Deleted")
        Rectangle.count -= 1  # Reduce the count to deleted object

    def display(self):
        print("Rectangle:", self.width, self.height)


rect1 = Rectangle(12, 34)
rect2 = Rectangle(24, 35)
rect3 = Rectangle(22, 46)
rect1.display()
rect2.display()
rect3.display()
print("Number of object:", Rectangle.count)
# Delete rect1
del rect1
# Display the remaining
# rect1.display(): This line will raise error since rect1 is already deleted
rect2.display()
rect3.display()
print("Number of objects:", Rectangle.count)
