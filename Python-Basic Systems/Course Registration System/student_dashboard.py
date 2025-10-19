import json
from course import Course
from user import Teacher
from student_course import StudentCourse


def student_options():
    print("Enter 'add course': New Course")
    print("Enter 'delete course': Drop Course")
    print("Enter 'change pass': Change Password")


def add_course(command, student):
    # Create file json
    filepath = f"student_course.json"
    course_filepath = f'course.json'
    # Add the course to json
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []  # Assume not found, set the json file

    # Load available courses
    try:
        with open(course_filepath, 'r') as f:
            course_data = json.load(f)
    except FileNotFoundError:
        print("% No courses available. Come back later")
        return

    while True:
        # Enter the course name to create it
        course_name = input(f"{command}>")
        # Break the loop if user enter 'exit'
        if course_name == 'exit':
            break

        # Convert the data to list
        # Iterate through the file to check
        for d in data:
            # Check if the student already registered for the course
            if (d['student_id'] == student.student_id and
                    d['course_id'] == course_name):
                print("% Course already registered. Choose a different course.")
                continue

        # Find the course in course list
        course_found = None
        for c in course_data:
            if c['course_name'].lower() == course_name.lower():
                course_found = Course(c['course_name'], c['teacher'], c['course_id'])
                break

        if not course_found:
            print("% Course does not exist. Choose a different course.")
            continue

        # Append to the data
        obj = StudentCourse(student, course_found).to_dict()
        # The teacher id is the teacher who teach the subject
        data.append(obj)
        # Save the dictionary to JSON file
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)

        print(f"* Course '{course_name}' registered successfully!!")


def student_dashboard(command, student):
    while True:
        student_input = input(f"{command}>")
        if student_input.lower() in ['show opt', 'sh opt', 'show option', 'sh option']:
            student_options()

        elif student_input.lower() == "add course":
            command = 'User(Student-Add Course)'
            # Enter the course name
            add_course('User(Student-Add Course)', student)

        elif student_input.lower() == 'log out':
            print(f"* Status: Logout")
            break
        else:
            print("% Command not found.")
