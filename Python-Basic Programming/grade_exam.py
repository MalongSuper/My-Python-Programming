# This program rewrite GradeExam.py to sort the students by grades
def main():
    print("Sort Student Grades")
    # Students' answers to the questions
    answers = [
        ['A', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['D', 'B', 'A', 'B', 'C', 'A', 'E', 'E', 'A', 'D'],
        ['E', 'D', 'D', 'A', 'C', 'B', 'E', 'E', 'A', 'D'],
        ['C', 'B', 'A', 'E', 'D', 'C', 'E', 'E', 'A', 'D'],
        ['A', 'B', 'D', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['B', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['B', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['E', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D']]

    # Key to the questions
    keys = ['D', 'B', 'D', 'C', 'C', 'D', 'A', 'E', 'A', 'D']
    correct_list = []
    # Grade all answers
    for i in range(len(answers)):
        # Grade one student
        correct_count = 0
        for j in range(len(answers[i])):
            if answers[i][j] == keys[j]:
                correct_count += 1
        # Make a list contains the student and the grade
        correct_list.append((i, correct_count))
    # Sort the grades and the students
    sorted_list = sorted(correct_list, key=lambda x: x[1], reverse=True)
    for i, grade in sorted_list:
        # Display the result
        print("Student", i, ":", grade)


main()  # Call the main function
