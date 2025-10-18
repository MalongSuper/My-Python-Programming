# Class Iteration: Using Loop in Class object
# Class Method

class Person:
    employees = []

    def __init__(self, name, numOfMonth=1, hourPerMonth=1.0, salaryPerMonth=10000.0):
        self.name = name
        self.numOfMonth = numOfMonth
        self.hourPerMonth = hourPerMonth
        self.salaryPerMonth = salaryPerMonth
        Person.employees.append(self)

    def __str__(self):
        return self.name

    def total_salary(self):
        return self.salaryPerMonth * self.numOfMonth

    def hourly_pay(self):  # Derived Attribute
        return self.salaryPerMonth // self.hourPerMonth

    @classmethod
    def display_employee(cls):
        for i in cls.employees:
            print(f"Employee {i}, Total Salary: {i.total_salary()}, Hourly Pay: {i.hourly_pay()}")


class Specialist(Person):
    pass


class Manager(Person):
    pass


def main():
    print("Inheritance -> Class Method")
    Specialist('John C', 3, 7, 18000)
    Specialist('Chris AC', 4, 8, 18000)
    Specialist('Chris AD', 4, 8, 20000)
    Manager('John FD', 4, 8, 25000)
    Manager('Anna N', 4, 6, 24000)
    Manager('Bard K', 4, 7, 23600)
    # Display all employees
    Person.display_employee()


main()
