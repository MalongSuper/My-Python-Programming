# Course Registration System
import json
from user import Student, Teacher
from course import Course
from teacher_dashboard import show_options, new_course


def password_rule(password):
    # Password must be 6-length long and has at least a number and a character
    if not (len(password) >= 6 and any(char.isdigit() for char in password)
            and any(char.isalpha() for char in password) and
            not any(char.isspace() for char in password)):
        return False
    return True


def login_terminal(command, instance):
    username = input(f"{command}>Username ")
    password = input(f"{command}>Password ")
    filepath = f"{instance.get_name()}.json"
    # Read the json file to check if the user exists
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            # Iterate through the file to check
            for d in data:
                if d['username'] == username and d['password'] == password:
                    print(f"* {instance.get_name()} login successfully!!")
                    print(f"* Status: Login as {instance.get_name()} {d['full_name']}")
                    # Return the instance for dashboard use
                    # Important because the attribute of the Class object
                    if instance.get_name() == 'Teacher':
                        return instance(d['full_name'], d['username'], d['email'], d['password'], d['teacher_id'])
                    elif instance.get_name() == 'Student':
                        return instance(d['full_name'], d['username'], d['email'], d['password'], d['student_id'])

                print(f"% {instance.get_name()} does not exist. Login Failed!!")
                return None

    except FileNotFoundError:
        print(f"% No {instance.get_name()} registered yet. Login Failed!!")
        return None
