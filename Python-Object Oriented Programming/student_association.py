# Association Class Demonstration

class Subject:
    def __init__(self, name):
        self.name = name
        self.registrations = []  # Instance variable for individual registrations

    def show_registrations(self):
        print(f"Registrations for Subject: {self.name}")
        for reg in self.registrations:
            print(f"Course: {reg.course.name}, Semester: {reg.semester}, Credits: {reg.num_credits}")


class Course:
    def __init__(self, name):
        self.name = name
        self.registrations = []  # Instance variable for individual registrations

    def show_registrations(self):
        print(f"Registrations for Course: {self.name}")
        for reg in self.registrations:
            print(f"Subject: {reg.subject.name}, Semester: {reg.semester}, Credits: {reg.num_credits}")


class Register:
    def __init__(self, subject: Subject, course: Course, semester, num_credits):
        self.subject = subject
        self.course = course
        self.semester = semester
        self.num_credits = num_credits
        print("Registration Successful!!")
        print(f"Course: {self.course.name}, Subject: {self.subject.name}")
        print(f"Semester: {self.semester}, Credits: {self.num_credits}")

        # Automatically link registration objects correctly
        subject.registrations.append(self)
        course.registrations.append(self)


def main():
    sub1 = Subject("Data Structures")
    sub2 = Subject("Object-Oriented Programming")
    course1 = Course("Python Programming")

    # Register subjects in course
    Register(sub1, course1, "Fall 2025", 4)
    Register(sub2, course1, "Fall 2025", 4)

    # Show registrations
    sub1.show_registrations()
    sub2.show_registrations()
    course1.show_registrations()


main()
