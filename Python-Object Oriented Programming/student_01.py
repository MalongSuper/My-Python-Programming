# Class Student

class Student:
    # The constructor for student_id, name, birth_year
    # Act as a template/blueprint
    def __init__(self):  # Set initial values
        self.student_id = ""
        self.name = ""
        self.birth_year = 1900

    def get_user(self):
        self.student_id = str(input("Enter Student ID: "))
        self.name = str(input("Enter Student Name: "))
        self.birth_year = int(input("Enter Birth Year: "))

    def display(self):
        # We not only use 'self', but can use any words
        # print(student_id, name, birth_year) raises error
        current_age = self.calculate_age()
        print(f"Student ID: {self.student_id} | Name: {self.name} | Age: {current_age}")

    def calculate_age(self):  # Calculate current year
        current_year = 2025
        return current_year - self.birth_year


def main():
    student = Student()
    student.get_user()
    student.display()


main()
