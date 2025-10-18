# Class Person, Student, Teacher, Alumni
# With Abstract Method
from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def introduce(self):
        pass


class Student(Person):
    def introduce(self):
        return f"I am {self.name}, a student."
