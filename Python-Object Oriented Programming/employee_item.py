# Class Iteration: Using Loop in Class object
# Inconsistent Method: Independent Classes


class Specialist:
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


class Manager:
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
        return self.salaryPerMonth / self.hourPerMonth


def main():
    s1 = Specialist('John A', 3, 7, 12000)
    s2 = Specialist('Chris B', 4, 8, 14000)
    m1 = Manager('John C', 4, 8, 23000)
    m2 = Manager('Anna M', 4, 6, 21000)
    # Calculate the Hourly Pay of every employee
    for i in [s1, s2, m1, m2]:
        print(f"Employee {i}, Total Salary: {i.total_salary()}, Hourly Pay: {i.hourly_pay()}")


main()
