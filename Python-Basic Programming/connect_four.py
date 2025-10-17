# This program implements Connect Four
# Rule to win: Four consecutive pieces of same color
# In either horizontal, vertical, or diagonal
import numpy as np

# Row and column board in Connect Four
row_board = 6
column_board = 7


def create_board():  # Create the game board
    board = np.zeros((row_board, column_board))
    return board


def drop_piece(board, move_row, move_col, piece):  # Drop the piece in the board
    board[move_row][move_col] = piece


def is_valid_location(board, move_col):  # Check if the location is valid
    return board[row_board - 1][move_col] == 0


def get_next_open_row(board, move_col):  # Get the next open row
    for r in range(row_board):
        if board[r][move_col] == 0:
            return r


def print_board(board):  # Flip the board
    print(np.flip(board, 0))


def winning_move(board, piece):
    # Check horizontal locations
    for c in range(column_board - 3):
        for r in range(row_board):
            if ((board[r][c] == piece) and (board[r][c + 1] == piece)
                    and (board[r][c + 2] == piece) and (board[r][c + 3] == piece)):
                return True

    # Check vertical locations
    for c in range(column_board):
        for r in range(row_board - 3):
            if ((board[r][c] == piece) and (board[r + 1][c] == piece)
                    and (board[r + 2][c] == piece) and (board[r + 3][c] == piece)):
                return True

    # Check positive diagonals
    for c in range(column_board - 3):
        for r in range(row_board - 3):
            if ((board[r][c] == piece) and (board[r + 1][c + 1] == piece)
                    and (board[r + 2][c + 2] == piece) and (board[r + 3][c + 3] == piece)):
                return True

    # Check negative diagonals
    for c in range(column_board - 3):
        for r in range(3, row_board):
            if ((board[r][c] == piece) and (board[r + 1][c + 1] == piece)
                    and (board[r + 2][c + 2] == piece) and (board[r + 3][c + 3] == piece)):
                return True


# Main Game
game_board = create_board()
game_over = False
player = 0
turn = 0
while not game_over:
    # Player 1 Input
    if turn == 0:
        col = int(input("Player 1 Make your selection (0-6): "))
        # Invalid input causes the opponent to win
        if col > 6 or col < 0:
            print("Invalid input. Player 2 wins!!")
            break
        # Check for validation, then drop the piece to the board
        if is_valid_location(game_board, col):
            row = get_next_open_row(game_board, col)
            drop_piece(game_board, row, col, 1)
            # Check for possible win move and update the status
            if winning_move(game_board, 1):
                player = 1
                game_over = True
    # Player 2 Input
    else:
        col = int(input("Player 2 Make your selection (0-6): "))
        # Invalid input causes the opponent to win
        if col > 6 or col < 0:
            print("Invalid input. Player 1 wins!!")
            break
        # Check for validation, then drop the piece to the board
        if is_valid_location(game_board, col):
            row = get_next_open_row(game_board, col)
            drop_piece(game_board, row, col, 2)
            # Check for possible win move and update the status
            if winning_move(game_board, 2):
                player = 2
                game_over = True
    # Update the game board
    print_board(game_board)
    # Switch turn
    turn += 1
    turn = turn % 2
# Display the final result
if game_over:
    print(f"Game Over. Player {player} wins!!")
