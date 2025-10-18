# Calculate GPA

class Course:

    __course_list = []  # For returning the result
    __grade_list = []  # For calculating GPA
    __total_credits = []  # For total credits
    __average_list = []  # For average
    __grade_points = []

    def __init__(self, name="", credit=1, points=0.0):
        self.__name = name
        self.__credit = credit
        self.__points = points
        self.__course_list.append([self.Name, self.Credit, self.Points, self.Grade[0],
                                   self.GradePoints])
        self.__grade_list.append(self.Grade[1])
        self.__total_credits.append(self.Credit)
        self.__average_list.append(self.Points)
        self.__grade_points.append(self.GradePoints)

        if self.Credit < 0:
            raise ValueError("Credits cannot be negative. The program stops abruptly")
        if self.Points < 0.0:
            raise ValueError("Points cannot be negative. The program stops abruptly")


    @property
    def Name(self):
        return self.__name

    @property
    def Credit(self):
        return self.__credit

    @property
    def Points(self):
        return self.__points

    @property
    def Grade(self):
        # If points >= 8.0 --> A
        # If points >= 6.5 --> B
        # If points >= 5.0 --> C
        # If points >= 3.5 --> D
        # If points < 3.5 --> F
        if self.__points >= 8.5:
            return "A", 4.0
        elif self.__points >= 7.0:
            return "B", 3.0
        elif self.__points >= 5.5:
            return "C", 2.0
        elif self.__points >= 4.0:
            return "D", 1.0
        else:
            return "F", 0.0

    @property
    def GradePoints(self):
        # Taking the product of the grade at 4.0 scale and the credits
        return self.Grade[1] * self.__credit

    @classmethod
    def calculate_GPA(cls):
        total_credits = sum(cls.__total_credits)
        avg = sum(cls.__average_list) / len(cls.__average_list)
        gpa = sum(cls.__grade_points) / sum(cls.__total_credits)
        return cls.__course_list, total_credits, round(avg, 2), round(gpa, 3)


def main():
    # Input nothing to stop the loop
    entry = 1
    while True:
        print(f"[Entry {entry}]")
        course = str(input(f"Enter course name: "))
        if course == "":
            break
        credit, points = eval(input("Enter course credits and points: "))
        # Append
        Course(course, credit, points)
        entry = entry + 1
    # Display course info
    for i in Course.calculate_GPA()[0]:
        print(f"Subject: {i[0]}; Credits: {i[1]}; Points: {i[2]}; Grade: {i[3]}; "
              f"Grade Points: {i[1]} * {i[2]} = {i[4]}")
    # Other info
    print(f"Total Credits: {Course.calculate_GPA()[1]}")
    print(f"Average Points: {Course.calculate_GPA()[2]}")
    print(f"GPA: {Course.calculate_GPA()[3]}")


main()
