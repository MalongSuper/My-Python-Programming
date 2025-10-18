# Class Composition + Multiplicity


class University:
    def __init__(self, name, library=True, cafeteria=True, auditoriums=1, classrooms=1):
        self.__name = name
        print(f"{self.__name} is under construction")
        # 1: There is exactly one library
        if not library:
            raise ValueError("Every university has exactly one library")
        self.__library = Library(input("Library name: "))
        # 0..1: There might be or might not be a cafeteria
        if not cafeteria:
            self.__cafeteria = None
        else:
            self.__cafeteria = Cafeteria(input("Cafeteria name: "))
        if auditoriums < 1:
            raise ValueError("A university has at least one auditorium")
        self.__auditorium = [Auditorium(f"{i}") for i in range(auditoriums)]
        # 1...*: There must be at least one classroom
        if classrooms < 1:
            raise ValueError("A university has at least one classroom")
        self.__classroom = [Classroom(f"Class{i + 1}", int(input(f"Class{i + 1} - Enter number of students: ")))
                            for i in range(classrooms)]

    def showFacilities(self):
        print(f"\nShow Facilities:"
              f"\nLibrary: {self.__library.getName()} "
              f"\nCafeteria: {self.__cafeteria.getName() if self.__cafeteria else None} "
              f"\nClassroom: ")
        for classroom in self.__classroom:
            print(f" + {classroom.getName()}: {classroom.getNumberOfStudents()}")


class Library:
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name


class Cafeteria:
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name


class Auditorium:
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name


class Classroom:
    def __init__(self, name, numberOfStudent=5):
        self.__name = name
        # Number of students in the class
        self.__numberOfStudents = numberOfStudent
        # A classroom must have at least 5 and at most 30 students.
        if self.__numberOfStudents < 5 or self.__numberOfStudents > 30:
            raise ValueError("A classroom must have at least 5 and at most 30 students")

    def getName(self):
        return self.__name

    def getNumberOfStudents(self):
        return self.__numberOfStudents


def main():
    uni = University("Hoa Sen University", True, True, 2, 12)
    uni.showFacilities()


main()
