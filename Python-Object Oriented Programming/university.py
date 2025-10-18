# Class Aggregation - One class contains the objects of other classes
# But these objects can exist independently


class University:
    def __init__(self, name):
        self.__name = name
        self.__students = []
        self.__teachers = []

    def add_student(self, student):
        if isinstance(student, Student):
            self.__students.append(student)
            print(f"Student {student.getName()} added to {self.__name}")
        else:
            raise Exception(f"Invalid instance {type(student)} for "
                            f"method add_student(self, student)")

    def add_teacher(self, teacher):
        if isinstance(teacher, Teacher):
            self.__teachers.append(teacher)
            print(f"Teacher {teacher.getName()} added to {self.__name}")
        else:
            raise Exception(f"Invalid instance {type(teacher)} for "
                            f"method add_teacher(self, teacher)")


class Student:
    def __init__(self, sid, name, major, credit):
        self.__sid = sid
        self.__name = name
        self.__major = major
        self.__credit = credit

    def getName(self):
        return self.__name

    def getMajor(self):
        return self.__major


class Teacher:
    def __init__(self, sid, name):
        self.__sid = sid
        self.__name = name

    def getName(self):
        return self.__name


def main():
    uni = University("Hoa Sen University")
    # Create Teacher objects, independent of any University
    t1 = Teacher("T01", "Mr.A")
    t2 = Teacher("T02", "Mr.B")
    t3 = Teacher("T03", "Mr.C")
    uni.add_teacher(t1)
    uni.add_teacher(t2)
    uni.add_teacher(t3)
    # Create Student objects, independent of any University
    s1 = Student("S01", "Mary A", "CSC", 0)
    s2 = Student("S02", "Alex B", "CSC", 0)
    s3 = Student("S03", "James D", "CSC", 0)
    uni.add_student(s1)
    uni.add_student(s2)
    uni.add_student(s3)


main()
