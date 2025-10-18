# Superclass Person and Subclass Student

class Person:
    def __init__(self, pid="123456"):
        self.__pid = pid

    def __str__(self):  # Display the object instead of its address
        return f"Citizen ID: {self.__pid}"

    def get_pid(self):
        return self.__pid


class Student(Person):  # Subclass
    def __init__(self, pid, sid="2000", name=None, major=None):  # Add pid to this class
        super().__init__(pid)
        self.__sid = sid
        self.__name = name
        self.__major = major

    def get_sid(self):
        return self.__sid

    def get_name(self):
        return self.__name

    def get_major(self):
        return self.__major

    # Override the __str__ method to include details about the student
    # Without this function, the __str__ of the Person class will be considered
    # You can also define a to_string() function for this instead of __str__
    def __str__(self):
        return f"[SID: '{self.__sid}', Name: '{self.__name}', Major: '{self.__major}', PID: '{self.get_pid()}']"


def main():
    print("Student Info")
    # Create instance Person
    p1 = Person("123322")
    print(p1)  # This will print the __str__ of the person
    # Create instance Student
    s1 = Student(p1.get_pid(), "2121", "Jimmy Cain", "IT")
    print(s1)  # This line will return the overridden __str__ (the __str__ in student)
    print("Student ID:", s1.get_sid())
    print("Student Name:", s1.get_name())
    print("Major:", s1.get_major())


main()
