# Class TicTacToe 3x3 Game
# Use Has-A Relationship

class Game:
    def __init__(self):
        self.board = Board()  # Get the Board class
        self.current_player = "O"  # initially, "O" starts first
        self.current_state = "PLAYING"  # Initially, PLAYING

    def playerMove(self):
        if self.current_player == "O":
            self.current_player = "X"
        else:
            self.current_player = "O"

    def close(self):  # Terminate game
        self.current_state = "CLOSED"
        return "The game is terminated"

    def update(self, currentRow, currentCol):
        # Update the status of the game
        # Create a Cell object for the current move
        cell = Cell(currentRow, currentCol, self.board)
        # Check if the cell is already occupied
        if self.board.cells[currentRow][currentCol] != "-":
            print("Invalid move! Cell is already filled.")
            return  # Exit, the line below won't be considered
        # E.g., self.playerMove() is not called
        # That makes the loop continue, but the currentPlayer does not change
        # Make the move (update the board)
        cell.draw(self.current_player)
        # If the current player won
        winner = self.board.hasWon(self.current_player)
        if winner:
            self.current_state = f"{winner} WON!"
            return  # Exit
        if self.board.isDraw():
            self.current_state = f"DRAW!!"
            return  # Exit
        # Update player
        self.playerMove()


class Board:
    def __init__(self, board_rows=3, board_cols=3):
        self.board_rows = board_rows
        self.board_cols = board_cols
        self.cells = [["-" for _ in range(board_cols)]
                      for _ in range(board_rows)]

    def draw(self):
        for i in range(self.board_rows):
            for j in range(self.board_cols):
                print(self.cells[i][j], end="\t")
            print("")

    # Check for winning
    def hasWon(self, currentPlayer):
        # Row won
        for row in self.cells:
            if all(cell == currentPlayer for cell in row):
                return currentPlayer
        # Column won
        for col in range(self.board_cols):
            if all(self.cells[row][col] == currentPlayer for row in range(self.board_rows)):
                return currentPlayer
        # Diagonal won
        if (all(self.cells[i][i] == currentPlayer for i in range(self.board_rows))
                or all(self.cells[i][2 - i] == currentPlayer for i in range(self.board_rows))):
            return currentPlayer
        # No winner
        return None

    def isDraw(self):
        if all(cell != '-' for row in self.cells for cell in row):
            return True
        return False


class Cell:
    def __init__(self, row, col, board):
        self.row = row
        self.col = col
        self.board = board

    def draw(self, currentPlayer):
        self.board.cells[self.row][self.col] = currentPlayer
        # Update the board
        self.board.draw()  # Call the draw from class Board

    def reset(self):
        # Reset from the latest move
        self.board.cells[self.row][self.col] = "-"
        self.board.draw()


def main():
    game = Game()
    game.board.draw()
    print("Game State:", game.current_state)
    while game.current_state == "PLAYING":
        row, col = eval(input(f"Player {game.current_player}'s turn (enter row, col): "))
        if 0 <= row < 3 and 0 <= col < 3:
            game.update(row, col)
        else:
            print("Invalid Move. Please enter again, (0-2) are valid.")
    print("Game State:", game.current_state)


main()
