# This program uses function for computing the distance between two points
def distance(x1, x2, y1, y2):
    # Calculate the distance
    compute_distance = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
    return compute_distance


def main():
    print("Compute Distance between two points")
    # Input value
    x1, y1 = eval(input("Enter x1 and y1 for Point 1: "))
    x2, y2 = eval(input("Enter x2 and y2 for Point 2: "))
    print("The distance between two points is", end=" ")
    print(distance(x1, x2, y1, y2))


# Display the result
main()
