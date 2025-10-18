# Class Distance Point

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def to_string(self):
        return f"({str(self.x)}, {str(self.y)})"

    def get_XY(self):
        return f"({self.x}, {self.y})"

    def set_XY(self, x, y):
        self.x = x
        self.y = y

    def distance_to_center(self):  # Calculate distance to (0, 0)
        dist = ((self.x - 0) ** 2 + (self.y - 0) ** 2) ** 0.5
        return dist

    def distance_to_coord(self, x, y):  # Calculate distance to (x, y)
        dist = ((self.x - x) ** 2 + (self.y - y) ** 2) ** 0.5
        return dist

    def distance_to_point(self, to_point):  # Calculate distance to another point
        dist = ((self.x - to_point.x) ** 2 + (self.y - to_point.y) ** 2) ** 0.5
        return dist


def main():  # Main function
    pointA = Point(3, 4)
    print(pointA.to_string())
    pointA.set_XY(4, 3)
    print(pointA.get_XY())
    print(pointA.distance_to_center())
    print(pointA.distance_to_coord(1, 2))
    pointB = Point(5, 4)
    print(pointA.distance_to_point(pointB))


main()
