from login import login_terminal
from register import register_terminal
from user import Student, Teacher
from teacher_dashboard import teacher_dashboard
from student_dashboard import student_dashboard


def check_command(value):
    if value.lower() == "t" or value.lower() == 'teacher':
        while True:
            decide = input(f"User(Teacher)>")
            if decide.lower() == "l" or decide.lower() == "login":
                teacher = login_terminal("User(Teacher-Login)", Teacher)
                if teacher is None:
                    continue
                teacher_dashboard("User(Teacher)", teacher)

            elif decide.lower() == "r" or decide.lower() == "register":
                register_terminal("User(Teacher-Register)", Teacher)
            elif decide.lower() == 'exit':
                break
            else:
                print("% Command not found.")

    elif value.lower() == "s" or value.lower() == "student":
        while True:
            decide = input(f"User(Student)>")
            if decide.lower() == "l" or decide.lower() == "login":
                student = login_terminal("User(Student-Login)", Student)
                if student is None:
                    continue
                student_dashboard("User(Student)", student)
            elif decide.lower() == "r" or decide.lower() == "register":
                register_terminal("User(Student-Register)", Student)
            elif decide.lower() == 'exit':
                break
            else:
                print("% Command not found.")

    elif value == "Tutorial" or value == "Tutor":
        print("Terminal Tutorial.")

    else:
        print("% Command not found.")
