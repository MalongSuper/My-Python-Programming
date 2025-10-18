# Class Person, Student, Teacher, Alumni
# Duck Typing

class Person:
    def __init__(self, name):
        self.__name = name

    def greets(self, student):
        print(f"My name is {self.__name}, Hello {student.name}, my new friend.")

    def introduces(self, student):
        print(f"I am {student.name}, the friend of {self.__name}")

    @property
    def name(self):
        return self.__name


class Student:
    def __init__(self, person):
        self.person = person

    def make_friend(self, another):
        self.person.greets(another)
        another.introduces(self.person)


def main():
    p1 = Person('Alice')
    p2 = Person('John')
    s1 = Student(p1)
    s2 = Student(p2)
    s1.make_friend(s2.person)

    p3 = Person('James')
    p4 = Person('Clark')
    s = Student(p4)
    s.make_friend(p3)


main()
