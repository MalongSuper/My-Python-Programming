# Realization (or Implementation): Relationship between
# Abstract class and subclasses (classes which inherit from the abstract class)
from abc import ABC, abstractmethod


class GPA(ABC):
    @abstractmethod
    def calculate_gpa(self):
        pass


class FirstSemester(GPA):
    def __init__(self, gpa=None):  # Take list for gpa
        if gpa is None:
            gpa = []
        self.__gpa = list(gpa)

    def calculate_gpa(self):
        return sum(self.__gpa) / len(self.__gpa)


class SecondSemester(GPA):
    def __init__(self, gpa=None):  # Take list for gpa
        if gpa is None:
            gpa = []
        self.__gpa = list(gpa)

    def calculate_gpa(self):
        if len(self.__gpa) == 0:
            return 0.0
        return sum(self.__gpa) / len(self.__gpa)


def main():
    score_1 = FirstSemester([8.5, 8.5, 9.3])
    print("First Semester:", score_1.calculate_gpa())
    score_2 = SecondSemester([8.5, 7.5, 7.8])
    print("Second Semester:", score_2.calculate_gpa())


main()
