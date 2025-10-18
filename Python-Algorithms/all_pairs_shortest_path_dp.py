# This program solves All Pairs Shortest Path
# Using Dynamic Programming approach
import numpy as np


def dynamic_programming_method(A0):
    # Matrix of order 4 requires 4 tables
    # Table A1, takes 1 is the intermediate index
    A1 = A0.copy()
    for i in range(len(A0)):
        for j in range(len(A0)):
            A1[j, i] = A1[0, i] + A1[j, 0]
            # If the path is longer, retains the original path
            if A1[j, i] > A0[j, i]:
                A1[j, i] = A0[j, i]
    # Table A2, takes 2 is the intermediate index
    A2 = A1.copy()
    for i in range(len(A1)):
        for j in range(len(A1)):
            A2[j, i] = A2[1, i] + A2[j, 1]
            # If the path is longer, retains the original path
            if A2[j, i] > A1[j, i]:
                A2[j, i] = A1[j, i]
    # Table A3, takes 2 is the intermediate index
    A3 = A2.copy()
    for i in range(len(A2)):
        for j in range(len(A2)):
            A3[j, i] = A3[2, i] + A3[j, 2]
            # If the path is longer, retains the original path
            if A3[j, i] > A2[j, i]:
                A3[j, i] = A2[j, i]
    # Table A3, takes 2 is the intermediate index
    A4 = A3.copy()
    for i in range(len(A3)):
        for j in range(len(A3)):
            A4[j, i] = A4[3, i] + A4[j, 3]
            # If the path is longer, retains the original path
            if A4[j, i] > A3[j, i]:
                A4[j, i] = A3[j, i]
    return A4


def main():
    # Initialize the table A0
    infinity = float('inf')
    A0 = np.array([[0, 3, infinity, 7],
                   [8, 0, 2, infinity],
                   [5, infinity, 0, 1],
                   [2, infinity, infinity, 0]])
    solution = dynamic_programming_method(A0)
    print(solution)


main()
