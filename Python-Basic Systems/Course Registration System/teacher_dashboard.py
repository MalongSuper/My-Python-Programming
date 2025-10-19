import json
from course import Course


def show_options():
    print("Enter 'new course': New Course")
    print("Enter 'drop course': Drop Course")
    print("Enter 'change pass': Change Password")
    print("Enter 'show student': Show Student")


def new_course(command, teacher):
    # Create file json
    filepath = f"course.json"
    # Add the course to json
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []  # Assume not found, set the json file

    while True:
        # Enter the course name to create it
        course_name = input(f"{command}>")
        # Break the loop if user enter 'exit'
        if course_name == 'exit':
            break

        # Convert the data to list
        # Iterate through the file to check
        for d in data:
            # Check if the course already exist
            if d['course_name'] == course_name:
                print("% Course already exists. Choose a different name.")
                continue

        # Append to the data
        obj = Course(course_name, teacher).to_dict()
        # The teacher id is the teacher who teach the subject
        data.append(obj)
        # Save the dictionary to JSON file
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)

        print(f"* Course '{course_name}' created successfully!!")


def drop_course(command, teacher):
    while True:
        course_name = input(f"{command}>")
        if course_name == 'exit':
            break

        filepath = f"course.json"
        # Add the course to json
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            print("% No Course Found.")
            continue

        # Filter out the course that matches both name and teacher ID
        # Important to avoid deleting every course with the name
        original_len = len(data)
        data = [course for course in data if not
        (course['course_name'].lower() == course_name.lower()
         and course['teacher'] == teacher.teacher_id)]

        if len(data) == original_len:
            print(f"% Course named '{course_name}' not in your data.")
        else:
            # New json file overrides the old one, dropping the course
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=4)
            print(f"* Course '{course_name}' dropped successfully!!")


def teacher_dashboard(command, teacher):
    while True:
        teacher_input = input(f"{command}>")
        if teacher_input.lower() in ['show opt', 'sh opt', 'show options',
                                     'sh option', 'show_option']:
            show_options()

        elif teacher_input.lower() == 'log out':
            print(f"* Status: Logout")
            return

        elif teacher_input.lower() == 'new course':
            new_course('User(Teacher-New Course)', teacher)

        elif teacher_input.lower() == 'drop course':
            drop_course('User(Teacher-Drop Course)', teacher)
