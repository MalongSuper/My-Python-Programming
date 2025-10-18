# This program finds the largest consecutive of 1s
import numpy as np


def find_consecutive(m, row, col):
    # Base Case
    if (row < 0 or row >= len(m) or col < 0
            or col >= len(m[0]) or m[row][col] != 1):
        return 0

    m[row][col] = 0  # Mark this as visited
    max_length = 1
    # Examine the direction
    ver, hor = (0, 1), (1, 0)  # Vertical and Horizontal
    # Diagonal from up left to down right and Diagonal from up right to down left
    dia_left, dia_right = (1, 1), (1, -1)
    direction = [ver, hor, dia_left, dia_right]
    for dx, dy in direction:
        max_length += find_consecutive(m, row + dx, col + dy)

    return max_length


def largest_consecutive(m):
    max_length = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            max_length = max(max_length, find_consecutive(m, i, j))
    return max_length


def main():
    print("Largest Consecutive Ones")
    r, c = eval(input("Enter Row and Column: "))
    matrix = np.random.randint(2, size=(r, c))
    for mat in matrix:
        print(' '.join(map(str, mat)))
    result = largest_consecutive(matrix)
    print(f"Largest Consecutive of 1s: {result}")


main()
