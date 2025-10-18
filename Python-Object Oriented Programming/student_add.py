# Class Student with Operator Overloading
# Using __add__, __sub__

class Student:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def __str__(self):
        return str(self.birth_year) + ' | ' + self.name

    # Return the information of two students as tuple, allow "+" to be used
    def __add__(self, other):
        # return "Anything"
        return (f"({self.name}, {self.birth_year}) | "
                f"({other.name}, {other.birth_year})")

    # allow "-" to be used, here we use to subtract a difference between
    # Two numerical values
    def __sub__(self, other):
        # Return the difference
        return abs(int(self.birth_year) - int(other.birth_year))


def main():
    s1 = Student("James Anton", "2005")
    s2 = Student("Kevin Duncan", "2004")
    print(s1)
    print(s2)
    # What if we have this line, without __add__
    # print(s1 + s2)
    # TypeError: unsupported operand type(s) for +: 'Student' and 'Student'
    print(s1 + s2)  # Output: "Anything"
    # This line is similar to:
    # s1.__add__(s2)
    # str(s1) + '\n' + str(s2)
    # s1.__str__() + '\n'+ s2.__str__()
    # Now, we want to calculate the difference between the birth_year
    print("Age difference:", s1 - s2)


main()
