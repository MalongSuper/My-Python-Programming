# Superclass Person, Subclasses Student and Teacher

class Person:
    def __init__(self, name=None, address=None):
        self.__name = name
        self.__address = address

    def getName(self):
        return self.__name

    def getAddress(self):
        return self.__address

    def setAddress(self, address):
        self.__address = address

    def __str__(self):
        return f"{self.__name}({self.__address})"


class Student(Person):

    def __init__(self, name=None, address=None):
        super().__init__(name, address)
        self.__courses = []
        self.__grades = []
        self.__numCourses = 0  # Treat each object separately
        # instead of using Student.__numCourses

    def __str__(self):  # Overriding
        return f"Student: {self.getName()}({self.getAddress()})"

    def addCourseGrade(self, course, grade):
        print(f"Add Course - {course}, Grade: {grade}")
        if not isinstance(course, str):
            raise ValueError(f"Course must be in type str, not int, or float")
        if not isinstance(grade, int):
            raise ValueError(f"Course must be in type int, not {type(grade)}")
        self.__courses.append(course)
        self.__grades.append(grade)
        self.__numCourses += 1  # Increment self.__numCourses to 1

    def printGrades(self):
        return self.__grades

    def getAverageGrade(self):
        return sum(self.__grades) / len(self.__grades)

    @property
    def numCourses(self):  # Since the attribute is private
        # We need to get it via property
        return self.__numCourses


class Teacher(Person):

    def __init__(self, name=None, address=None):
        super().__init__(name, address)
        self.__courses = []
        self.__numCourses = 0  # Treat each object separately
        # instead of using Teacher.__numCourses

    def __str__(self):  # Overriding
        return f"Teacher: {self.getName()}({self.getAddress()})"

    def addCourse(self, course):
        print(f"Add Course - {course}")
        if not isinstance(course, str):
            raise ValueError(f"Course must be in type str, not int or float")
        elif course in self.__courses:
            print("The course already exists, addCourse failed")
        else:
            self.__courses.append(course)
            self.__numCourses += 1

    def removeCourse(self, course):
        print(f"Remove Course - {course}")
        if not isinstance(course, str):
            raise ValueError(f"Course must be in type str, not int or float")
        elif course not in self.__courses:
            print("The course does not exist, removeCourse failed")
        else:
            self.__courses.remove(course)
            self.__numCourses -= 1

    @property
    def numCourses(self):  # Since the attribute is private
        # We need to get it via property
        return self.__numCourses


def TestPerson():
    # For Student
    student = Student("Nguyen Thi Thu Ngan",
                      "223 Havana Street")
    print(student)
    student.addCourseGrade("Python Programming", 8)
    student.addCourseGrade("Object-Oriented Programming with Python", 7)
    print("Number of courses:", student.numCourses)
    print("Average:", student.getAverageGrade())
    # For teacher
    teacher = Teacher("Le Nguyen Minh Khoi", "24/5 St.James Street")
    print(f"\n{teacher}")
    teacher.addCourse("Python Programming")
    print("Number of courses:", teacher.numCourses)
    teacher.addCourse("Python Programming")
    print("Number of courses:", teacher.numCourses)
    teacher.addCourse("Java Programming")
    print("Number of courses:", teacher.numCourses)
    teacher.addCourse("Object-Oriented Programming with Python")
    print("Number of courses:", teacher.numCourses)
    teacher.removeCourse("Java Programming")
    print("Number of courses:", teacher.numCourses)
    teacher.removeCourse("C++ Programming")
    print("Number of courses:", teacher.numCourses)


TestPerson()
