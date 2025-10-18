# Class Student with Class method, Static method


class Student:
    __sid = 230000  # Initial ID

    def __init__(self, name, major):
        # Private attributes: Only be retrieved, modified in the class
        # Read-only attributes
        self.__name = name  # Instead of self.name = name
        self.__major = major  # Instead of self.major = major
        Student.__sid += 1  # For any new student, __sid is incremented to 1
        self.__sid = Student.__sid  # Store the current student id for that student

    @classmethod
    def getID(cls):
        return cls.__sid

    @property
    def Name(self):
        return self.__name

    @property
    def Major(self):
        return self.__major

    # For Setter, we use @attribute_name.setter,
    # attribute_name is typically the initial function name
    @Major.setter
    def Major(self, major):
        self.__major = major

    @property
    def getInfo(self):
        return (f"(Student ID: {self.__sid}, "
                f"Name: '{self.__name}', "
                f"Major: '{self.__major}')")


def main():
    s1 = Student("Nguyen Van Long", "IT")
    s2 = Student("Nguyen Thanh Hieu", "IT")
    s3 = Student("Nguyen Tri Hieu", "IT")
    s4 = Student("Nguyen Hoang Phuc", "CSC")
    s5 = Student("Nguyen Thi Ha", "AI")
    print(s1.getInfo)
    print(s2.getInfo)
    print(s3.getInfo)
    print(s4.getInfo)
    print(s5.getInfo)
    print(s1.getInfo)


main()
