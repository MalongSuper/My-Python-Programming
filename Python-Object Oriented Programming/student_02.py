# Class Student with getter/setter

class Student:
    def __init__(self, sid, name, major):
        # Private attributes: Only be retrieved, modified in the class
        # Read-only attributes
        self.__sid = sid  # Instead of self.sid = sid
        self.__name = name  # Instead of self.name = name
        self.__major = major  # Instead of self.major = major

    # Getter
    def getID(self):
        return self.__sid

    def getName(self):
        return self.__name

    def getMajor(self):
        return self.__major

    # Setter
    def setMajor(self, major):
        self.__major = major
        return self.__major


def main():
    s = Student(100001, "James Arthur", "IT")
    # This line 'print(s.__sid)' causes AttributeError
    # Unless we add this line: "s.__sid = 12"
    s.__sid = 12  # --> this does not modify the actual __sid in the class
    print(s.__sid)  # However, this line now returns 12
    print("==============================")
    print("Student Information")
    print("Student ID:", s.getID())  # This function still returns the initial value
    print("Student Name:", s.getName())
    print("Major:", s.getMajor())
    print("==============================")
    # Change Major
    s.setMajor("MARKETING")
    print()
    print("==============================")
    print("Updated Student Information")
    print("Student ID:", s.getID())  # This function still returns the initial value
    print("Student Name:", s.getName())
    print("Major:", s.getMajor())
    print("==============================")


main()
