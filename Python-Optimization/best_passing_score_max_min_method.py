# This program solves Best Passing Score
# Using Max-Min method
# This method is applied for Curve Fitting Problem
# That is finding a polynomial curve line
# which the total distance is minimum


def max_min_method(student, mean):  # Using the max-min method, brute-force search
    # The student scores are points in a straight line
    # or in a plot
    # Calculate the distance between the point X
    # and the student score
    n = len(student)
    distance_dict = {}
    max_distance_list = []
    # Let x starts with the mean
    x = mean
    # Assume the score is within 0 to 10
    while x > 0:  # Try with number lower than x
        for i in range(n):
            distance = abs(student[i] - x)
            distance_dict[x] = distance  # Store in dicts
        # Get the maximum distances and numbers
        max_distance = max(distance_dict.items(), key=lambda x: x[1])
        max_distance_list.append(list(max_distance))  # Append them to list as a list (2D Array)
        # Get the element with the maximum distance
        # Subtract the x
        x = x - 0.01
    # Finally, return the minimum element and the minimum distance
    return min(max_distance_list, key=lambda x: x[1])


def main():
    # Suppose all the students score below average
    # For example: [2.5, 3.2, 2.8, 4.5, 2.1, 3.0]
    print("Max-Min Method Optimization")
    number = int(input("Enter number of students: "))
    student = []
    for n in range(number):
        score = float(input(f"Enter the score of student {n + 1}: "))
        while score < 0 or score > 10:
            print("Invalid score. Must be within 1 to 10")
            score = float(input(f"Enter the score of student {n + 1}: "))
        student.append(score)  # Append it to list
    mean = sum(student) / len(student)
    result = max_min_method(student, mean)
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
