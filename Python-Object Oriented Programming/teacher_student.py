# Class Association - Simple Association


class Teacher:
    def __init__(self, teacher_id, name):
        self.__teacher_id = teacher_id
        self.__name = name
        self.__students = []

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def add_student(self, student):
        self.__students.append(student)
        # student.getName() calls the method of the student object
        # self.getName() calls the method of the teacher object
        # the object within the class is called with self
        print(f"Student {student.getName()} is assigned to {self.getName()}")


class Student:
    def __init__(self, sid, name):
        self.__sid = sid
        self.__name = name

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name


def main():
    teacher = Teacher("T101", "Mr.Swiss")
    s1 = Student("S101", "James C")
    s2 = Student("S102", "Chris B")
    teacher.add_student(s1)
    teacher.add_student(s2)


main()
