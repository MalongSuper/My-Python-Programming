# Class Student with Class property


class Student:
    student_list = []  # Initial List

    def __init__(self, sid, name, major):
        # Private attributes: Only be retrieved, modified in the class
        # Read-only attributes
        self.__sid = sid  # Instead of self.sid = sid
        self.__name = name  # Instead of self.name = name
        self.__major = major  # Instead of self.major = major
        # For every new object created, append it to the list
        self.student_list.append([sid, name, major])

    @classmethod
    def printAll(cls):
        print("{:>3} | {:<13} | {:>5}".format("ID", "Name",  "Major"))
        print("-----------------------------")
        for i in range(len(cls.student_list)):
            print("{:>1} | {:<13} | {:<5}".format(cls.student_list[i][0],
                                                  cls.student_list[i][1], cls.student_list[i][2]))


s1 = Student(100, "Tran Van Hung", "IT")
s2 = Student(101, "Le Thi Hoa", "CSC")
s3 = Student(102, "Nguyen Huu An", "CSC")
Student.printAll()
