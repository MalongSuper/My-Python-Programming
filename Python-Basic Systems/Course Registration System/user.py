# A simple Student Management System Class
import uuid
from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, full_name, username, email, password):
        self.full_name = full_name
        self.username = username
        self.email = email
        self.password = password

    @abstractmethod
    def to_dict(self):
        return NotImplemented


class Student(User):
    def __init__(self, full_name, username, email, password, student_id=None):
        super().__init__(full_name, username, email, password)
        self.student_id = student_id if student_id else 'S' + str(uuid.uuid4())

    @staticmethod
    def get_name():
        return "Student"

    def to_dict(self):
        return {'student_id': self.student_id,
                'full_name': self.full_name,
                'username': self.username, "email": self.email,
                "password": self.password}

    def get_info(self):
        return (f"Student ID: {self.student_id}, "
                f"Student Name: {self.full_name}, "
                f"Username: {self.username}, Email: {self.email}, "
                f"Password: {self.password}")


class Teacher(User):
    def __init__(self, full_name, username, email, password, teacher_id=None):
        super().__init__(full_name, username, email, password)
        self.teacher_id = teacher_id if teacher_id else 'T' + str(uuid.uuid4())

    @staticmethod
    def get_name():
        return "Teacher"

    def to_dict(self):
        return {'teacher_id': self.teacher_id,
                'full_name': self.full_name,
                'username': self.username, "email": self.email,
                "password": self.password}

    def get_info(self):
        return (f"Teacher ID: {self.teacher_id} "
                f"Teacher Name: {self.full_name}, "
                f"Username: {self.username}, Email: {self.email}, "
                f"Password: {self.password}")



