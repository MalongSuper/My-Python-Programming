# Dynamic Binding in Class

class Person:
    # No __init__: use a default object
    def __str__(self):
        return "This is a Person"

    def display(self):
        print(self.__str__())


class Student(Person):
    def __str__(self):
        return "This is a Student"


def main():
    p = Person()
    s = Student()
    p.display()  # This line returns "This is a Person"
    s.display()  # This line returns "This is a Student"
    # Though the display() function does not exist in Class Student
    # This is Dynamic Binding


main()
