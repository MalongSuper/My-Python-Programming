# This program solves Best Passing Score
# Problem: Given a list of students' score
# The task is minimizing the passing score, so that
# We can select the student to pass the subject
# This is similar to the problem of finding a linear segment
# which the total distance is minimum


def min_method(student, mean):  # Using the min method, brute-force search
    # The student scores are points in a straight line
    # or in a plot
    # Calculate the distance between the point X
    # and the student score
    n = len(student)
    sum_distance_right = 0
    sum_distance_left = 0
    left_dict, right_dict = {}, {}
    # Let x starts with the mean
    x = mean
    # Assume the score is within 0 to 10
    while x > 0:  # Try with number lower than x
        for i in range(n):
            distance = abs(student[i] - x)
            sum_distance_left += distance  # Calculate the sum of the distances
            left_dict[x] = sum_distance_left  # Store in dicts
        # Subtract the x
        x = x - 0.01
    # Restore the mean
    x = mean
    while x < 10:  # Try with number greater than x
        for i in range(n):
            distance = abs(student[i] - x)
            sum_distance_right += distance  # Calculate the sum of the distances
            right_dict[x] = sum_distance_right  # Store in dicts
        # Increase the x
        x = x + 0.01
    # Update two dicts and returns the min element of that list
    left_dict.update(right_dict)
    # Return the min distance and the x corresponding to that distance
    return min(left_dict, key=left_dict.get), min(left_dict.values())


def main():
    # Suppose all the students score below average
    # For example: [2.5, 3.2, 2.8, 4.5, 2.1, 3.0]
    print("Min Method Optimization")
    number = int(input("Enter number of students: "))
    student = []
    for n in range(number):
        score = float(input(f"Enter the score of student {n + 1}: "))
        while score < 0 or score > 10:
            print("Invalid score. Must be within 1 to 10")
            score = float(input(f"Enter the score of student {n + 1}: "))
        student.append(score)  # Append it to list
    mean = sum(student) / len(student)
    result = min_method(student, mean)
    # With this, those who are near or greater
    # than the passing score can be considered passing the subject
    print("The best passing score:", result[0])
    print("The minimum distance:", result[1])
    # Get all the students whose scores are greater than the passing score
    print("The students who can pass the subject:")
    for n in range(len(student)):
        if student[n] >= result[0]:
            print(f"Student {n}. Score: {student[n]}")


main()
