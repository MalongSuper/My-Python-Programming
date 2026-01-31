# Distance Metrics for two points
import numpy as np


def euclidean_distance(point1, point2):
    d = np.sqrt((point2[0] - point1[0]) ** 2
                + (point2[1] - point1[1]) ** 2)
    return d


def manhattan_distance(point1, point2):
    m = np.abs(point2[0] - point1[0]) + np.abs(point2[1] - point1[1])
    return m


def chebyshev_distance(point1, point2):
    c = max(np.abs(point2[0] - point1[0]), np.abs(point2[1] - point1[1]))
    return c


def main():
    x1, y1 = eval(input("Enter (x1, y1): "))
    x2, y2 = eval(input("Enter (x2, y2): "))
    point1, point2 = [x1, y1], [x2, y2]
    print("Euclidean Distance:", euclidean_distance(point1, point2))
    print("Manhattan Distance:", manhattan_distance(point1, point2))
    print("Chebyshev Distance:", chebyshev_distance(point1, point2))


main()
