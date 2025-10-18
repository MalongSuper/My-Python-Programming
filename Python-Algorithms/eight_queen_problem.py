# 8-Queen using Backtracking 
import numpy as np

N = 8  # Table 8x8


def is_safe(board, row, col):
    # Row on the left
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Upper Diagonal on the left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Under Diagonal on the left
    for i, j in zip(range(row, N, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def queen_solution(board, col):
    # Case 1: All queens
    if col >= N:
        return True
    # Case 2: Queen can be put in each row
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            if queen_solution(board, col + 1):
                return True
            board[i][col] = 0
    # If a queen cannot be put anywhere
    return False


def main():
    print("8-Queens Problem")
    board = np.zeros((N, N), int)
    if queen_solution(board, 0) is False:
        print("Unsolvable")
        return False
    print("Result")
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
    return True


main()
