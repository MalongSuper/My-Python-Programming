# Class Composition - One class (the whole) contains other classes (the parts)
# The parts depend on the whole
# When the whole is destroyed, the parts are destroyed


class University:
    def __init__(self, name):
        self.__name = name
        self.__library = Library("Hoa Sen Library")
        self.__cafeteria = Cafeteria("Hoa Sen Cafeteria")
        self.__classroom = Classroom("Classrooms from Year1 to Year4")

    def showFacilities(self):
        print(f"{self.__name} is under construction"
              f"\nLibrary: {self.__library.getName()} "
              f"\nCafeteria: {self.__cafeteria.getName()} "
              f"\nClassroom: {self.__classroom.getName()}")


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


class Classroom:
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name


def main():
    uni = University("Hoa Sen University")
    uni.showFacilities()


main()
