# Class Student with decorator

class Student:
    def __init__(self, sid, name, major):
        # Private attributes: Only be retrieved, modified in the class
        # Read-only attributes
        self.__sid = sid  # Instead of self.sid = sid
        self.__name = name  # Instead of self.name = name
        self.__major = major  # Instead of self.major = major

    # Getter with @property decorator
    # @property: the function can be treated as an attribute
    @property
    def SID(self):
        return self.__sid

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

    # Now, the Major is treated as an attribute and can be retrieved,
    # and modified as both Setter and Getter
    # Major is still private, but now can be modified like an attribute


def main():
    s = Student(100001, "James Arthur", "IT")
    print("==============================")
    print("Student Information")
    print("Student ID:", s.SID)
    print("Student Name:", s.Name)
    print("Major:", s.Major)
    print("==============================")
    # Change Major
    s.Major = "MARKETING"
    print()
    print("==============================")
    print("Updated Student Information")
    print("Student ID:", s.SID)
    print("Student Name:", s.Name)
    print("Major:", s.Major)
    print("==============================")
    # Note: If we call s.SID(), s.Name(), s.Major() --> ERROR


main()
