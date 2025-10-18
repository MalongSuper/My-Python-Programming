# Class Abstract Student
from abc import ABC, abstractmethod


class DataAccess(ABC):  # abstract class DataAccess
    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def update(self):
        pass


class Student:
    def __init__(self, sid='', name='', major=''):
        self.__sid = sid
        self.__name = name
        self.__major = major

    @property
    def Sid(self):
        return self.__sid

    @Sid.setter
    def Sid(self, sid):
        self.__sid = sid

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, name):
        self.__name = name

    @property
    def Major(self):
        return self.__major

    @Major.setter
    def Major(self, major):
        self.__major = major


class FileAccess(DataAccess, Student):  # Use Has-A Relationship
    def __init__(self, base: Student):
        super().__init__()
        self.base = base

    def insert(self):
        return f"Inserting student {self.base.Sid} to file... Done"

    def update(self):
        return f"Updating student {self.base.Sid} to file... Done"

    def delete(self):
        return f"Deleting student {self.Sid} to file... Done"


class DatabaseAccess(DataAccess, Student):  # Use Has-A Relationship
    def __init__(self, base: Student):
        super().__init__()
        self.base = base

    def insert(self):
        return f"Inserting student {self.base.Sid} to database... Done"

    def update(self):
        return f"Updating student {self.base.Sid} to database... Done"

    def delete(self):
        return f"Deleting student {self.base.Sid} to database... Done"


def TestStudent():
    student = Student('123', 'Nguyen Van Binh', 'AI')
    file_student = FileAccess(student)
    database_student = DatabaseAccess(student)
    print(file_student.insert())
    print(file_student.update())
    print(file_student.delete())
    print(database_student.insert())
    print(database_student.update())
    print(database_student.delete())


TestStudent()
