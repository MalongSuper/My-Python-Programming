from user import Student
from course import Course


class StudentCourse:
    def __init__(self, student: Student, course: Course):
        self.student = student
        self.course = course

    def to_dict(self):
        return {'student_id': self.student.student_id,
                'course_id': self.course.course_id}
