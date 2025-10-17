# This program revises NearestPoints.py to
# find the nearest two points in three-dimensional space
from math import sqrt


def distance(x1, x2, y1, y2, z1, z2):  # Define function to compute distance
    distance_point = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    return distance_point


def nearest_points(points):  # Define function to find the nearest points
    p1, p2 = 0, 1
    shortest_distance = distance(points[p1][0], points[p1][1], points[p1][2],
                                 points[p2][0], points[p2][1], points[p2][2])

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = distance(points[i][0], points[i][1], points[i][2],
                         points[j][0], points[j][1], points[j][2])
            # Determine the minimum distance
            if shortest_distance > d:
                p1, p2 = i, j  # New value of p1, p2
                shortest_distance = d  # New shortest distance

    return p1, p2


def main():  # Define main function
    points = []
    print("Nearest Point of Three-Dimensional Space")
    number = int(input("Enter the number of points: "))
    if number > 1:
        for num in range(number):
            x, y, z = eval(input(f"Enter x, y, z for point {num}: "))
            points.append([x, y, z])  # Create a list of the points
        # Get the result from the function
        result = nearest_points(points)
        print("Points:", points)
        # The result returns the point, from there get the number of points
        print("The two nearest points:", points[result[0]], "and", points[result[1]])
    else:
        print("Invalid number of points. Please proceed and try again")


# Display the result
main()
