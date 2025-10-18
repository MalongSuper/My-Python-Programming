# Class Person, Student, Teacher, Alumni
# Composition

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student:
    def __init__(self, person: Person, student_id):
        self.person = person
        self.student_id = student_id

    def introduce(self):
        return f"I am student {self.person.name}, age {self.person.age}, ID {self.student_id}."


def main():
    person = Person('John C', 12)
    student = Student(person, '223123')
    print(student.introduce())


main()
