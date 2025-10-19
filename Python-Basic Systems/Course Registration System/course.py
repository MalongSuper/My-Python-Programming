import uuid
from user import Student, Teacher


class Course:
    def __init__(self, course_name, teacher: Teacher, course_id=None):
        self.course_id = course_id if course_id else "Course" + str(uuid.uuid4())
        self.course_name = course_name
        self.teacher = teacher

    def get_name(self):
        return self.course_name

    def to_dict(self):
        return {'course_id': self.course_id,
                'course_name': self.course_name,
                'teacher': self.teacher.teacher_id}

    def get_teacher(self):
        return self.teacher.get_name()


