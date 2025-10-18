# Class Linear Equation
from math import sqrt


class LinearEquation:
    def __init__(self, a=0.0, b=0.0, x1=0.0):
        self.__a = a
        self.__b = b
        self.__x1 = x1

    @property
    def A(self):
        return self.__a

    @A.setter
    def A(self, a):
        self.__a = a

    @property
    def B(self):
        return self.__b

    @B.setter
    def B(self, b):
        self.__b = b

    @property
    def X1(self):
        return self.__x1

    @X1.setter
    def X1(self, x1):
        self.__x1 = x1

    def __str__(self):
        # Display the equation
        if self.__b < 0:
            return f"{self.__a}x - {abs(self.__b)} = {self.__x1}"
        return f"{self.__a}x + {self.__b} = {self.__x1}"

    def is_solution(self):  # The number of solutions, and the solution
        if self.__a == 0 and self.__b == 0:  # Many solutions
            return -1
        if self.__a == 0:  # No solution
            return 0
        x = (self.__x1 - self.__b) / self.__a
        return 1, x

    def get_solution(self):
        if self.is_solution() == 0:
            print(f"The equation {self.__str__()} has no solution")
        elif self.is_solution() == -1:
            print(f"The equation {self.__str__()} has multiple solutions")
        else:
            print(f"The equation {self.__str__()} has 1 solution "
                  f"x = {self.is_solution()[1]}")


class QuadraticEquation(LinearEquation):
    def __init__(self, a=0.0, b=0.0, c=0.0, x2=0.0):
        super().__init__(a, b)
        self.__c = c
        self.__x2 = x2

    @property
    def C(self):
        return self.__c

    @C.setter
    def C(self, c):
        self.__c = c

    @property
    def X2(self):
        return self.__x2

    @X2.setter
    def X2(self, x2):
        self.__x2 = x2

    def __str__(self):
        # Display the equation
        if self.B < 0 and self.C < 0:
            return f"{self.A}x^2 - {abs(self.B)}x - {abs(self.C)} = {self.X2}"
        if self.B < 0:
            return f"{self.A}x^2 - {abs(self.B)}x + {self.C} = {self.X2}"
        if self.C < 0:
            return f"{self.A}x^2 + {self.B}x - {abs(self.C)} = {self.X2}"

        return f"{self.A}x^2 + {self.B}x + {self.C} = {self.X2}"

    # Override
    def is_solution(self):
        if self.A == 0:  # Linear Equation
            # Ax^2 + Bx + C = 0 --> Bx + C = 0
            # Store original value
            original_A, original_B, original_x1 = self.A, self.B, self.X1
            # Change the value, only for the calculation
            self.A, self.B, self.X1 = self.B, self.C, self.X2
            result = super().is_solution()
            # Return to the original value for display
            self.A, self.B, self.X1 = original_A, original_B, original_x1
            return result
        # The solution X2 can be not 0
        if self.X2 != 0:  # If X2 != 0, move it to the left side
            # Subtract it with self.C
            self.C = self.C - self.X2
            self.X2 = 0  # Then set X2 = 0
        # Find delta
        delta = (self.B ** 2) - (4 * self.A * self.C)
        if delta < 0:
            return -1  # No solution
        elif delta == 0:
            x = (-self.B) / (2 * self.A)
            return 1, x  # One solution
        else:
            x1 = ((-self.B) + sqrt(delta)) / (2 * self.A)
            x2 = ((-self.B) - sqrt(delta)) / (2 * self.A)
            return 2, x1, x2  # Two distinct solutions

    def get_solution(self):
        if self.A == 0:  # Use the get_solution() method of the LinearEquation class
            super().get_solution()
        elif self.is_solution() == -1:
            print(f"The equation {self.__str__()} has no solution")
        elif self.is_solution()[0] == 1:
            print(f"The equation {self.__str__()} has one solution x1 = x2 = {self.is_solution()[1]}")
        else:
            print(f"The equation {self.__str__()} has 2 solutions "
                  f"x1 = {self.is_solution()[1]}, x2 = {self.is_solution()[2]}")


def main():
    equation1 = LinearEquation(0, 3, 0)
    equation1.get_solution()
    equation2 = LinearEquation(0, 0, 0)
    equation2.get_solution()
    equation3 = LinearEquation(6, -3, 0)
    equation3.get_solution()
    equation4 = LinearEquation(2, 3, 0)
    equation4.get_solution()
    equation5 = LinearEquation(8, 0, 0)
    equation5.get_solution()
    print()
    equation6 = QuadraticEquation(2, -4, 2, 0)
    equation6.get_solution()
    equation7 = QuadraticEquation(2, -4, 0, 0)
    equation7.get_solution()
    equation8 = QuadraticEquation(1, 2, 5, 0)
    equation8.get_solution()
    equation9 = QuadraticEquation(0, 5, 0, 0)
    equation9.get_solution()
    equation10 = QuadraticEquation(2, 5, 4, 3)
    equation10.get_solution()
    equation11 = QuadraticEquation(0, 2, 24, 8)
    equation11.get_solution()


main()
