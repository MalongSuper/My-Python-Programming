# Class Iteration: Using Loop in Class object
# Using Inheritance -> Polymorphism

class Person:
    def __init__(self, name, numOfMonth=1, hourPerMonth=1.0, salaryPerMonth=10000.0):
        self.name = name
        self.numOfMonth = numOfMonth
        self.hourPerMonth = hourPerMonth
        self.salaryPerMonth = salaryPerMonth

    def __str__(self):
        return self.name

    def total_salary(self):
        return self.salaryPerMonth * self.numOfMonth

    def hourly_pay(self):  # Derived Attribute
        return self.salaryPerMonth // self.hourPerMonth


class Specialist(Person):
    def __init__(self, name, numOfMonth=1, hourPerMonth=1.0, salaryPerMonth=10000.0):
        super().__init__(name, numOfMonth, hourPerMonth, salaryPerMonth)


class Manager(Person):
    def __init__(self, name, numOfMonth=1, hourPerMonth=1.0, salaryPerMonth=10000.0):
        super().__init__(name, numOfMonth, hourPerMonth, salaryPerMonth)


def main():
    print("Inheritance")
    s1 = Specialist('John C', 3, 7, 18000)
    s2 = Specialist('Chris AC', 4, 8, 18000)
    m1 = Manager('John FD', 4, 8, 25000)
    m2 = Manager('Anna N', 4, 6, 24000)
    # Calculate the Hourly Pay of every employee
    for i in [s1, s2, m1, m2]:
        print(f"Employee {i}, Total Salary: {i.total_salary()}, Hourly Pay: {i.hourly_pay()}")


main()
