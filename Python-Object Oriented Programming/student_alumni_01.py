# Class Person, Student, Teacher, Alumni
# With Inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        return f"I am student {self.name}, ID: {self.student_id}."


def main():
    p = Person("John C", 13)
    s = Student("Alice A", 12, '23012123')
    print(p.introduce())
    print(s.introduce())


main()
