# This program finds all the closest pair of points
# Based on the minimum distance
def distance(x1, y1, x2, y2):  # Define function to compute the distance
    return ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) ** 0.5


def closest_points(points):  # Define function to find all the pairs of points
    min_distance = float('inf')  # Initial value of minimum distance to be positive
    closest_pair = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):  # Find the distance
            d = distance(points[i][0], points[i][1],
                         points[j][0], points[j][1])
            if d < min_distance:
                min_distance = d
                closest_pair = [[i, j]]
            elif d == min_distance:
                closest_pair.append((i, j))
    return closest_pair


def main():  # Define main function
    print("Closest pairs of points")
    points = []
    number_of_points = int(input("Enter the number of points: "))
    if number_of_points > 0:
        for num in range(number_of_points):
            point = 2 * [0]
            point[0], point[1] = eval(input(f"Enter x, y for Point {num}: "))
            points.append(point)
        closest_pairs = closest_points(points)
        if closest_pairs:
            print("The Closest pairs of points:")
            for pair in closest_pairs:
                # Display all the closest pairs of points
                p1, p2 = pair
                print("[", str(points[p1][0]), ",", str(points[p1][1]),
                      "]", "and", "[", str(points[p2][0]), ",", str(points[p2][1]), "]")
        else:
            print("No Closest pairs of points found")
    else:
        print("Invalid number of points. Please proceed and try again")


# Display the result
main()
